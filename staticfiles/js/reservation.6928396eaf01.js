// reservation.js
// Initialize EmailJS with your user ID

emailjs.init('Owrv1SDMAjElxr32G');

// Function to send email using EmailJS
function sendEmail(formData) {
    emailjs.send('service_6mvg1rq', 'template_a8d0erf', formData)
        .then(function(response) {
            console.log('Email sent successfully:', response);
            displayConfirmation(formData); // Display confirmation message after email is sent successfully
        })
        .catch(function(error) {
            console.error('Error sending email:', error);
            alert('There was an error sending your reservation. Please try again later.');
        });
}

// Function to validate reservation form data
function validateReservation(data) {
    // checking if all fields are filled
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

// Function to display confirmation message
function displayConfirmation(data) {
    // Construct confirmation message
    const confirmationMessage = `Reservation successful!\n\nReservation Details:
        Date: ${data.date}
        Time: ${data.time}
        Number of People: ${data.people}
        Email: ${data.email}
        Phone: ${data.phone}`;

    // Display confirmation message to the user
    alert(confirmationMessage);
}

// Add event listener to reservation form submission
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
        // If validation passes, send email using EmailJS
        sendEmail(formData);
    } else {
        // Optionally, show an error message to the user
    }
});
