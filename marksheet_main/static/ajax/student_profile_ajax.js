$(document).ready(function(){

    function validateEmail(email) {
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}

     $("#add").off().on("click",  function(e){
        e.preventDefault();

        url = $("#getUrl").val();

        students_name = $("#id_students_name").val();
        regn_no = $("#id_regn_no").val();
        roll_no = $("#id_roll_no").val();
        mobile_no = $("#id_mobile_no").val();
        alternate_no = $("#id_alternate_no").val();
        email_address = $("#id_email_address").val();


        message = '';

        if (students_name == '') {
            message = "Enter Students Name";
              $("#id_students_name").focus();
        } else if (regn_no == '') {
            message = "Enter Registration Name";
             $("#id_regn_no").focus();
        } else if (roll_no == '') {
            message = "Enter Roll Number";
             $("#id_roll_no").focus();
        } else if (mobile_no == '') {
            message = "Enter Mobile Number";
              $("#id_mobile_no").focus();
         } else if (alternate_no == '') {
            message = "Enter Alternate Mobile Number";
              $("#id_alternate_no").focus();
        } else if (!validateEmail(email_address)) {
            message = "Enter Proper Email Address";
              $("#id_email_address").focus();
        };

        if (message != '') {                
            Swal.fire({
            icon: "error",
            title: "Required Fields",
            text: message,
            });  

            
        }
        else {
             $.ajax({
             beforeSend: function(){
                  $('.ajax-loader').css("visibility", "visible");
                },

            type: "POST",
            url: url,
            datatype: "json",
            data:{
                students_name:students_name,
                regn_no:regn_no,
                roll_no:roll_no,
                mobile_no:mobile_no,
                alternate_no:alternate_no,
                email_address:email_address,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(response) {
            if (response.status === 'success') {            
              Swal.fire({
                icon: 'success', // Use message tags (e.g., 'success', 'error') as icon
                title: 'Save', // Capitalize the tag for the title
                text: 'Student Profile Created Successfully',                
                showConfirmButton: true, // Optional: hide the confirm button
               // position: 'top-end' // Optional: position the alert
              });

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

            complete: function(response){  
                if (response.status === 'success') {
                    $('#id_students_name').val('');
                    $('#id_regn_no').val('');
                    $('#id_roll_no').val('');
                    $('#id_mobile_no').val('');
                    $('#id_alternate_no').val('');
                    $('#id_email_address').val('');
                    $('#id_students_name').focus();
                   
                }                             
                  $('.ajax-loader').css("visibility", "hidden");
                  },           

            
        });
        }
     });
});



