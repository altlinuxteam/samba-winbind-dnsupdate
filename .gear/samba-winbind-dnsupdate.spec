%define script_name winbind-dnsupdate

Name: samba-winbind-dnsupdate
Version: 0.1
Release: alt1

Summary: Dynamic dns update for winbind backend
License: GPLv3
URL: https://github.com/Arzdez/samba-winbind-dnsupdate.git
VCS: https://github.com/Arzdez/samba-winbind-dnsupdate.git

BuildArch: noarch
Group: System/Configuration/Networking
Source:   %name-%version.tar

BuildRequires(pre): rpm-macros-alterator
BuildRequires: shellcheck

Requires: samba-winbind

%description
A program that implements dynamic update of addresses
on a DNS server when used as a winbind backend

%prep
%setup

%build
# Change version
sed -i 's/^VERSION=.*/VERSION=%version/' %script_name

%install

install -Dm 755 %script_name %buildroot/%_bindir/%script_name
install -Dm 644 %script_name-completions \
     %buildroot%_datadir/bash-completion/completions/%script_name
install -Dm 644 %script_name.timer %buildroot%_unitdir/%script_name.timer
install -Dm 644 %script_name.service %buildroot%_unitdir/%script_name.service

%check
shellcheck %script_name

%files
%_bindir/%script_name
%_unitdir/%script_name.timer
%_unitdir/%script_name.service
%_datadir/bash-completion/completions/%script_name

%changelog
* Mon Jul 29 2024 Evgenii Sozonov  <arzdez@altlinux.org> 0.1-alt1
- Initial release.
