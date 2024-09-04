- [1.Описание](###Описание)
- [2.Установка](###Установка)
- [3.Использование](###Использование)

## winbind-dnsupdate
### Описание
**winbind-dnsupdate** - программа, реализующая динамическое обновление адресов
на DNS-сервере при использовании *winbind* в качестве клиента домена.

**Основным функционалом** является обновление IPv4 (A), IPv6 (AAAA) и соответствующих PTR DNS-записей. Для обновления DNS-записей winbind-dnsupdate использует файл /etc/resolv.conf. В пакете вместе со скриптом предоставляются юниты systemd timer и  systemd service. Таймер запускает сервисный юнит для обновления DNS-записи через 5 минут после загрузки системы и затем каждый час. Для изменения частоты запуска нужно редактировать таймер.

### Установка
Перед началом установки убедитесь, что ваша машина введена в домен и на вашей системе установлены следующие компоненты:

+ samba-winbind

**Для машин под управлением ОС «Альт» предусмотрена установка пакетом:**

	# apt-get install samba-winbind-dnsupdate
После установки необходимо активировать и запустить таймер и сервис:

	  # systemctl enable winbind-dnsupdate.timer

	  # systemctl start winbind-dnsupdate.timer

**В остальных случаях:**

Сначала скачайте исходный код приложения. Если у вас есть исходный архив, распакуйте его с помощью команды:

	$ unzip samba-winbind-dnsupdate-master.zip
	$ cd samba-winbind-dnsupdate-master

Скопируйте скрипты и файлы конфигурации в соответствующие директории:

* Установка исполняемого файла

      # install -Dm 755 winbind-dnsupdate /usr/bin/winbind-dnsupdate

* Установка автодополнения для bash

      # install -Dm 644 winbind-dnsupdate.bash-completion /usr/share/bash-completion/completions/winbind-dnsupdate

* Установка unit-файлов systemd

      # install -Dm 644 winbind-dnsupdate.timer /usr/lib/systemd/system/winbind-dnsupdate.timer
      # install -Dm 644 winbind-dnsupdate.service /usr/lib/systemd/system/winbind-dnsupdate.service

* Установка конфигурационного файла

      # install -Dm 644 winbind-dnsupdate.sysconfig /etc/sysconfig/winbind-dnsupdate
* После установки необходимо активировать и запустить таймер и сервис:

	  # systemctl enable winbind-dnsupdate.timer

	  # systemctl start winbind-dnsupdate.timer

Это позволит автоматически проверять и обновлять DNS-записи  в соответствии с расписанием.

* Перезагрузка и перечитывание всех конфигов юнитов:

      # systemctl daemon-reload

### Использование
**Основные параметры**

       -h, --help
              Показать справку.

       -v, --version
              Вывести версию.

       -a, --all
              Включить обновление всех записей.

       -6, --update-ipv6
              Включить обновление IPv6 (AAAA) записей.

       -d, --daemon
              Отправить логи в journald.

       -t, --ttl <time>
              Задать TTL ("время жизни", указывает, как долго ваши настройки DNS должны храниться в кэше, прежде чем они будут автоматически обновлены.)

       --allow-ipv4-ptr-update
              Включить обновление обратной DNS-записи IPv4 (A) PTR.

       --allow-ipv6-ptr-update
              Включить обновление обратной DNS-записи IPv6 (AAAA) PTR.

       --disable-dconf
              Отключить считывание конфигурационных данных из Dсonf.


Пример вывода:

	[INFO]: Hostname: clw4-sis.domain.alt
	[INFO]: Check winbind status.
	[INFO]: Winbind is running. Continue.
	[INFO]: Checking the availability of DNS servers
	[INFO]: DNS servers available
	[INFO]: Get host credentials
	[INFO]: Retrieving host credentials successfully
	[INFO]: ----------------------------------------------------------
	[INFO]: Update IPv4
	[INFO]: Trying to get the name and IPv4 address of a domain controller
	[INFO]: Successful. DC info:
	[INFO]: Domain controller name: dc1.domain.alt
	[INFO]: Domain controller IPv4: 10.64.177.101
	[INFO]: Trying parse connection interface name
	[INFO]: Successful. Intraface name: eth0
	[INFO]: Checking the existence of A record
	[INFO]: IPv4 record exists.
	[INFO]: Checking whether the IPv4 records needs to be updated
	[INFO]: Current IPv4 address: 10.64.177.145
	[INFO]: IPv4 address in DNS server: 10.64.177.130
	[INFO]: The IPv4 address of interface eth0 has not been changed.
	[INFO]: The update was skipped
	[INFO]: IPv4 update was successful
	[INFO]: The update was successful.
	[INFO]: Destroy host credential.