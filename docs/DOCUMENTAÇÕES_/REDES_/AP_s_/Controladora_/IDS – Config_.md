PM

Configuração do IDS na Mobility Controller:

Configuration -\> System -\> Profiles -\> IDS -\> IDS -\> IDS-Frimesa (Profile criado)

![image1](../../../../_resources/image1-4.png)

**Terminologia básica:**

**Rogue AP:** Um rogue AP é um AP não autorizado que foi conectado na parte cabeada da rede. Qualquer outro AP que for visto no ambiente RF que não for parte da rede empresarial, pode causar interferência. Embora interferência não seja prejudicial e não represente ameaça, pode ser que ocorra de um AP causando interferência ser considerado como Rogue AP.

Doc: <https://www.arubanetworks.com/techdocs/ArubaOS_8.11.0_Web_Help/Content/arubaos-solutions/wireless-intrus-prev/dete-rogu-aps.htm>

**Valid AP (AP válido):** AP's válidos ou autorizados. AP que pertence a infraestrutura WLAN. O arubaOS automaticamente aprende APS autorizados.

Doc: <https://www.arubanetworks.com/techdocs/ArubaOS_8.9.0_Web_Help/Content/arubaos-solutions/wireless-intrus-prev/unde-infr-intr-dete.htm>

**Valid Client (Cliente válido):** Clientes são determinados como válidos se foram associados a um AP autorizado ou válido usando criptografia.

Doc: <https://www.arubanetworks.com/techdocs/ArubaOS_85_Web_Help/Content/arubaos-solutions/wireless-intrus-prev/unde-clie-intr-dete.htm#:~:text=ArubaOS%20automatically%20learns%20a%20valid,packet%20in%20a%20communication%20session>

**Contained (Contido):** Derruba o cliente/AP via DoS.

**AP Containment (Contenção de AP):** Se detectado dispositivos classificados como rogue e se há clientes conectando ao mesmo, é realizado a contenção. A contenção pode ser realizada seguindo os seguintes métodos:

Deauth-only: Desautentica o cliente do rogue AP;

Tarpit non valid sta: Apenas clientes não autorizados que tentam se associar a um AP são enviados ao tarpit.

Tarpit all sta: Qualquer cliente que tentar se associar a um WIAP marcado para contenção é enviado spoofing frames.

Os métodos tarpit chamam-se tarpit shielding. Caso um cliente tente se associar a um rogue WIAP, é derrubado a conexão do cliente com o rogue AP, criado um canal/BSSID falso com o mesmo nome do rogue AP, para o cliente se conectar nele (porém em um ambiente controlado), assim o cliente não se comunica mais com o rogue AP.

![image2](../../../../_resources/image2-2.png)

Tarpit shielding doc:

<https://www.arubanetworks.com/techdocs/ArubaOS_83_Web_Help/Content/ArubaFrameStyles/New_WIP/config_tarpit_shield.htm>

Tarpit shielding explained:

<https://community.arubanetworks.com/community-home/librarydocuments/viewdocument?DocumentKey=8e87c741-a722-41ea-a62d-27d9a667059f&CommunityKey=2fd943a6-8898-4dbe-915f-4f09e4d3c317&tab=librarydocuments>

No aruba OS, para usar o tarpit, precisa de uma licença especial. Já as opções none e deauth-only são gratuitas com o arubaOS 8.

**Doc com terminologia completa:**

<https://www.arubanetworks.com/techdocs/ArubaOS_8.11.0_Web_Help/Content/arubaos-solutions/wireless-intrus-prev/dete-rogu-aps.htm>

**IDS DOS – IDS_DOS-Frimesa (Profile frimesa):**

