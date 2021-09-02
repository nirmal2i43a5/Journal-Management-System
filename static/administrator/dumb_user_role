
/*
This ajax logic retrieve all the user when select role
 */

  $('#id_role').on('click', function(event){

    event.preventDefault();

    var role = $('#id_role').val();
    options = ''
    
    $.ajax({

      url : "/user_role/",
      method: 'POST',
      dataType: 'json',
      data: {role:role},

      error: function(){
        alert("Something Went Wrong!")
      },

      success: function(response){

        user_data = response

      for  (var i = 0;i<user_data.length;i++){

        options+= 
        ` 
        <option value = "${user_data[i].id}">${user_data[i].full_name}</option>
        `
        
        $('#id_user').html(options)//append this field to user when u select user_role
    
        
      }
      

      }


    });
   
  });
