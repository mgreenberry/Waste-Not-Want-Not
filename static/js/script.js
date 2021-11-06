$(document).ready(function(){
    $(".sidenav").sidenav({edge: "right"});
    $('.collapsible').collapsible();
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $('.modal').modal();
    $('.datepicker1').datepicker({
      format: "dd mmmm, yyyy",
      maxDate: new Date(),
      showClearBtn: true,
      autoClose: true,
      i18n: {
        done: "Select"
      }
    });
    $('.datepicker2').datepicker({
      format: "dd mmmm, yyyy",
      minDate: new Date(),
      autoClose: true,
      showClearBtn: true,
      i18n: {
        done: "Select"
      }
    });
  });

  $('.navbar-collapse a').click(function(){
    $(".navbar-collapse").collapse('hide');
  });