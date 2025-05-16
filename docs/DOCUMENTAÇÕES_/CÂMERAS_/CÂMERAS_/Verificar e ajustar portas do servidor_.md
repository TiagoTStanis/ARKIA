**<u>Arquitetura</u>**

n/a

**<u>Contas de Serviço</u>**

n/a

**<u>Configurações do Ambiente</u>**

n/a

**<u>Configurações Gerais</u>**

\- Verificar configuração atual das portas:

Abrir cmd e rodar:

netsh int ipv4 show dynamicport udp
netsh int ipv4 show dynamicport tcp

\- Ajustar configuração (para servidor UFA caso esteja entre 5100 e 4900 deve ser ajustado):  

netsh int ipv4 set dynamicport tcp start=5100 num=15000
netsh int ipv4 set dynamicport udp start=5100 num=15000

| Editor       | Data       | Motivo                  | Alteração |
|--------------|------------|-------------------------|-----------|
| Thiago Leite | 29/08/2024 | Criação da documentação |          |
|              |            |                         |           |
|              |            |                         |           |
|              |            |                         |           |
|              |            |                         |           |
