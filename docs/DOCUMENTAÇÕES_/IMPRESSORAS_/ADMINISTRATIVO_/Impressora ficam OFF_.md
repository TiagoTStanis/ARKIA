Após um tempo o dispositivo fica inativo por alguns minutos e chega no período de log-off do switch e força o cliente fora da tabela de usuários e a porta é bloqueado pelo AAA. O log-off é forçado sobre todos os clientes conectados e tem um valor padrão de 300 segundos. Assim, é necessário configurar a porta para que, trave o cliente a sua tabela MAC sem forçar o log-off.

aaa port-access mac-based \< PORT-LIST\> mac-pin

Outro problema existente é quando o dispositivo fica ocioso por muito tempo e entra em hibernação para economia de energia, mudando o status da porta do Switch, causando a perca do cliente na tabela de cliente ativos e perdendo a comunicação com o dispositivo. Assim, é realizado uma configuração baseado na direção do trafego, em que todo trafego é permitido apenas trafego de entrada a porta (que é enviado ao dispositivo) seja permitido para clientes não autenticados, para que assim, quando houver uma resposta, seja acionado novamente a autenticação MAC.

aaa port-access \<port-list\> controlled-direction in

| Editor      | Data       | Motivo                  | Alteração |
|-------------|------------|-------------------------|-----------|
| Iago Vargas | 01/03/2024 | Criação da documentação |          |
