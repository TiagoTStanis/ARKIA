AM

Documentação do servidor WINK.

## Especificações de hardware:

**hostname:** WINK
**CPU**: 2 vCPUs
**Memory:** 4GB.
**Disks:** 1 disco
- WINK_SO.vhdx = aprox 22gb.
**OS:** Oracle Linux Server release 6.5
**Kernel**: 2.6.32-431.17.1.el6.x86_64

## Aplicações:
O Server hospeda atualmente duas aplicações legado, O RH-QUESTIONARIO e o FRICLIENTE.

## Especificações de rede:
Rede: VLAN-Servers-DMZ
IP: 172.31.119.8
Vlan: 119
Vdom: Backend
OBS: Rede DMZ isolada, propria para acesso externo.

## Identidade:
O server, por se encontrar numa versão muito antiga do Oracle linux, não pode ser integrado ao AD. Desta forma, ao cesso ao mesmo é feito com o usuário root (analistas) e usuário local, nomeado, para os demais.

#  RH questionário

## Descrição:

Utilizado pelo RH para alguma coisa.

## Serviços utilizados (dependências):
- Apache 2.2.15 / built: Apr 3 2014 15:09:15 - /usr/sbin/httpd
- PHP (PHP 5.3.3 / built: Jan 10 2017 22:26:04 - /usr/bin/php

## Acesso:
- URL: [http://rhquestionario.frimesa.com.br/rh-questionario/#](http://rhquestionario.frimesa.com.br/rh-questionario/)
- Acessado apenas internamente.

## Localização:
- /var/www/html/rh-questionario

## Desenvolvedores envolvidos(Possuem usuario no server):
- Artur Jefferson Farias da Silva (arsilva)
- Fabiano da rosa (fabiano)

# FRICLIENTE

## Descrição:
- ?

## Serviços utilizados:
- Tomcat 7.0.53 / built Mar 25 2014 06:20:16 - /dados/apache-tomcat-7.0.53
- JRE 1.7.0_55 - /dados/jdk/

## Acesso:
- <https://fricliente.frimesa.com.br/FR_CADCLI/login.xhtml>
- Acessado externamente e internamente.

## Localização:
- /dados/apache-tomcat-7.0.53/webapps/FR_CADCLI

## ACESSO EXTERNO:
O acesso externo é fornecido a partir de um VIP, que aponta para o FortiADC. O FortiADC faz o encaminhamento do acesso ao server, intermediando tal ação.

VIP:
Nome: VIP-COPEL-ADC
Virtual Server: VS_FRICLIENTE
IP VS: 172.31.221.30
Redirect port: 8345

# REVISÕES:
| EDITOR        | DATA       | MOTIVO                  | ALTERAÇÃO | VERSÃO |
|---------------|------------|-------------------------|-----------|--------|
| Matheus Baldo | 01/11/2023 | Criação da documentação |          | 1      |
|              |           |                        |          |       |
