
Tuesday, October 31, 2023
5:22 PM

Relação de IP’s dos equipamentos atuais:
Mediatrix: 172.26.128.1
telefones físicos em geral: 172.26.128.X

**IP Voice Manager Cloud**
Seguindo as tabelas da documentação, essa primeira tabela parece ter referência aos telefones físicos. No caso, o Mediatrix também sai por essa regra, uma vez que ele está nesta mesma rede. Para cumprir a primeira sequência, foi criada a regra descrita abaixo:

![image1](../../../_resources/image1-35.png)

Regra criada permitindo tráfego de saída com as seguintes configurações:
O**rigem:** 172.26.128.0/24 (REDE DE TELEFONIA)
**Destino:** [a.ntp.br](http://a.ntp.br) / 35.199.86.162
**Serviços liberados:**
**NTP** UDP/123
**RTP** UDP/10000~65535
**SIP** TCP/5060~5064, UDP/5060~6064

**UC Voice Manager Cloud**
Para a segunda tabela, onde parece ser referência ao softphone, software instalado nos computadores, foi feito a seguinte regra:
![image2](../../../_resources/image2-17.png)

Regra criada permitindo tráfego de saída com as seguintes configurações:
**Origem:** Zona-LAN-Computadores (engloba todas as redes de computadores atuais)
**Destino:** [xsp.gc.italk.net.br](http://xsp.gc.italk.net.br) / [ums1.gc.italk.net.br](http://ums1.gc.italk.net.br) / [webrtc1.gc.italk.net.br](http://webrtc1.gc.italk.net.br)
**Serviços liberados:**
ANY TCP/ANY, UDP/ANY

**Gateway**
Tabela de requisitos para o Mediatrix, de acordo com a documentação.
![image3](../../../_resources/image3-9.png)

Para essa necessidade, foi realizada a criação de um VIP, uma vez que a origem do tráfego é externa.
configuração do VIP:
**IP externo**: 200.101.131.99
**IP Interno:** 172.26.128.1
**Interface:** Interface referente ao IP 200.101.131.99
**Serviços liberados:**
TCP/ANY, UDP/ANY
Para filtrar o tráfego, criado a regra permitindo tráfego de ENTRADA, com as seguintes configurações:
**Origem:** 35.199.86.162
**Destino:** 172.26.128.1
**Serviços liberados:**
RTP TCP/10000~20000, UDP/10000~20000
SIP TCP/5060, UDP/5060

Resumidamente, os telefones e o mediatrix saem pela primeira regra descrita acima.
Os computadores com softphone saem pela segunda regra.
O mediatrix recebe tráfego de origem externa através da terceira regra.

# REVISÕES:
| EDITOR        | DATA       | MOTIVO                  | ALTERAÇÃO | VERSÃO |
|---------------|------------|-------------------------|-----------|--------|
| Matheus Baldo | 04/01/2023 | Criação da documentação |          | 1      |
|              |           |                        |          |       |

