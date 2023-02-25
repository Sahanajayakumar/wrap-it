const express = require('express');
const app = express();

app.use(express.json());

app.post('/api/youtube', (req, res) => {
  const youtubeUrl = req.body.youtubeUrl;
  // Process the YouTube URL here
  console.log(youtubeUrl);
  res.sendStatus(200);
});

app.listen(5000, () => {
  console.log('Server started on port 5000');
});
