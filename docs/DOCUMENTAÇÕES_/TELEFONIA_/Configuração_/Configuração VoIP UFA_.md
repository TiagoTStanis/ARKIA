Configuração VoIP UFA
Friday, November 24, 2023
1:57 PM

**<u>Arquitetura</u>**

n/a

**<u>Contas de Serviço</u>**

n/a

**<u>Configurações do Ambiente</u>**

n/a

**<u>Configurações Gerais</u>**

Vá em Maintence -\> Upgrade and Provisioning e de um reset nas abas Firmware e Config File (se config file falhar, apenas ignore)

Mude a senha em System Settings -\> Security Settings -\> User Info Management -\> Admin Password:

Senha antiga: GsVm22

Senha nova: frimesa-ufa

Obs.: Aqui terminam os resets necessários caso o telefone já tenha sido configurado anteriormente. Idealmente, é indicado o reset de fábrica no aparelho, pois assim não ficam configurações "lixo" restantes no telefone.

Vá em Programmable Keys -\> Idle Screen Softkeys e remova a opção "5. Não perturbe"

Vá para Accounts e em General Settings, altere o seguinte:

Account Name: RAMAL

SIP Server: 172.26.128.1

SIP User ID: RAMAL

SIP Authentication ID: RAMAL

SIP Authentication Password: drk3rt

Name: Nome do local (ex: Suporte T.I.)

Salve e aplique.
- ![image1](../../../_resources/image1-34.png)

Vá em Status, se em Account, estiver com o ícone verde e no SIP Server puxando o IP correto, funcionou. Ex.

![image2](../../../_resources/image2-16.png)

**<u>Últimas atualizações</u>**  

| Editor            | Data       | Motivo                  | Alteração |
|-------------------|------------|-------------------------|-----------|
| André Luiz Fronza | 20/11/2023 | Criação da documentação |          |
| André Luiz Fronza | 24/11/2023 | Padronização            |           |
|                   |            |                         |           |
|                   |            |                         |           |
|                   |            |                         |           |


