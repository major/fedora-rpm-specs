Name:           borgmatic
Version:        1.7.2
Release:        1%{?dist}
Summary:        Simple Python wrapper script for borgbackup

License:        GPLv3
URL:            https://torsion.org/borgmatic
Source0:        https://projects.torsion.org/borgmatic-collective/borgmatic/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros

Requires:       borgbackup


%description
borgmatic (formerly atticmatic) is a simple Python wrapper script for
the Borg backup software that initiates a backup, prunes any old backups
according to a retention policy, and validates backups for consistency.

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup -n %{name}

%build
%pyproject_wheel

%{__python3} -c 'from borgmatic.commands.completion import bash_completion; print(bash_completion())' > %{name}-bash-completion


%install
%pyproject_install
%pyproject_save_files %{name}

install -dm 0750 %{buildroot}%{_sysconfdir}/borgmatic
install -dm 0750 %{buildroot}%{_sysconfdir}/borgmatic.d

sed -i 's#/root/.local/bin/borgmatic#%{_bindir}/%{name}#' sample/systemd/%{name}.service
install -Dpm 0644 sample/systemd/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -Dpm 0644 sample/systemd/%{name}.timer %{buildroot}%{_unitdir}/%{name}.timer

install -Dpm 0644 %{name}-bash-completion %{buildroot}%{_datadir}/bash-completion/completions/%{name}


%files -f %{pyproject_files}
%doc AUTHORS NEWS README.md
%license LICENSE
%attr(0750, root, root) %{_sysconfdir}/borgmatic
%attr(0750, root, root) %{_sysconfdir}/borgmatic.d
%{_bindir}/borgmatic
%{_bindir}/generate-borgmatic-config
%{_bindir}/upgrade-borgmatic-config
%{_bindir}/validate-borgmatic-config
%{_datadir}/bash-completion/completions/%{name}
%{_unitdir}/borgmatic.service
%{_unitdir}/borgmatic.timer


%post
%systemd_post borgmatic.timer


%preun
%systemd_preun borgmatic.timer


%postun
%systemd_postun borgmatic.timer


%changelog
* Fri Sep 09 2022 Felix Kaechele <felix@kaechele.ca> - 1.7.2-1
- update to 1.7.2

* Sat Sep 03 2022 Felix Kaechele <felix@kaechele.ca> - 1.7.1-1
- update to 1.7.1

* Thu Jul 21 2022 Felix Kaechele <felix@kaechele.ca> - 1.6.6-1
- update to 1.6.6

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 01 2022 Felix Kaechele <felix@kaechele.ca> - 1.6.5-1
- update to 1.6.5

* Sun Jun 26 2022 Felix Kaechele <felix@kaechele.ca> - 1.6.4-2
- fixup version in setup.py
- use pyproject_save_files

* Sat Jun 25 2022 Felix Kaechele <felix@kaechele.ca> - 1.6.4-1
- update to 1.6.4
- update source URL

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.6.3-2
- Rebuilt for Python 3.11

* Fri Jun 10 2022 Felix Kaechele <felix@kaechele.ca> - 1.6.3-1
- update to 1.6.3

* Wed Jun 01 2022 Felix Kaechele <felix@kaechele.ca> - 1.6.2-2
- use pyproject rpm macros
- drop support for EPEL < 9

* Wed Jun 01 2022 Felix Kaechele <felix@kaechele.ca> - 1.6.2-1
- update to 1.6.2
- install bash-completion files

* Wed May 25 2022 Felix Kaechele <felix@kaechele.ca> - 1.6.1-1
- update to 1.6.1

* Wed Apr 27 2022 Felix Kaechele <felix@kaechele.ca> - 1.6.0-1
- update to 1.6.0

* Mon Mar 14 2022 Felix Kaechele <felix@kaechele.ca> - 1.5.24-1
- update to 1.5.24

* Thu Feb 10 2022 Felix Kaechele <felix@kaechele.ca> - 1.5.23-1
- update to 1.5.23

* Fri Feb 04 2022 Felix Kaechele <felix@kaechele.ca> - 1.5.22-2
- fix sed on systemd unit to only replace the path

