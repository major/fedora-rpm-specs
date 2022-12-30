%global owner gbcox
%global commit 9cb5f4278e9fa473ac39968fc78bf19b52a875f1
%global shortcommit %(c=%{commit}; echo ${c:0:12})

Name:     ykocli
Version:  1.0.2
Release:  1%{?dist}
Summary:  Front-end script for ykman to obtain TOTP tokens

License:  GPL-3.0-or-later
URL:      https://bitbucket.org/%{owner}/%{name}
Source0:  https://bitbucket.org/%{owner}/%{name}/get/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Source1:  %{name}.rpmlintrc

BuildArch:      noarch
BuildRequires:  make
Requires:       figlet
Requires:       copyq
Requires:       yubikey-manager

%description
ykocli is a front-end command line utility (actually, a bash script)
that places ykman obtained TOTP tokens into the CopyQ clipboard.

%prep
%autosetup -n %{owner}-%{name}-%{shortcommit}

%build

%install
%make_install prefix=%{_prefix} sysconfdir=%{_sysconfdir}

%files
%license LICENSE.md
%doc README.md contributors.txt examples/
%config(noreplace) %{_sysconfdir}/ykocli.conf
%{_bindir}/ykocli
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/src-yko-set-colors.sh
%{_libexecdir}/%{name}/src-yko-ck-input.sh
%{_libexecdir}/%{name}/src-yko-figlet.sh
%{_libexecdir}/%{name}/src-yko-help.sh
%{_libexecdir}/%{name}/src-yko-main.sh
%{_libexecdir}/%{name}/src-yko-time.sh
%{_libexecdir}/%{name}/src-yko-trap.sh
%{_mandir}/man1/ykocli.1*

%changelog
* Wed Dec 28 2022 Gerald Cox <gbcox@fedoraproject.org> - 1.0.2-1
- Add optional background mode

* Wed Nov 23 2022 Gerald Cox <gbcox@fedoraproject.org> - 1.0.1-1
- Fedora Review rhgz#2144611

* Mon Nov 21 2022 Gerald Cox <gbcox@fedoraproject.org> - 1.0.0-1
- Fedora Review rhbz#2144611
