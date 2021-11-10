$(document).ready(function(){
    /* Below code from Materalize css */
    $(".sidenav").sidenav({
      edge: "right",
      closeonClick: true
    });
    $('.collapsible').collapsible();
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $('.modal').modal();
    /* Below adapted from Materalize css for own use 
    Allows the purchase date to only be today or past date 
    and allows the use by date to be today or future only */
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