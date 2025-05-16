**Configuração Fortigate 40F**

****

**Equipamentos necessários**
- 2 caixas Fortigate modelo 40F
- 3 cabos de rede
- 1 adaptador de rede (RJ45 – USB)
- 1 cabo console

**1 – Conexão física**

1.1 – Primeiramente deve-se conectar as duas caixas para uso da “HA”, isto faz com a caixa tenha alta disponibilidade, em caso de falha em uma delas, a segunda já entra em ação, as portas a serem usadas para isto são:

Porta 2 ——————- Porta 2

Porta 3 ——————- Porta 3

1.2 – Feito isto, deve ser verificado quem é a caixa com o S/N mais alto, pois é assim que o Fortigate irá eleger quem será a caixa master, e consequentemente a caixa de número menor, será a slave.

1.3 – Conectar o cabo console na entrada console do Fortigate master

1.4 – Conectar o cabo de rede na porta “a” do fortigate e no adaptador de rede conectado ao computador.

**2 – Conexão Console**

2.1 - Acessar via Putty com a velocidade 9600.

2.2 – Se ao entrar você se deparar com a mensagem:

![image1](../../../../_resources/image1.jpg)

Significa que o fortigate não possui nenhum firmware instalado.

2.3 – Se ao entrar você se deparar com a mensagem solicitando login, significa que o fortigate possui firmware e possivelmente está configurado.

2.4 – No caso de o firmware já estar instalado deverá ser formatado e feito novamente.

**3 – Firmware**

3.1 – Para instalar o firmware você deve possuir o arquivo .out da versão homologada e utilizada atualmente no ambiente. Na data da documentação, o firmware utilizado é o: **FGT_40F-v7.0.12.M-build0523-FORTINET.out**

3.2 – É possível localizar o firmware no Sharepoint: T.I. Infra - Procedimentos técnicos \> Documentos \> General \> Firmwares \> FORTIGATE

**4 – Configuração TFTP para transferência do Firmware**

4.1 – Ao iniciar o menu de configuração você pode verificar os parâmetros TFTP clicando \[**R**\]

![image2](../../../../_resources/image2.jpg)

4.2 – Ao clicar, você verá uma tela como esta:

![image3](../../../../_resources/image3.jpg)

4.3 – Configurações:
- Image download port: A (porta que conectamos o cabo de rede)
- Local VLAN ID: N/A
- Local IP address: IP do fortigate (padrão)
- Local subnet mask: N/A
- Local gateway: N/A
- TFTP server IP: 192.168.1.100 (este IP deve ser configurado no adaptador)
- Firmware file name: FGT_40F-v7.0.12.M-build0523-FORTINET.out
4.4 – Para configurar os parâmetros:
- \[**C**\]: Configure TFTP parameters.
- \[**F**\]: Set firmware file name (digitar o firmware selecionado)
- \[**H**\]: Display this list of options.
- \[**P**\]: Set firmware download port.
- \[**3**\]: port A.
- \[**Q**\]: Quit this menu.

**5 – Transferência TFTP**

5.1 – Para transferência é necessário download de algum programa que permita a transferência TFTP do firmware para a caixa. Neste exemplo, irei utilizar o programa **Tftpd64**.

5.2 – O programa pode ser baixado no SharePoint na mesma pasta dos Firmwares.

5.3 – Configurar o adaptador de rede com mesmo IP setado nos parâmetros de TFTP (neste caso, 192.168.1.100).

5.4 – Abrir o programa baixado:
- Current Directory -\> caminho onde se encontra o firmware.
- Server interfaces -\> adaptador de rede

![image4](../../../../_resources/image4.jpg)

5.5 – Retornar ao console

\[**T**\]: Initiate TFTP firmware transfer.

![image5](../../../../_resources/image5.jpg)

Save as Default firmware/Backup firmware/Run image without saving:\[D/B/R\]? **D**

Continue:\[Y/N\]? **Y**

![image6](../../../../_resources/image6.jpg)

**OBS.: Se o Kaspersky estiver pausado o Firewall do Windows irá assumir o controle da máquina, consequentemente bloqueará a tentativa de transferência.**

**6 – Configuração Fortigate**

Login: admin

Password: blank

6.1 – Deletar configurações padrões não necessárias.

config firewall address

delete lan

end

config firewall policy

delete 1

end

config system dhcp server

delete 1

end

config system ntp

unset server-mode

end

config system virtual-switch

delete lan

end

6.2 – Realizar configurações administrativas da caixa.

config system global

set admin-scp enable

set admin-sport 8443

