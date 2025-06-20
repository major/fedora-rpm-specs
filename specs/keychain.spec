Name:       keychain
Summary:    Agent manager for OpenSSH, ssh.com, Sun SSH, and GnuPG
Version:    2.9.2
Release:    %autorelease
License:    GPL-2.0-only
URL:        https://www.funtoo.org/Keychain
Source0:    https://github.com/funtoo/keychain/archive/%{version}/keychain-%{version}.tar.gz
Source1:    keychain.sh
Source2:    keychain.csh
Source3:    README.Fedora
BuildArch:  noarch
BuildRequires: make
BuildRequires: perl-podlators
Requires:   findutils


%description
Keychain is a manager for OpenSSH, ssh.com, Sun SSH and GnuPG agents.
It acts as a front-end to the agents, allowing you to easily have one
long-running agent process per system, rather than per login session.
This dramatically reduces the number of times you need to enter your
passphrase from once per new login session to once every time your
local machine is rebooted.

%prep
%setup -q
sed -i -e 's|/usr/ucb:||' keychain.sh

%build
make keychain keychain.1

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 755 keychain %{buildroot}%{_bindir}/keychain
install -pm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d/keychain.sh
install -pm 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/profile.d/keychain.csh
install -pm 644 keychain.1 %{buildroot}%{_mandir}/man1
install -pm 644 %{SOURCE3} README.Fedora

%files
%doc ChangeLog.md README.md README.Fedora
%license COPYING.txt
%config(noreplace) %{_sysconfdir}/profile.d/keychain.sh
%config(noreplace) %{_sysconfdir}/profile.d/keychain.csh
%{_bindir}/keychain
%{_mandir}/man1/keychain.1*

%changelog
%autochangelog