* Fri Feb 04 2022 Felix Kaechele <felix@kaechele.ca> - 1.5.22-1
- update to 1.5.22

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 24 2021 Felix Kaechele <felix@kaechele.ca> - 1.5.21-1
- update to 1.5.21

* Mon Oct 11 2021 Felix Kaechele <felix@kaechele.ca> - 1.5.20-1
- update to 1.5.20

* Tue Aug 10 2021 Felix Kaechele <heffer@fedoraproject.org> - 1.5.18-1
- update to 1.5.18

* Tue Aug 03 2021 Felix Kaechele <heffer@fedoraproject.org> - 1.5.17-1
- update to 1.5.17

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 18 2021 Felix Kaechele <heffer@fedoraproject.org> - 1.5.15-1
- update to 1.5.15

* Tue Jun 08 2021 Felix Kaechele <heffer@fedoraproject.org> - 1.5.14-1
- update to 1.5.14

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.13-2
- Rebuilt for Python 3.10

* Wed Mar 31 2021 Felix Kaechele <heffer@fedoraproject.org> - 1.5.13-1
- update to 1.5.13

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 21 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.5.11-1
- update to 1.5.11

* Fri Sep 04 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.5.10-1
- update to 1.5.10

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.5.9-1
- update to 1.5.9

* Sun Jul 12 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.5.8-1
- update to 1.5.8

* Wed Jun 24 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.5.7-1
- update to 1.5.7
- add python3-setuptools BuildRequires

* Sun Jun 07 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.5.6-1
- update to 1.5.6

* Thu May 28 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.5-2
- Rebuilt for Python 3.9

* Wed May 27 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.5.5-1
- update to 1.5.5

* Sat May 16 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.5.4-1
- update to 1.5.4

* Thu May 14 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.5.3-1
- update to 1.5.3

* Sat Apr 25 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.5.2-1
- update to 1.5.2

* Mon Feb 03 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.5.1-1
- update to 1.5.1

* Tue Jan 28 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.5.0-1
- update to 1.5.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Felix Kaechele <heffer@fedoraproject.org> - 1.4.22-1
- update to 1.4.22

* Sat Dec 21 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.21-1
- update to 1.4.21

* Fri Dec 13 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.20-1
- update to 1.4.20
- added missing Requires for python-requests

* Mon Dec 09 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.18-1
- update to 1.4.18

* Sat Dec 07 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.17-1
- update to 1.4.17

* Tue Dec 03 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.16-1
- update to 1.4.16

* Tue Nov 26 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.15-1
- update to 1.4.15

* Tue Nov 26 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.14-1
- update to 1.4.14

* Wed Nov 20 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.13-1
- update to 1.4.13

* Mon Nov 18 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.12-1
- update to 1.4.12

* Mon Nov 18 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.11-1
- update to 1.4.11

* Wed Nov 13 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.10-1
- update to 1.4.10

* Tue Nov 12 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.9-1
- update to 1.4.9

* Tue Nov 12 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.8-1
- update to 1.4.8

* Mon Nov 04 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.6-1
- update to 1.4.6

* Wed Oct 23 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.4.0-1
- update to 1.4.0

* Mon Oct 21 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.3.26-1
- update to 1.3.26

* Sat Oct 12 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.3.23-2
- insert conditionals for F29 and EL7
- bring back python3_version variable for EL7 compatibility

* Fri Oct 11 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.3.23-1
- update to 1.3.23
- fix dependencies
- build for noarch
- use release tarball directly from upstream
- include docs and license from release tarball
- use included unit and timer files
- remove tests, they require internet access
- cleanups and modernizations

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-5
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Benjamin Pereto <benjamin@sandchaschte.ch> - 1.2.0-1
- upstream release 1.2.0
- added missing deps ruamel.yaml and pykwalify

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.15-3
- Rebuilt for Python 3.7

* Thu Apr 12 2018 Benjamin Pereto <benjamin@sandchaschte.ch> - 1.1.15-2
- add empty /etc/borgmatic.d as described in documentation
- add empty /etc/borgmatic as described in documentation

* Thu Apr 12 2018 Benjamin Pereto <benjamin@sandchaschte.ch> - 1.1.15-1
- Initial packaging for the borgmatic project

