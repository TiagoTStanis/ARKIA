Padrão de criação - DISK SPACE
Tuesday, October 31, 2023
5:29 PM

## PADRÕES E REQUISITOS A SEREM SEGUIDOS DURANTE A CRIAÇÃO DE UM NOVO SERVIDOR LINUX:

### System reqs:
Distribuir 40GB entre as partições padrão (Space = folder):

20GB = /
10GB = /home
8GB = /swap
500mb = /boot

### Application reqs:
Para a aplicação ou serviço que a máquina rodará, criação a partir de 30GB para a partição.
Ex:
30GB = /myapp

**OBS:** Criar um grupo para as partições: /home, /swap e /boot. Criar outro separado para a partição da aplicação (ex: /myapp).

