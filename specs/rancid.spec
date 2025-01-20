Name: rancid
Version: 3.13
Release: 14%{?dist}
Summary: Really Awesome New Cisco confIg Differ

License: BSD-3-Clause
URL: http://www.shrubbery.net/rancid/
Source0: https://shrubbery.net/pub/%{name}/%{name}-%{version}.tar.gz
Source1: %{name}.cron
Patch0: %{name}-Makefile.patch
Patch1: %{name}-configure-no-ping-test.patch
Patch2: %{name}-3.13-dnos10-psu-filter.patch

BuildRequires: automake, autoconf
BuildRequires: make
BuildRequires: gcc
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: expect >= 5.40
BuildRequires: findutils
# To configure ping command line arguments:
BuildRequires: iputils
# To configure path to /usr/sbin/sendmail:
BuildRequires: ssmtp
# To configure telnet command line arguments:
BuildRequires: telnet

Requires(pre): shadow-utils
Requires: expect >= 5.40
# For control_rancid's use of find command:
Requires: findutils
# For lg.cgi's use of ping command:
Requires: iputils
Requires: perl-interpreter
Requires: /usr/sbin/sendmail
Requires: cronie
Requires: openssh-clients
Requires: git
Suggests: telnet

%description
RANCID monitors a router's (or more generally a device's) configuration, 
including software and hardware (cards, serial numbers, etc) and uses CVS 
(Concurrent Version System), Subversion, or Git to maintain history of changes.


%prep
%autosetup -p1

%build
%configure \
    --sysconfdir=%{_sysconfdir}/%{name} \
    --bindir=%{_libexecdir}/%{name} \
    --libdir=%{perl_vendorlib} \
    --localstatedir=%{_localstatedir}/%{name} \
    --enable-conf-install \
    --with-git
%make_build


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
install -d -m 0755 %{buildroot}/%{_localstatedir}/%{name}
install -d -m 0755 %{buildroot}/%{_localstatedir}/log/%{name}
install -d -m 0755 %{buildroot}/%{_localstatedir}/log/%{name}/old
install -d -m 0755 %{buildroot}/%{_sysconfdir}/cron.d
install -d -m 0755 %{buildroot}/%{_bindir}/

#symlink some bins from %%{_libexecdir}/%%{name} to %%{_bindir}
for base in \
 %{name} %{name}-cvs %{name}-fe %{name}-run
 do
 ln -sf ../libexec/%{name}/${base} \
  %{buildroot}/%{_bindir}/${base}
done

install -D -p -m 0644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/cron.d/%{name}

#Patch cron file to point to correct installation directory
sed -i 's|RANCIDBINDIR|%{_libexecdir}/%{name}|g' %{buildroot}/%{_sysconfdir}/cron.d/%{name}

#Patch to point to correct log directory
grep -rlF '$BASEDIR/logs' %{buildroot} | xargs sed -i 's|\$BASEDIR/logs|%{_localstatedir}/log/%{name}|'

#Remove docs that will get installed to docdir in files section below
rm -f %{buildroot}%{_datadir}/%{name}/{CHANGES,FAQ,README,README.lg,UPGRADING,Todo,COPYING}


%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -d %{_localstatedir}/%{name}/ -s /bin/bash \
	    -k /etc/skel -m -c "RANCID" %{name}
exit 0


%files
%doc CHANGES FAQ README README.lg UPGRADING Todo
%license COPYING

#%%{_sysconfdir}-files
%attr(750,%{name},%{name}) %dir %{_sysconfdir}/%{name}
%attr(640,%{name},%{name}) %config(noreplace) %{_sysconfdir}/%{name}/*
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/cron.d/%{name}

#%%{_libexecdir}/%%{name}-files
%{_libexecdir}/%{name}

#%%{_bindir}-files
%{_bindir}/*

#%%{_mandir}-files
%{_mandir}/*/*

#%%{_datadir}/%%{name}-files
%{_datadir}/%{name}

#%%{_localstatedir}-directories
%attr(750,%{name},%{name}) %dir %{_localstatedir}/log/%{name}
%attr(750,%{name},%{name}) %dir %{_localstatedir}/log/%{name}/old
%attr(750,%{name},%{name}) %dir %{_localstatedir}/%{name}/

