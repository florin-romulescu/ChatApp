const socket = io(); // creating connection
const messageText = document.getElementById("text"); // the text input bar
const messageForm = document.getElementById("message-form"); // the form where we send messages

messageForm.addEventListener('submit', (event) => {
    event.preventDefault(); // the form does't send a post message to the server
    const message = messageText.value; //get the message from the input bar
    socket.emit("message", {data: message}); // send the message to the server
    messageText.value = "";
});

socket.on("connect", function() {
    socket.emit("connection", "I am connected!");
});

socket.on("message-handler", (response) => {
    console.log(response);
    const chatBox = document.getElementById("chat-box");
    chatBox.setAttribute('class', 'testClass');
    message = response.data;
    textBox = document.createTextNode(message + "\n");
    chatBox.appendChild(textBox);
});


