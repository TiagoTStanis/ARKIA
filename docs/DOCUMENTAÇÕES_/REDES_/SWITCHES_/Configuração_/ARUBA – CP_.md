ARUBA – CP
Monday, November 6, 2023
9:40 AM

\#
banner motd %
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\* ATENCAO!!! \*
\* ESTE EQUIPAMENTO E PRIVADO E RESTRITO A PESSOAS AUTORIZADAS. \*
\* INVASORES SERAO PROCESSADOS LEGALMENTE! DESCONECTE IMEDIATAMENTE, \*
\* SEUS ACESSOS ESTAO SENDO MONITORADOS EM TEMPO REAL. \*
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*%
hostname "UFQ-ALMCEN-S01"
dhcp-snooping
dhcp-snooping vlan 113 2000 3210 3230 3240
trunk 51-52 trk1 lacp \#cria interface para fibra
**\#ntp server**
timesync ntp
ntp unicast
ntp server 172.31.107.101 iburst
ntp enable
time timezone -180
ip dns server-address priority 1 172.31.107.101
ip dns server-address priority 2 172.31.107.102
ip dns server-address priority 3 172.31.107.103
\#gateway
ip route 0.0.0.0 0.0.0.0 172.26.245.199
\#allows tracking of IP address of Authenticated clients
ip client-tracker trusted
ip client-tracker probe-delay 120
\#(https://community.arubanetworks.com/community-home/artificial-intelligence-tech-corner/viewdocument?DocumentKey=5dd456b4-853d-42c3-acc4-de40c131a036&CommunityKey=2fd943a6-8898-4dbe-915f-4f09e4d3c317&tab=librarydocuments)
interface Trk1
dhcp-snooping trust
Exit

**\#user creation and local managment**
snmp-server community "public" unrestricted
snmp-server community "iMC_public" operator
snmp-server community "iMC_private" operator unrestricted
snmp-server host 172.31.107.1 community "iMC_public" trap-level all
snmp-server trap-source 172.31.107.1
snmp-server contact "[infra-datacenter@frimesa.com.br" location "UFA-PRE16-S01"](mailto:infra-datacenter@frimesa.com.br)
aaa authorization group "admins" 100 match-command "\*" permit
aaa authentication local-user "imc" group "admins" password sha1 "b34e36f75219422dc1b7275d0de4c6d96344916a"
aaa authentication local-user "admin" group "admins" password sha1 "==b3119db22fdfbfa6c2b3936430d76ba57f8eb2b7=="
**\#ClearPasss**
crypto ca-download usage clearpass retry 5
no cwmp enable
include-credentials
include-credentials clearpass-key
\#Criação do radius para o clearpass
\#UFM
radius-server host 172.31.200.1 key "6dPDBtWvp2lC7r"
radius-server host 172.31.200.1 dyn-authorization
radius-server host 172.31.200.1 time-window plus-or-minus-time-window
radius-server host 172.31.200.1 time-window 30
radius-server host 172.31.200.1 clearpass
\#UFA
radius-server host 172.26.249.8 key "6dPDBtWvp2lC7r"
radius-server host 172.26.249.8 dyn-authorization
radius-server host 172.26.249.8 time-window plus-or-minus-time-window
radius-server host 172.26.249.8 time-window 30
radius-server host 172.26.249.8 clearpass
\#Configuração do usuário para download de regras dur
radius-server cppm identity "arubaos_sw_dur" key "6dPDBtWvp2lC7r"
\#Configurações de server-group
aaa server-group radius "clearpass" host 172.31.200.1
aaa server-group radius "clearpass" host 172.26.249.8
aaa accounting update periodic 5
aaa accounting network start-stop radius server-group "clearpass"
aaa authorization user-role enable download
aaa authentication port-access eap-radius server-group "clearpass"
aaa authentication mac-based chap-radius server-group "clearpass"
aaa authentication local-user "clearpass" group "Level-15"
\#aplicação de 802.1x em portas especificas
aaa port-access authenticator active
aaa port-access authenticator 1-48 tx-period 10
aaa port-access authenticator 1-48 supplicant-timeout 10
aaa port-access authenticator 1-48 client-limit 10
aaa port-access authenticator 1-48 reauth-period 7200
aaa port-access authenticator 1-48

