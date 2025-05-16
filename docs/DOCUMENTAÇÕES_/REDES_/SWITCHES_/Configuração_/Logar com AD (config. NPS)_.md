**<u>Arquitetura</u>**  
Servidores ThreeTowers.  
Switches.

**<u>Contas de Serviço</u>**  
Conta para conexão dos switches com o NPS. Senha no KeePass compartilhado da infraestrutura.

**<u>Configurações do Ambiente</u>**

**Radius Client and Servers:**  
Configuração de cliente RADIUS (RADIUS Clients):  
![image1](../../../../_resources/image1-3.png)  
Tela usado para identificar os clientes que o NPS receberá solicitações. Neste também é definido a senha para a conexão com o NPS.

**Policies:**  
Connection Request Policies:  
Aqui temos duas políticas criadas especificadamente para switches, porém estas não são necessárias, pois possui uma política padrão do NPS que recebe todas as conexões, a política "Use Windows Authentication for all users";

Network Policies:  
Nesta tela é feita a configuração da política que irá permitir logon de um usuário AD no switch.  
Primeiramente, nota-se que há dois modelos diferentes de configuração, logon usando PAP e PEAP. PAP é um método sem criptografia e PEAP usa criptografia. PAP é usado nos 1920 e PEAP nos 2930F. Atente-se a ordem também, onde o PEAP é antes do PAP, isso se faz pois o NPS verifica as regras de cima para baixo, se um switch 2930F fizer uma solicitação e a política de PAP estiver acima da PEAP, está ele irá utilizar, porém ocorrerá em erro devido a diferença de método de autenticação.

**Política PAP:**  
Overview:  
![image2](../../../../_resources/image2-1.png)

Conditions:  
![image3](../../../../_resources/image3-1.png)  
Nesta tela selecionamos as condições para acesso. Aqui colocamos que o usuário deve ser membro do grupo "ACESSO-SWITCHES" e o Switch deve ter um IP na faixa 172.31.103.0.

Constraints:  
![image4](../../../../_resources/image4.png)  
Nesta tela apenas colocamos qual o tipo de autenticação a ser utilizado, neste caso, autenticação sem criptografia PAP.

Settings:  
![image5](../../../../_resources/image5.png)  
Por fim, realizamos as configurações finais, onde definimos o tipo de serviço como Administrativo. O serviço tipo administrativo permite logon ao usuário a interface administrativa onde é possível ser executado comandos privilegiados.  
https://www.rfc-editor.org/rfc/rfc2865.html#page-31

![image6](../../../../_resources/image6.png)

Apesar de definirmos o acesso como administrativo, ainda precisamos uma flag a mais para permitir a execução de comandos privilegiados no 1920. Este pode ser definido configurando um atributo específico do fornecedor, neste caso, da HPE/Comware.  
Para permitir, é necessário criar um novo atributo, com o código de fornecedor 2011, usando o atributo 29 de valor decimal 3 (três níveis, sendo o nível 3 o maior).

**Política PEAP**:  
Na política PEAP, muda-se apenas alguns parâmetros, sendo estes:  
Conditions:  
![image7](../../../../_resources/image7.png)  
Neste é adicionado a condição do tipo de autenticação, sendo especificado EAP;

Constraints:  
![image8](../../../../_resources/image8-1.png)  
Especifica o uso do PEAP;

Settings:  
![image9](../../../../_resources/image9.png)  
Apenas coloque o serviço como tipo administrativo. O nível de permissão após o logon é feito diretamente através de comandos executados no switch.

**<u>CASO QUEIRA APENAS REPLICAR AS CONFIGURAÇÕES:</u>**

Acessar threetowers 1,2 ou 3 > Abrir Network Policy Server

1 - Em "Policies" > "Network Policies" duplicar política que possui as mesmas características que o seu caso necessita  
SW 2930 - PEAP

SW 1920 - PAP

Caso a filial tenha os 2 modelos, fazer duas políticas, mas colocar na seguinte ordem:

1º PEAP

2º PAP

![image10](../../../../_resources/image10.png)

2 - Na aba "Overview" atualizar nome da política e ativa-la checando a caixa conforme imagem a seguir:

![image11](../../../../_resources/image11-1.png)

3 - Na aba "Conditions" atualizar o IP com o da rede da vlan 103 (lan-ativos-rede) e então aplicar

![image12](../../../../_resources/image12.png)

4 - Mover para cima até ficar sobre "Connections to other access servers"  
![image13](../../../../_resources/image13.png)

5 - Em "RADIUS Clients and Servers" > "RADIUS Clients" clicar em "New"

![image14](../../../../_resources/image14-1.png)

6 - Na aba "Settings" adicionar nome conforme padrão, IP com o da rede da filial e a senha

![image15](../../../../_resources/image15.png)

**Configurações Gerais**

A ser executado no switch:  
2930F:  
#UFM – 2930F  
radius-server host 172.31.107.102 key "----"  
radius-server host 172.31.107.103 key "----"  
aaa server-group radius "threetowers" host 172.31.107.102  
aaa server-group radius "threetowers" host 172.31.107.103  
aaa authentication login privilege-mode  
aaa authentication ssh login peap-mschapv2 server-group "threetowers" local  
aaa authentication ssh enable peap-mschapv2 server-group "threetowers" local  
#UFA – 2930F  
radius-server host 172.26.249.104 key "----"  
aaa server-group radius "threetowers" host 172.26.249.104  
aaa authentication login privilege-mode  
aaa authentication ssh login peap-mschapv2 server-group "threetowers" local  
aaa authentication ssh enable peap-mschapv2 server-group "threetowers" local

1920:

#NPS  
radius scheme frradiusws  
server-type extended  
primary authentication 172.31.107.103 key simple ----  
secondary authentication 172.31.107.102 key simple -----  
user-name-format without-domain  
attribute 25 car  
\# nas-ip 172.31.103.47  
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
domain default enable ws

**<u>Últimas atualizações</u>**

| Editor | Data | Motivo | Alteração |
| --- | --- | --- | --- |
| Thiago Leite | 20/02/2024 | Criação da documentação |     |
| André Luiz Fronza | 21/02/2024 | Informações adicionais | Informações gerais e especificas sobre o NPS |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |