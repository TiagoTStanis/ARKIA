AM

**Configuração Fortigate 60E**

****

**Equipamentos necessários**
- 2 caixas Fortigate modelo 60E
- 3 cabos de rede
- 1 adaptador de rede (RJ45 – USB)
- 1 cabo console

**1 – Conexão física**

1.1 – Primeiramente deve-se conectar as duas caixas para uso da “HA”, isto faz com a caixa tenha alta disponibilidade, em caso de falha em uma delas, a segunda já entra em ação, as portas a serem usadas para isto são:

Porta 2 ——————- Porta 2

Porta 3 ——————- Porta 3

1.2 – Feito isto, deve ser verificado quem é a caixa com o S/N mais alto, pois é assim que o Fortigate irá eleger quem será a caixa master, e consequentemente a caixa de número menor, será a slave.

1.3 – Conectar o cabo console na entrada console do Fortigate master

1.4 – Conectar o cabo de rede na porta “WAN2” do fortigate e no adaptador de rede conectado ao computador.

**2 – Conexão Console**

2.1 - Acessar via Putty com a velocidade 9600.

2.2 – Se ao entrar você se deparar com a mensagem:

![image1](../../../../_resources/image1-1.jpg)

Significa que o fortigate não possui nenhum firmware instalado.

2.3 – Se ao entrar você se deparar com a mensagem solicitando login, significa que o fortigate possui firmware e possivelmente está configurado.

2.4 – No caso de o firmware já estar instalado deverá ser formatado e feito novamente.

**3 – Firmware**

3.1 – Para instalar o firmware você deve possuir o arquivo .out da versão homologada e utilizada atualmente no ambiente. Na data da documentação, o firmware utilizado é o:

**FGT_60E-v7.0.14.M-build0601-FORTINETout**

3.2 – É possível localizar o firmware no Sharepoint: T.I. Infra - Procedimentos técnicos \> Documentos \> General \> Firmwares \> FORTIGATE

**4 – Configuração TFTP para transferência do Firmware**

4.1 – Ao iniciar o menu de configuração você pode verificar os parâmetros TFTP clicando \[**R**\]

![image2](../../../../_resources/image2-1.jpg)

4.2 – Ao clicar, você verá uma tela como esta:

![image3](../../../../_resources/image3.png)

4.3 – Configurações:
- Image download port: A (porta que conectamos o cabo de rede)
- Local VLAN ID: N/A
- Local IP address: IP do fortigate (padrão)
- Local subnet mask: N/A
- Local gateway: N/A
- TFTP server IP: 192.168.1.100 (este IP deve ser configurado no adaptador)
- Firmware file name: FGT_60E-v7.0.14.M-build0601-FORTINET.out
4.4 – Para configurar os parâmetros:
- \[**C**\]: Configure TFTP parameters.
- \[**F**\]: Set firmware file name (digitar o firmware selecionado)
- \[**H**\]: Display this list of options.
- \[**P**\]: Set firmware download port.
- \[**3**\]: port WAN2.
- \[**Q**\]: Quit this menu.

**5 – Transferência TFTP**

5.1 – Para transferência é necessário download de algum programa que permita a transferência TFTP do firmware para a caixa. Neste exemplo, irei utilizar o programa **Tftpd64**.

5.2 – O programa pode ser baixado no SharePoint na mesma pasta dos Firmwares.

5.3 – Configurar o adaptador de rede com mesmo IP setado nos parâmetros de TFTP (neste caso, 192.168.1.100).

5.4 – Abrir o programa baixado:
- Current Directory -\> caminho onde se encontra o firmware.
- Server interfaces -\> adaptador de rede

![image4](../../../../_resources/image4-1.jpg)

5.5 – Retornar ao console

\[**T**\]: Initiate TFTP firmware transfer.

![image5](../../../../_resources/image5-1.jpg)

Save as Default firmware/Backup firmware/Run image without saving:\[D/B/R\]? **D**

Continue:\[Y/N\]? **Y**

![image6](../../../../_resources/image6-1.jpg)

**OBS.: Se o Kaspersky estiver pausado o Firewall do Windows irá assumir o controle da máquina, consequentemente bloqueará a tentativa de transferência.**

**6 – Configuração Fortigate**

Login: admin

Password: blank

6.1 – Conectar via interface Web

Por padrão a interface DMZ está configurada com o IP 10.10.10.1. Conectar o cabo de rede na entrada DMZ e alterar a faixa de IP do adaptador para 10.10.10.10 para acessar via interface Web

