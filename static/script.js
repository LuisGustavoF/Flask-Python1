// static/script.js
document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('formPerfil');
  const botaoEnviar = document.getElementById('btnEnviar');

  form.addEventListener('submit', function() {
    botaoEnviar.textContent = 'Enviando...';
    botaoEnviar.disabled = true;
  });
});

document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('formPerfil');
  const botaoEnviar = document.getElementById('btnEnviar');
  const botaoVoltar = document.getElementById('btnVoltar');

  if (botaoVoltar) {
    botaoVoltar.addEventListener('click', function() {
      window.location.href = urlPerfil;
    });
  }

  if (form) {
    form.addEventListener('submit', function() {
      botaoEnviar.textContent = 'Enviando...';
      botaoEnviar.disabled = true;
    });
  }
});
