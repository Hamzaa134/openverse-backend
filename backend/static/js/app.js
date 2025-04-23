document.addEventListener("DOMContentLoaded", function () {
  const resetBtn = document.getElementById("clear-filters");
  const searchForm = document.querySelector("form");
  const licenseSelect = document.getElementById("license-filter");
  const mediaTypeSelect = document.getElementById("media-type");
  const searchInput = document.querySelector("input[type='text']");
  const resultsContainer = document.querySelector(".results");

  async function fetchAndDisplayResults() {
    const query = searchInput.value;
    const license = licenseSelect.value;
    const mediaType = mediaTypeSelect.value;

    let url = `/api/search/?q=${encodeURIComponent(query)}`;
    if (license) url += `&license=${encodeURIComponent(license)}`;
    if (mediaType && mediaType !== "all") url += `&media_type=${encodeURIComponent(mediaType)}`;

    try {
      const response = await fetch(url);
      const data = await response.json();

      resultsContainer.innerHTML = "<h2>Search Results:</h2>";

      if (!data.results || data.results.length === 0) {
        resultsContainer.innerHTML += "<p>No results found.</p>";
        return;
      }

      data.results.forEach(item => {
        const card = document.createElement("div");
        card.className = "media-card";

        if (item.media_type === "image") {
          card.innerHTML = `
            <img src="${item.url}" alt="media result" />
            <p><strong>Title:</strong> ${item.title || "Untitled"}</p>
            <p><strong>License:</strong> ${item.license || "Unknown"}</p>
            <a href="${item.url}" target="_blank">View Full</a>
          `;
        } else if (item.media_type === "audio") {
          card.innerHTML = `
            <audio controls src="${item.url}"></audio>
            <p><strong>Title:</strong> ${item.title || "Untitled"}</p>
            <p><strong>License:</strong> ${item.license || "Unknown"}</p>
            <a href="${item.url}" target="_blank">Listen Full</a>
          `;
        }

        resultsContainer.appendChild(card);
      });
    } catch (error) {
      console.error("Error fetching data:", error);
      alert("Something went wrong. Please try again later.");
    }
  }

  searchForm.addEventListener("submit", function (e) {
    e.preventDefault();
    fetchAndDisplayResults();
  });

  licenseSelect.addEventListener("change", fetchAndDisplayResults);
  mediaTypeSelect.addEventListener("change", fetchAndDisplayResults);

  if (resetBtn) {
    resetBtn.addEventListener("click", function (e) {
      e.preventDefault();

      console.log("Reset button clicked!");

      licenseSelect.value = '';
      mediaTypeSelect.value = 'all';
      searchInput.value = '';

      fetchAndDisplayResults();
    });
  } else {
    console.log("Reset button not found");
  }
});
