<!DOCTYPE html>
<html>
<head>
    <title>챗봇</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
</head>
<body>
    <h1>챗봇</h1>
    
    <div id="chat-container">
        <div id="chat-log"></div>
        <input type="text" id="user-input">
        <button id="send-button">전송</button>
    </div>
    
    <script>
        $(document).ready(function() {
            // 전송 버튼 클릭 이벤트 처리
            $('#send-button').click(function() {
                sendMessage();
            });
            
            // 입력 필드에서 엔터 키 입력 이벤트 처리
            $('#user-input').keypress(function(event) {
                if (event.which === 13) {
                    sendMessage();
                }
            });
            
            // 메시지 전송 함수
            function sendMessage() {
                var userInput = $('#user-input').val();
                
                // 사용자 입력 로그에 표시
                var userLog = $('<p>').addClass('user-log').text(userInput);
                $('#chat-log').append(userLog);
                
                // 사용자 입력을 서버로 전송하고 응답 받기
                $.get('/get_response/', {msg: userInput}, function(response) {
                    var chatbotResponse = response.response;
                    
                    // 챗봇 응답 로그에 표시
                    var chatbotLog = $('<p>').addClass('chatbot-log').text(chatbotResponse);
                    $('#chat-log').append(chatbotLog);
                    
                    // 입력 필드 초기화
                    $('#user-input').val('');
                });
            }
        });
    </script>
</body>
</html>
