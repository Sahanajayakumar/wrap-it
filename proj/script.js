const form = document.querySelector('form');
const input = document.querySelector('#video-url');

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const videoUrl = input.value;
  console.log(`Video URL: ${videoUrl}`);
  // Call function to retrieve video from backend using videoUrl
});
