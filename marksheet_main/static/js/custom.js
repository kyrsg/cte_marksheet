// DELETE QUERY 
$(document).on('click', '.remove', function(e) {
     e.preventDefault();   
     url = $(this).attr('data-url');
     
  

  Swal.fire({
  title: "Are you sure?",
  text: "You won't be able to revert this!",
  icon: "warning",
  showCancelButton: true,
  confirmButtonColor: "#3085d6",
  cancelButtonColor: "#d33",
  confirmButtonText: "Yes, delete it!"
}).then((result) => {
  if (result.isConfirmed) {

    
     $.ajax({
        type: 'GET',
        url: url,
        success: function(response){
       
         if (response.status == 'success') {
          getID= "ROW-" + response.id;    
        
          document.getElementById(getID).remove();
        
          Swal.fire({
          title: "Deleted!",
          text:  response.module + " deleted successfully.",
          icon: "success"
      });
         }
        }
     });


   
  }
});
});  
 
//========================================================