<https://10.10.10.1>

6.2 – Excluir configurações padrão não necessárias

config firewall policy

delete 1

end

config firewall addrgrp

delete G\\ Suite

delete Microsoft\\ Office\\ 365

end

config firewall address

delete wildcard.dropbox.com

delete wildcard.google.com

delete gmail.com

delete login.windows.net

delete login.microsoftonline.com

delete login.microsoft.com

end

6.3 - Excluir interface fortilink

![image7](../../../../_resources/image7-1.jpg)

![image8](../../../../_resources/image8.png)

6.4 – Excluir interface Hardware Switch

![image9](../../../../_resources/image9.jpg)

Desatibilitar a opção “Create address object matching subnet”

![image10](../../../../_resources/image10.jpg)

Desabilitar o DHCP Server

![image11](../../../../_resources/image11.png)

Excluir a interface

![image12](../../../../_resources/image12.jpg)

6.5 – Configuração interface

config system interface

edit internal1

set role lan

set alias "LAN"

set allowaccess ping

next

end

6.6 – Configurar interface DMZ (utilizada para fazer o acesso individual na caixa)

config system interface

edit "dmz"

set ip ==172.21.159.1== 255.255.255.0

set allowaccess ping https ssh fgfm

set device-identification enable

set lldp-transmission enable

next

end

\*Observe que aqui a conexão será perdida pois alteramos o IP da interface DMZ. Logo, temos que alterar o IP da interface de rede para a mesma faixa de IP e acessar novamente a caixa pelo novo IP

<https://172.20.159.1>

6.7 – Realizar configurações administrativas da caixa

config system global

set admin-scp enable

set admin-sport 8443

set admintimeout 30

set gui-theme neutrino

set hostname =="FISA-LOG-G02"==

set switch-controller enable

set timezone 18

set gui-firmware-upgrade-warning disable

set gui-forticare-registration-setup-warning disable

unset alias

end

\*Observe que aqui a conexão será perdida novamente pois alteramos a porta pela qual acessamos o fortigate, sendo necessário inserir a mesma para termos acesso

<https://172.20.159.1:8443>

6.8 – Configurar HA, é através desta configuração que as duas caixas irão conversar

Primeiramente desabilitar associação de sub-rede da interface DMZ

![image13](../../../../_resources/image13.jpg)

config system ha

set group-name "==FISA-LOG-GHA=="

set mode a-a

set password ==senhapadraoswitch==

set hbdev "internal2" 50 "internal3" 50

set session-pickup enable

set ha-mgmt-status enable

config ha-mgmt-interfaces

edit 1

set interface "dmz"

set gateway 172.21.159.199

next

end

set override disable

set monitor "internal1"

end

Todas as configurações acima devem ser realizadas em ambas as caixas fortigate. Após configuração e validação da HA, poderá seguir com a configuração abaixo apenas na caixa Master.

**7 – Configuração Caixa Master**

**OBS.: Informações grifadas em amarelo devem ser alteradas conforme a filial.**

7.1 – Configurar o link secundário para realização das configurações em bancada, através dela será possível simular o link da filial.

config system interface

edit "VLAN123"

set vdom "root"

set mode dhcp

set allowaccess ping https ssh snmp fgfm

set alias "WAN-Link-Secundario"

set device-identification enable

set defaultgw disable

set dns-server-override disable

set role wan

set interface "internal1"

set vlanid 123

end

7.2 – Configuração da interface gráfica do Fortigate.

config system settings

set sip-expectation enable

set allow-subnet-overlap enable

set gui-dynamic-routing enable

set gui-policy-based-ipsec enable

set gui-application-control disable

set gui-endpoint-control disable

set gui-wireless-controller disable

set gui-wan-load-balancing enable

set gui-antivirus disable

set gui-webfilter disable

set gui-multiple-interface-policy enable

set gui-application-control enable

set gui-webfilter enable

set gui-ztna enable

set gui-dns-database enable

end

7.3 – Desabilitar modo anicast da licença fortiguard.

config system fortiguard

set fortiguard-anycast disable

end

7.4 – Criar todas as redes necessárias para a unidade.

config system interface

edit "VLAN103"

set vdom "root"

set ip ==172.21.158.199== 255.255.255.0

set allowaccess ping

set alias "LAN-Ativos-Rede"

