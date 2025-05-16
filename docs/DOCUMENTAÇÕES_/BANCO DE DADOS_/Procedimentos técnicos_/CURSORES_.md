CURSORES
Wednesday, November 1, 2023
8:26 AM

Verificar cursores abertos:

select user_process username, "Recursive Calls", "Opened Cursors", "Current Cursors" from ( select nvl(ss.USERNAME,'ORACLE PROC')\|\|'('\|\|se.sid\|\|') ' user_process, sum(decode(NAME,'recursive calls',value)) "Recursive Calls", sum(decode(NAME,'opened cursors cumulative',value)) "Opened Cursors", sum(decode(NAME,'opened cursors current',value)) "Current Cursors" from v\$session ss, v\$sesstat se, v\$statname sn where se.STATISTIC# = sn.STATISTIC# and (NAME like '%opened cursors current%' or NAME like '%recursive calls%' or NAME like '%opened cursors cumulative%') and se.SID = ss.SID and ss.USERNAME is not null group by nvl(ss.USERNAME,'ORACLE PROC')\|\|'('\|\|se.SID\|\|') ' ) orasnap_user_cursors order by USER_PROCESS,"Recursive Calls" ;

Verificar quantidade de cursores:

select name,value from v\$parameter where name = 'open_cursors';

Alterar quantidade de cursores no banco.

alter system set open_cursors= 50000 scope=both;

**OBS:** Parâmetro Scope=both faz com que a alteração seja aplicada imediatamente e seja permanentemente salva, até mesmo dps de um bounce.
Para verificar o número máximo de cursores, pode-se executar o comando:

select v.value as numopencursors, s.machine, s.osuser, s.username from V\$SESSTAT v, V\$SESSION s where v.statistic# = 3 and v.sid = s.sid

