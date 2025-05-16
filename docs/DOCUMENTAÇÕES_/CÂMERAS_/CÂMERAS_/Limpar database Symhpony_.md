**<u>Arquitetura</u>**

n/a

**<u>Contas de Serviço</u>**

Usuário: sa  
Senha: keepass

**<u>Configurações do Ambiente</u>**

n/a

**<u>Configurações Gerais</u>**

Faça logon no MSMSS (senha no keepass)

Fazer backup:

Aira - Tasks - Backup - Add: "F:\\DB\\AIRA-DB-03-06-24.bak" - ok

Parar serviços AI

1º  
clique direito na base e vai em tasks -> shrink -> Database -> ok  
2º  
Tasks -> shrink -> files -> ok  
cmd as admin  
dbupdater "select 'dbupdater \\drop table ' + EventLogDataTable + '; drop table ' + EventLogTable + '\\' from EventLogArchive"  
dps  
dbupdater "ALTER TABLE EventLogData DROP CONSTRAINT FK_EventLogData_EventLog;TRUNCATE TABLE EventLogData;TRUNCATE TABLE EventLog;ALTER TABLE EventLogData WITH CHECK ADD CONSTRAINT FK_EventLogData_EventLog FOREIGN KEY (EventID) REFERENCES EventLog (ID);"  
\- Conferir tamanho do arquivo aira C:\\Program Files\\Microsoft SQL Server\\MSSQL15.SENSTAR\\MSSQL\\DATA

\- shrink database e files de novo  
\- Rodar o setupwizard (executar)

**<u>Últimas atualizações</u>**

| Editor | Data | Motivo | Alteração |
| --- | --- | --- | --- |
| Thiago Leite | 26/03/2024 | Criação da documentação |     |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |