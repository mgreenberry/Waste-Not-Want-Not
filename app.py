import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    foods = mongo.db.food.find()
    return render_template("index.html", foods=foods)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # Displays message if username entered for registration already exists
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        # Form for registration
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)
        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    # Takes new user to their profile page once completed
    return render_template("register.html")


@app.route("/index", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "modifies", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("index"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("index"))

    return render_template("profile.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):  # displays current user's profile page.
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)


@app.route("/logout")  # allows user to log out of current session
def logout():
    # Logs user out
    flash("You have logged out")
    session.pop("user")
    return redirect(url_for("index"))


@app.route("/add_food", methods=["GET", "POST"])  
# Adds food item to current stock list
def add_food():
    if request.method == "POST":
        short_date = "on" if request.form.get("short_date") else "off"
        food = {  # Form collects the food item entered
            "location": request.form.get("location"),  # Fridge, cupboard, etc
            "food_name": request.form.get("food_name"),  # Milk, bread, etc
            "barcode": request.form.get("barcode"), 
            # Barcode, batch code for packs or similar id number
            "purchase_date": request.form.get("purchase_date"),
            "use_by_date": request.form.get("use_by_date"),
            "short_date": short_date,
            "created_by": session["user"]
        }
        mongo.db.food.insert_one(food)  # inserts the completed form to the db
        flash("Food added succesfully")
        return redirect(url_for("modifies"))

    foods = mongo.db.food.find().sort("food_name", 1)
    return render_template("add_food.html", foods=foods)


@app.route("/edit_food/<food_name>", methods=["GET", "POST"])
def edit_food(food_name):
    # Allows user to change food details if error in list
    if request.method == "POST":
        short_date = "on" if request.form.get("short_date") else "off"
        submit = {
            "location": request.form.get("location"),
            "food_name": request.form.get("food_name"),
            "barcode": request.form.get("barcode"),
            "purchase_date": request.form.get("purchase_date"),
            "use_by_date": request.form.get("use_by_date"),
            "short_date": short_date,
            "created_by": session["user"]
        }
        mongo.db.food.update({"_id": ObjectId(food_name)}, submit)
        flash("Food updated succesfully")
        return redirect(url_for("modifies"))

    food = mongo.db.food.find_one({"_id": ObjectId(food_name)})
    foods = mongo.db.food.find().sort("food_name", 1)
    return render_template("edit_food.html", food=food, foods=foods)


@app.route("/delete_food/<food_name>")
def delete_food(food_name):
    # Allows user to delete food item. User will have warning message displayed
    mongo.db.food.remove({"_id": ObjectId(food_name)})
    flash("Food Item Deleted")
    return redirect(url_for("modifies"))


@app.route("/modifies")
def modifies():  # Displays current food list
    modifies = list(mongo.db.food.find().sort('use_by_date', 1))
    return render_template("modifies.html", modifies=modifies)


@app.route("/shopping/<food_name>", methods=['GET', 'POST'])
def shopping(food_name):
    # Finds the selected food item from the food list collection
    food = mongo.db.food.find_one({"food_name": food_name})
    # Deletes the following unneeded fields from the record.
    del food["_id"]
    del food["location"]
    del food["purchase_date"]
    del food["use_by_date"]
    del food["short_date"]
    del food["barcode"]
    # Inserts the food item, apart from 'id' to the shopping list collection
    mongo.db.shopping.insert_one(food)
    # Removes the original item from the food list collection
    mongo.db.food.remove({"food_name": food_name})
    # Displays a success message to the user
    flash("Food Item added to Shopping List")
    # Sorts the new shopping list into alphabetical order
    items = list(mongo.db.shopping.find().sort('food_name', 1))
    # Creates the shopping list on the 'shopping.html' page
    return render_template("shopping.html", items=items)


@app.route("/shopping_list", methods=['GET', 'POST'])  # For navigation
def shopping_list():  # With some great support from Sean and Scott from CI
    items = list(mongo.db.shopping.find().sort('food_name', 1))
    return render_template("shopping.html", items=items)


@app.route("/delete_shopping/<food_name>")
def delete_shopping(food_name):
    # Allows user to delete shopping list item. 
    # User will have warning message displayed
    mongo.db.shopping.remove({"_id": ObjectId(food_name)})
    flash("Shopping List Item Deleted")
    return redirect(url_for("shopping_list"))


@app.route("/add_shopping", methods=["GET", "POST"])  
# Adds food item to current stock list
def add_shopping():
    if request.method == "POST":
        food = {  # Form collects the food item entered
            "food_name": request.form.get("food_name"),  # Milk, bread, etc
            "quantity": request.form.get("quantity"),
            "created_by": session["user"]
        }
        mongo.db.shopping.insert_one(food)
        # inserts the completed form to the db
        flash("Shopping Item Added succesfully")
        return redirect(url_for("shopping_list"))

    foods = mongo.db.shopping.find().sort("food_name", 1)
    return render_template("add_shopping.html", foods=foods)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)