%{perl_vendorlib}/*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 19 2024 Charles R. Anderson <cra@alum.wpi.edu> - 3.13-12
- Enable git as default VCS for new installs
- Remove extraneous BuildRequires
- Requires /usr/sbin/sendmail and cronie for crontabs
- Requires openssh-clients and git
- Suggests telnet

* Fri Apr 19 2024 Charles R. Anderson <cra@alum.wpi.edu> - 3.13-11
- Convert License tag to SPDX format
- Convert to autosetup
- Use relative symlinks from /usr/bin/* to ../libexec/rancid/*
- Remove doc files that were duplicated in /usr/share/rancid

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 17 2023 Charles R. Anderson <cra@alum.wpi.edu> - 3.13-7
- add patch to filter PSU output on Dell OS10 10.5.3.2
  https://shrubbery.net/pipermail/rancid-discuss/2022-April/011186.html

* Fri Mar 10 2023 Chris Adams <linux@cmadams.net> - 3.13-6
- fix BASEDIR and LOGDIR (#2092029)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 08 2021 Charles R. Anderson <cra@alum.wpi.edu> - 3.13-1
- Update to 3.13
- Use https rather than ftp for source0
- Remove logrotate and add cron job to delete log files older than 30 days (rhbz#1873378)
- Disable configure ping syntax test since it fails in mock environment

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Charles R. Anderson <cra@wpi.edu> - 3.12-1
- Update to 3.12

* Tue Feb 11 2020 Charles R. Anderson <cra@wpi.edu> - 3.11-1
- Update to 3.11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Charles R. Anderson <cra@wpi.edu> - 3.9-1
- Update to 3.9
- mention that Git is supported in the package description
- Bring up to date with packaging guidelines:
- remove unnecessary buildroot cleaning
- use %%license tag
- fix macro usage in Source0 URL
- remove redundant %%dir usage
- use %%make_build
- adjust some whitespace for readability

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 17 2017 David Brown <david.brown@pnnl.gov> - 3.6.2-1
- New upstream version

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 3.2-6
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 30 2015 David Brown <david.brown@pnnl.gov> - 3.2-2
- Add upstream patches

* Wed Nov 19 2014 David Brown <david.brown@pnnl.gov> - 3.2-1
- New Upstream Version
- Fix Bugzilla #1165738

* Wed Nov 19 2014 Sven Lankes <sven@lank.es> - 3.1-3
- Filter uptime of Foundry Switch Fabric Modules (fixes rhbz #1165738)

* Mon Oct 6 2014 David Brown <david.brown@pnnl.gov> - 3.1-2
- New updated version

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.3.8-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Sven Lankes <sven@lank.es> - 2.3.8-1
- New upstream release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 23 2011 Peter Robinson <pbrobinson@gmail.com> 2.3.6-1
- New upstream 2.3.6 release

* Tue Sep 28 2010 Peter Robinson <pbrobinson@gmail.com> 2.3.4-1
- New upstream 2.3.4 release

* Wed Jul 22 2009 Gary T. Giesen <giesen@snickers.org> 2.3.2-3
- Changed GECOS name for rancid user

* Wed Jul 22 2009 Gary T. Giesen <giesen@snickers.org> 2.3.2-2
- Added logrotate (and updated crontab to let logrotate handle log file 
  cleanup
- Removed Requires: for rsh, telnet, and openssh-clients
- Removed Requires: for cvs
- Cleaned up file permissions
- Added shell for rancid user for CVS tree creation and troubleshooting
- Patch cron file for installation path
- Removed installation of CVS root to permit SVN use
- Moved from libdir to libexecdir

* Thu Jul 16 2009 Gary T. Giesen <giesen@snickers.org> 2.3.2-1
- Updated to 2.3.2 stable
- Removed versioned expect requirement so all supported Fedora/EPEL releases
  now meet the minimum
- Spec file cleanup/style changes

* Wed Oct 08 2008 Aage Olai Johnsen <aage@thaumaturge.org> 2.3.2-0.6a8
- Some fixes (#451189)

* Tue Sep 30 2008 Aage Olai Johnsen <aage@thaumaturge.org> 2.3.2-0.5a8
- Some fixes (#451189)

* Tue Sep 30 2008 Aage Olai Johnsen <aage@thaumaturge.org> 2.3.2-0.4a8
- More fixes (#451189)
- Patched Makefiles - Supplied by Mamoru Tasaka (mtasaka@ioa.s.u-tokyo.ac.jp) 

* Tue Sep 23 2008 Aage Olai Johnsen <aage@thaumaturge.org> 2.3.2-0.3a8
- More fixes (#451189)

* Wed Jul 09 2008 Aage Olai Johnsen <aage@thaumaturge.org> 2.3.2a8-0.2a8
- Plenty of fixes (#451189)
- Patched rancid.conf-file
- Added cronjob

* Sat May 31 2008 Aage Olai Johnsen <aage@thaumaturge.org> 2.3.2a8-0.1
- Initial RPM release
