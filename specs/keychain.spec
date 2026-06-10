Name:           keychain
Summary:        Agent manager for OpenSSH, ssh.com, Sun SSH, and GnuPG
Version:        2.9.8
Release:        %autorelease
License:        GPL-2.0-only
URL:            https://github.com/danielrobbins/%{name}
Source:         https://github.com/danielrobbins/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.sh
Source2:        %{name}.csh
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
sed -i -e 's|/usr/ucb:||' %{name}.sh
# Remove shebang from bash completion script
sed -i -e '1{\@^#!/usr/bin/env bash@d}' completions/%{name}.bash

%build
%make_build %{name} %{name}.1

%install
install -D -p -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh
install -D -p -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# Bash completion
install -D -p -m 0644 completions/%{name}.bash %{buildroot}%{bash_completions_dir}/%{name}

%files
%license COPYING.txt
%doc ChangeLog.md README.md README.Fedora
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.sh
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.csh
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{bash_completions_dir}/%{name}

%check
# Basic check to ensure the binary was built correctly and to silent rpmlint
./%{name} --version

%changelog
%autochangelog
