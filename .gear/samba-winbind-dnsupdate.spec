Name: samba-winbind-dnsupdate
Version: 0.1
Release: alt1

Summary: Dynamic dns update for winbind backend
License: GPLv3
URL: https://github.com/Arzdez/samba-winbind-dnsupdate.git

BuildArch: noarch
Group: System/Configuration/Networking
Source:   %name-%version.tar

Requires: samba-winbind
Requires: samba-winbind-clients
Requires: samba-common-tools
Requires: krb5-kinit
Requires: net-tools
Requires: bind-utils


%description
A program that implements dynamic update of addresses
on a DNS server when used as a winbind backend

%prep
%setup

%install

install -Dm 755 winbind-dnsupdate %buildroot/%_bindir/winbind-dnsupdate
install -Dm 644 winbind-dnsupdate-completions \
     %buildroot%_sysconfdir/bash_completion.d/winbind-dnsupdate-completions

install -Dm 644 winbind-dnsupdate.timer %buildroot%_unitdir/winbind-dnsupdate/winbind-dnsupdate.timer
install -Dm 644 winbind-dnsupdate.service %buildroot%_unitdir/winbind-dnsupdate/winbind-dnsupdate.service


%files
%_bindir/winbind-dnsupdate
%_unitdir/winbind-dnsupdate/winbind-dnsupdate.timer
%_unitdir/winbind-dnsupdate/winbind-dnsupdate.service
%_sysconfdir/bash_completion.d/winbind-dnsupdate-completions


%changelog
* Mon Jul 29 2024 Evgenii Sozonov  <arzdez@altlinux.org> 0.1-alt1
- Initial release