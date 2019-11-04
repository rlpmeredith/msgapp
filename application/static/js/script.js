var currentChat
var currentUser
const loadedMessages = new Set();

const retrieveMessages = (chat_id, user_id) => {
    const url = `/api/chats/${chat_id}/messages?user_id=${user_id}`
    fetch(url, {
        method: 'GET'
    }).then(res => res.json())
       .then(data => addMessages(data))
}

const conversationElements = document.getElementsByClassName("convo");

const convoClick = (event) => {

    // populate form chat_id input
    const clicked = event.currentTarget;
    const dataAttributes = clicked.dataset
    const chat_id = dataAttributes.chat_id
    const user_id = dataAttributes.user_id
    currentChat = chat_id
    currentUser = user_id
    document.querySelector('#sndr-chat_id').value = chat_id;

     // clear out messages
    let pageElement = document.querySelector('#main-chat-wrap');
    pageElement.innerHTML = ''
    loadedMessages.clear();

    // retrieve messages for clicked conversation
    retrieveMessages(chat_id, user_id)
}

for(let i = 0; i < conversationElements.length; i++) {
    conversationElements[i].addEventListener('click', convoClick, false);
}

const createMessage = (message) => {

    let msgWrap = document.createElement('div');
    msgWrap.classList.add('message-wrap');

    let messageIo = document.createElement('div');
    var urlParams = new URLSearchParams(window.location.search);
    var user_id = urlParams.get("user_id");
    messageIo.classList.add('message')
    if (message.userfrom.uid == user_id) {
        messageIo.classList.add('out')
      } else {
        messageIo.classList.add('in')
      }
    // messageIo.classList.add( message.uid == user_id ? 'out' : 'in')

    // let messageIo = document.createElement('div')
    // messageIo.classList.add('message')
    // if message.user_id = 
    
    // let msgOut = document.createElement('div');
    // msgOut.classList.add('message', 'out');

    let msgP = document.createElement('p');
    msgP.classList.add("mssg");
    msgP.innerHTML =  message.text
        
    let msgTime = document.createElement('p');
    msgTime.classList.add("mssg-time");
    msgTime.innerHTML =  message.timestamp;


    
    messageIo.appendChild(msgP);
    messageIo.appendChild(msgTime);

    msgWrap.appendChild(messageIo);
    

    let pageElement = document.querySelector('#main-chat-wrap');
    pageElement.appendChild(msgWrap)
    
}


const addMessages = (messages) =>{
    for(const message of messages) {
        if(!loadedMessages.has(message.mid)) {
            loadedMessages.add(message.mid);
            createMessage(message);
        }
    }
}

const deleteMessages = () => {
    document.querySelector('#main-chat-wrap').innerHTML = ''
}

setInterval(() => {
    if (currentChat !== null && currentUser != null) {
        retrieveMessages(currentChat, currentUser)   }
}, 2000);

const submitNewMessage = () => {
    const newMessage = document.querySelector('#new-message').value;
    const chat_id = document.querySelector('#sndr-chat_id').value
    const user_id = document.querySelector('#sndr-user_id').value

    const url = `/api/chats/${chat_id}/messages?user_id=${user_id}`

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'message': newMessage
        })
    })
    .then(res => res.json())
    // .then(data => createMessage(data));   
    // console.log(data.mid) 
    // loadedMessages.add(data.mid)                                                        
    // document.querySelector('#new-message').value = '';                                                                                                                                                    
}

function updateScroll(){
    var scrolldiv = document.getElementById("main-chat-wrap");
    scrolldiv.scrollTop = scrolldiv.scrollHeight;
}
setInterval(updateScroll,500);
