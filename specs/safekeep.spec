%global commit 75e66fe16a3afcb78db5786018487adb63e91793
%global date 20230910
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%define name    safekeep
%define version 1.5.1
%define release 4
%define homedir %{_localstatedir}/lib/%{name}

Name:           %{name}
Version:        %{version}^%{date}git%{shortcommit}
Release:        %{release}%{?dist}
Summary:        The SafeKeep backup system

License:        GPL-2.0-or-later
URL:            http://%{name}.sourceforge.net
Source0:        https://github.com/dimipaun/%{name}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz
Source1:        README.Fedora

BuildArch:      noarch
BuildRequires: make
BuildRequires:  xmlto, asciidoc > 6.0.3

%description
SafeKeep is a client/server backup system which enhances the
power of rdiff-backup with simple, centralized configuration.

%package common
Summary:        The SafeKeep backup system (common component)
Requires:       rdiff-backup
Requires:       python3 >= 3.4

%description common
SafeKeep is a client/server backup system which enhances the
power of rdiff-backup with simple, centralized configuration.

This is the common component of SafeKeep. It is shared in 
between the client/server components.

%package client
Summary:        The SafeKeep backup system (client component)
Requires:       openssh-server
Requires:       coreutils
Requires:       util-linux
Requires:       %{name}-common = %{version}-%{release}

%description client
SafeKeep is a client/server backup system which enhances the
power of rdiff-backup with simple, centralized configuration.

This is the client component of SafeKeep. It should be
installed on all hosts that need to be backed-up.

%package server
Summary:        The SafeKeep backup system (server component)
Requires(pre):  /usr/sbin/useradd
Requires(pre):  /usr/sbin/groupadd
Requires:       openssh, openssh-clients
Requires:       %{name}-common = %{version}-%{release}
Requires:       crontabs

%description server
SafeKeep is a client/server backup system which enhances the
power of rdiff-backup with simple, centralized configuration.

This is the server component of SafeKeep. It should be
installed on the server on which the data will be backed-up to.

%prep
%setup -q -n %{name}-%{commit}
cp -p %{SOURCE1} .

%build
make %{?_smp_mflags} build

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -d -m 750 "%{buildroot}%{homedir}"
install -d -m 700 "%{buildroot}%{homedir}/.ssh"

%pre server
%{_sbindir}/groupadd -f -r %{name}
id %{name} >/dev/null 2>&1 || \
%{_sbindir}/useradd -r -g %{name} -d %{homedir} -s /sbin/nologin \
  -c "Used by %{name} to run and store backups." %{name}

%files common
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%doc AUTHORS COPYING README INSTALL TODO samples/client-script-sample.sh
%{!?_licensedir:%global license %doc}
%license LICENSE
%doc README.Fedora

%files client

%files server
%attr(750,%{name},%{name}) %dir %{homedir}
%attr(700,%{name},%{name}) %dir %{homedir}/.ssh
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/backup.d
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%{_sysconfdir}/cron.daily/%{name}
%{_mandir}/man5/%{name}.conf.5*
%{_mandir}/man5/%{name}.backup.5*
%doc samples/sample.backup

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1^20230910git75e66fe-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1^20230910git75e66fe-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1^20230910git75e66fe-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Sep 10 2023 Frank Crawford <frank@crawford.emu.id.au> - 1.5.1^20230910git75e66fe-1
- Update with latest patches for rdiff-backup 2.2
- Pull latest git version

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 21 2022 Frank Crawford <frank@crawford.emu.id.au> - 1.5.1-6
- SPDX license update

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 17 2020 Frank Crawford <frank@crawford.emu.id.au> 1.5.1-1
- Latest upstream release 

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 24 2019 Frank Crawford <frank@crawford.emu.id.au> 1.5.0-1
- Latest upstream release 
- Updated for Python 3

* Sun Feb 10 2019 Frank Crawford <frank@crawford.emu.id.au> 1.4.5-1
- Latest upstream release 

* Fri Feb 08 2019 Frank Crawford <frank@crawford.emu.id.au> - 1.4.4-8
- Correct FTBS error due to default in F30 as python3, replace with python2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.4.4-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jul  9 2016 Frank Crawford <frank@crawford.emu.id.au> 1.4.4-1
- Latest upstream release 

