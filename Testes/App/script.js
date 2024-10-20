const video = document.getElementById('myVideo');
const question = document.getElementById('question');
const answer = document.getElementById('answer');

// Tempo em segundos que a pergunta deve aparecer
const tempoDaPergunta = 3;

function showQuestion() {
    if (video.currentTime >= tempoDaPergunta) {
        video.pause();
        question.style.display = 'block';
        clearInterval(interval); // Para de verificar o tempo após a pergunta aparecer
    }
}

// Verifica o tempo do vídeo a cada segundo
const interval = setInterval(showQuestion, 1000);