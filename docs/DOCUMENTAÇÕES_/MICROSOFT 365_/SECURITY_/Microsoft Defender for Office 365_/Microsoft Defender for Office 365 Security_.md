**O que é?**

Toda assinatura Microsoft 365 vem com features de segurança. As variações estão nas proteções que cada licença acompanha. O Defender for Office 365 Security é dividido em 3 serviços principais de segurança, ligados ao tipo de licença, que são:

1 - Exchange Online Protection (EOP).

2 - Microsoft Defender for Office 365 365 Plan 1 (Defender for Office 365 P1).

3 - Microsoft Defender for Office 365 365 Plan 2 (Defender for Office 365 P2).

A segurança do M365 tem como base as principais proteções oferecidas pelo serviço 1, o EOP. O EOP está presente em todas as assinaturas de Exchange Online. podemos resumir os 3 serviços da seguinte forma:

**EOP →** Prevenção contra ataques conhecidos amplamente e baseados em volume.

**365 P1 →** Protege os e-mails e colaboração de malwares zero-day, pishing e BEC attack (business email compromise).

**365 P2 →** Investigação, caça e resposta pós-violação, automação e simulação (treinamentos).
Ex:
![image1](../../../../_resources/image1.jpeg)
*OBS: Apesar da ênfase nas fases, todas as proteções cumprem com todos os objetivos descritos.*

Estes níveis podem ser vistos como camadas de segurança, e possuem uma estrutura cumulativa. o EOP é o core da segurança office 365, o P1 possui o EOP, e o P2 possui o EOP e P1.

**O que temos?**

Atualmente a Frimesa conta com a licença Microsoft Entra ID P2, que engloba todos os níveis de segurança disponíveis no contexto.
Pode consultar o que cada serviço oferece, em:

