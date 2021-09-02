
/*
This ajax logic retrieve all the user when select role
 */

  $('#id_role').change(function(event){

    event.preventDefault();

    var role = $('#id_role').val();
    
    $.ajax({

      //url : "{% url 'admin_app:user_role' %}",
      url : "/get_user_by_role/",
      data: {'role':role},
      success: function(response){
          $("#id_user").html(response);
      },
      error: function(){
        alert("Something Went Wrong!")
      },


    });
   
  });
