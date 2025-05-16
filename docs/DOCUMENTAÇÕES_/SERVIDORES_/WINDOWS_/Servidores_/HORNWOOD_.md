AM

**<u>Appliance</u>**

- IP: 172.31.107.36;
- RAM: 5GB;
- Adaptador de rede: PUBLICA, vlan 107;
- SCSI: Um discos:
  - Disco 1: Sistema operacional, 100GB.
    - Caminho: C:\ClusterStorage\VV_WOLFSWOOD_RPWIN01_DC1\HORNWOOD

**<u>Arquitetura</u>**

Serviços na máquina: DCA and Cloud Connector

**<u>Contas de Serviço</u>**

n/a

**<u>Configurações do Ambiente</u>**

- Comunicação entre servidor e impressoras:
  - Protocolo SNMP, portas 161 e 162;
- Comunicação entre servidor e nuvem NDD:
  - Protocolo HTTP e HTTPS, portas 80 e 443.
  - 
**<u>Configurações Gerais</u>**

- DCA and Cloud Connector;
  - Serviço para gerenciamento e monitoramento das impressoras;
  - Não disponibiliza interface gráfica no servidor;
  - É composto por cinco serviços apenas, sendo estes:
    - NDD – Computer Monitor;
    - NDD – DCA and Cloud Connector;
    - NDD – Print Queue;
    - NDD – Printer Monitor;
    - NDD – Printer Monitor USB.
  - O gerenciamento da aplicação é realizado via WEB, na plataforma da NDD Orbix, qual o pessoal da Docutech possui acesso. Nesta plataforma, é possível verificar informações sobre as impressoras de determinadas faixas de rede (informadas pela infraestrutura¹) e informações do servidor (recurso utilizado, informações básicas de hardware e S.O.). Também é possível reiniciar, de forma remota, os serviços da NDD no servidor.
  - Os serviços executam a cada duas horas para realizar a busca das informações nas impressoras na rede.
¹ É necessário o mapeamento de todas as faixas de IP’s de impressoras e repassar a Docutech para inserção das faixas para busca na plataforma NDD

Chave para ativação:

Provedor: DOCUTECH

Chave: 31e5c4fb-152d-44cd-c1b0-08dbc4d34427

O NDD ainda não é usado, apenas o Print Audit. Print AUDIT 6 já foi descontinuado e não é usado. Atualmente é usado o Print Audit ICE Administrator.

**<u>Últimas atualizações</u>**  

| Editor            | Data       | Motivo                  | Alteração |
|-------------------|------------|-------------------------|-----------|
| André Luiz Fronza | 11/04/2022 | Criação da documentação |          |
| André Luiz Fronza | 24/11/2023 | Padronização            |           |
|                   |            |                         |           |
|                   |            |                         |           |
|                   |            |                         |           |

