$("#country").change(function(){
    var country_id = $(this).val();
    
    if (country_id) {
        $("#state").prop('disabled', false);

        $.ajax({
            url: '/vendor/get_state/', 
            data: {'country_id' : country_id},
            success: function(data) {
                var State = $('#state');
                console.log(State);
                State.empty();
                State.append($('<option>', { value : '', text : 'Select State' }));              
                $.each(data.states, function(i, state){
                    State.append($('<option>', { value : state.id, text : state.name }));
                });
            }
        });
    }

    else {
        $("#state").prop('disabled', true);
        $("#city").prop('disabled', true);
        $("#state").empty().append('<option value = ""> Select State </option>');
        $("#city").empty().append('<option value = ""> Select City </option>');
    }
});

$("#state").change(function(){
    var state_id = $(this).val();

    if (state_id) {
        $("#city").prop('disabled', false);

        $.ajax({
            url : '/vendor/get_city/', 
            data : {'state_id' : state_id},
            success : function(data) {
                var City = $('#city');
                console.log(City);
                City.empty();
                City.append($('<option>', { value : '', text : 'Select City' }));
                $.each(data.city, function(i, city){
                    City.append($('<option>', { value : city.id, text : city.name }));
                });
            }
        });
    }

    else {
        $("#city").prop('disabled', true);
        $("#city").empty().append('<option value = ""> Select City </option>');
    }

});