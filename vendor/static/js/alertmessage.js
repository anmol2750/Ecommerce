function confirmReject(username, action) {
    console.log('Action: ${action}')
    if (action === 'reject' && !confirm('Do you really want to reject the vendor : ' + username)) {
        event.preventDefault(); // Prevent form submission if "Cancel" is clicked
        return;
    }
}