Não bloquear sessão ociosa
Friday, March 1, 2024
9:20 AM

**<u>Arquitetura</u>**

n/a

**<u>Contas de Serviço</u>**

Usuário administrador local

**<u>Configurações do Ambiente</u>**

1.  Ir nas configurações (Win + I) -\> sistema -\> Energia e suspensão -\> Alterar ambos para “Nunca”;
2.  Clicar em configurações avançadas de energia, no canto superior direito da tela;
    1.  Outro método, é abrir as configurações de energia do painel de controle (powercfg.cpl);
    2.  Ir em Alterar configurações de plano, no plano selecionado;
    3.  Alterar ambos para “Nunca”;
1.  Abrir o Regedit como Administrador e ir para HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\238C9FA8-0AAD-41ED-83F4- 97BE242C8F20\7bc4a2f9-d8fc-4469-b07b-33eb785aaca0;
    1.  Clique em “Attributes” e coloque o valor como 2;
1.  Volte para o passo 2b, clique em “Alterar configurações de energia avançadas”, vá em Suspender e aparecerá uma nova opção "Tempo limite de suspensão sem supervisão do sistema” e mude o valor para 0;
2.  Na GPO “Bloquear sessão ociosa”, adicionar o usuário como exceção para não a aplicar.

**<u>Configurações Gerais</u>**

**<u>Últimas atualizações</u>**  

| Editor            | Data       | Motivo                  | Alteração |
|-------------------|------------|-------------------------|-----------|
| André Luiz Fronza | 01/03/2024 | Criação da documentação |          |
|                  |           |                        |           |
|                   |            |                         |           |
|                   |            |                         |           |
|                   |            |                         |           |

