%global bashcompdir %(pkg-config --variable=completionsdir bash-completion)

Name:           lynis
Version:        3.1.3
Release:        2%{?dist}
Summary:        Security and system auditing tool
License:        GPL-3.0-only
URL:            https://cisofy.com/lynis/
Source0:        https://cisofy.com/files/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  git-core
%if 0%{?el6}
BuildRequires:  procps
%else
BuildRequires:  procps-ng
%endif
Requires:       audit
Requires:       e2fsprogs
Requires:       module-init-tools

%description
Lynis is an auditing and hardening tool for Unix/Linux and you might even call
it a compliance tool. It scans the system and installed software. Then it 
performs many individual security control checks. It determines the hardening 
state of the machine, detects security issues and provides suggestions to 
improve the security defense of the system.

%prep
%autosetup -S git -n %{name} 

%build
# Empty build.

%install
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
install -p default.prf %{buildroot}%{_sysconfdir}/%{name}

mkdir -p %{buildroot}%{_bindir}
install -p lynis %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_mandir}/man8
install -p lynis.8 %{buildroot}%{_mandir}/man8

mkdir -p  %{buildroot}%{_datadir}/%{name}/include/
# Forced by upstream. Otherwise these scripts can't be executed.
install -p include/* %{buildroot}%{_datadir}/%{name}/include/
chmod 644 %{buildroot}%{_datadir}/%{name}/include/*

mkdir -p  %{buildroot}%{_datadir}/%{name}/plugins/
install -p plugins/* %{buildroot}%{_datadir}/%{name}/plugins/

cp -pR db/ %{buildroot}%{_datadir}/%{name}/

mkdir -p %{buildroot}%{bashcompdir}
install -p extras/bash_completion.d/lynis %{buildroot}%{bashcompdir}/

mkdir -p %{buildroot}%{_localstatedir}/log/
touch %{buildroot}%{_localstatedir}/log/lynis.log
touch %{buildroot}%{_localstatedir}/log/lynis-report.dat

%check
# Sanity check
./lynis audit system --quick --pentest

%files
%doc CHANGELOG* CONTRIBUTORS* FAQ* README*
%doc extras/systemd/
%license LICENSE
%{_bindir}/lynis
%{bashcompdir}/*
%{_datadir}/lynis/
%{_mandir}/man8/lynis.8*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/default.prf
%ghost %{_localstatedir}/log/lynis.log
%ghost %{_localstatedir}/log/lynis-report.dat

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 16 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.1.3-1
- 3.1.3

* Fri Sep 27 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.1.2-1
- 3.1.2

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Mar 18 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.1.1-1
- 3.1.1

* Tue Mar 12 2024 Gwyn Ciesla <gwync@protonmail.com> - 3.1.0-1
- 3.1.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 19 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.0.9-5
- Additional egrep patch

* Wed Dec 06 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.0.9-4
- pgrep patch

* Tue Sep 19 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.0.9-3
- Additional egrep patch

* Mon Aug 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.0.9-2
- Upstream patch to remove egrep usage

* Sat Aug 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.0.9-1
- 3.0.9

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 28 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.0.8-4
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 13 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.0.8-1
- 3.0.8

* Wed Jan 19 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.0.7-1
- 3.0.7

* Fri Jul 23 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.0.6-1
- 3.0.6

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.0.1-1
- 3.0.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 20 2020 Othman Madjoudj Othman Madjoudj <athmane@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0 (rhbz #1848716)
- Fixes CVE-2020-13882 / CVE-2019-13033

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 15 2019 Othman Madjoudj <athmane@fedoraproject.org> - 2.7.5-4
- Relax include perms

* Sun Sep 15 2019 Othman Madjoudj <athmane@fedoraproject.org> - 2.7.5-3
- Leave file perms as provided by upstream (rhbz #1674509)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 29 2019 Athmane Madjoudj <athmane@fedoraproject.org> - 2.7.5-1
- Update to 2.7.5 (rhbz #1686372)

* Thu Feb 14 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.7.1-1
- 2.7.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 26 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.7.0-1
- 2.7.0

* Wed Aug 29 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.6.8-1
- 2.6.8

* Thu Jul 19 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.6.6-1
- Update to 2.6.6 (rhbz #1598940)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.6.5-1
- 2.6.5

* Sat May 05 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.6.4-1
- Update to 2.6.4 (rhbz #1574130)

* Sun Mar 11 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.6.3-1
- Update to 2.6.3 (rhbz #1552963)

* Thu Feb 22 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.6.2-1
- Update to 2.6.2 (rhbz #1539272)

* Wed Feb 21 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.6.1-1
- Update to 2.6.1 (rhbz #1539272)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0 (rhbz #1536241)

* Thu Jan 18 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 2.5.9-1
- Update to 2.5.9 (rhbz #1534521)

* Sat Dec 30 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.5.8-1
- Update to 2.5.8 (rhbz #1529807)

* Thu Nov 02 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.5.7-2
- Fix BR in epel6

* Wed Nov 01 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.5.7-1
- Update to 2.5.7 (rhbz #1508417)

* Sun Oct 01 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.5.5-2
- Add check section

* Tue Sep 12 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.5.5-1
- Update to 2.5.5 (rhbz #1488452)

* Fri Aug 18 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.5.3-1
- Update to 2.5.3 (rhbz #1482518)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.5.2-1
- Update to 2.5.2
- Remore upstreamed patch

* Sun Jun 18 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.5.1-2
- Add patch to fix lynis show changelog

* Sun Jun 18 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.5.1-1
- Update to 2.5.1

* Wed May 03 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.5.0-1
- Update to 2.5.0

* Thu Mar 30 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.4.8-1
- Update to 2.4.8

* Sat Mar 25 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.4.7-1
- Update to 2.4.7

* Sun Mar 05 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.4.4-1
- Update to 2.4.4

* Sat Feb 18 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.4.2-1
- Update to 2.4.2

* Fri Feb 10 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2.4.1-1
- Update to 2.4.1

* Sat Oct 29 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0

* Mon Oct 03 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 2.3.4-1
- Update to 2.3.4

* Sat Mar 19 2016 Athmane Madjoudj <athmane@fedoraproject.org> 2.2.0-3
- Update to 2.2.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 10 2015 Christopher Meng <rpm@cicku.me> - 2.1.1-1
- Update to 2.1.1

* Mon Jul 13 2015 Christopher Meng <rpm@cicku.me> - 2.1.0-1
- Update to 2.1.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 14 2014 Christopher Meng <rpm@cicku.me> - 1.6.4-1
- Update to 1.6.4

* Fri Sep 12 2014 Christopher Meng <rpm@cicku.me> - 1.6.1-1
- Update to 1.6.1

* Sun Aug 03 2014 Christopher Meng <rpm@cicku.me> - 1.5.9-1
- Update to 1.5.9

* Fri Jul 11 2014 Christopher Meng <rpm@cicku.me> - 1.5.7-1
- Update to 1.5.7

* Mon Jun 16 2014 Christopher Meng <rpm@cicku.me> - 1.5.6-1
- Update to 1.5.6

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Christopher Meng <rpm@cicku.me> - 1.5.3-1
- Update to 1.5.3

* Fri Apr 11 2014 Christopher Meng <rpm@cicku.me> - 1.5.0-1
- Update to 1.5.0

* Sat Mar 08 2014 Christopher Meng <rpm@cicku.me> - 1.4.4-1
- Update to 1.4.4

* Thu Feb 27 2014 Christopher Meng <rpm@cicku.me> - 1.4.3-1
- Update to 1.4.3

* Fri Feb 21 2014 Christopher Meng <rpm@cicku.me> - 1.4.2-1
- Update to 1.4.2

* Wed Feb 19 2014 Christopher Meng <rpm@cicku.me> - 1.4.1-1
- Update to 1.4.1

* Fri Feb 07 2014 Christopher Meng <rpm@cicku.me> - 1.4.0-1
- Update to 1.4.0

* Fri Jan 10 2014 Christopher Meng <rpm@cicku.me> - 1.3.9-1
- Update to 1.3.9

* Sat Dec 28 2013 Christopher Meng <rpm@cicku.me> - 1.3.8-1
- Update to 1.3.8

* Thu Dec 12 2013 Christopher Meng <rpm@cicku.me> - 1.3.7-1
- Update to 1.3.7

* Wed Dec 04 2013 Christopher Meng <rpm@cicku.me> - 1.3.6-1
- Update to 1.3.6

* Tue Nov 26 2013 Christopher Meng <rpm@cicku.me> - 1.3.5-1
- Update to 1.3.5

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 30 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 1.2.9-1
- Updated to 1.2.9

* Fri Dec 04 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 1.2.7-1
- Updated to 1.2.7

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 08 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 1.2.6-2
- fixed requires tag

* Sun Apr 12 2009 Rakesh Pandit <rakesh@fedoraporject.org> - 1.2.6-1
- Updated to 1.2.6: CHANHELOG for details

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 07 2008 Rakesh Pandit <rakesh@fedoraproject.org> - 1.2.1-3
- cleaned %%files

* Fri Nov 07 2008 Rakesh Pandit <rakesh@fedoraproject.org> - 1.2.1-2
- macros consistency - fixed hard code path

* Fri Oct 31 2008 Rakesh Pandit <rakesh@fedoraproject.org> - 1.2.1-1
- Initial package
