# Boards Image Downloader
#### Um simples programa em PyQt4 que baixa imagens e vídeos de várias Imageboards!

### Descrição:

###### Este é um simples programa escrito em Python e utiliza PyQt4 para a utilização de uma interface gráfica (GUI) simples e leve.

###### Este programa realiza o download de imagens (.jpg, .png, .gif e .pdf) e vídeos (.webm, .mp4 e .swf) de um tópico escolhido em uma Imageboard.

###### Basta o usuário escolher a Imageboard desejada e inserir a ID do tópico e a board onde o tópico se encontra. O usuário deverá escolher também a pasta de destino onde será armazenado os arquivos.

###### É necessário que o arquivo de configurações 'imageboards.ini' esteja presente junto ao programa, pois é neste arquivo que estarão todas as informações necessárias para que o programa possa listar as imageboards e fazer o download dos arquivos. 

###### Aqui estão as Imageboards que o programa suporta na atual versão:
- 4chan
- 8chan
- GUROchan

###### O usuário tem a opção de inserir as suas imageboards favoritas no arquivo de configurações, ficando atento as exigências descritas nos comentários do arquivo!

### Opções do Programa:

###### O usuário também poderá usar algumas opções do programa, tais como:
- Abrir a pasta de destino quando o download for concluído
- Substituir arquivos existentes (por padrão, o programa pula o download de arquivos existentes)
- Criar subpasta para o tópico (com o nome do tópico e a ID, ex: Tópico-[123456])
- Selecionar o tipo de arquivo a ser salvo (Salvar tudo, Apenas imagens, Apenas vídeos)

![Boards Image Downloader](http://i.imgur.com/wfy9U48.png)

### [Verifique o CHANGELOG para maiores informações sobre novas versões!](https://raw.github.com/Wolfterro/Boards-Image-Downloader/master/CHANGELOG.txt)

### Requisitos:

#### Compilando:
- Python 2.7
- PyQt4 para Python 2.7
- PyInstaller
- Microsoft Visual C++ 2010 Redistributable (Windows apenas)

##### Para compilar o programa, basta executar o script build.bat (Windows) ou build.sh (Linux/BSD/Outros).
##### ***OBS:*** É necessário que o programa pyinstaller seja reconhecido como comando interno no prompt de comando (Windows) ou no shell que estiver usando (Linux/BSD/Outros), caso contrário os scripts para compilar o programa irão falhar!

#### Binário:
- ***Linux:*** Pode ser executado diretamente, sem qualquer requisito ou dependência.
- ***Windows:*** Requer o Microsoft Visual C++ 2010 Redistributable instalado (provavelmente já vem instalado em sistemas atualizados).
##### O programa, em seu formato binário, não requer o Python ou o PyInstaller instalados!

### Download:

#### Linux: https://github.com/Wolfterro/Boards-Image-Downloader/releases/tag/v2.0-Linux
#### Windows: https://github.com/Wolfterro/Boards-Image-Downloader/releases/tag/v2.0-Windows

###### Caso não possua o git e queira também baixar o repositório por completo, baixe através deste [Link](https://github.com/Wolfterro/Boards-Image-Downloader/archive/master.zip) ou clique em "Clone or Download", no topo da página.
