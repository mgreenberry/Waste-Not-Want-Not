$(document).ready(function(){
    $(".sidenav").sidenav({edge: "right"});
    $('.collapsible').collapsible();
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $('.modal').modal();
    $('.datepicker').datepicker({
      format: "dd mmmm, yyyy",
      yearRange: 3,
      showClearBtn: true,
      i18n: {
        done: "Select"
      }
    });
  });

  $('.navbar-collapse a').click(function(){
    $(".navbar-collapse").collapse('hide');
  });