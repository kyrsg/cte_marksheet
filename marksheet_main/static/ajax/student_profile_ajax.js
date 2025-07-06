$(document).ready(function(){

    function validateEmail(email) {
        var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        return regex.test(email);
    }

//===========CREATE STUDENT PROFILE BEGINS HERE ==================
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
     //==============CREATE STUDENT PROFILE ENDS HERE================================



     //===========EDIT STUDENT PROFILE BEGINS HERE ==================
     $("#edit").off().on("click",  function(e){
        e.preventDefault();

        url = $("#getUrl").val();
        getid = $("#getId").val();    

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
                id: getid,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(response) {
            if (response.status === 'success') {            
              Swal.fire({
                icon: 'success', // Use message tags (e.g., 'success', 'error') as icon
                title: 'Update', // Capitalize the tag for the title
                text: 'Student Profile Updated Successfully',                
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
     //==============EDIT STUDENT PROFILE ENDS HERE================================

     //==============FILTER QUERY BEGINS HERE =====================================
     $("#search").off().on("click", function(e){
        e.preventDefault();

        filter_field = $("#_dm-filterField").val();
        value_field = $("#filtervalue").val();
       
        url = $("#getUrl").val();

      
        message = '';

        if (filter_field == 'None') {
            message = "Select Proper Filter Criteria";
              $("#_dm-filterField").focus();
        } else if (value_field == '') {
            message = "Enter Text to Search";
             $("#filtervalue").focus();
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
                type:"GET",
                url:url,
                data:{
                    filter_field:filter_field,
                    value_field:value_field,
                   
                },
                datatype:"json",
                success: function(response) {
                console.log(response);
                    var tableBody = $('#myTable tbody');
                    tableBody.empty(); // Clear existing data
                    $.each(response, function(index, item) {
                       var row = '<tr id="ROW-' + item.id + '"><td>' + item.students_name + '</td><td>' + item.email_address + '</td> <td>' + item.regn_no + '</td> <td>' + item.roll_no + '</td> <td>' + item.mobile_no + '</td><td><a href=/student-profile/edit/' + item.id + '><img src="/static/img/cert.jpg"> </img></a></td><td><a href=/student-profile/edit/' + item.id + '><img src="/static/img/edit.png"> </img></a></td><td><a href="#" class="remove" data-id=' + item.id + ' data-url="/student-profile/delete/'  + item.id + '/"> <img src="/static/img/delete.png"> </img> </a></td></tr>';                       
                       tableBody.append(row);

                    });
                }
            });
        }

     })

     //==============FILTER QUERY ENDS HERE ======================================
});



