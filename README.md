# Stupefy - Um Conversor de Playlists do Spotify para o Youtube

## Conceito do projeto
O projeto é um script em Python, que interliga as API's do Spotify e YouTube e permite a conversão de playlists existentes do Spotify para uma nova playlist do YouTube. Foi desenvolvido com a ideia de aproveitar o algoritmo de criação de playlists do Spotify, que usa conceitos avançados de machine learning, com a praticidade do YouTube ao reproduzir playlists.

## Pré-requisitos e recursos utilizados
É necessário ter o projeto cadastro em ambas API's, para ter o uso autorizado das chaves de usuário. 
O grupo utilizou Python (v3.7) para desenvolver o projeto, além das seguintes bibliotecas e API's:

1. YouTube Data API, disponível em (https://developers.google.com/youtube/v3/docs)
2. Spotify Web API, disponivél em (https://developer.spotify.com/documentation/web-api/)
3. Spotipy, uma implementação para facilitar o uso da API acima, disponível em (https://spotipy.readthedocs.io/en/latest/)
4. oauth2client, disponível em (https://github.com/googleapis/oauth2client)
5. google_auth_oauthlib.flow, disponível em (https://google-auth-oauthlib.readthedocs.io/en/latest/reference/google_auth_oauthlib.flow.html)
6. pyfiglet, para uma interface mais amigável no terminal, disponível em (https://pypi.org/project/pyfiglet/0.7/)
7. time, disponível em (https://docs.python.org/3/library/time.html)
8. json, disponível em (https://docs.python.org/3/library/json.html)
9. sys, disponível em (https://docs.python.org/3/library/sys.html)

Além de dois módulos implementados pelo próprio grupo (interface.py e settings_config.py), aonde implementamos, respectivamente, uma interface para o script e um arquivo com todas as configurações necessárias, já que o uso das API's requer chaves para o usuário.
  
## Passo a passo

1. Registramos o projeto em ambas API's para obter as chaves de acesso (https://developer.spotify.com e https://console.cloud.google.com)
2. Estudamos as documentações disponíveis procurando entender o que precisaríamos para implementar o código
3. Buscamos bibliotecas que ajudassem no nosso trabalho (encontramos a biblioteca spotipy, disponível nos links anteriores)
4. Implementamos primeiro, as funções de comunicação com o Spotify, por apresentar uma biblioteca que facilitasse sua interação, criamos funções de buscar a playlist requerida a partir de um link URI do Spotify e que lesse todos os itens daquela playlist
5. Implementamos uma interface gráfica com o pyfiglet para mostrar o nome do projeto ao rodar o script
6. Procuramos incessantemente por alguma biblioteca que facilitasse o acesso ao YouTube, somente para falhar e ter que ler (novamente) toda a documentação
7. Implementamos as funções de pesquisar os itens da playlist e de criar a playlist no YouTube, além das funções de autorização e login na conta da Google
8. Esbarramos com um erro super chato de limite de ações com a YouTube Data APi
9. Descobrimos que só podíamos converter 50 músicas por dia
10. Ajustamos o código para funcionar de acordo com as limitações impostas pela API usada


## Instalação

a)
  1. Inscreva seu projeto nos devidos sites das API's para conseguir as chaves de acesso
  2. Assim que obtiver as chaves, cole-as nos lugares indicados no arquivo config.py (stupefy/settings_config/config.py)
  3. Não esqueça de adicionar à pasta stupefy/settings_config o arquivo .json com o client secret do YouTube

 b)
  1. Entre na pasta do projeto pelo terminal
  ```
  Execute o comando python3 stupefy.py, no terminal, na pasta do projeto
  ```

## Execução

  ```
  Execute o comando python3 stupefy.py, no terminal, na pasta do projeto
  ```

  2. Abra o link para logar na sua conta do Google em que deseja criar a playlist
  3. Autorize a aplicação e cole no terminal a chave gerada para autorizar o login
  4. Cole no terminal, quando for pedido, o URI da playlist do Spotify que deseja converter
  5. Digite o nome e a descrição de sua nova playlist do YouTube
  6. Torça para não ter excedido o limite diário de músicas
  7. Espere um pouquinho...
  8. Curta sua música!

## Bugs/problemas conhecidos
  Devido ao uso da YouTube Data API ter um limite de ações diárias para desenvolvedores, só podemos converter 50 músicas ao dia, sem que a API lance uma exceção esquisitissíma e nem um pouco amigável ao usuário. Conhecendo esse problema, ao tentar colocar uma playlist maior no conversor, a aplicação encerra sem converter nenhuma música. Essa foi uma decisão de projeto e embora haja uma interface perguntando se o usuário deseja converter as primeiras 50 músicas da playlist, foi implementado posteriormente a interrupção do script, impedindo qualquer erro inesperado da API. Procuramos atualizar a interface em uma nova versão. 
  
OBS: o projeto se encontra todo em inglês, devido às API's utilizadas, que possuem interfaces padrão em inglês. Tentaremos algum jeito de traduzir as interfaces, também.

## Autores
* Bruno Frítoli Carrazza ([Carrazza](https://github.com/Carrazza))
* Jade Manzur de Almeida ([jdmanzur](https://github.com/jdmanzur))

## Imagens/screenshots
É necessário colocar pelo menos 3 imagens/screenshots do projeto, porém fiquem a vontade para colocar mais, a medida do que vocês acharem legal para ilustrar o projeto.

Para colocar imagens no Readme do Github, vocês podem usar o seguinte comando (abrir este Readme no modo raw ou como txt):

![Imagem](https://github.com/Infinitemarcus/Hackerspace-template/blob/master/exemplo.png)

É preferível que vocês usem imagens hospedadas no próprio GitHub do projeto. É só referenciar o link delas no comando acima.
