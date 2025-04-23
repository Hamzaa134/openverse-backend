document.getElementById("home-search-form").addEventListener("submit", async function (e) {
    e.preventDefault();
  
    const query = document.getElementById("home-search-input").value;
    const resultsContainer = document.querySelector(".results");
    
    // Clear previous results
    resultsContainer.innerHTML = `<h2>Search Results:</h2>`;
  
    try {
      const response = await fetch(`/api/search/?q=${query}`);
      const data = await response.json();
  
      if (!data.results || data.results.length === 0) {
        resultsContainer.innerHTML += "<p style='font-size: 16px; color: red;'>No results found.</p>";
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
            <a href="${item.url}" target="_blank" style="color: #007BFF;">View Full</a>
          `;
        } else if (item.media_type === "audio") {
          card.innerHTML = `
            <div style="height: 180px; display: flex; align-items: center; justify-content: center; background: #f9f9f9; border-radius: 6px; margin-bottom: 10px;">
              <audio controls style="width: 90%;">
                <source src="${item.url}" type="audio/mpeg">
                Your browser does not support the audio element.
              </audio>
            </div>
            <p><strong>Title:</strong> ${item.title || "Untitled"}</p>
            <p><strong>License:</strong> ${item.license || "Unknown"}</p>
            <a href="${item.url}" target="_blank" style="color: #007BFF;">Listen Full</a>
          `;
        }
  
        resultsContainer.appendChild(card);
      });
    } catch (error) {
      resultsContainer.innerHTML += `<p style='color: red;'>Error fetching results: ${error.message}</p>`;
    }
  });
  