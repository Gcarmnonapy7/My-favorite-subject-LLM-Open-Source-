//Variaveis para uso
const input = document.getElementById("#input");
const chat = document.getElementById("#chat");
const send = document.getElementById("#send");

async function sendMessage() {
  //Se o valor do input == a nulo retornará nada
  if (input.value == null|| input.value=="") return;
  let message = input.value;
  input.value = "";
  //Cria nova bolha de usuário
  let newBubble = CreateUserBubble();
  newBubble.innerHTML = message;
  chat.appendChild(newBubble);

  let newBotBubble = createBotBubble();
  chat.appendChild(newBotBubble);
  chatEnd();
  newBotBubble.innerHTML = "Carregando...";
  
  const awnser = await fetch ("http://127.0.0.1:5500/chatbot-ETEP/chat_bot/index.html",
    {method : "POST",
     headers : {"Content-Type":"application/json"},
     body : JSON.stringify({"msg":message})}
  );
};


function createUserBubble(){};

function createBotBubble(){};

function chatEnd() {};

send.addEventListener("click",sendMessage);
input.addEventListener("keyup",function(event){event.preventDefault(); 
  if (event =="Enter"){send.click();}
})