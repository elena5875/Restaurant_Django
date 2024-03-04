document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("reservation-form").addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent default form submission
        
        // Get form data
        const formData = new FormData(this);
        const reservationData = {
            date: formData.get("date"),
            time: formData.get("time"),
            people: formData.get("people"),
            email: formData.get("email"),
            phone: formData.get("phone")
        };

        // Perform validation
        if (validateReservation(reservationData)) {
            // If validation passes, display confirmation message
            displayConfirmation(reservationData);
        }
    });
});

function validateReservation(data) {
    // Perform validation here (e.g., check if the date, time, etc., are valid)
    // You can implement custom validation rules based on your requirements

    // Here's a simple example just checking if all fields are filled
    if (!data.date || !data.time || !data.people || !data.email || !data.phone) {
        alert("Please fill in all fields.");
        return false;
    }

    // Check if the phone number contains only numbers and has a maximum of 9 digits
    const phoneRegex = /^\d{1,9}$/;
    if (!phoneRegex.test(data.phone)) {
        alert("Please enter a valid phone number (maximum 9 digits).");
        return false;
    }

    return true;
}

function displayConfirmation(data) {
    // Display confirmation message to the user
    const confirmationMessage = `Reservation Details:
    Date: ${data.date}
    Time: ${data.time}
    Number of People: ${data.people}
    Email: ${data.email}
    Phone: ${data.phone}`;

    alert("Reservation successful!\n\n" + confirmationMessage);
}
