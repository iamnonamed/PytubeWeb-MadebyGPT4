document.getElementById("download-form").addEventListener("submit", function (event) {
    const videoUrlInput = document.getElementById("video_url");
    const urlRegex = /^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$/;

    if (!urlRegex.test(videoUrlInput.value)) {
        event.preventDefault();
        alert("Please enter a valid YouTube video URL.");
    }
});
