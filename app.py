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
def home():
    """
    Function to load the homepage
    """
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Checks if username and/or password already taken
    Allows new user to register for site
    Displays success or error message to user
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        user = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }

        mongo.db.users.insert_one(user)
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Will check that username and password match database
    Allows user to log in
    Displays success or error message to user
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))

                return redirect(url_for("groceries", username=session["user"]))

            else:
                flash("Incorrect Username and/or Password.")
                flash("Have you already registered?")
                return redirect(url_for("home"))

        else:
            flash("Incorrect Username and/or Password.")
            flash("Have you already registered?")
            return redirect(url_for("home"))

    return render_template("profile.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Takes new user to profile page
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)


@app.route("/logout")
def logout():
    """
    Logs user out from profile page and current session
    """
    flash("You have logged out")
    session.clear()
    return redirect(url_for("home"))


@app.route("/add_food", methods=["GET", "POST"])
def add_food():
    """
    Adds food item to current food stock list
    Displays success message to user
    """
    if request.method == "POST":
        food = {
            "location": request.form.get("location"),
            "food_name": request.form.get("food_name"),
            "quantity": request.form.get("quantity"),
            "barcode": request.form.get("barcode"), 
            "purchase_date": request.form.get("purchase_date"),
            "use_by_date": request.form.get("use_by_date"),
            "created_by": session["user"]
        }
        mongo.db.food.insert_one(food)
        flash("Food added succesfully")
        return redirect(url_for("groceries"))

    foods = mongo.db.food.find().sort("food_name", 1)
    return render_template("add_food.html", foods=foods)


@app.route("/edit_food/<food_name>", methods=["GET", "POST"])
def edit_food(food_name):
    """
    Allows user to change food details if error in list
    Displays success message to user
    """
    if request.method == "POST":
        submit = {
            "location": request.form.get("location"),
            "food_name": request.form.get("food_name"),
            "quantity": request.form.get("quantity"),
            "barcode": request.form.get("barcode"),
            "purchase_date": request.form.get("purchase_date"),
            "use_by_date": request.form.get("use_by_date"),
            "created_by": session["user"]
        }
        mongo.db.food.update({"_id": ObjectId(food_name)}, submit)
        flash("Food updated succesfully")
        return redirect(url_for("groceries"))

    food = mongo.db.food.find_one({"_id": ObjectId(food_name)})
    foods = mongo.db.food.find().sort("food_name", 1)
    return render_template("edit_food.html", food=food, foods=foods)


@app.route("/delete_food/<food_name>")
def delete_food(food_name):
    """
    Allows user to delete food item
    User will have warning message displayed
    """
    mongo.db.food.delete_one({"_id": ObjectId(food_name)})
    flash("Food Item Deleted")
    return redirect(url_for("groceries"))


@app.route("/groceries")
def groceries():
    """
    Displays current food list
    """
    items = mongo.db.food.find().sort('use_by_date', 1)
    return render_template("groceries.html", groceries=items)


@app.route("/shopping/<food_name>", methods=['GET', 'POST'])
def shopping(food_name):
    """
    Moves selected food item from the food list collection to the shopping list
    Displays success message to user
    """
    food = mongo.db.food.find_one({"food_name": food_name})
    del food["_id"]
    del food["location"]
    del food["purchase_date"]
    del food["use_by_date"]
    del food["barcode"]
    mongo.db.shopping.insert_one(food)
    mongo.db.food.remove({"food_name": food_name})
    flash("Food Item added to Shopping List")

    items = list(mongo.db.shopping.find().sort('food_name', 1))
    return render_template("shopping.html", items=items)


@app.route("/shopping_list", methods=['GET', 'POST'])
def shopping_list():
    """
    For Navigation
    """
    items = list(mongo.db.shopping.find().sort('food_name', 1))
    return render_template("shopping.html", items=items)


@app.route("/delete_shopping/<food_name>")
def delete_shopping(food_name):
    """
    Allows user to delete shopping list item
    Displays message to user
    """
    mongo.db.shopping.remove({"_id": ObjectId(food_name)})
    flash("Shopping List Item Deleted")
    return redirect(url_for("shopping_list"))


@app.route("/add_shopping", methods=["GET", "POST"])  
def add_shopping():
    """
    Adds food item to current stock list
    Displays message to user
    """
    if request.method == "POST":
        food = {
            "food_name": request.form.get("food_name"),
            "quantity": request.form.get("quantity"),
            "created_by": session["user"]
        }
        mongo.db.shopping.insert_one(food)

        flash("Shopping Item Added succesfully")
        return redirect(url_for("shopping_list"))

    foods = mongo.db.shopping.find().sort("food_name", 1)
    return render_template("add_shopping.html", foods=foods)


@app.route("/edit_shopping/<food_name>", methods=["GET", "POST"])
def edit_shopping(food_name):
    """
    Allows user to change shopping list item details if error in list
    Displays message to user
    """
    if request.method == "POST":
        submit = {
            "food_name": request.form.get("food_name"),
            "quantity": request.form.get("quantity"),
            "created_by": session["user"]
        }
        mongo.db.shopping.update({"_id": ObjectId(food_name)}, submit)
        flash("Shopping List Item Updated Succesfully")
        return redirect(url_for("shopping_list"))

    shopping = mongo.db.shopping.find_one({"_id": ObjectId(food_name)})
    return render_template("edit_shopping.html", shopping=shopping)


@app.route("/waste/<food_name>", methods=['GET', 'POST'])
def waste(food_name):
    """
    Moves item from food list to wasted food item list
    Displays message to user
    """
    food = mongo.db.food.find_one({"food_name": food_name})
    del food["_id"]
    del food["location"]
    del food["purchase_date"]
    del food["use_by_date"]
    del food["barcode"]

    mongo.db.waste.insert_one(food)
    mongo.db.food.delete_one({"food_name": food_name})
    flash("Food Item added to Wasted Food List")

    items = list(mongo.db.waste.find().sort('food_name', 1))
    return render_template("waste.html", items=items)


@app.route("/waste_list", methods=['GET', 'POST'])
def waste_list():
    """
    For navigation from nav menu
    """
    items = list(mongo.db.waste.find().sort('food_name', 1))
    return render_template("waste.html", items=items)


@app.route("/delete_waste/<food_name>")
def delete_waste(food_name):
    """
    Allows user to delete waste list item
    """
    mongo.db.waste.delete_one({"_id": ObjectId(food_name)})
    flash("Waste Food Item Deleted")
    return redirect(url_for("waste_list"))


if __name__ == "__main__":
    """
    MUST Change debug=True to 
    if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=os.environ.get("DEBUG"))
    """
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
