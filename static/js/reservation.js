// Function to send a mock email (replace this with your actual email sending logic)
function sendMockEmail(formData) {
    // Log the email details to the console
    console.log('Mock email sent:', formData);

    // Display a confirmation message to the user
    displayConfirmation(formData);
}

// Function to validate reservation form data
function validateReservation(data) {
    // Checking if all fields are filled
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

// Function to display a confirmation message
function displayConfirmation(data) {
    // Construct the confirmation message
    const confirmationMessage = `Reservation successful!\n\nReservation Details:
        Date: ${data.date}
        Time: ${data.time}
        Number of People: ${data.people}
        Email: ${data.email}
        Phone: ${data.phone}`;

    // Display the confirmation message to the user
    alert(confirmationMessage);
}

// Add an event listener to the reservation form submission
document.getElementById("reservation-form").addEventListener("submit", function(event) {
    event.preventDefault();

    // Get form data
    const formData = {
        date: document.getElementById('date').value,
        time: document.getElementById('time').value,
        people: document.getElementById('people').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value
    };

    // Validate form data
    if (validateReservation(formData)) {
        // If validation passes, send a mock email
        sendMockEmail(formData);
    } else {
        // Optionally, show an error message to the user
    }
});
