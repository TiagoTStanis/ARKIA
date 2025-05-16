**<u>Appliance</u>**

- IP: 172.31.106.43;
- RAM: 8GB;
- Adaptador de rede: PUBLICA, vlan 106;
- SCSI: Dois discos:
  - Disco 1: Sistema operacional, 100GB.
    - Caminho: C:\ClusterStorage\VV_WOLFSWOOD_RPLIN02_DC1\SIENAL\Virtual Hard Disks\SIENAL.vhdx
  - Disco 2: Aplicações, 100GB. Montado em /u01.
    - Caminho: C:\ClusterStorage\VV_WOLFSWOOD_RPLIN02_DC1\SIENAL\Virtual Hard Disks\SIENAL_APP.vhdx

**<u>Arquitetura</u>**

Este serviço foi desenvolvido em JAVA e usa do Tomcat como WebService para disponibilizar sua aplicação.
- JDK 8u202:
  - Path: ==/u01/java/latest/bin/==
- Tomcat:
  - Path: ==/u01/tomcat/apache-tomcat-9.0.58/bin/==
  - Inicializar serviço: \# ==sh startup.sh==
    - Acesso: <http://172.31.106.43:8080/automacao/>
  - Path:==/u01/tomcat/apache-tomcat 9.0.58/webapps/FR_WebServicesWMS==
    - Acesso: <http://172.31.106.43:8080/FR_WebServicesWMS/restai/automacao/>
- Aplicação Automação:
  - Path: ==/u01/Automacao/servidores-rmi-automacao/prod/bin/==
  - Inicializar serviço: \# ==./prod start==
- Servidor Spoon coletando dados da refinaria, graxaria e Câmera da Toscana:
  - Path: ==/u01/Automacao/servidores-rmi-automacao/spoon-server/bin/==
  - Inicializar serviço: \# ==./spoon-server start==

**<u>Contas de Serviço</u>**

Geral: User: bpm – Password: 4ut@m!1310

Mosquitto: User: mosquitto – Password: @ntenn4e

**<u>Configurações do Ambiente</u>**

Portas liberadas no firewall: 1883 (Mosquitto), 8080 (Tomcat), 9024, 9026, 9096, 9097, 9098 e 9099;

Possui regras de acesso SSH no firewall;

Todas as regras e scripts para execução estão na pasta /frinfra/util/;

Timezone BRT America/Sao_Paulo;

Chronyd como NTP;

Variáveis de ambiente nos usuários root e bpm:

==\# vim /home/bpm/.bash_profile==

==PATH=\$PATH:\$HOME/bin==

==export PATH==

==export JAVA_HOME=/u01/java/latest==

==export CATALINA_HOME=/u01/tomcat/latest==

==PATH=\$PATH:\$HOME/.local/bin:\$HOME/bin:/snap/bin==

**<u>Configurações Gerais</u>**

**JDK**

Passar o arquivo para a máquina, extrair na pasta /u01 e criar um link simbólico latest.

==\# cd /u01/java==

==\# tar -zvxf jdk8u202-linux-x64.tar.gz==

==\# ln -s jdk1.8.0_202/ latest==

==\# chown -R bpm:bpm .==

**TOMCAT**

Necessário conta de serviço para o sistema. Usamos a bpm. Usado Tomcat 9.0.58, baixado diretamente do site.

==\# cd /u01/tomcat==

==\# tar -zvxf apache-tomcat-9.0.30.tar.gz==

==\# ln -s apache-tomcat-9.0.30 latest==

**MOSQUITTO**

No Oracle Linux 8, a instalação do Mosquitto é realizada através do snap. Para este, é necessário instalação do epel-release e snapd.

Epel-Release (RHEL 8):

==dnf install <https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm>==

Após, instalar o snapd e inicializar:

==yum install snapd==

==systemctl enable –now snapd.socket==

Habilitar suporte clássico snap:

==ln -s /var/lib/snapd/snap /snap==

Instalar mosquito:

==snap install mosquito==

Após instalar, adicionar o /snap/bin na variável path, através do .bash_profile, para executar os binários instalados pelo snap:

==PATH=\$PATH:\$HOME/.local/bin:\$HOME/bin:/snap/bin==

Autenticação MQTT: Criar um arquivo com o nome creds.txt, adicionar o usuário na seguinte formatação: username1:password1 e criptografar o arquivo com o seguinte:

==mosquito_passwd -U creds.txt==

Criar um arquivo de configuração do mosquitto:

==vim /var/snap/mosquito/common/mosquito.conf==

==listener 1883==

==allow_anonymous false==

==password_file /var/snap/mosquito/common/mosquito.conf==

Adicionar porta no firewall

==firewall-cmd --permanent --zone=public --add-port=1883/tcp==

Reiniciar o serviço:

==snap restart mosquitto==

Fonte: <https://blogs.oracle.com/developers/post/installing-securing-mosquitto-for-encrypted-mqtt-messaging-in-the-oracle-cloud>

**<u>Últimas atualizações</u>**  

| Editor            | Data       | Motivo                  | Alteração |
|-------------------|------------|-------------------------|-----------|
| André Luiz Fronza | 11/04/2022 | Criação da documentação |          |
| André Luiz Fronza | 24/11/2023 | Padronização            |           |
|                   |            |                         |           |
|                   |            |                         |           |
|                   |            |                         |           |