[Office 365 Security including Microsoft Defender for Office 365 and Exchange Online Protection](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/mdo-security-comparison?view=o365-worldwide#the-microsoft-365-security-ladder-from-eop-to-defender-for-office-365)

**A Proteção**
Conforme dito anteriormente, toda organização Microsoft 365 possui uma proteção padrão, a partir do momento em que é criada, porém, é possível aprimorar as configurações para uma melhor proteção. Abaixo, algumas melhorias são a autenticação de e-mail e políticas de proteção.

**Autenticação de e-mail**
A autenticação de e-mail consiste na configuração de 3 componentes, **SPF**, **DKIM** e **DMARC**.

**1 - SPF (Sender policy Framework)**
O SPF valida os e-mails enviados do nosso domínio para saber se estão vindo de quem diz ser, prevenindo o spoofing. Sua configuração consiste em criar um registro DNS TXT personalizado, e adicionar o mesmo ao nosso DNS externo.

**1 -** criado o registro DNS SPF TXT:

==v=spf1 ip4:177.220.165.77 include:spf.protection.outlook.com include:rp.oracleemaildelivery.com -all==

**2 -** Adicionado o mesmo ao DNS externo e validado a string. A mesma está ok, conforme imagem abaixo:

![image2](../../../../_resources/image2-15.png)

**DKIM (DomainKeys Identified Mail)**
O DKIM trabalha melhor em conjunto com o SPF, prevenindo falsos positivos e aumentando a segurança da autenticação. Ele adiciona uma assinatura criptografada no cabeçalho do e-mail quando enviado, e o servidor de destino pode validar essa assinatura quando recebe a mensagem, auxiliando no anti-spoofing do nosso domínio. Também é uma camada a mais de segurança, prevenindo os falsos positivos spams em caso de falha do SPF. Sua configuração consiste em publicar o registro DNS com a configuração gerada pela Microsoft.

**1 -** Primeiro, publicado os registros DNS CNAME no DNS externo.

**2 -** Após, habilitado o DKIM no Defender, para o domínio [Frimesa.com.br](http://Frimesa.com.br).

![image3](../../../../_resources/image3-8.png)

Rodado teste Microsoft para validar o funcionamento das chaves DKIM, e a princípio, tudo ok, conforme resultado:

![image4](../../../../_resources/image4-7.png)

**DMARC (domain-based Message Authentication, Reporting, and Conformance)**
O DMARC trabalha em conjunto com o SPF e DKIM, e serve para garantir que o sistema de e-mail destinatário confie nas mensagens enviadas a partir do nosso domínio. Ele também dita o que os sistemas destinatários farão com os e-mails que são enviados do nosso domínio (ou que estão tentando se passar por ele).
O cabeçalho de um e-mail contém campos que não são visíveis para os usuários, Um exemplo é o campo “Mail From” e o “From”. O Campo “From” de um cabeçalho, refere-se ao endereço de e-mail que o usuário irá visualizar quando recebe uma mensagem, no seu aplicativo de e-mail. Já o campo “Mail From” é para identificar o o remetente e define para onde enviar erros com o envio da mensagem, etc. O SPF utilizado sozinho faz a checagem do campo “Mail From”, porém, o criminoso pode adulterar o campo “From” e acabar se passando por outra pessoa/empresa/domínio, enganando o destinatário facilmente.

Exemplo:
- Mail from address (5321.MailFrom): <phishing@contoso.com>
- From address (5322.From): <frimesa@frimesa.com.br>
O Remetente irá receber um e-mail com o remetente sendo mostrado como “frimesa@frimesa.com.br”;
Quando utiliza-se o DMARC, basicamente o servidor de destino também irá checar o campo “5322.From”, com o intuito de validar se é verdadeiro, ou não, e seguir as orientações de descarte informadas na string configurada.

**1 - DMARC para entrada de e-mails**
Não precisamos configurar nada para a entrada de e-mails. Esta questão fica com a Microsoft, totalmente gerenciada por eles.

**2 - DMARC para saída de e-mails**
Para e-mails enviados por nós, é necessário configurar o DMARC. A configuração consiste em montar um registro DNS TXT e publica-lo no DNS externo. Na montagem do registro, é necessário definir alguns pontos importantes, como a política que será aplicada para os e-mails enviados com o domínio Frimesa e a configuração de relatórios.

**2.1 - A política aplicada**
No registro DNS, devemos informar o que o servidor DESTINO, que recebe nosso e-mail, fará com uma mensagem que não passe nas validações de autenticação. É possível escolher entre:

**p=none →** O Servidor destino não tomará nenhuma ação.
**p=quarentine →** A mensagem será posta em quarentena.(Em muitos casos, movida para o SPAM).
**p=reject →** O servidor irá rejeitar a mensagem.
Quando um DMARC está setado para reject, é muito difícil um agente malicioso conseguir êxito no spoofing do nosso domínio. Em contra partida, é necessário um bom planejamento para configurar a política como Reject, buscando evitar a perda de e-mails.

**2.2 - Relatórios**
Também é possível inserir um e-mail no registro DNS, para que sistemas de mensagem nos enviem relatórios analíticos com informações sobre a atuação do DMARC, o que nos da uma boa base de como a tecnologia impacta a comunicação da empresa. Os arquivos geralmente são no formato XML e difíceis de ler, sendo necessário alguma ferramenta externa para ler o arquivo com maior facilidade, possibilitando a interpretação dos dados. As informações variam de acordo com o serviço que forneceu o relatório, podendo conter as falhas de autenticação, sucesso, informações de rede, etc.

**configuração**
Feito a publicação do registro DNS TXT DMARC no DNS externo. A string foi feita com a política NONE, e, adicionado o e-mail “ti-infra@frimesa.com.br” para receber os reports.

**Funcionamento**
Realizado o enivo de um e-mail e validado no cabeçalho da mensagem os testes de autenticação:
Os reports estão sendo recebidos normalmente no e-mail:

**Protection policies**
As preset security policies permitem aplicar configurações de proteção, baseado nas recomendações da Microsoft. Basicamente, são configurações prontas que a Microsoft disponibiliza, com o intuito de trazer uma segurança balanceada no controle de conteúdo prejudicial e a evitar interrupções de serviços.

Existem algumas preset policies disponíveis, que são:
- **Standard →** Perfil básico padrão, indicado para a maioria dos usuários.
- **Strict →** Política mais agressiva, indicada para usuários alvos e prioritários.
- **Built-in protection →** Políticas padrões para safe links e safe attachments, apenas.

Por padrão, todos os usuários já possuem a proteção Built-in Protection” habilitada para os seus usuários. A Standard e Strict devem ser habilitadas conforme necessidade.
Preset security utiliza de versões especiais de políticas de proteções individuais, que estão disponíveis no EOP e no MDO365. Essas políticas são criadas automaticamente após a atribuição das preset policies aos usuários.

As proteções podem ser resumidas em:
- EOP Policies
  - Anti-spam
  - anti-malware
  - anti-phishing (spoofing)
- MDO365
  - Anti-phishing (spoofing)
    - Impersonation settings
    - Advanced Phishing thresholds
  - Safe link policies
  - Safe attachments policies

Todas essas políticas possuem diversos níveis de configuração, quando criadas manualmente. As preset policies criam as mesmas com um padrão recomendado pela Microsoft, muitas vezes com uma proteção melhor do que as criadas manualmente, pois podemos esquecer alguma config, ou, não atualizar as mesmas, e até mesmo, realizar configurações conflitantes ou que não são efetivas.
A aplicação das preset policies é prioritária, o que faz com que políticas criadas manualmente, de outras proteções já ativadas, etc, sejam sobrescritas com as preset policies. Resumidamente, todas as políticas criadas anteriormente praticamente não são aplicadas aos usuários que recebem preset policies, pois a sua priorização é superior. Aos usuários que são postos como exceção, deve-se consultar a lista de aplicação das regras para validar o que o mesmo receberá.
Mais informações sobre, em:

[Preset security policies](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/preset-security-policies?view=o365-worldwide)

**Configuração**
A Frimesa iniciou a utilização da política **Standard preset policy.**

1 - Foi habilitado a Standard Preset Policy.
2 - Atribuído a proteção EOP para todos os recipientes (todas as contas).
3 - Atribuído a proteção MDO365 para todos os recipientes (todas as contas).
4 - Atribuído alguns usuários que pensamos ser de risco na config de Impersonation protection (Users).
5 - Atribuído o domínio [Frimesa.com.br](http://Frimesa.com.br) na configuração de impersonation protection(Domains).
6 - Não atribuído nenhuma configuração relacionada a domínios e remetentes confiáveis.

Os endereços de usuários atribuídos na proteção, estão listados na imagem abaixo (possível atribuir até 350 usuários, atualmente):
![image5](../../../../_resources/image5-3.png)

**Validação**
Para validar a efetividade das configurações realizadas, podemos visualizar uma das políticas criadas pela Preset security policy, nas configurações de Anti-phishing. Notamos na imagem que a política foi criada com um nome padrão, está “On” e não possui prioridade definida, uma vez que ela tem a prioridade maior que qualquer outra:
![image6](../../../../_resources/image6-2.png)

**Conclusão**
Neste documento, foi apresentado o Microsoft Defender for Office 365 Security, que consiste em uma série de serviços de segurança integrados ao Microsoft 365. Os três principais serviços são o Exchange Online Protection (EOP), o Microsoft Defender for Office 365 365 Plan 1 (Defender for Office 365 P1) e o Microsoft Defender for Office 365 365 Plan 2 (Defender for Office 365 P2). O EOP fornece proteção contra ataques conhecidos em grande escala, enquanto o P1 protege contra malwares zero-day, phishing e ataques de comprometimento de e-mail empresarial. O P2 oferece recursos avançados, como investigação, caça e resposta pós-violação, automação e simulação. A Frimesa possui a licença Microsoft Entra ID P2, que abrange todos os níveis de segurança disponíveis.
Além disso, foram abordadas melhorias na proteção, como a configuração de autenticação de e-mail, incluindo SPF, DKIM e DMARC. O SPF valida os e-mails enviados do domínio para prevenir o spoofing, enquanto o DKIM adiciona uma assinatura criptografada no cabeçalho do e-mail para aumentar a segurança da autenticação. O DMARC trabalha em conjunto com o SPF e DKIM para garantir que os sistemas de e-mail confiem nas mensagens enviadas pelo domínio e dita as ações a serem tomadas em caso de falha na autenticação.
Também foi mencionado o uso de políticas de proteção pré-definidas, que permitem aplicar configurações de segurança recomendadas pela Microsoft. As preset security policies oferecem proteção contra spam, malware, phishing e oferecem recursos como Safe Links e Safe Attachments. Essas políticas têm prioridade sobre outras configurações e se aplicam a todos os usuários, garantindo uma segurança equilibrada e evitando interrupções nos serviços.
Em conclusão, a Frimesa adotou medidas abrangentes para garantir a segurança do Microsoft Defender for Office 365 Security. A configuração de autenticação de e-mail, incluindo SPF, DKIM e DMARC, fortalece a proteção contra spoofing e aumenta a confiança nas mensagens enviadas pelo domínio. Além disso, a implementação das políticas de proteção pré-definidas oferece uma camada adicional de segurança, protegendo contra spam, malware e phishing.
# REVISÕES:
| EDITOR        | DATA       | MOTIVO                  | ALTERAÇÃO | VERSÃO |
|---------------|------------|-------------------------|-----------|--------|
| Matheus Baldo | 17/11/2023 | Criação da documentação |          | 1      |
|              |           |                        |          |       |
