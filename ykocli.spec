%global owner gbcox
%global commit 01500f50f2aeb7ba0e397e632854c74eef9f77a5
%global shortcommit %(c=%{commit}; echo ${c:0:12})

Name:     ykocli
Version:  1.2.1
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
Requires:       zbar

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
%config %{_sysconfdir}/ykocli.conf
%{_bindir}/ykocli
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/src-yko-set-colors.sh
%{_libexecdir}/%{name}/src-yko-set-variables.sh
%{_libexecdir}/%{name}/src-yko-conf-override.sh
%{_libexecdir}/%{name}/src-yko-ck-input.sh
%{_libexecdir}/%{name}/src-yko-ck-touch.sh
%{_libexecdir}/%{name}/src-yko-figlet.sh
%{_libexecdir}/%{name}/src-yko-help.sh
%{_libexecdir}/%{name}/src-yko-table.sh
%{_libexecdir}/%{name}/src-yko-time.sh
%{_libexecdir}/%{name}/src-yko-trap.sh
%{_libexecdir}/%{name}/src-yko-totp.sh
%{_libexecdir}/%{name}/src-yko-add.sh
%{_libexecdir}/%{name}/src-yko-delete.sh
%{_libexecdir}/%{name}/src-yko-rename.sh
%{_libexecdir}/%{name}/src-yko-devinfo.sh
%{_mandir}/man1/ykocli.1*

%changelog
* Mon Jan 23 2023 Gerald Cox <gbcox@fedoraproject.org> - 1.2.1-1
- Add Touch Mode; mod cfg ovrd rhbz#2162909; rhbz#2162885

* Mon Jan 23 2023 Gerald Cox <gbcox@fedoraproject.org> - 1.2.0-1
- Add Touch Mode; mod cfg ovrd rhbz#2162909; rhbz#2162885

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Gerald Cox <gbcox@fedoraproject.org> - 1.1.1-1
- Allow multiple yubikeys rhbz#2161474

* Mon Jan 16 2023 Gerald Cox <gbcox@fedoraproject.org> - 1.1.0-1
- Refactor for Add, Delete, Rename functionality

* Wed Dec 28 2022 Gerald Cox <gbcox@fedoraproject.org> - 1.0.2-1
- Add optional background mode

* Wed Nov 23 2022 Gerald Cox <gbcox@fedoraproject.org> - 1.0.1-1
- Fedora Review rhgz#2144611

* Mon Nov 21 2022 Gerald Cox <gbcox@fedoraproject.org> - 1.0.0-1
- Fedora Review rhbz#2144611
