let chatSocket = new ReconnectingWebSocket(
    'wss://' + window.location.host + window.location.pathname);

let currentUser = "{{ user.first_name|escapejs }}";

document.querySelector('.msg_history').scrollTop = 9999;

chatSocket.onopen = function(e) {
    console.log(e)
};

chatSocket.onmessage = function(e) {
    let data = JSON.parse(e.data);
    console.log(data);
    let message = data['message'];
    let user = data['user'];

    console.log(currentUser);
    let messageType = (currentUser === user) ? 'outgoing_msg' : 'incoming_msg';
    let messageType2 = (currentUser === user) ? 'sent_msg' : 'received_msg';

    let default_img = (currentUser !== user) ?`<div class="incoming_msg_img">
        <img src="https://ptetutorials.com/images/user-profile.png" alt="sunil">
    </div>` : '';

    $('.msg_history').append(`<div class="${messageType}">
        ${default_img}
        <div class="${messageType2}">
            <div class="received_withd_msg">
                <p>${message}</p>
                <span class="time_date">${moment().format('MMM. DD, YYYY, h:mm a')}</span>
            </div>
        </div>`);
    document.querySelector('.msg_history').scrollTop = 9999
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('.write_msg').focus();
document.querySelector('.write_msg').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('.msg_send_btn').click();
    }
};

document.querySelector('.msg_send_btn').onclick = function(e) {
    let messageInputDom = document.querySelector('.write_msg');
    let message = messageInputDom.value;
    if (message.length) {
        chatSocket.send(JSON.stringify({
            'message': message
        }));
    }

    messageInputDom.value = '';
};