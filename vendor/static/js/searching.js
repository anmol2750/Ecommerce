
$(document).ready(function() {
    $('#search').on('input', function() {
        var query = $(this).val();

        $.ajax({

            url: '/vendor/search/',        //URL pattern defined in your urls.py
            data: { 'query' : query },
            dataType: 'json',
            success: function(data) {
                // Clear previous search results
                $('#table tbody').empty();
                    
                if (data.length === 0) {
                    $('#no_results_message').show();
                }
                else {

                    $('#no_results_message').hide();

                    // Append new search results to the table
                    $.each(data, function(index, item) {

                        var row = $(
                            '<tr><td><center>' + item.id + 
                            '</td><td><center>' + item.date_joined + 
                            '</td><td><center><img src = "' + item.logo + '" alt = "user logo" width = "40px" height = "40px" style = "border-radius : 50%;" >' +
                            '</td><td><center>' + item.username + 
                            '</td><td><center>' + item.email + 
                            '</td><td><center>' + item.first_name + 
                            '</td><td><center>' + item.last_name +  
                            '</td></tr>'
                        );

                        // Create the Status cell based on is_active
                        var statusCell = $('<td><center>' + (item.is_active ? 'Active' : 'Inactive') + '</td>');

                        // Create the Action cell
                        var actionCell = $('<td><center></td>');
                        var acceptButton = $('<button type = "submit" name = "action" value = "accept" class =  "action-button active-button btn btn-outline-primary btn-sm"><i class="fa-solid fa-circle-check"></i></button>');
                        acceptButton.on('click', function() {
                        // Handle button click event, e.g., open a link
                            window.location.href = "/vendor/action/";
                        });
                        var rejectButton = $('<button type = "submit" name = "action" value = "reject" class =  "action-button active-button btn btn-outline-primary btn-sm"><i class="fa-solid fa-circle-xmark"></i></button>');
                        rejectButton.on('click', function() {
                        // Handle button click event, e.g., open a link
                            window.location.href = "/vendor/action/";
                        });
                        acceptButton.css('margin-right', '3px');
                        actionCell.append(acceptButton, rejectButton);

                        // Create the Update cell
                        var updateCell = $('<td></td>');
                        var editButton = $('<button class = "btn btn-outline-primary btn-sm"><i class="fas fa-edit"></i></button>');
                        editButton.on('click', function() {
                        // Handle button click event, e.g., open a link
                            window.location.href = "/vendor/updatevendor/" + item.id;
                        });
                        updateCell.append(editButton);

                        // Create the Delete cell
                        var deleteCell = $('<td></td>');
                        var deleteButton = $('<button class = "btn btn-outline-primary btn-sm"><i class="fa-solid fa-trash"></i></button>');
                        deleteButton.on('click', function() {
                        // Handle button click event, e.g., open a link
                            window.location.href = "#";
                        });
                        deleteCell.append(deleteButton);

                        // Create the View cell
                        var viewCell = $('<td><center></td>');
                        var viewButton = $('<button class = "btn btn-link btn-sm">View</button>');
                        viewButton.on('click', function() {
                        // Handle button click event, e.g., open a link
                            window.location.href = "/vendor/vendordetails/" + item.id;
                        });
                        viewCell.append(viewButton);

                        row.append(statusCell);         // Add the Status cell to the row

                        row.append(actionCell);        // Add the Action cell to the row

                        row.append(updateCell);        // Add the Update cell to the row

                        row.append(deleteCell);        // Add the Delete cell to the row

                        row.append(viewCell);          // Add the View cell to the row

                        $('#table tbody').append(row);
                    });
                }
            }                
        });
    });
}); 
