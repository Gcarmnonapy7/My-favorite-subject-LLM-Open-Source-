//Const for use
const input = document.getElementById("#input");
const chat = document.getElementById("#chat");
const send = document.getElementById("#send");

async function sendMessage() {
  //If the value of the input == "" or null return None
  if (input.value == null|| input.value=="") return;
  let message = input.value;
  input.value = "";
  //Creates new user bubble
  let newBubble = CreateUserBubble();
  newBubble.innerHTML = message;
  chat.appendChild(newBubble);
  //Creates new bot bubble
  let newBotBubble = createBotBubble();
  chat.appendChild(newBotBubble);
  chatEnd();
  //Loading message until the server respond and after that the server will pick the awnser of the bot in a JSON.strignify
  newBotBubble.innerHTML = "Loading...";
  
  const awnser = await fetch ("http://127.0.0.1:5500/chatbot-ETEP/chat_bot/index.html",
    {method : "POST",
     headers : {"Content-Type":"application/json"},
     body : JSON.stringify({"msg":message})}
  );
};


function createUserBubble(){
  //Create a element p for the user
  let bubble = document.createElement('p');
  bubble.classList = "chat_p--user";
  return bubble;
};

function createBotBubble(){
  //Create a element p for the bot
  let bubble = document.createElement('p');
  bubble.classList = "chat_p--bot";
  return bubble
};

function chatEnd() {
  chat.scrollTop = chat.scrollHeight;
};

//Activation of the sendMessage when the click on the button happens
// that will create new bubbles for the user and bot
send.addEventListener("click",sendMessage);
input.addEventListener("keyup",function(event){event.preventDefault(); 
  if (event =="Enter"){send.click();}
})