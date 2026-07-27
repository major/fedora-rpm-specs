Name:           keychain
Summary:        Agent manager for OpenSSH, ssh.com, Sun SSH, and GnuPG
Version:        3.0.0
Release:        %autorelease
License:        GPL-3.0-only
URL:            https://kernel-seeds.org/projects/keychain/
Source:         https://github.com/danielrobbins/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.sh
Source2:        %{name}.csh
Source3:        README.Fedora
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  help2man

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

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files keychain
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh

# Generate man page
mkdir -p %{buildroot}%{_mandir}/man1
PYTHONPATH=%{buildroot}%{python3_sitelib} help2man --no-info --name="Agent manager for OpenSSH, ssh.com, Sun SSH, and GnuPG" --version-string="%{version}" %{buildroot}%{_bindir}/%{name} -o %{buildroot}%{_mandir}/man1/%{name}.1

%files -f %{pyproject_files}
%license LICENSE
%doc ChangeLog.md README.md README.Fedora
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.sh
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.csh
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%check
%pyproject_check_import
PYTHONPATH=%{buildroot}%{python3_sitelib} %{buildroot}%{_bindir}/%{name} --version

%changelog
%autochangelog
