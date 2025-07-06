
    $(document).ready(function() {
        $('#id_semester_id').change(function() {
            
            var selectedValue = $(this).val();
            $.ajax({
                beforeSend: function(){
                  $('.ajax-loader').css("visibility", "visible");
                },

                url: '{% url "get_filtered_data" %}',
                data: {
                    'selected_value': selectedValue
                },
                dataType: 'json',
                success: function(data) {   
                    var tableBody = $('#myTable tbody');
                    tableBody.empty(); // Clear existing data
                    $.each(data, function(index, item) {
                        var row = '<tr id="ROW-' + item.id +'"><td>' + item.code + '</td> <td>' + item.heads + '</td> <td><a href=/subject/edit/' + item.id + '><img src="{% static "img/edit.png" %}"> </img></a></td><td><a href="#" class="remove" data-id=' + item.id + ' data-url="/subject/delete/'  + item.id + '/"> <img src="{% static "img/delete.png" %}"> </img> </a></td></tr>';
                        tableBody.append(row);
                    });
                },
                 complete: function(){
                  $('.ajax-loader').css("visibility", "hidden");
                  },

                error: function(xhr, status, error) {
                    console.error("AJAX Error:", status, error);
                }
            });
        });
    });



    $(document).on('submit', '#myform', function(e) {
         e.preventDefault();

         $.ajax({
             beforeSend: function(){
                  $('.ajax-loader').css("visibility", "visible");
                },

            type: 'POST',
            url: '{% url "subject-add" %}',
            data: {
               semester_id: $('#id_semester_id').val(),
               code: $('#id_code').val(),
               heads: $('#id_heads').val(),           
               csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
             success: function(data) {
                
                    var tableBody = $('#myTable tbody');
                    tableBody.empty(); // Clear existing data
                    $.each(data, function(index, item) {
                        var row = '<tr id="ROW-' + item.id + '"><td>' + item.code + '</td> <td>' + item.heads + '</td> <td><a href=/subject/edit/' + item.id + '><img src="{% static "img/edit.png" %}"> </img></a></td><td><a href="#" class="remove" data-id=' + item.id + ' data-url="/subject/delete/'  + item.id + '/"> <img src="{% static "img/delete.png" %}"> </img> </a></td></tr>';                       
                        tableBody.append(row);
                    });

               Swal.fire({
                icon: 'success', // Use message tags (e.g., 'success', 'error') as icon
                title: 'Save', // Capitalize the tag for the title
                text: 'Record Saved Successfully',
                timer: 3000, // Optional: automatically close after 3 seconds
                showConfirmButton: true, // Optional: hide the confirm button
               // position: 'top-end' // Optional: position the alert
            });
                },
                 complete: function(){
                  $('#id_code').val('');  
                  $('#id_code').attr('required', 'required');              
                  $('#id_heads').val('');
                  $('.ajax-loader').css("visibility", "hidden");
                  },

                error: function(data) {
                
                Swal.fire({
                icon: 'error', // Use message tags (e.g., 'success', 'error') as icon
                title: data.responseJSON.status, // Capitalize the tag for the title
                text: data.responseJSON.errors,
                timer: 3000, // Optional: automatically close after 3 seconds
                showConfirmButton: true, // Optional: hide the confirm button
                position: 'top-end' // Optional: position the alert
            });

                 
                   
                }
         });        
        });
    
