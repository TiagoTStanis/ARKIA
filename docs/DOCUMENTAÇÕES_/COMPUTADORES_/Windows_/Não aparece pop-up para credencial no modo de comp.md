Não aparece pop-up para credencial no modo de compatibilidade do IE no Edge  
Friday, March 1, 2024  
9:30 AM  
**<u>Arquitetura</u>**

n/a

**<u>Contas de Serviço</u>**

Usuário administrador local

**<u>Configurações do Ambiente</u>**

n/a

**<u>Configurações Gerais</u>**

Problema ocorre em alguns sites que funcionam apenas no navegador Internet Explorer, porém tal foi descontinuado pela Microsoft no Windows 11, e se há necessidade de uso, é necessário usar o modo de compatibilidade do edge.

Nesse problema, em especifico, ao acessar o site deveria aparecer um pop-up solicitando as credenciais de acesso, porém não aparece, o site fica carregando e eventualmente da falha na solicitação das credenciais.

Para corrigir o problema, é necessário primeiramente adicionar o site como site confiável nas “Opções de Internet”, através da GPO “Frimesa – Zonas de Sites”.

Após aplicado, é necessário alterar o regedit da máquina, em especifico, adicionar uma nova entrada, nomeada Flags, DWORD, com o valor 143 no caminho HKU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Zones\\1\\

Essa entrada, na teoria, desmarca a opção “Exigir verificação do servidor (https:) para todos os sites desta zona” em sites confiáveis.

Caminho completo, para marcar e desmarcar a opção, respectivamente:

- HKU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Zones\\1\\Flags: 0x00000143(323)
- HKU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\Zones\\1\\Flags: 0x00000147(327)

Cada uma das zonas no regedit é representada como:

- Zona 1 – Intranet Sites
- Zona 2 – Sites confiáveis
- Zona 3 – Internet Sites
- Zona 4 – Sites restritos  
    Após realizar ambas as configurações, basta reiniciar a máquina e testar

**<u>Últimas atualizações</u>**

| Editor | Data | Motivo | Alteração |
| --- | --- | --- | --- |
| André Luiz Fronza | 01/03/2024 | Criação da documentação |     |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |