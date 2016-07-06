# Boards Image Downloader
#### Um simples programa em PyQt4 que baixa imagens e vídeos de várias Imageboards!

### Descrição:

###### Este é um simples programa escrito em Python e utiliza PyQt4 para a utilização de uma interface gráfica (GUI) simples e leve.

###### Este programa realiza o download de imagens (.jpg, .png e .gif) e vídeos (.webm e .mp4) de um tópico escolhido em uma Imageboard escolhida.

###### Aqui estão as Imageboards que o programa suporta na atual versão:
- 4chan
- 8chan
- 55chan
- BRchan
- GUROchan

###### Ao escolher a Imageboard, a board e o tópico desejado, o programa irá fazer uma varredura para determinar a quantidade de imagens e vídeos disponíveis. Ele então irá fazer o download de todos os arquivos do tópico para a pasta que você tenha escolhido ou para a pasta 'Boards' do usuário atual, caso não tenha escolhido nenhuma pasta de destino.

![Boards Image Downloader](https://raw.githubusercontent.com/Wolfterro/wolfterro.github.io/master/posts/img/imagens_de_projetos/boards_image_downloader.png)

### [Verifique o CHANGELOG para maiores informações sobre novas versões](https://raw.github.com/Wolfterro/Boards-Image-Downloader/master/CHANGELOG.txt)

### Requisitos:

#### Compilando:
- Python 2.7
- PyQt4 para Python 2.7
- PyInstaller

###### Execute o PyInstaller para compilar o programa:

      - Linux:
      pyinstaller --noconsole --onefile "Boards Image Downloader.py"
      
      - Windows
      pyinstaller --icon="BID-Icon.ico" --noconsole --onefile "Boards Image Downloader.py"

#### Binário:
- ***Linux:*** Pode ser executado diretamente, sem qualquer requisito ou dependência.
- ***Windows:*** Requer o Microsoft Visual C++ 2010 Redistributable instalado (provavelmente já vem instalado em sistemas atualizados).

### Download:

#### Linux: https://github.com/Wolfterro/Boards-Image-Downloader/releases/tag/v1.1-Linux

#### Windows: https://github.com/Wolfterro/Boards-Image-Downloader/releases/tag/v1.1-Windows

###### Caso não possua o git e queira também baixar o repositório por completo, baixe através deste [Link](https://github.com/Wolfterro/Boards-Image-Downloader/archive/master.zip) ou clique em "Clone or Download", no topo da página.