set device-identification enable

set role lan

set interface "internal1"

set vlanid 103

next

edit "VLAN104"

set vdom "root"

set ip ==172.21.159.199== 255.255.255.0

set allowaccess ping https ssh snmp fgfm

set alias "LAN-FortiGates"

set device-identification enable

set role lan

set interface "internal1"

set vlanid 104

next

edit "VLAN113"

set vdom "root"

set ip ==172.21.157.199== 255.255.255.0

set allowaccess ping

set alias "LAN-Ativos-WiFi"

set device-identification enable

set role lan

set interface "internal1"

set vlanid 113

next

edit "VLAN2000"

set vdom "root"

set dhcp-relay-service enable

set ip ==172.21.144.199== 255.255.255.0

set allowaccess ping

set alias "LAN-Computadores"

set device-identification enable

set role lan

set dhcp-relay-ip "172.31.111.10"

set interface "internal1"

set vlanid 2000

next

edit "VLAN3100"

set vdom "root"

set dhcp-relay-service enable

set ip ==172.21.146.199== 255.255.255.0

set allowaccess ping

set alias "VLAN3100"

set device-identification enable

set role lan

set dhcp-relay-ip "172.31.111.10"

set interface "internal1"

set vlanid 3100

next

edit "VLAN3210"

set vdom "root"

set dhcp-relay-service enable

set ip ==172.21.148.199== 255.255.255.0

set allowaccess ping

set alias "LAN-Impressoras"

set device-identification enable

set role lan

set dhcp-relay-ip "172.31.111.10"

set interface "internal1"

set vlanid 3210

next

edit "VLAN3220"

set vdom "root"

set ip ==172.21.156.199== 255.255.255.0

set allowaccess ping

set alias "LAN-Relogios"

set device-identification enable

set role lan

set interface "internal1"

set vlanid 3220

next

edit "VLAN3230"

set vdom "root"

set ip ==172.21.155.199== 255.255.255.0

set allowaccess ping

set alias "LAN-VoIP"

set device-identification enable

set role lan

set interface "internal1"

set vlanid 3230

next

edit "VLAN3240"

set vdom "root"

set ip ==172.21.154.199== 255.255.255.0

set allowaccess ping

set alias "LAN-Cameras"

set device-identification enable

set role lan

set interface "internal1"

set vlanid 3240

next

