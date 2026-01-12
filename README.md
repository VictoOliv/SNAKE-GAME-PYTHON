# 🐍 Snake Game - Python

Um jogo clássico da Cobra (Snake) implementado em Python usando a biblioteca `curses` para interface no terminal.

## 📋 Descrição

Este projeto é uma implementação do famoso jogo Snake, onde você controla uma cobra que deve comer frutas para crescer e aumentar sua pontuação. O jogo termina quando a cobra colide com as bordas da tela ou com seu próprio corpo.

## ✨ Funcionalidades

- 🎮 Controle da cobra usando as setas do teclado
- 🍎 Sistema de frutas que aparecem aleatoriamente na tela
- 📊 Sistema de pontuação
- ⚡ Três níveis de dificuldade (fácil, médio, difícil)
- 🎯 Detecção de colisões (bordas e corpo da cobra)
- 🎨 Interface visual no terminal com bordas e caracteres especiais

## 📚 Bibliotecas Utilizadas

Este projeto utiliza apenas bibliotecas padrão do Python:

- **`curses`**: Biblioteca para criação de interfaces de texto interativas no terminal
  - Usada para desenhar a tela, controlar a entrada do teclado e criar a interface visual
  - Disponível nativamente no Python (Windows requer instalação adicional)

- **`random`**: Biblioteca para geração de números aleatórios
  - Usada para posicionar as frutas aleatoriamente na tela

- **`time`**: Biblioteca para operações relacionadas a tempo
  - Usada para pausar a tela de "Game Over" antes de fechar

## 🚀 Como Executar

### Pré-requisitos

- Python 3.11 ou superior
- No Windows, você pode precisar instalar o pacote `windows-curses`:
  ```bash
  pip install windows-curses
  ```

### Executando o Jogo

1. Clone o repositório ou baixe os arquivos:
   ```bash
   git clone https://github.com/seu-usuario/SNAKE-GAME-PYTHON.git
   cd SNAKE-GAME-PYTHON
   ```

2. Execute o arquivo principal:
   ```bash
   python main.py
   ```

3. Escolha a dificuldade quando solicitado:
   - `easy`: Velocidade lenta (1000ms)
   - `medium`: Velocidade média (100ms)
   - `hard`: Velocidade rápida (10ms)

## 🎮 Controles

- **↑ (Seta para cima)**: Move a cobra para cima
- **↓ (Seta para baixo)**: Move a cobra para baixo
- **← (Seta para esquerda)**: Move a cobra para esquerda
- **→ (Seta para direita)**: Move a cobra para direita

**Nota**: A cobra não pode se mover na direção oposta à atual (ex: se está indo para baixo, não pode ir para cima diretamente).

## 🎯 Regras do Jogo

1. A cobra começa com 4 segmentos
2. Quando a cobra come uma fruta (`@`), ela cresce e sua pontuação aumenta
3. O jogo termina quando:
   - A cobra colide com as bordas da tela
   - A cobra colide com seu próprio corpo
4. A pontuação final é exibida na tela de "Game Over"

## 📁 Estrutura do Código

```
Snake-game-python/
│
├── main.py          # Arquivo principal com toda a lógica do jogo
└── README.md        # Este arquivo
```

### Principais Funções

- `game_loop()`: Loop principal do jogo
- `draw_screen()`: Desenha a tela e bordas
- `draw_snake()`: Desenha a cobra na tela
- `move_snake()`: Move a cobra baseado na direção
- `snake_hit_fruit()`: Verifica se a cobra comeu uma fruta
- `snake_hit_border()`: Verifica colisão com bordas
- `snake_hit_itself()`: Verifica colisão com o próprio corpo
- `select_dificult()`: Permite escolher a dificuldade do jogo

## 🛠️ Tecnologias

- **Python 3.11+**
- **curses** (biblioteca padrão)
- **random** (biblioteca padrão)
- **time** (biblioteca padrão)

## 📝 Notas

- O jogo funciona melhor em terminais que suportam curses
- No Windows, certifique-se de ter o pacote `windows-curses` instalado
- O tamanho da janela do terminal afeta o tamanho da área de jogo

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📄 Licença

Este projeto é de código aberto e está disponível para uso livre.

---

Desenvolvido com ❤️ usando Python 3.11.9

