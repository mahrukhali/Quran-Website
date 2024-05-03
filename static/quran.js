var element = document.getElementById("discard-btn");
if (typeof element != "undefined" && element != null) {
  element.addEventListener("click", function () {
    if (window.confirm("Are you sure you want to discard changes?")) {
      // If the user confirms, redirect to the view page without saving changes
      var pathArray = window.location.pathname.split("/");

      var itemId = pathArray[pathArray.length - 1];
      window.location.href = "/view/" + itemId;
    }
  });
}

document
  .getElementById("search-form")
  .addEventListener("submit", function (event) {
    var searchTerm = document.getElementById("search-input").value.trim();

    // Check if the search input is empty
    if (searchTerm === "") {
      console.log("comes here");
      // Prevent default form submission
      event.preventDefault();
      // Clear whitespace
      document.getElementById("search-input").value = "";
      // Keep focus on search input
      document.getElementById("search-input").focus();
    }
  });

// Define the container element where popular items will be inserted
var popularItemsContainer = document.getElementById("popular-items-container");

// Function to generate HTML for a single popular item
function createPopularItemHTML(item) {
  return `
    <div class="popular-item row " data-item-id="${item.id}">
      <div class="col-md-3">
        <a href="${item.verses}" target="_blank">
          <img src="${item.img}" alt=" Circle image of ${item["separa"]}" class="img-fluid smaller-image">
        </a>
      </div>
      <div class="col-md-9 align-self-center text-left pl-0">
        <u><h5 class="mt-0 title">${item.separa}</h5></u>
        <p class="mb-1">${item.summary}</p> 
        <p>${item.surahs}</p>
      </div>
    </div>
  `;
}

var popularItems = [
  {
    id: "1",
    img: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJgLPMGTMXkx2qEF-1YbjkC0uKhzqu_kzvJw&usqp=CAU",
    separa: "Alif Lam Meem",
    verses: "https://quran.com/en/an-nasr/1-3",
    summary: "The first verse invokes the name of the one God/Allah...",
    surahs: ["Al-Fatiha Verse 1", "Al-Baqarah Verse 141"],
  },
  {
    id: "8",
    img: "https://play-lh.googleusercontent.com/j0Bki3GKlrEH38yjXdO90CkbxUKc9r69shUDdgRQ9Of6xHDsTbIrKkn_9O-lD7xhH_E",
    separa: "Wa Lau Annana",
    verses: "https://www.clearquran.com/007.html",
    video: "https://www.youtube.com/watch?v=eTcU3Zf0sY8",
    ayahs: "75",
    summary:
      "Surah Anfal also called Surah Badr is the 8th chapter of the Quran..",
    surahs: ["Al-An'am Verse 111", "Al-A'raf Verse 87"],
  },
  {
    id: "10",
    img: "https://play-lh.googleusercontent.com/6SyW760mou2Yq_OF7Jf60WyzoK4WRk_aTX1YTDebWfSy6Wr4i98AnbyaPKDrK2fwC9Y",
    separa: "Wa A'lamu",
    verses: "https://www.clearquran.com/009.html",
    video: "https://www.youtube.com/watch?v=KWvLj5y46sA",
    ayahs: "109",
    summary:
      "This chapter makes a brief reference to the Prophet Jonah (v. 98)...",
    surahs: ["Al-Anfal Verse 41", "At-Tauba Verse 92"],
  },
];

// Generate HTML for each popular item and insert it into the container
popularItems.forEach(function (item) {
  var popularItemHTML = createPopularItemHTML(item);
  popularItemsContainer.innerHTML += popularItemHTML;
});

// Function to handle click events on popular items
function handlePopularItemClick(itemId) {
  // Redirect the user to the view page for the selected item
  window.location.href = "/view/" + itemId;
}

// Attach click event listeners to each popular item
var popularItems = document.querySelectorAll(".popular-item");
popularItems.forEach(function (item) {
  var itemId = item.dataset.itemId;
  item.addEventListener("click", function () {
    handlePopularItemClick(itemId);
  });
});

