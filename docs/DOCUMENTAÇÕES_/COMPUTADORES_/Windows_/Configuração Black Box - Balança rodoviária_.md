Configuração Black Box - Balança rodoviária
Friday, March 1, 2024
9:34 AM

**<u>Arquitetura</u>**

n/a

**<u>Contas de Serviço</u>**

Usuário administrador local

**<u>Configurações do Ambiente</u>**

n/a

**<u>Configurações Gerais</u>**

1\. Instalar o driver do cabo Black Box
1.1. O driver mais recente do Black Box pode ser encontrado no site da [FTDI](https://ftdichip.com/drivers/d2xx-drivers/)<u>. Nota-se que o driver para ser instalado é o VCP (Virtual COM Port) e D2XX.</u>
1.2. Instalação do driver pelo arquivo executável:
1.2.1. Baixar o arquivo executável e executa-lo com o cabo Black Box desconectado da máquina;
1.3 Baixar pelos arquivos do Driver:
1.3.1. Baixar os arquivos do driver, ir ao gerenciador de dispositivo, e atualizar os drivers do HS USB Serial Cable, selecionar procurar drivers no meu computador e selecionar a pasta em que foi baixado os arquivos do driver. Diferente do passo 1.2.1, esse precisa do Black Box conectado na máquina.
1.4. Após instalar o driver do Black Box, é possível testar, usando o software [Hércules](https://balancascapital.com.br/suporte-grupo-capital/)<u>, disponibilizado pela capital balanças. Caso o software retorne dígitos aleatórios, significa que está com uma falha na comunicação entre o PC e a balança.</u>
2\. Instalar balança rodoviária na máquina
2.1. Para instalar a balança rodoviária, é necessário primeiramente instalar o JAVA.
2.2. Após instalar o Java, instalar ambos o testes de portas e a balança rodoviária.
2.2.1. No testes de portas, selecionar a porta COM que está sendo utilizada, e verificar se está funcionando, ou seja, mostrando o peso.
2.2.2. Para utilizar a balança rodoviária, é necessário configurar no Oracle a máquina que irá utilizar a balança e a porta COM. Caso estas não estejam configuradas, a balança rodoviária irá abrir e fechar automaticamente.
2.2.3. Para utilizar a balança rodoviária, não pode ter outra aplicação usando a porta COM, sendo necessário fechar as aplicações que estiverem utilizando a mesma (teste de portas). Caso o problema persista, siga os passos 2.2.3.1 e 2.2.3.2.
2.2.3.1 Vá ao gerenciador de dispositivos, selecione a porta COM e restaure as predefinições.
2.2.3.2 Abra o CMD, execute o comando netstat -aon \| findstr COM(X), e verifique as aplicações que estão sendo utilizadas pela porta. Para finalizar uma aplicação usa-se o comando TASKKILL /PID 'numero' /F.
2.2.4. Caso alguma das aplicações da automação esteja com problema de Crash ao captar o peso da balança, é necessário instalar outra versão do Java. Na data 20/08/2021 o Java Update 241 funcionou sem dar crash.
3\. Após a balança estar comunicando com a automação corretamente, solicitar para testar no Oracle. Caso o peso não é enviado ao Oracle, solicitar ao Conti para verificar o protocolo da balança.

**<u>Últimas atualizações</u>**  

| Editor            | Data       | Motivo                  | Alteração |
|-------------------|------------|-------------------------|-----------|
| André Luiz Fronza | 01/03/2024 | Criação da documentação |          |
|                  |           |                        |           |
|                   |            |                         |           |
|                   |            |                         |           |
|                   |            |                         |           |

