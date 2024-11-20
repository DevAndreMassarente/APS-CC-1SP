document.addEventListener('DOMContentLoaded', function() {
    const votoInput = document.getElementById('voto');
    const sugestoesVoto = document.getElementById('sugestoes-voto');
    const votarBtn = document.getElementById('votar-btn');
    const naoTenhoTimeBtn = document.getElementById('nao-tenho-time-btn');
    const confirmacaoModal = document.getElementById('confirmacao-modal');
    const confirmacaoMensagem = document.getElementById('confirmacao-mensagem');
    const confirmarVotoBtn = document.getElementById('confirmar-voto-btn');
    const cancelarBtn = document.getElementById('cancelar-btn');
    const logoClube = document.getElementById('logo-clube');
    const logoContainer = document.querySelector('.logo-container');
    let currentForm;

    function adicionarAnimacaoPulsar(elemento) {
        elemento.classList.add('pulsar');
        elemento.addEventListener('animationend', () => {
            elemento.classList.remove('pulsar');
        });
    }

    function atualizarLogo(time) {
        if (!time) {
            logoClube.style.display = 'none';
            resetarCoresLaterais();
            return;
        }

        const logoPath = `/static/logoclubes/${time.replace(/\s+/g, '')}.png`;
        logoClube.style.opacity = '0';

        fetch(logoPath)
            .then(response => {
                if (response.ok) {
                    logoClube.src = logoPath;
                    logoClube.style.display = 'block';
                    console.log(`Logo do clube ${time} carregada com sucesso.`);

                    setTimeout(() => {
                        logoClube.style.opacity = '1';
                        adicionarAnimacaoPulsar(logoContainer);
                    }, 300);

                    // Atualizar cores laterais
                    atualizarCoresLaterais(time);
                } else {
                    logoClube.style.display = 'none';
                    console.log(`Logo do clube ${time} não encontrada.`);
                    resetarCoresLaterais();
                }
            })
            .catch(error => {
                console.error('Erro ao carregar a logo:', error);
                logoClube.style.display = 'none';
                resetarCoresLaterais();
            });
    }

    function atualizarCoresLaterais(time) {
        fetch('/get_cores_time', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ time: time }),
        })
        .then(response => response.json())
        .then(data => {
            const cores = data.cores || ['transparent', 'transparent'];
            document.body.style.setProperty('--cor-esquerda', cores[0]);
            document.body.style.setProperty('--cor-direita', cores[1] || cores[0]);
        })
        .catch(error => {
            console.error('Erro ao obter cores do time:', error);
            resetarCoresLaterais();
        });
    }

    function resetarCoresLaterais() {
        document.body.style.setProperty('--cor-esquerda', 'transparent');
        document.body.style.setProperty('--cor-direita', 'transparent');
    }

    votoInput.addEventListener('input', function() {
        const query = votoInput.value.toLowerCase();
        if (query === '') {
            atualizarLogo('');
            return;
        }
        fetch(`/autocomplete?query=${query}`)
            .then(response => response.json())
            .then(data => {
                sugestoesVoto.innerHTML = '';
                data.forEach(time => {
                    if (time.toLowerCase().includes(query)) {
                        const li = document.createElement('li');
                        li.textContent = time;
                        li.addEventListener('click', function() {
                            votoInput.value = time;
                            sugestoesVoto.innerHTML = '';
                            adicionarAnimacaoPulsar(votoInput);
                            atualizarLogo(time);
                        });
                        sugestoesVoto.appendChild(li);
                    }
                });
            });
    });

    votarBtn.addEventListener('click', function() {
        const voto = votoInput.value;
        if (voto) {
            confirmacaoMensagem.textContent = `Você está votando no time: ${voto}. Confirmar voto?`;
            confirmacaoModal.style.display = 'block';
            currentForm = document.getElementById('voto-form');
            adicionarAnimacaoPulsar(confirmacaoModal);
        } else {
            alert('Por favor, escolha um time antes de votar.');
        }
    });

    naoTenhoTimeBtn.addEventListener('click', function() {
        confirmacaoMensagem.textContent = 'Você está votando como "Não tenho um time". Confirmar voto?';
        confirmacaoModal.style.display = 'block';
        currentForm = document.getElementById('nao-tenho-time-form');
        adicionarAnimacaoPulsar(confirmacaoModal);
    });

    confirmarVotoBtn.addEventListener('click', function() {
        confirmacaoModal.style.display = 'none';
        const container = document.querySelector('.container');
        adicionarAnimacaoPulsar(container);
        setTimeout(() => {
            currentForm.submit();
        }, 500);
    });

    cancelarBtn.addEventListener('click', function() {
        confirmacaoModal.style.display = 'none';
    });

    [votarBtn, naoTenhoTimeBtn, confirmarVotoBtn, cancelarBtn].forEach(btn => {
        btn.addEventListener('mouseover', () => {
            btn.style.transform = 'translateY(-2px)';
            btn.style.boxShadow = '0 5px 15px rgba(0, 0, 0, 0.1)';
        });
        btn.addEventListener('mouseout', () => {
            btn.style.transform = 'translateY(0)';
            btn.style.boxShadow = 'none';
        });
    });

    const titulo = document.querySelector('h1');
    const textoOriginal = titulo.textContent;
    titulo.textContent = '';
    let index = 0;

    function digitarTitulo() {
        if (index < textoOriginal.length) {
            titulo.textContent += textoOriginal.charAt(index);
            index++;
            setTimeout(digitarTitulo, 100);
        }
    }

    digitarTitulo();
});document.addEventListener('DOMContentLoaded', function() {
    const votoInput = document.getElementById('voto');
    const sugestoesVoto = document.getElementById('sugestoes-voto');
    const votarBtn = document.getElementById('votar-btn');
    const naoTenhoTimeBtn = document.getElementById('nao-tenho-time-btn');
    const confirmacaoModal = document.getElementById('confirmacao-modal');
    const confirmacaoMensagem = document.getElementById('confirmacao-mensagem');
    const confirmarVotoBtn = document.getElementById('confirmar-voto-btn');
    const cancelarBtn = document.getElementById('cancelar-btn');
    const logoClube = document.getElementById('logo-clube');
    const logoContainer = document.querySelector('.logo-container');
    let currentForm;

    function adicionarAnimacaoPulsar(elemento) {
        elemento.classList.add('pulsar');
        elemento.addEventListener('animationend', () => {
            elemento.classList.remove('pulsar');
        });
    }

    function atualizarLogo(time) {
        if (!time) {
            logoClube.style.display = 'none';
            resetarCoresLaterais();
            return;
        }

        const logoPath = `/static/logoclubes/${time.replace(/\s+/g, '')}.png`;
        logoClube.style.opacity = '0';

        fetch(logoPath)
            .then(response => {
                if (response.ok) {
                    logoClube.src = logoPath;
                    logoClube.style.display = 'block';
                    console.log(`Logo do clube ${time} carregada com sucesso.`);

                    setTimeout(() => {
                        logoClube.style.opacity = '1';
                        adicionarAnimacaoPulsar(logoContainer);
                    }, 300);

                    // Atualizar cores laterais
                    atualizarCoresLaterais(time);
                } else {
                    logoClube.style.display = 'none';
                    console.log(`Logo do clube ${time} não encontrada.`);
                    resetarCoresLaterais();
                }
            })
            .catch(error => {
                console.error('Erro ao carregar a logo:', error);
                logoClube.style.display = 'none';
                resetarCoresLaterais();
            });
    }

    function atualizarCoresLaterais(time) {
        fetch('/get_cores_time', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ time: time }),
        })
        .then(response => response.json())
        .then(data => {
            const cores = data.cores || ['transparent', 'transparent'];
            document.body.style.setProperty('--cor-esquerda', cores[0]);
            document.body.style.setProperty('--cor-direita', cores[1] || cores[0]);
        })
        .catch(error => {
            console.error('Erro ao obter cores do time:', error);
            resetarCoresLaterais();
        });
    }

    function resetarCoresLaterais() {
        document.body.style.setProperty('--cor-esquerda', 'transparent');
        document.body.style.setProperty('--cor-direita', 'transparent');
    }

    votoInput.addEventListener('input', function() {
        const query = votoInput.value.toLowerCase();
        if (query === '') {
            atualizarLogo('');
            return;
        }
        fetch(`/autocomplete?query=${query}`)
            .then(response => response.json())
            .then(data => {
                sugestoesVoto.innerHTML = '';
                data.forEach(time => {
                    if (time.toLowerCase().includes(query)) {
                        const li = document.createElement('li');
                        li.textContent = time;
                        li.addEventListener('click', function() {
                            votoInput.value = time;
                            sugestoesVoto.innerHTML = '';
                            adicionarAnimacaoPulsar(votoInput);
                            atualizarLogo(time);
                        });
                        sugestoesVoto.appendChild(li);
                    }
                });
            });
    });

    votarBtn.addEventListener('click', function() {
        const voto = votoInput.value;
        if (voto) {
            confirmacaoMensagem.textContent = `Você está votando no time: ${voto}. Confirmar voto?`;
            confirmacaoModal.style.display = 'block';
            currentForm = document.getElementById('voto-form');
            adicionarAnimacaoPulsar(confirmacaoModal);
        } else {
            alert('Por favor, escolha um time antes de votar.');
        }
    });

    naoTenhoTimeBtn.addEventListener('click', function() {
        confirmacaoMensagem.textContent = 'Você está votando como "Não tenho um time". Confirmar voto?';
        confirmacaoModal.style.display = 'block';
        currentForm = document.getElementById('nao-tenho-time-form');
        adicionarAnimacaoPulsar(confirmacaoModal);
    });

    confirmarVotoBtn.addEventListener('click', function() {
        confirmacaoModal.style.display = 'none';
        const container = document.querySelector('.container');
        adicionarAnimacaoPulsar(container);
        setTimeout(() => {
            currentForm.submit();
        }, 500);
    });

    cancelarBtn.addEventListener('click', function() {
        confirmacaoModal.style.display = 'none';
    });

    [votarBtn, naoTenhoTimeBtn, confirmarVotoBtn, cancelarBtn].forEach(btn => {
        btn.addEventListener('mouseover', () => {
            btn.style.transform = 'translateY(-2px)';
            btn.style.boxShadow = '0 5px 15px rgba(0, 0, 0, 0.1)';
        });
        btn.addEventListener('mouseout', () => {
            btn.style.transform = 'translateY(0)';
            btn.style.boxShadow = 'none';
        });
    });

    const titulo = document.querySelector('h1');
    const textoOriginal = titulo.textContent;
    titulo.textContent = '';
    let index = 0;

    function digitarTitulo() {
        if (index < textoOriginal.length) {
            titulo.textContent += textoOriginal.charAt(index);
            index++;
            setTimeout(digitarTitulo, 100);
        }
    }

    digitarTitulo();
});