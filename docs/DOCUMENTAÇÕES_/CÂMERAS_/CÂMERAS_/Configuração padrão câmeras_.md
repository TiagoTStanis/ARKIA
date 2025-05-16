**<u>APPLIANCE</u>**

![image1](../../../_resources/image1-38.png)

![image1](../../../_resources/image1-38.png)

Todos os modelos de câmera HikVision DS-\*.

**<u>ARQUITETURA</u>**

Atualmente utilizamos duas ferramentas para visualização das imagens de câmeras IP, sendo essas Symphony (UFM, UFA e UFLM) e Digifort (UFQ e UFR). Essa documentação tem por objetivo demonstrar a configuração padrão das câmeras em ambas as ferramentas.

**<u>Contas de Serviço</u>**

Usuário: admin

Senha: Keepass da Infra

**<u>Configurações</u>**

Primeiramente, após a instalação local da câmera, é necessário configurá-la em nossa rede. Para isso, são necessários os seguintes passos:
1.  Reservar o IP no DHCP (UFQ e UFR o FortiGate age como DHCP);
2.  Configurar a porta do Switch para a VLAN de câmera;
3.  Cadastrar o endereço MAC no AD;
4.  Anotar na planilha “Cameras TI.xlxs” no SharePoint (item para controle apenas).

A câmera sempre deve ficar em DHCP, porém com o IP reservado. Isso ocorre para melhorar o gerenciamento das câmeras, pois, as mesmas não possuem registro DNS.

**Configurações padrões de câmeras:**

Após a câmera possuir um IP e estar acessível na rede, inicia-se a configuração padrão da câmera. Para acessar a câmera, conecte na câmera no Edge, através de seu endereço IP, utilizando modo de compatibilidade do IE. Na primeira conexão, será necessário instalar um plugin da Hikvision. Após instalado, faça login e já poderá alterar as configurações da câmera.

- Ativar a detecção de movimento e maximizar a sensibilidade: Sobre Evento -\> Evento -\> Ativar a detecção de movimento.

- Stream principal
  - FPS: 4: Vídeo e áudio -\> Número de Imagens;
  - Resolução: 1920x1080 (ou a mais próxima): Vídeo e áudio -\> Resolução;
  - Codec: H.265: Vídeo e áudio -\> Codif. Vídeo;
  - Intervalo de I-Frames: 4
- Sub-Stream:
  - FPS: 4: Vídeo e áudio -\> Número de Imagens;
  - Resolução: 640x480 (ou a mais próxima): Vídeo e áudio -\> Resolução;
  - Codec: H.265: Vídeo e áudio -\> Codif. Vídeo;
  - Intervalo de I-Frames: 4

![image2](../../../_resources/image2-19.png)

![image3](../../../_resources/image3-10.png)

Os tópicos acima são uma configuração padrão que todas as câmeras da Frimesa devem, obrigatoriamente, possuir. Também, antes de colocar a câmera em uma ferramenta, é necessário atualizar a câmera. Para este, também possui uma documentação.

Obs.: As configurações realizadas acima são feitas de forma automática no Symphony (exceto pela detecção de movimento).

**Symphony:**

No Symphony, a configuração é mais simples. Através deste é possível alterar algumas configurações na câmera, sem precisar acessa-la diretamente. Primeiramente, ao instalar uma nova câmera, pesquise se a mesma já possui uma pasta no Symphony (representando o setor) em que pertencerá, caso contrário, vá em Arvore de câmeras e crie uma pasta. Após, vá em adicionar dispositivo -\> coloque o IP -\> credenciais para acesso -\> Continuar -\> Nomeie a câmera -\> Adicione um template a câmera -\> Atribuía ao grupo correto -\> Finalize.

No Symphony existem templates que definem configurações padrões da câmera. Através destes, é possível alterar algumas configurações como FPS, resolução e outros sem precisar acessar diretamente a câmera. No entanto, não é possível ativar a detecção de movimento da câmera através de um template, essa configuração precisa ser feita manualmente.