function handleAddItemFormSubmission(event) {
  event.preventDefault(); // Prevent default form submission

  // Remove existing error messages
  document.querySelectorAll(".error-message").forEach(function (errorMessage) {
    errorMessage.remove();
  });

  // Extract data from the form
  var newItemData = {
    img: document.getElementById("img").value,
    separa: document.getElementById("separa").value,
    ayahs: document.getElementById("ayahs").value,
    summary: document.getElementById("summary").value,
    verses: document.getElementById("verses").value,
    surahs: document.getElementById("surahs").value,
    video: document.getElementById("video").value,
    // Add other fields as necessary
  };

  var hasErrors = false; // Flag to track errors

  // Function to validate if a value is a number
  function isNumber(value) {
    return !isNaN(value);
  }

  // Function to display error message
  function displayErrorMessage(field, message) {
    var errorMessage = document.createElement("p");
    errorMessage.textContent = message;
    errorMessage.classList.add("error-message");
    errorMessage.style.color = "red";
    document
      .getElementById(field)
      .insertAdjacentElement("afterend", errorMessage);
  }

  // Validate each field separately
  for (var key in newItemData) {
    if (newItemData.hasOwnProperty(key)) {
      if (newItemData[key].trim() === "") {
        console.log("here");
        displayErrorMessage(key, "*Error: Field cannot be blank.");
        hasErrors = true;
      } else if (key !== "ayahs" && isNumber(newItemData[key])) {
        displayErrorMessage(key, "*Error: Field cannot be a number.");
        hasErrors = true;
      } else if (key === "ayahs" && !isNumber(newItemData[key])) {
        displayErrorMessage(key, "*Error: Ayahs must be a number.");
        hasErrors = true;
      } else if (key === "surahs") {
        var surahsArray = newItemData[key].split(",");
        surahsArray.forEach(function (surah) {
          if (surah.trim() === "") {
            displayErrorMessage(
              "surahs",
              "*Error: *Surah name cannot be blank."
            );
            hasErrors = true;
          } else if (isNumber(surah.trim())) {
            displayErrorMessage(
              "surahs",
              "Error: *Surah name cannot be a number."
            );
            hasErrors = true;
          }
        });
      }
    }
  }

  // If any error occurred, prevent form submission
  if (hasErrors) {
    return;
  }
  // Send a POST request to the server to add the new item
  $.ajax({
    type: "POST",
    url: "/add",
    contentType: "application/json",
    data: JSON.stringify(newItemData),
    success: function (response) {
      // Handle successful response here
      console.log(response);
      // For example, display a success message to the user
      var successMessage = document.createElement("p");
      successMessage.textContent = "New item added successfully!";
      var messageContainer = document.getElementById("message-container");
      messageContainer.appendChild(successMessage);

      // Extract the new item ID from the response
      var newItemId = response.id;
      // Construct the URL for viewing the item
      var viewItemUrl = "/view/" + newItemId;
      var viewItemLink = document.createElement("a");
      viewItemLink.href = viewItemUrl;
      viewItemLink.textContent = "View the new item";
      messageContainer.appendChild(viewItemLink);
      window.scrollTo(0, 0);
      // Clear the form fields
      document.getElementById("img").value = "";
      document.getElementById("separa").value = "";
      document.getElementById("ayahs").value = "";
      document.getElementById("summary").value = "";
      document.getElementById("verses").value = "";
      document.getElementById("video").value = "";
      document.getElementById("surahs").value = "";
      // Focus on the first input field
      document.getElementById("separa").focus();
    },
    error: function (xhr, status, error) {
      alert("Error adding new item. Please try again.");
    },
  });
}

// Event listeners for input fields to remove error messages on input
document.getElementById("img").addEventListener("input", function () {
  removeErrorMessage("img");
});

document.getElementById("separa").addEventListener("input", function () {
  removeErrorMessage("separa");
});

document.getElementById("ayahs").addEventListener("input", function () {
  removeErrorMessage("ayahs");
});

document.getElementById("summary").addEventListener("input", function () {
  removeErrorMessage("summary");
});

document.getElementById("verses").addEventListener("input", function () {
  removeErrorMessage("verses");
});

document.getElementById("video").addEventListener("input", function () {
  removeErrorMessage("video");
});
