cd /var/log - Logs do sistema linux

tail -f auth.log - logs de autenticação em tempo real

cat auth.log | grep "Failed" - Busca logs apenas falhas no host.

cat syslog | grep "attackalert" - Ver logs do "honeypot" em tempo real
tail syslog | grep "attackalert" - Para ver logs do "honeypot" em tempo real

