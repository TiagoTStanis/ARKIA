Instalar Kaspersky MacOS
Friday, March 1, 2024
9:41 AM

**<u>Arquitetura</u>**

n/a

**<u>Contas de Serviço</u>**

Usuário administrador local

**<u>Configurações do Ambiente</u>**

n/a

**<u>Configurações Gerais</u>**
Para realizar a instalação, o agente de rede será realizado através de uma conta administrador na máquina, e o Endpoint pelo agente de rede.
I. Permitir acesso remoto via SSH a máquina:
a\. Vá nas configurações do sistema, compartilhamento e configure conforme imagem a seguir:
![image1](../../../_resources/image1-18.png)
II\. Atribuir permissão total para acesso via SSH ao usuário administrador.
a\. Abra o terminal, digite o comando \[sudo visudo\] e coloque a senha do usuário administrador.
Na linha 56, de um enter e adicione o seguinte \[administrador ALL = (ALL) NOPASSWD: ALL\]. Essa linha permitirá que o usuário administrador execute todos os comandos sem solicitar senha.
![image2](../../../_resources/image2-10.png)

b\. Saia do editor vim e feche o terminal.
III\. Após as configurações acimas, agora possuímos permissão completa para acesso remoto. O próximo passo é realizar [download](https://www.kaspersky.com/small-to-medium-business-security/downloads/endpoint?icid=gl_sup-site_trd_ona_oth__onl_b2b_klsupport_tri-dl____kes___) <u>dos instaladores na página do Kaspersky:</u>
a\. Primeiramente, realize o download e execute o Plugin para o Security center:
![image3](../../../_resources/image3-6.png)

![image4](../../../_resources/image4-5.png)
b\. Após, é necessário baixar o Agente de Rede e o Endpoint (Distributive):
c\. Descompacte os arquivos.
IV\. Criar pacote de instalação do Network Agent:
a\. Abra o Security Center;
b\. Vá em Avançado -\> Instalação remota -\> Pacotes de Instalação;
c\. Crie um pacote de instalação -\> Criar um pacote de instalação para um aplicativo Kaspersky -\> Atribua um nome -\> Procurar -\> Vá na pasta do Network Agent que baixou na internet e selecione o arquivo .KUD e clique em abrir, irá aparecer a versão do aplicativo -\> Aceite o contrato -\> Avançar e OK.
d\. Após criado, vá em Configurar pacote de instalação, na aba Configurações defina uma senha de desinstalação e em conexão altere o servidor de administração para o IP do servidor, não pode ser o hostname.
e\. Agora, vamos instalar o aplicativo, selecione a opção “Selecionar dispositivos para a instalação” e adicione o endereço IP da máquina qual deseja instalar -\> Desmarque a opção “Usando o agente de Rede” -\> Não migrar dispositivos -\> Conta Necessária (coloque a conta administrador local da máquina, qual tem acesso ao SSH configurado no passo II) -\> Marque a opção “Não executar a tarefa após a conclusão do Assistente de Instalação Remota” -\> Concluir.
f\. Por fim, na tarefa criada na seção anterior, vá em Configurações e desmarque a opção “Verificar o tipo do Sistema operacional antes de baixar”.
g\. Após, basta iniciar a task, esperar finalizar, esperar mais um pouco para o Agente de rede enviar as informações ao Kaspersky e verificar se funcionou.
V. Criar pacote de instalação do Endpoint:
a\. Neste, siga a etapa 4, até a seção C, apenas alterando o arquivo do Agente de Rede para o do Endpoint, qual também foi baixado anteriormente.
b\. No tipo de instalação, onde solicitar os pacotes de instalação, deixe todos selecionados.
c\. Após, instalar a aplicação -\> selecionar o dispositivo através do IP -\> Realizar a instalação através do Network Agent -\> Não usar chave -\> Não usar conta -\> Avançar e Ok.
d\. Por fim, basta iniciar a task.
VI\. Permissões Kaspersky, ativação e KSN:
a\. Etapa intuitiva, basta apenas permitir conforme for solicitado.
![image5](../../../_resources/image5-2.png)
b\. Após, ative o Kaspersky, caso ainda não esteja ativo;
c\. Va as preferencias do Kaspersky, selecione a aba KSN e marque a opção “Participar na Kaspersky Security Network”.
d\. Atualize o banco e pronto.

**<u>Últimas atualizações</u>**  

| Editor            | Data       | Motivo                  | Alteração |
|-------------------|------------|-------------------------|-----------|
| André Luiz Fronza | 01/03/2024 | Criação da documentação |          |
|                  |           |                        |           |
|                   |            |                         |           |
|                   |            |                         |           |
|                   |            |                         |           |


