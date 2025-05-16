COMWARE - CP  
Wednesday, November 1, 2023  
8:42 AM

#Hostname  
sysname FIBH-LOG-S01  
#Configurar TimeZone  
clock timezone brasil minus 03:00:00  
#Configurar DNS  
dns resolve  
dns server 172.31.107.101  
dns server 172.31.107.102  
dns server 172.31.107.103  
dns domain frimesa.local  
#Habilitar DNS e SSH  
telnet server enable  
ssh server enable  
\___\___\___\___\___\___\___\___\___\__  
#Criar VLANs  
vlan 103  
description LAN-Ativos-Rede  
name LAN-Ativos-Rede  
#  
vlan 104  
description LAN-FortiGates  
name LAN-FortiGates  
#  
vlan 113  
description LAN-Ativos-WiFi  
name LAN-Ativos-WiFi  
#  
vlan 122  
description WAN-Link-Principal  
name WAN-Link-Principal  
#  
vlan 123  
description WAN-Link-Secundario  
name WAN-Link-Secundario  
#  
vlan 2000  
description LAN-Computadores  
name LAN-Computadores  
#  
vlan 3100  
description CORP100  
name CORP100  
#  
vlan 3140  
description GUEST  
name WLAN-Visitantes  
#  
vlan 3160  
description MOBILE160  
name WLAN-Mobile  
#  
vlan 3192  
description WLAN-Colaboradores  
name WLAN-Colaboradores  
#  
vlan 3210  
description LAN-Impressoras  
name LAN-Impressoras  
#  
vlan 3220  
description LAN-Relogios  
name LAN-Relogios  
#  
vlan 3230  
description LAN-VoIP-ADM  
name LAN-VoIP  
#  
vlan 3232  
description LAN-VoIP-IND  
name LAN-VoIP-IND  
#  
vlan 3240 e 3241  
description LAN-Cameras  
name LAN-Cameras  
\___\___\___\___\___\___\___\___\___\__  
#Configuração global 802.1x  
dot1x  
dot1x authentication-method eap  
#Reautenticação do cliente na porta  
dot1x timer reauth-period 7200  
#Intervalo de mensagens EAP enviada ao cliente  
dot1x timer tx-period 10  
dot1x timer supp-timeout 10

#Comandos para remoção do método de autenticação já existente (se houver)  
undo mac-authentication  
undo mac-authentication domain  
interface range g1/0/1 to g1/0/48  
undo mac-authentication  
undo mac-authentication domain  
quit  
#Cria a conexão com as informações do servidor ClearPass (chave, IP)  
radius scheme clearpass  
primary authentication 172.31.200.1 key simple 6dPDBtWvp2lC7r  
primary accounting 172.31.200.1 key simple 6dPDBtWvp2lC7r  
secondary authentication 172.26.249.8 key simple 6dPDBtWvp2lC7r  
secondary accounting 172.26.249.8 key simple 6dPDBtWvp2lC7r  
user-name-format without-domain  
quit  
#Configuração do dominio de autenticação  
domain frimesa.local  
authentication lan-access radius-scheme clearpass  
authorization lan-access radius-scheme clearpass  
accounting lan-access radius-scheme clearpass  
quit  
#Ativação global do mac-authentication e especificação do dominio de autenticação  
mac-authentication  
mac-authentication domain frimesa.local  
\___\___\___\___\___\___\___\___\___\__  
#configurando usuários de acesso (numeros da senha segundo e terceiro bloco da rede do switch)  
local-user admin  
password simple senha  
authorization-attribute level 3  
service-type lan-access  
service-type ssh telnet terminal  
service-type ftp  
service-type web  
local-user imc  
password simple senha  
authorization-attribute level 3  
service-type lan-access  
service-type ssh telnet terminal  
service-type ftp  
service-type web  
\___\___\___\___\___\___\___\___\___\__  
#SYSLOG  
info-center source SHELL channel 2  
info-center source CFGMAN channel 2  
info-center source WEB channel 2  
info-center source LS channel 2  
info-center source VLAN channel 2  
info-center source NTP channel 2  
info-center source CFM channel 2  
info-center source TELNET channel 2  
info-center source SNMP channel 2  
info-center source MACAUTH channel 2  
info-center source ETH channel 2  
undo info-center source default channel 2  
#NPS  
radius scheme frradiusws  
server-type extended  
primary authentication 172.31.107.103 key simple zwErT79S6yKnTjMU9XS  
secondary authentication 172.31.107.102 key simple zwErT79S6yKnTj  
user-name-format without-domain  
attribute 25 car  
quit  
domain ws  
authentication default radius-scheme frradiusws local  
authorization default radius-scheme frradiusws local  
authentication login radius-scheme frradiusws local  
authorization login radius-scheme frradiusws local  
access-limit disable  
state active  
idle-cut disable  
self-service-url disable  
accounting optional  
quit