\#aplicação de mac-authentication em portas especificas (posso fazer por server group)
aaa port-access mac-based 1-48
aaa port-access mac-based 1-48 addr-limit 2
aaa port-access mac-based 1-48 quiet-period 15
\#SYSLOG
logging 172.31.107.1
logging facility syslog
logging notify running-config-change transmission-interval 10
aaa accounting exec start-stop syslog
aaa accounting commands stop-only syslog
\#NPS (COLOCAR SÓ UM DOS DOIS, PARA TODAS AS FILIAIS, UFM E FILIAIS – USAR O DE UFM ------------ UFA – USAR O DE UFA)
\#UFM – 2930F
radius-server host 172.31.107.102 key "zwErT79S6yKnTjMU9XS"
radius-server host 172.31.107.103 key "zwErT79S6yKnTjMU9XS"
aaa server-group radius "threetowers" host 172.31.107.102
aaa server-group radius "threetowers" host 172.31.107.103
aaa authentication login privilege-mode
aaa authentication ssh login peap-mschapv2 server-group "threetowers" local
aaa authentication ssh enable peap-mschapv2 server-group "threetowers" local
\#UFA – 2930F
radius-server host 172.26.249.104 key "iAzlLdk6otPRRiFbrxcQ"
aaa server-group radius "threetowers" host 172.26.249.104
aaa authentication login privilege-mode
aaa authentication ssh login peap-mschapv2 server-group "threetowers" local
aaa authentication ssh enable peap-mschapv2 server-group "threetowers" local
\#VLANS
vlan 103
name "LAN-Ativos-Rede"
tagged Trk1
ip address 172.19.1.31 255.255.255.0
untagged 45 e 48
exit
\#COLOCAR VLAN 103 NAS PORTA 45 E 48
vlan 104
name "LAN-FortiGate"
tagged Trk1
untagged 47
no ip address
exit
vlan_DEFAULT
tagged Trk1
untagged 45 e 48
description "VLAN para FortiNet e Switch S02"
vlan 117
name "MGMT-WIRELESS"
tagged Trk1
untagged 38
no ip address
exit

\#FRIMESA-CORP
vlan 3100
tagged Trk1,38
no ip address
exit

\#FRIMESA-LIVRE
vlan 3121
tagged Trk1, 38
no ip address
exit

\#FRIMESA-COLABORADORES -\> padrão indústria
vlan 3100
tagged Trk1,38
no ip address
exit

\#FRIMESA-COLABORADORES -\> sem captive portal (usuário AD com grupo CP-MACAUTH-MOBILE )
\#FRIMESA-VISITANTES -\> com captive portal (documento cadastrado na guarita)
vlan 3160
tagged Trk1,38
no ip address
exit

\#FRIMESA-COLABORADORES -\> padrão administrativo
vlan 3192
tagged Trk1,38
no ip address
exit

vlan 122
name "WAN-Link-Principal"
tagged Trk1
untagged 46
no ip address
exit
vlan 123
name "WAN-Link-Secundario"
tagged Trk1
untagged 46
no ip address
exit
vlan 2000
name "LAN-Computadores"
tagged Trk1
untagged 1-18
no ip address
exit
vlan 3210
name "LAN-Impressoras"
tagged Trk1
untagged 27-33
no ip addr-limit
exit
vlan 3220
name "LAN-Relogio"
tagged Trk1
untagged 34-37
no ip address
exit
vlan 3230
name "LAN-VOIP"
tagged Trk1
tagged 1-18
no ip address
exit
vlan 3240
name "LAN-Cameras"
tagged Trk1
untagged 19-26
no ip address
exit
\#protocolo anti-loop
spanning-tree
spanning-tree Trk1 priority 4
spanning-tree force-version rstp-operation
spanning-tree \<interface\> bpdu-protection \#todas as portas, exceto uplink
allow-unsupported-transceiver
\#permitir <u>transceiver</u>
y
\#password manager plaintext
\#password operator plaintext

password operator user-name "operator" sha1 "==c7403f8c396652cbeeb255ed1673d6a190ce76dd=="
password manager user-name "admin" sha1 "==c7403f8c396652cbeeb255ed1673d6a190ce76dd=="
no tftp server
no autorun
no dhcp config-file-update
no dhcp image-file-update
no dhcp tr69-acs-url
