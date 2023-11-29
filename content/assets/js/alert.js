$(document).ready(function() {
    $("#reject").on("click", function(e) {
      e.preventDefault(); // Prevent the form from submitting immediately
      
      if (confirm("Are you sure you want to reject this vendor?")) {
        // If the user confirms, submit the form
        $(this).closest("form").submit();
      }
    });
});