set admintimeout 30

set gui-theme neutrino

set hostname "UFLM-ADM-G01"

set switch-controller enable

set timezone 18

set gui-firmware-upgrade-warning disable

set gui-forticare-registration-setup-warning disable

unset alias

end

6.3 – Configurar a interface DMZ, está será utilizada para fazer o acesso para configurações individuais na caixa.

config system interface

edit "a"

set ip ==172.21.143.2== 255.255.255.0 **\#setar IP da caixa**

set allowaccess ping https ssh fgfm snmp

set type physical

set device-identification enable

set lldp-transmission enable

set role lan

next

end

**OBS.: A PARTIR DAQUI É POSSÍVEL CONFIGURAR TANTO POR CLI QUANTO GUI**

6.4 – Alterar o IP do adaptador para a mesma faixa de IP da caixa. Após, acessar o firewall pelo IP setado -\> <https://ip-interface-a:8443>

6.5 – Navegar até Network \> Interfaces \> fortilink
- Remover Interface members;
- Address: Manual
- Receive LLDP: Disable
- Transmit LLDP: Disable
- DHCP Server: Disable
- Status: Disabled

![image7](../../../../_resources/image7.jpg)

6.6 – Deletar interface fortilink.

6.7 – Montar a configuração de HA, é através desta configuração que as duas caixas irão comunicar.

6.7¹ – Configuração por CLI:

config system ha

set group-name "==FIGO-LOG-GHA=="

set mode a-a

set password senhapadraoswitch

set hbdev "lan2" 50 "lan3" 50

set session-pickup enable

set ha-mgmt-status enable

config ha-mgmt-interfaces

edit 1

set interface "a"

set gateway ==172.21.143.199==

next

end

set override disable

set monitor "lan1"

end

6.7² – Configuração por GUI:

![image8](../../../../_resources/image8.jpg)

Todas as configurações acima devem ser realizadas em ambas as caixas fortigate. Após configuração e validação da HA, poderá seguir com a configuração abaixo apenas na caixa Master.

**7 – Configuração Caixa Master**

**OBS.: Informações grifadas em amarelo devem ser alteradas conforme a filial.**

7.1 – Configurar o link secundário para realização das configurações em bancada, através dela será possível simular o link da filial.

config system interface

edit "VLAN123"

set vdom "root"

set mode dhcp

set allowaccess ping https ssh snmp fgfm

set alias "WAN-Link-Secundario

set device-identification enable

set defaultgw disable

set dns-server-override disable

set role wan

set interface "lan1"

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