* Thu Jun 23 2016 Frank Crawford <frank@crawford.emu.id.au> 1.4.3-1
- Latest upstream release 

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 22 2013 Jóhann B. Guðmundsson <johannbg@fedoraproject.org> - 1.4.2-3
- Add a missing requirement on crontabs to spec file

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun  2 2013 Frank Crawford <frank@crawford.emu.id.au> 1.4.2-1
- Latest upstream release 

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jan 19 2013 Frank Crawford <frank@crawford.emu.id.au> 1.4.1-1
- Latest upstream release 

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 12 2012 Frank Crawford <frank@crawford.emu.id.au> 1.4.0-1
- Latest upstream release 

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 27 2011 Frank Crawford <frank@crawford.emu.id.au> 1.3.3-1
- Latest upstream release 
- Dropped safekeep.cron patch as issue addressed up stream

* Sun May 08 2011 Frank Crawford <frank@crawford.emu.id.au> 1.3.2-2
- Patch safekeep.cron to not run unless safekeep has been configured

* Sat Mar 12 2011 Frank Crawford <frank@crawford.emu.id.au> 1.3.2-1
- Latest upstream release 

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 14 2009 Jef Spaleta <jspaleta AT fedoraproject DOT org> 1.2.1-1
- Latest upstream release 

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 3 2009 Jef Spaleta <jspaleta AT fedoraproject DOT org> 1.0.5-1
- Latest upstream release 

* Tue Jul 1 2008 Jef Spaleta <jspaleta AT fedoraproject DOT org> 1.0.4-1
- Latest upstream release 

* Fri Oct 19 2007 Jef Spaleta <jspaleta@gmail.com> 1.0.3-2
- Added README.Fedora with explanation of client subpackaging.

* Fri Oct 19 2007 Dimi Paun <dimi@lattica.com> 1.0.3-1
- Clarify licensing in lite of the new GPLv3 license;
- New --force option to handle unexpected problems with the data repository;
- Better logging and status handling when we invoke external commands
- Clearer backup status on job end.
- A small packaging bug got fixes.

* Fri Sep 7 2007 Dimi Paun <dimi@lattica.com> 1.0.2-1
- Add missing buildroot removal in install section (Jeff Spaleta)
- Remove references to PACKAGE_VERSION, follow the Fedora 
  guidelines closer.
- Provide default attr for all packages.
- Clarify the licensing in .rpm package.
- We don't need to include AUTHORS COPYING LICENSE multiple times, 
  keeping them in -common is enough.
- More acceptable SF link.

* Sun Jun 17 2007 Dimi Paun <dimi@lattica.com> 1.0.1-1
- The safekeep user no longer requires a working shell
- Add support for Fedora 7 to the testing script
- Packaging improvements for integration into Fedora
- Remove the old configuration migration scripts
- Do not package the testing script, it's used only during development

* Wed May 16 2007 Dimi Paun <dimi@lattica.com> 1.0.0-1
- Small documentation inprovements.

* Fri Apr 27 2007 Dimi Paun <dimi@lattica.com> 0.9.3-1
- Use /bin/bash as the shell for the safekeep system account;
- Invoke rdiff-backup with --force when trimming histroy;
- A few small logging bugs got fixed;
- Small documentation tweaks.

* Tue Mar 13 2007 Dimi Paun <dimi@lattica.com> 0.9.2-1
- Client configuration files have been moved to 
  /etc/safekeep/backup.d, and have the extension '.backup';
- A new global configuration file has been added in 
  /etc/safekeep/safekeep.conf;
- A number of command line options have been deprecated;
  (-e/--email, -s/--smtp), and moved to the global configuration.
- SafeKeep now knows of the user under which the backup will execute,
  making it possible to better deploy keys, avoid the need to invoke
  safekeep(1) via sudo(8), and execute the backup as root if need be;
- Relative paths now have more intuitive behaviour;
- Some documentation improvements;
- Automatic migration of old configuration to the new format;
- A CRITICAL (e.g. data loss) race has been fixed.

* Mon Feb 12 2007 Dimi Paun <dimi@lattica.com> 0.9.1-1
- Lots of documentation improvements;
- Prepare the RPMs for Fedora acceptance (Jef Spaleta);
- Automatic creation of data store directory;
- A few bug fixes.

* Thu Feb  1 2007 Dimi Paun <dimi@lattica.com> 0.9.0-1
- Initial release