Configurado para detectar ataques de AP Flood (quando existem mais de x AP's iguais ou similares na rede). Será alertado caso a quantidade de tais APs sejam maior que 5. Também foram selecionados algumas outras detecções para intrusão de clientes. A maioria das selecionadas já vem por default.

Aruba OS 8 ids dos-profile doc:

<https://www.arubanetworks.com/techdocs/CLI-Bank/Content/aos8/ids-dos-pro.htm>

**IDS Genreal – IDS_General-Frimesa**

Parametrização gerais para gerenciamento da IDS nos WIAPs. Também é configurado se deseja realizar o containment (contenção) via cabo ou wireless. A contenção atua junto com os profiles IDS Unauthorized Device e IDS Impersonation. Aqui ela é selecionada se será usado ou não.

A contenção atua em modos diferentes, como desautenticação e tarpitting (tarpit shielding).

IDS events: logs-only

IDS Wireless Containment: deauth-only

**IDS Impersonation – IDS_Impersonation-Frimesa:**

Profile usado para configurar se existem AP spoofing e AP impersonation. Nele é possível configurar para proteger contra AP impersonation. Essa proteção é feita realizando um ataque DoS desabilitando ambos os WIAPs, o impersonificado e o legitimo.

Um WIAP é considerado como impersonificado quando um atacante configura um AP que assume o BSSID e ESSID de um WIAP válido.

Detect AP impersonation: yes

Protect AP impersonation: yes

Detect AP Spoofing: yes

Aruba OS 8 impersonation-profile doc:

<https://www.arubanetworks.com/techdocs/CLI-Bank/Content/aos8/ids-imperson-pro.htm>

**IDS Signature Matching Profile – default;**

**IDS Unauthorized Device – IDS_Unauthorized-Frimesa:**

Profile usado para detectar e proteger conexões a dispositivos não autorizados.

Detect Adhoc Network: yes

Protect from adhoc network: no (quando redes adhoc são detectadas, são derrubadas via DoS. Precisa da opção de Wireless-containment na IDS General.)

Detect Adhoc networks using valid SSID: yes

Protect from Adhoc Networks Using Valid SSID: yes

Rogue AP classification: yes

Overlay Rogue AP classification: yes

OUI-based Rogue AP Classification: yes

Detect Valid SSID misuse: yes (intervenção ou AP próximo usando SSID válido ou protegido).

Protect SSID: no (Não deixei configurado pois nem todos os clientes da Frimesa são considerados válidos. Nos logs da Controller, existem diversos registros de usuários que autenticam-se sem criptografia, logo, tornam-se usuários inválidos.)

Detect Windows Bridge: yes

Protect Windows Bridge: no

Detect Wireless Hosted Network: yes

Protect Wireless Hosted Network: no (When you enable the wireless hosted network protection feature, Mobility Conductor enforces containment on a wireless hosted network by launching a denial of service attack to disrupt associations between a Windows 7 software-enabled Access Point (softAP) and a client, and disrupt associations between the client that is hosting the softAP and any access point to which the host connects. When a wireless hosted network triggers this feature, wireless hosted network protection sends the Wireless Hosted Network Containment and  
Host of Wireless Network Containment warning level security log messages, and the wlsxWirelessHostedNetworkContainment and wlsxHostOfWirelessNetworkContainment SNMP traps.)

Tipos de proteção explicado:

Doc:

<https://www.arubanetworks.com/techdocs/central/2.5.8/content/aos10x/rogue-ap-mgmt/conf-ids-params.htm#:~:text=Protect%20SSID%E2%80%94Enforces%20policy%20where,clients%20from%20associating%20to%20it>.
- Protect SSID—Política que força que SSIDs protegidos/válidos só podem ser usados por AP's validos. Caso contrário, o AP tentando usar o SSID válido é contido via DoS.
- Rogue Containment— Quando um Rogue AP é identificado, ele não é desabilitado. Se configurar essa opção, ele será automáticamente desabilitado via DoS.
- Protect AP Impersonation— Quando um AP impersonificado é detectado, é realizado um ataque DoS desabilitando o AP falso e o legitimo.
- Protect from Adhoc Networks—Quanto detectado redes Adhoc, são desabilitadas via DoS.
- Protecting Valid Stations: Desconectar o cliente se conectar-se a um AP não válido.
- Protect Wireless Hosted Network: Disable Windows hostspot, Wi-Fi repeaters (repetidores) e etc.
- Protecting Windows Bridge: Conter o cliente que está formando a bridge para que não consiga mais se conectar ao AP. Windows bridge doc explicando: <https://community.arubanetworks.com/community-home/librarydocuments/viewdocument?DocumentKey=0eceb52b-c1a9-46c3-9145-ec2c7cb7d0c9&CommunityKey=39a6bdf4-2376-46f9-853a-49420d2d0caa&tab=librarydocuments> )

Detect an misconfigured AP: yes (Um AP é considerado com configuração errada quando é classificado como válido e não segue os parametros a seguir:
- Canais válidos;
- Tipo de criptografia;
- Lista de AP MAC OUIs válidos;
- Lista de SSID válido.)
Protect from an misconfigured AP: no (previne conexão de clientes ao AP);

Detect Unencrypted Valid Clients: yes

Detect Valid Client Misassociation: yes

Protect Valid Stations: no (Desconectar o cliente se conectar-se a um AP não válido.).

Infraestructure Intrustion Protection doc (bem explicado):

<https://www.arubanetworks.com/techdocs/ArubaOS_87_Web_Help/Content/arubaos-solutions/wireless-intrus-prev/unde-infr-intr-prot.htm#:~:text=Protect%20Misconfigured%20AP%20enforces%20that,clients%20from%20associating%20to%20it>.

Aruba OS 8 unauthorized-device-profile doc:

<https://www.arubanetworks.com/techdocs/CLI-Bank/Content/aos8/ids-unauth-dev.htm>

