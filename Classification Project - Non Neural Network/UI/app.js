// Ensure Dropzone isn't auto-initialized (important if Dropzone script is included in the HTML).
Dropzone.autoDiscover = false;

// Initialize the functionality after the document is fully loaded.
$(document).ready(function() {
    console.log("Ready!");

    // Hide elements that should not be visible initially.
    $("#error").hide();
    $("#resultHolder").hide();
    $("#divClassTable").hide();

    initDropzone();
});

// Function to initialize Dropzone
function initDropzone() {
    let dz = new Dropzone("#dropzone", {
        url: "/classify_image/",  // Using relative URL to match the domain
        maxFiles: 1,
        addRemoveLinks: true,
        dictDefaultMessage: "Drop files here or click to upload",
        autoProcessQueue: false // Do not auto-process the queue to give us control over when to upload.
    });

    // Event when a file is added
    dz.on("addedfile", function() {
        // Ensure only one file is in the queue (remove any previous ones)
        if (dz.files[1]!=null) {
            dz.removeFile(dz.files[0]);
        }
    });

    // Setup the submit button to process the queue manually
    $("#submitBtn").on('click', function (e) {
        dz.processQueue();
    });

    // Handle the file upload response
    dz.on("complete", function (file) {
        if (file.status === "success") {
            let response = JSON.parse(file.xhr.responseText);
            updateUIWithResults(response.results);
        } else {
            displayError("Failed to process image.");
        }

        dz.removeFile(file); // Remove the file from the dropzone area once processed.
    });
}

// Function to update UI with results from the server
function updateUIWithResults(data) {
    if (!data || data.length === 0) {
        displayError("Can't classify image. Classifier was not able to detect face and two eyes properly.");
        return;
    }

    $("#error").hide();
    $("#resultHolder").show();
    $("#divClassTable").show();

    let players = ["lionel_messi", "maria_sharapova", "roger_federer", "serena_williams", "virat_kohli"];

    let match = data.reduce((prev, current) => {
        return (prev.class_probability[0] > current.class_probability[0]) ? prev : current;
    }, data[0]);

    $("#resultHolder").html($(`[data-player="${match.class}"`).html());

    for (let person of players) {
        let scoreElement = `#score_${person}`;
        let score = match.class_dictionary[person] !== undefined ? match.class_probability[match.class_dictionary[person]] : 0;
        $(scoreElement).html(score);
    }
}

// Function to display error messages
function displayError(message) {
    $("#error").text(message);
    $("#error").show();
    $("#resultHolder").hide();
    $("#divClassTable").hide();
}
