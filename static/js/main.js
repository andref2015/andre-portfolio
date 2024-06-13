// Generalized function to fetch data from a given endpoint and update a specific element
function fetchDataAndUpdateDOM(endpoint, elementId) {
  fetch(endpoint)
    .then(response => response.text())
    .then(data => {
      document.getElementById(elementId).innerHTML = data;
    });
}

// Dedicated functions for fetching specific data using the generalized function
function fetchBitmap() {
  fetchDataAndUpdateDOM('/bitmap', 'bitmap');
}

function fetchJoke() {
  fetchDataAndUpdateDOM('/joke', 'joke');
}

function fetchNews() {
  fetchDataAndUpdateDOM('/news', 'newsDigest');
}

// Periodic updates and initial data loading
setInterval(fetchBitmap, 3000); // Update every 3 seconds

window.onload = function() {
  fetchNews();
};