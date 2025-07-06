$(document).ready(function(){
    //BEGINNING OF ADD BATCH//
   $("#add").off().on("click",  function(e){
         e.preventDefault();
       
         url = $("#getUrl").val();                  
       
         if ($("#id_heads").val() == "") {          
          
            Swal.fire({
            icon: "error",
            title: "Required Fields",
            text: "Kindly fill the fields marked in Red",
            });        
          
         }
         else {
             $.ajax({
              beforeSend: function(){
                  $('.ajax-loader').css("visibility", "visible");
                },

            type: 'POST',
            url : url,
            data : {
                heads : $("#id_heads").val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },

            success: function(response) {
                console.log(response.status);
                if (response.status == "success") {
                     var tableBody = $('#myTable tbody');
                var row = '<tr id="ROW-' + response.id + '"><td>' + response.heads + '</td> <td><a href=/batch/edit/' + response.id + '><img src="/static/img/edit.png"> </img></a></td><td><a href="#" class="remove" data-id=' + response.id + ' data-url="/batch/delete/'  + response.id + '/"> <img src="/static/img/delete.png"> </img> </a></td></tr>';                       
                tableBody.append(row);  
                }
                else {
                     Swal.fire({
                icon: 'error', // Use message tags (e.g., 'success', 'error') as icon
                title: response.status, // Capitalize the tag for the title
                text: response.message,
                timer: 3000, // Optional: automatically close after 3 seconds
                showConfirmButton: true, // Optional: hide the confirm button
                position: 'top-end' // Optional: position the alert
                })
                }
            },

            complete: function(){                               
                  $('#id_heads').val('');
                  $('.ajax-loader').css("visibility", "hidden");
                  },           
         });
         } 
   });

   //END OF ADD BATCH//


   //BEGINNING OF EDIT BATCH //

   $("#edit").off().on("click",  function(e){
         e.preventDefault();
      
         url = $("#getUrl").val();
         getid = $("#getId").val();    

       
       
         if ($("#id_heads").val() == "") {          
          
            Swal.fire({
            icon: "error",
            title: "Required Fields",
            text: "Kindly fill the fields marked in Red",
            });        
          
         }
         else {
             $.ajax({
              beforeSend: function(){
                  $('.ajax-loader').css("visibility", "visible");
                },

            type: 'POST',
            url : url,
            data : {
                heads : $("#id_heads").val(),
                id : getid,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },

            success: function(response) {
            
            if (response.status === 'success') {
              
            if (response.redirect_url) {
                window.location.href = response.redirect_url; // Redirect to the specified URL
            } else {
                // Handle success without redirection, e.g., update UI
                console.log("Operation successful, no redirection specified.");
            }
        } else {
            // Handle errors or display error messages
            Swal.fire({
            icon: "error",
            title: "Error Details",
            text: response.message,
            });      
            //  console.error("Error:", response.message);
        }
            },

            complete: function(){                               
                  $('#id_heads').val('');
                  $('.ajax-loader').css("visibility", "hidden");
                  },           
         });
         } 
   });

   //END OF EDIT BATCH //
});



