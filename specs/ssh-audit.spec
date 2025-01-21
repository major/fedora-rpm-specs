Name:           ssh-audit
Version:        3.3.0
Release:        2%{?dist}
Summary:        An SSH server & client configuration security auditing tool

License:        MIT
URL:            https://github.com/jtesta/ssh-audit
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source:         %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
# Ideally this would be hosted not next to the sources, but, I cannot find one
Source:         %{url}/releases/download/v%{version}/jtesta_2020-2025.asc

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  gnupg2
BuildRequires:  python3dist(pytest)

%description
ssh-audit is an SSH server & client security auditing (banner, key exchange,
encryption, mac, compression, compatibility, security, etc)

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup

#remove shebang
sed -i -e '1{\@^#!/usr/bin/env python@d}' src/ssh_audit/ssh_audit.py

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
# importable module is underscore :)
%pyproject_save_files ssh_audit

install -t %{buildroot}%{_mandir}/man1 -Dpm 0644 ssh-audit.1

%check
# Upstream uses tox, but doesn't have definitions for py3.12 yet
%pytest

%files -f %{pyproject_files}
%doc README.md
%{_mandir}/man1/ssh-audit.1*
%{_bindir}/ssh-audit

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 18 2024 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 3.3.0-1
- Update to 3.3.0 rhbz#2318995

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.2.0-2
- Rebuilt for Python 3.13

* Tue May 14 2024 Neil Hanlon <neil@shrug.pw> - 3.2.0-1
- fedora#2276538

* Fri Apr 26 2024 Danie de Jager <danie.dejager@doxim.com> - 3.2.0-1
- update to version 3.2.0

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 02 2024 Neil Hanlon <neil@shrug.pw> - 3.1.0-1
- add in man page
- use pytest

* Sun Oct 15 2023 Neil Hanlon <neil@shrug.pw> - 3.0.0-1
- Initial package.
