AM

**<u>Arquitetura</u>**

FortiGate CLI.

**<u>Contas de Serviço</u>**

Usuário: \*-adm com grupo de acesso FGT-Admin.

**<u>Configurações do Ambiente</u>**

edit "VLAN2608"
set vdom "vd_frontend"
set dhcp-relay-service enable
set ip 172.26.8.199 255.255.255.0
set allowaccess ping
set description "LAN-ADM"
set device-identification enable
set role lan
set dhcp-relay-ip "172.26.249.104" "172.31.111.10"
set interface "LAN/WAN"
set vlanid 2608
next
end
config system zone
edit zone xxx

append interface "VLAN2613"

next
end

**<u>Configurações Gerais</u>**

n/a

**<u>Últimas atualizações</u>**  

| Editor            | Data       | Motivo                  | Alteração |
|-------------------|------------|-------------------------|-----------|
| André Luiz Fronza | 24/11/2023 | Criação da documentação |          |
|                   |            |                         |           |
|                   |            |                         |           |
|                   |            |                         |           |
|                   |            |                         |           |

