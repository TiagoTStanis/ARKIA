**<u>Arquitetura</u>**
- Hostname: Essovius
- IP: 172.31.201.2;
- RAM: 48GB;
- CPU: 24VCPU
- Adaptador de rede: PUBLICA, vlan 201;
- SCSI: Tres discos:
  - 1 S.O.: 100GB
  - 1 APP: 100GB
  - 1 Imagens: 130TB

- Hostname: Jaegeri
- IP: 172.26.249.7;
- RAM: 52GB;
- CPU: 24VCPU
- Adaptador de rede: PUBLICA, vlan 1249;
- SCSI: Tres discos:
  - 1 S.O.: 100GB
  - 1 APP: 100GB
  - 1 Imagens: 46TB
  - 2 Imagens: 46TB

- Hostname: Visby
- IP: 172.19.255.2;
- RAM: 14GB;
- CPU: 10VCPU
- Adaptador de rede: PUBLICA, vlan 1255;
- SCSI: Tres discos:
  - 1 S.O.: 100GB
  - 1 APP: 100GB
  - 1 Imagens: 67TB
.

**<u>Contas de Serviço</u>**

n/a

**<u>Configurações do Ambiente</u>**

Server -\> câmeras: Ping HTTP, HTTP_8000, porta 554 e porta 137.

Client -\> Server: HTTPS e Dynamic Ports (49152-65535 TCP e UDP)

**<u>Configurações Gerais</u>**

Já possuímos diversos tutoriais de configurações das câmeras na guia CMERAS -\> CMERAS.

Deixarei este para registrar alguns problemas que já ocorrem no servidor:

- Serviço InfoService reiniciando constantemente devido a problema no HTTP (servidor não consegue subir WebServer, erro The application domain in which the thread was running has been unloaded. / Failed to start the web server):

A solução encontrada para este erro foi a alteração do TLS no servidor, ativando os TLS's, usando o IISCRYPTO:

![image1](../../../../_resources/image1-23.png)

- Câmeras ativas porém aparecem como desativadas no Symphony (erro Live555 error message: bind() error (port number: 5961):
Este problema era referente as portas dos servidores, em servidores que tem muitas câmeras, se faz necessário permitir mais portas do que o default:

==netsh int ipv4 show dynamicport tcp==

==netsh int ipv4 show dynamicport udp==

==netsh int ipv4 set dynamicport tcp start=5100 num=15000==

==netsh int ipv4 set dynamicport udp start=5100 num=15000==

**<u>Últimas atualizações</u>**  

| Editor            | Data       | Motivo                  | Alteração |
|-------------------|------------|-------------------------|-----------|
| André Luiz Fronza | 10/04/2024 | Criação da documentação |          |
|                  |           |                        |           |
|                   |            |                         |           |
|                   |            |                         |           |
|                   |            |                         |           |

