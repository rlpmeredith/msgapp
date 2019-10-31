const retrieveMessages = (req_info) => {
    const url = `/api/chats/${req_info.chat_id}/messages?user_id=${req_info.user_id}`
    fetch(url, {
        method: 'GET'
    }).then(res => res.json())
       .then(data => addMessages(data))
}

const conversationElements = document.getElementsByClassName("convo");

const convoClick = (event) => {
    const clicked = event.currentTarget;
    console.log(clicked.dataset)
    deleteMessages()
    retrieveMessages(clicked.dataset);
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
    messageIo.classList.add( message.id == user_id ? 'out' : 'in')

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


const addMessages = (messages) => {
    messages.forEach(msg => createMessage(msg));
}

const deleteMessages = () => {
    document.querySelector('#main-chat-wrap').innerHTML = ''
}
