Name:           keychain
Summary:        Agent manager for OpenSSH, ssh.com, Sun SSH, and GnuPG
Version:        2.9.8
Release:        %autorelease
License:        GPL-2.0-only
URL:            https://github.com/danielrobbins/keychain
Source0:        https://github.com/danielrobbins/keychain/archive/%{version}/keychain-%{version}.tar.gz
Source1:        keychain.sh
Source2:        keychain.csh
Source3:        README.Fedora
BuildArch:      noarch
BuildRequires:  bash-completion
BuildRequires:  make
BuildRequires:  perl-podlators
Requires:       findutils


%description
Keychain is a manager for OpenSSH, ssh.com, Sun SSH and GnuPG agents.
It acts as a front-end to the agents, allowing you to easily have one
long-running agent process per system, rather than per login session.
This dramatically reduces the number of times you need to enter your
passphrase from once per new login session to once every time your
local machine is rebooted.

%prep
%autosetup
cp %{SOURCE3} .
# Remove /usr/ucb from PATH as it's not used in Fedora
sed -i -e 's|/usr/ucb:||' keychain.sh
# Remove shebang from bash completion script
sed -i -e '1{\@^#!/usr/bin/env bash@d}' completions/keychain.bash

%build
%make_build keychain keychain.1

%install
install -D -p -m 0755 keychain %{buildroot}%{_bindir}/keychain
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d/keychain.sh
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/profile.d/keychain.csh
install -D -p -m 0644 keychain.1 %{buildroot}%{_mandir}/man1/keychain.1

# Bash completion
install -D -p -m 0644 completions/keychain.bash %{buildroot}%{_datadir}/bash-completion/completions/keychain

%files
%license COPYING.txt
%doc ChangeLog.md README.md README.Fedora
%config(noreplace) %{_sysconfdir}/profile.d/keychain.sh
%config(noreplace) %{_sysconfdir}/profile.d/keychain.csh
%{_bindir}/keychain
%{_mandir}/man1/keychain.1*
%{_datadir}/bash-completion/completions/keychain

%check
# Basic check to ensure the binary was built correctly and to silent rpmlint
./%{name} --version

%changelog
%autochangelog
