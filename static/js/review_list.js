// review_list.js

// Define a function to fetch recent reviews
function fetchRecentReviews() {
    // Make an AJAX request to fetch recent reviews
    // You need to replace 'url_to_fetch_reviews' with the actual URL endpoint for fetching reviews
    fetch('url_to_fetch_reviews')
        .then(response => response.json())
        .then(reviews => {
            // Clear existing content
            const recentReviewsList = document.getElementById('recent-reviews-list');
            recentReviewsList.innerHTML = '';

            // Populate the list with fetched reviews
            reviews.forEach(review => {
                const li = document.createElement('li');
                li.textContent = review.title + ' - ' + review.content;
                recentReviewsList.appendChild(li);
            });
        })
        .catch(error => console.error('Error fetching recent reviews:', error));
}

// Call the fetchRecentReviews function when the page loads
window.onload = fetchRecentReviews;
