const speakBtn = document.getElementById('speak-btn');
const statusEl = document.getElementById('status');

const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang = 'en-IN';
recognition.interimResults = false;

speakBtn.addEventListener('click', () => {
  statusEl.innerText = "Listening...";
  recognition.start();
});

recognition.onresult = (event) => {
  const transcript = event.results[0][0].transcript;
  statusEl.innerText = "Processing...";
  sendQuery(transcript);
};

recognition.onerror = (event) => {
  console.error(event.error);
  statusEl.innerText = "Error recognizing voice. Try again.";
};

function sendQuery(query) {
  fetch('http://localhost:5000/process', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query })
  })
  .then(res => res.json())
  .then(data => {
    statusEl.innerText = "Response: " + data.response;
    speak(data.response);
  })
  .catch(err => {
    console.error(err);
    statusEl.innerText = "Error fetching response.";
  });
}

function speak(text) {
  const synth = window.speechSynthesis;
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = 'en-IN';
  synth.speak(utterance);
}