Nota-se que no Symphony existem cinco templates:
- FR-2F-H264
- FR-2F-H265
- MVMT-2F-H264
- MVMT-2F-H265
- OEA-2F-H265
As principais configurações do template são iguais, mudando a forma de gravação e a codificação. Câmeras que começam com FR gravam o tempo todo, enquanto as MVMT gravam apenas quando há movimento detectado pela câmera. Quando configurado, o parâmetro para tal foi a localização das câmeras, quando em ambiente aberto (estacionamento, ruas e etc) grava o tempo todo.

O H264 e H265 representa o tipo de codificação que a câmera usa. Algumas câmeras mais antigas não possuem H265 e usam H264. Se a câmera possuir, preferencialmente, sempre use H265.

Também há a configuração 2F que define dois fluxos, porém esse não está sendo usado devido a um problema no Symphony que a câmera abre a sessão e a fecha imediatamente após, causando erro e falha na câmera.

**Digifort**

Para adicionar uma câmera no Digifort, acesse o cliente de administração, vá em Servidor de Gravação, e verifique a árvore de câmeras, se já possui uma pasta para a câmera qual deseja instalar. Caso não, crie uma. Após, seleciona a pasta, e clique na arrow down, localizada ao lado da box “Adicionar” e selecione a opção “Câmera”.

Irá abrir uma nova tela, em que nesta deve se preencher os seguintes campos: Nome, descrição, Fabricante, Modelo, Endereço da câmera, usuário e senha para acesso e diretório para gravação. Preencha cada text box com suas respectivas informações, e em Diretório para gravação, seleciona o ícone da pasta -\> Selecione o diretório I: \[IMAGES\]\\ -\> Abra a pasta Gravações -\> Crie uma nova pasta com o Nome da câmera -\> Selecione a pasta recém criada.

![image4](../../../_resources/image4-8.png)

Após, nas opções apresentadas na lateral esquerda da tela, selecione Detecção de Movimento e ative “Utilizar detecção de movimento pelo dispositivo”. Nota-se que essa opção ficará disponível baseado no Modelo da câmera. O modelo é uma informação obrigatória para ser preenchida, mas não necessariamente precisa estar correta, uma vez que os modelos usados nas filiais não possuem no DB da ferramenta. Assim, pode deixar o modelo padrão DS-2CD2021G1-I. Ambos esses modelos permitem a detecção de movimento pelo dispositivo. Vá em Streaming -\> Perfis de mídia e edite ambos, no perfil gravação coloque o codec H.265 e Stream 1, já no perfil visualização coloque o codec H.265 e Stream 2.

![image5](../../../_resources/image5-4.png)

![image6](../../../_resources/image6-3.png)

![image7](../../../_resources/image7-1.png)

Ainda na aba Streaming, vá em Gravação -\> verifique se o perfil de mídia está como Gravação e ative a opção “Na ocorrência de movimento”.

![image8](../../../_resources/image8-2.png)

Vá em “Visualização ao vivo” e verifique se o perfil de mídia está Visualização. Caso não esteja, o mude.

![image9](../../../_resources/image9-1.png)

Por último, vá em Gravação -\> em “Tipo de Gravação” selecione “Gravação por movimento”. Clique em OK. Assim finaliza-se a inserção de uma câmera no Digifort

![image10](../../../_resources/image10-1.png)

No Digifort, não é possível alterar parâmetros de configuração da câmera como FPS e afins, para tanto, é necessário acessar a câmera e alterar todos os parâmetros manualmente.

![image11](../../../_resources/image11-2.png)

![image12](../../../_resources/image12-1.png)

**ÚLTIMAS ATUALIZAÇÕES**
| Editor | Data | Motivo | Alteração |
|----|----|----|----|
| André Luiz Fronza | 21/11/2023 | Novo modelo de documentação | Padronização do texto |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

