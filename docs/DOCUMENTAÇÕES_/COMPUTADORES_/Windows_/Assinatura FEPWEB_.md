Assinatura FEPWEB
Friday, November 24, 2023
2:35 PM

**<u>Arquitetura</u>**

n/a

**<u>Contas de Serviço</u>**

n/a

**<u>Configurações do Ambiente</u>**

n/a

**<u>Configurações Gerais</u>**

Quando acessado um site que executa através da plataforma FEPWeb, é necessário o download do Plug-in e do FEPWeb Host instalado na máquina. Ao acessar o site, o plugin chama o executável que carrega os certificados. Uma vez carregado, se alterado, o plugin não chamava o aplicativo host novamente.
Para contornar a situação, foi desabilitado a opção "Executar aplicativos em segundo plano quando o Google Chrome estiver fechado":
![image1](../../../_resources/image1-13.png)

Assim, toda vez que o Chrome é aberto e acessado um site da FEPWeb, o plugin chama o executável novamente, assim carregando o driver correto.
Nota-se que, no entanto, ainda é necessário reiniciar o Google Chrome para funcionar o certificado correto.

**<u>Últimas atualizações</u>**  

| Editor            | Data       | Motivo                  | Alteração |
|-------------------|------------|-------------------------|-----------|
| André Luiz Fronza | 30/10/2023 | Criação da documentação |          |
| André Luiz Fronza | 24/11/2023 | Padronização            |           |
|                   |            |                         |           |
|                   |            |                         |           |
|                   |            |                         |           |