domain default enable ws  
#Ativar o Spanning tree (evita loop na rede)  
stp mode rstp  
stp enable  
\___\___\___\___\___\___\___\___\___\__  
#Excluindo VLAN 1 (DEFAULT_VLAN)  
undo interface vlan 1  
\___\___\___\___\___\___\___\___\___\__  
#Configurando VLANs nas portas  
interface Vlan-interface103 #Cria interface digital para o switch  
description LAN-Ativos-Rede  
ip address 172.21.126.1 255.255.255.0  
#A port is considered as an edge port when it is directly connected to the user terminal or server,  
#instead of any other switches or shared network segments.  
#Configurando portas para rede LAN-computadores  
#Configuração da porta  
interface range GigabitEthernet1/0/1 to GigabitEthernet1/0/30  
stp edged-port enable  
port link-type trunk  
port trunk permit vlan 2000 3230  
port trunk pvid vlan 2000  
undo port trunk permit vlan 1  
dot1x  
dot1x unicast-trigger  
undo dot1x multicast-trigger  
dot1x mandatory-domain frimesa.local  
undo dot1x handshake  
mac-authentication  
mac-authentication domain frimesa.local  
#Conexão switch entre S01 e S02  
interface GigabitEthernet1/0/45  
description FIBH-LOG-S02  
port link-type trunk  
port trunk permit vlan all  
dhcp-snooping trust  
stp edged-port disable  
undo port auto-power-down  
#Configurando porta para Link Principal ou BKP  
interface GigabitEthernet1/0/46  
description LINK-PRINCIPAL  
port access vlan 122  
stp edged-port disable  
undo port auto-power-down  
#Configurando porta para Fortinets (DMZ)  
interface GigabitEthernet1/0/47  
description FIBH-LOG-G01-DMZ  
port access vlan 104  
stp edged-port disable  
undo port auto-power-down  
#Configurando porta para Fortine (LAN 1)  
interface GigabitEthernet1/0/48  
description FIBH-LOG-G01-01  
port link-type trunk  
port trunk permit vlan all  
dhcp-snooping trust  
stp edged-port disable  
undo port auto-power-down  
#Ativa DHCP Snooping  
dhcp-snooping  
#  
ip route-static 0.0.0.0 0.0.0.0 172.21.126.199  
#  
info-center loghost 172.31.107.1  
#  
#Simple Network Management Protocol (SNMP)  
snmp-agent  
snmp-agent community read iMC_public  
snmp-agent community write iMC_private  
snmp-agent sys-info contact [infra-datacenter@frimesa.com.br](mailto:infra-datacenter@frimesa.com.br)  
snmp-agent sys-info location UFM-GUARI-S02  
snmp-agent sys-info version v3  
snmp-agentgroupv3v3_aes_shaprivacywrite-viewViewDefault  
snmp-agentusm-userv3snmpv3_imcv3_aes_shaauthentication-modeshaFipURx8zITO00WEmHjQcprivacy-modeaes1289HptfGL4rEIxOZpM53MA  
#  
header motd %  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
\* ATENCAO!!! \*  
\* ESTE EQUIPAMENTO E PRIVADO E RESTRITO A PESSOAS AUTORIZADAS. \*  
\* INVASORES SERAO PROCESSADOS LEGALMENTE! DESCONECTE IMEDIATAMENTE, \*  
\* SEUS ACESSOS ESTAO SENDO MONITORADOS EM TEMPO REAL. \*  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*%  
#  
ntp-service unicast-server 172.31.107.101  
#  
\# antes de rodar este comando verificar se nenhuma porta uplink está com o comando stp edged-port enable  
stp bpdu-protection  
#  
#login authentication  
user-interface aux 0  
authentication-mode scheme  
user-interface vty 0 15 #vty (virtual teletype (is a command line interface (CLI) created in a router and used to facilitate a connection to the daemon via Telnet, a network protocol used in local area networks))  
authentication-mode scheme  
#