7.4 – Criar todas as redes necessárias para a unidade.[\[IV(1\]](file:///U:/Configuração%20Fortigate%2040F%20-%20NEW.docx#_msocom_1)

config system interface

edit "VLAN103"

set vdom "root"

set ip ==172.21.142.199== 255.255.255.0

set allowaccess ping

set alias "LAN-Ativos-Rede"

set device-identification enable

set role lan

set interface "lan1"

set vlanid 103

next

edit "VLAN104"

set vdom "root"

set ip ==172.21.143.199== 255.255.255.0

set allowaccess ping https ssh snmp fgfm

set alias "LAN-FortiGates"

set device-identification enable

set role lan

set interface "lan1"

set vlanid 104

next

edit "VLAN113"

set vdom "root"

set ip ==172.21.141.199== 255.255.255.0

set allowaccess ping

set alias "LAN-Ativos-WiFi"

set device-identification enable

set role lan

set interface "lan1"

set vlanid 113

next

edit "VLAN2000"

set vdom "root"

set dhcp-relay-service enable

set ip ==172.21.128.199== 255.255.255.0

set allowaccess ping

set alias "LAN-Computadores"

set device-identification enable

set role lan

set dhcp-relay-ip "172.31.111.10"

set interface "lan1"

set vlanid 2000

next

edit "VLAN3100"

set vdom "root"

set dhcp-relay-service enable

set ip ==172.21.130.199== 255.255.255.0

set allowaccess ping

set alias "VLAN3100"

set device-identification enable

set role lan

set dhcp-relay-ip "172.31.111.10"

set interface "lan1"

set vlanid 3100

next

edit "VLAN3210"

set vdom "root"

set dhcp-relay-service enable

set ip ==172.21.132.199== 255.255.255.0

set allowaccess ping

set alias "LAN-Impressoras"

set device-identification enable

set role lan

set dhcp-relay-ip "172.31.111.10"

set interface "lan1"

set vlanid 3210

next

edit "VLAN3220"

set vdom "root"

set ip ==172.21.140.199== 255.255.255.0

set allowaccess ping

set alias "LAN-Relogios"

set device-identification enable

set role lan

set interface "lan1"

set vlanid 3220

next

edit "VLAN3230"

set vdom "root"

set ip ==172.21.139.199== 255.255.255.0

set allowaccess ping

set alias "LAN-VoIP"

set device-identification enable

set role lan

set interface "lan1"

set vlanid 3230

next

edit "VLAN3240"

set vdom "root"

set ip ==172.21.138.199== 255.255.255.0

set allowaccess ping

set alias "LAN-Cameras"

set device-identification enable

set role lan

set interface "lan1"

set vlanid 3240

next

edit "VLAN3192"[\[IV2\]](file:///U:/Configuração%20Fortigate%2040F%20-%20NEW.docx#_msocom_2)

set vdom "root"

set ip ==172.21.134.199== 255.255.255.0

set allowaccess ping

set alias "WLAN-FRIMESA-COLAB"

set security-mode captive-portal

set security-external-web “<https://cppm.frimesa.com.br/guest/colab_autentication.php>[\[IV(3\]](file:///U:/Configuração%20Fortigate%2040F%20-%20NEW.docx#_msocom_3)”

set security-redirect-url "<https://eu.frimesa.com.br>"

set device-identification enable

set role lan

set interface "lan1"

set vlanid 3192

next

edit "VLAN3167"

set vdom "root"

set ip ==172.21.57.199== 255.255.255.0

set allowaccess ping

set alias "WLAN-IOT"

set device-identification enable

set role lan

set interface "lan1"

set vlanid 3167

next

edit "VLAN3160"

set vdom "root"

set ip ==172.21.136.199== 255.255.255.0

set allowaccess ping

set alias "WLAN-MOBILE"

set device-identification enable

set role lan

set interface "lan1"

set vlanid 3160

next

edit "VLAN122"

set vdom "root"

set allowaccess ping https ssh snmp fgfm

set alias "WAN-Link-Principal"

set device-identification enable

set role wan

set interface “lan1”

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

set default-gateway ==172.21.141.199==

set netmask 255.255.255.0

set interface "VLAN113"

config ip-range

edit 0

set start-ip ==172.21.141.1==

set end-ip ==172.21.141.198==

next

edit 0

set start-ip ==172.21.141.200==

set end-ip ==172.21.141.254==

next

end

set timezone-option default

set dns-server1 172.31.107.101

set dns-server2 172.31.107.102

set dns-server3 172.31.107.103

next

edit 0

set default-gateway ==172.21.139.199==

set netmask 255.255.255.0

set interface "VLAN3230"

config ip-range

edit 0

set start-ip ==172.21.139.4==

set end-ip ==172.21.139.198==

next

edit 0

set start-ip ==172.21.139.200==

set end-ip ==172.21.139.254==

next

end

set timezone-option default

set dns-server1 172.31.107.101

set dns-server2 172.31.107.102

set dns-server3 172.31.107.103

next

edit 0

set mac-acl-default-action block

set default-gateway ==172.21.138.199==

set netmask 255.255.255.0

set interface "VLAN3240"

config ip-range

edit 0

set start-ip ==172.21.138.1==

set end-ip ==172.21.138.198==

next

edit 0

set start-ip ==172.21.138.200==

set end-ip ==172.21.138.254==

next

end

set timezone-option default

set dns-server1 172.31.107.101

set dns-server2 172.31.107.102

set dns-server3 172.31.107.103

next

edit 0

set mac-acl-default-action block

set default-gateway ==172.21.136.199==

set netmask 255.255.255.0

set interface "VLAN3160"

config ip-range

edit 0

set start-ip ==172.21.136.1==

set end-ip ==172.21.136.198==

next

edit 0

set start-ip ==172.21.136.200==

set end-ip ==172.21.136.254==

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

set default-gateway ==172.21.134.199==

set netmask 255.255.255.0

set interface "VLAN3192"

config ip-range

edit 0

set start-ip ==172.21.134.1==

set end-ip ==172.21.134.198==

next

edit 0

set start-ip ==172.21.134.200==

set end-ip ==172.21.134.254==

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

9 – Concluídas etapas acima, deve ir para o FortiManager e aprovar a caixa, adicionando-a na sua VDOM.

| Editor      | Data       | Motivo                  | Alteração |
|-------------|------------|-------------------------|-----------|
| Iago Vargas | 26/01/2024 | Criação da documentação |          |
|             |            |                         |           |
|             |            |                         |           |
|             |            |                         |           |
|             |            |                         |           |