edit "VLAN3192"[\[IV1\]](file:///U:/Configuração%20Fortigate%2060E.docx#_msocom_1)

set vdom "root"

set ip ==172.21.150.199== 255.255.255.0

set allowaccess ping

set alias "WLAN-FRIMESA-COLAB"

set security-mode captive-portal

set security-external-web "<https://cppm.frimesa.com.br/guest/colab_autentication.php>"

set security-redirect-url "<https://eu.frimesa.com.br>"

set device-identification enable

set role lan

set interface "internal1"

set vlanid 3192

next

edit "VLAN3167"

set vdom "root"

set ip ==172.21.57.199== 255.255.255.0

set allowaccess ping

set alias "WLAN-IOT"

set device-identification enable

set role lan

set interface "internal1"

set vlanid 3167

next

edit "VLAN3160"

set vdom "root"

set ip ==172.21.152.199== 255.255.255.0

set allowaccess ping

set alias "WLAN-MOBILE"

set device-identification enable

set role lan

set interface "internal1"

set vlanid 3160

next

edit "VLAN122"

set vdom "root"

set allowaccess ping https ssh snmp fgfm

set alias "WAN-Link-Principal"

set device-identification enable

set role wan

set interface "internal1"

set vlanid 122

next

end

7.5 – Criar uma zona interna e adicionar todas as LANs criadas para a filial. Esta será utilizada nas regras que se referem a todas as redes da filial

config system zone

edit "zn_AtivosRede"

set interface VLAN103

next

edit "zn_AtivosWifi"

set interface VLAN113

next

edit "zn_ControleAcesso"

set interface VLAN3220

next

edit "zn_InternalLAN"

set interface VLAN104 VLAN2000 VLAN3100 VLAN3210 VLAN3240

next

edit "zn_Voip"

set interface VLAN3230

next

end

7.6 – Configurar DHCP Server para todas as redes que necessitam. Ajustar de acordo com a necessidade das redes da unidade.

config system dhcp server

edit 0

set default-gateway ==172.21.157.199==

set netmask 255.255.255.0

set interface "VLAN113"

config ip-range

edit 0

set start-ip ==172.21.157.1==

set end-ip ==172.21.157.198==

next

edit 0

set start-ip ==172.21.157.200==

set end-ip ==172.21.157.254==

next

end

set timezone-option default

set dns-server1 172.31.107.101

set dns-server2 172.31.107.102

set dns-server3 172.31.107.103

next

edit 0

set default-gateway ==172.21.155.199==

set netmask 255.255.255.0

set interface "VLAN3230"

config ip-range

edit 0

set start-ip ==172.21.155.4==

set end-ip ==172.21.155.198==

next

edit 0

set start-ip ==172.21.155.200==

set end-ip ==172.21.155.254==

next

end

set timezone-option default

set dns-server1 172.31.107.101

set dns-server2 172.31.107.102

set dns-server3 172.31.107.103

next

edit 0

set mac-acl-default-action block

set default-gateway ==172.21.154.199==

set netmask 255.255.255.0

set interface "VLAN3240"

config ip-range

edit 0

set start-ip ==172.21.154.1==

set end-ip ==172.21.154.198==

next

edit 0

set start-ip ==172.21.154.200==

set end-ip ==172.21.154.254==

next

end

set timezone-option default

set dns-server1 172.31.107.101

set dns-server2 172.31.107.102

set dns-server3 172.31.107.103

next

edit 0

set mac-acl-default-action block

set default-gateway ==172.21.152.199==

set netmask 255.255.255.0

set interface "VLAN3160"

config ip-range

edit 0

set start-ip ==172.21.152.1==

set end-ip ==172.21.152.198==

next

edit 0

set start-ip ==172.21.152.200==

set end-ip ==172.21.152.254==

next

end

set timezone-option default

set dns-server1 172.31.107.101

set dns-server2 172.31.107.102

set dns-server3 172.31.107.103

next

edit 0

set mac-acl-default-action block

set default-gateway ==172.21.59.199==

set netmask 255.255.255.0

set interface "VLAN3167"

config ip-range

edit 0

set start-ip ==172.21.57.1==

set end-ip ==172.21.57.198==

next

edit 0

set start-ip ==172.21.57.200==

set end-ip ==172.21.57.254==

next

end

set timezone-option default

set dns-server1 172.31.107.101

set dns-server2 172.31.107.102

set dns-server3 172.31.107.103

next

edit 0

set lease-time 60000

set default-gateway ==172.21.150.199==

set netmask 255.255.255.0

set interface "VLAN3192"

config ip-range

edit 0

set start-ip ==172.21.150.2==

set end-ip ==172.21.150.254==

next

end

set dns-server1 208.67.222.222

set dns-server2 208.67.222.220

next

end

7.7 – Configurar monitoramento Zabbix.

config system snmp community

edit 0

set name "zabbixby7"

config hosts

edit 0

set ip 172.31.106.250 255.255.255.255

next

end

next

end

\*É necessário ativar o SNMP Agent manualmente

![image14](../../../../_resources/image14.png)

7.8 – Criar rota para o FortiManager.

config router static

edit 0

set dst 189.42.118.169 255.255.255.255

set gateway 189.42.118.161

set device VLAN123

end

7.9 – Adicionar a caixa na gerência do FortiManager (ele responde no IP da Embratel, caso ocorra algum problema, pode-se adicionar o IP 189.42.118.169. Porém, ao encaminhar para filial, o mesmo deve ser alterado para sua URL e validado que o DNS da caixa está conseguindo resolvê-la.

config system central-management

set type fortimanager

set fmg "fgtmgmt.frimesa.com.br"

end

8 – Configurar comando em todas as VLANs com DHCP relay para SEDE.

config system interface

edit VLAN2000

set dhcp-relay-interface-select-method sdwan

next

edit VLAN3210

set dhcp-relay-interface-select-method sdwan

next

edit VLAN3100

set dhcp-relay-interface-select-method sdwan

next

end

config system fortiguard

==set dhcp-relay-interface-select-method sdwan==

end

9 – Concluídas etapas acima, deve ir para o FortiManager e aprovar a caixa, adicionando-a na sua VDOM.

| Editor      | Data       | Motivo                  | Alteração |
|-------------|------------|-------------------------|-----------|
| Iago Vargas | 26/01/2024 | Criação da documentação |          |
|             |            |                         |           |
|             |            |                         |           |
|             |            |                         |           |
|             |            |                         |           |

