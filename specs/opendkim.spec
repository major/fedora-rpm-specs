%global systemd (0%{?fedora} >= 18) || (0%{?rhel} >= 7)
# F21+ and RHEL8+ have systemd 211+ which offers RuntimeDirectory
# use that instead of tmpfiles.d
%global systemd_runtimedir (0%{?fedora} >= 21) || (0%{?rhel} >= 8)
%global tmpfiles ((0%{?fedora} >= 15) || (0%{?rhel} == 7)) && !%{systemd_runtimedir}


%global upname OpenDKIM
%global bigname OPENDKIM

%global full_version 2.11.0-Beta2

Summary: A DomainKeys Identified Mail (DKIM) milter to sign and/or verify mail
Name: opendkim
Version: 2.11.0
Release: 0.40%{?dist}
License: BSD-3-Clause AND Sendmail-Open-Source-1.1
URL: http://%{name}.org/
Source0: https://github.com/trusteddomainproject/OpenDKIM/archive/%{full_version}.tar.gz
Source1: opendkim.conf
Source2: opendkim.sysconfig
Source3: SigningTable
Source4: KeyTable
Source5: TrustedHosts
Source6: README.fedora

# https://github.com/trusteddomainproject/OpenDKIM/pull/70
Patch0: 0001-support-for-lua-5.3.patch
# https://github.com/trusteddomainproject/OpenDKIM/pull/136
Patch1: opendkim-2.11.0-comment-separator.patch
# systemd service type=simple
Patch2: opendkim-systemd-service-simple.patch
# https://github.com/trusteddomainproject/OpenDKIM/pull/189
Patch3: opendkim-CVE-2022-48521-fix.patch

# Required for all versions
Requires: lib%{name}%{?_isa} = %{version}-%{release}
BuildRequires: make
BuildRequires: openssl-devel, libtool, pkgconfig, libbsd, libbsd-devel, opendbx-devel, lua-devel
Requires(pre): shadow-utils

%{?systemd_requires}
BuildRequires: systemd
BuildRequires: libdb-devel
# Fedora 35+ and CentOS 9+ changed to libmemcached-awesome
%if 0%{?fedora} >= 35 || 0%{?epel} >= 9
BuildRequires: libmemcached-awesome-devel
%else
BuildRequires: libmemcached-devel
%endif


BuildRequires: sendmail-milter-devel

BuildRequires: openldap-devel

%description
%{upname} allows signing and/or verification of email through an open source
library that implements the DKIM service, plus a milter-based filter
application that can plug in to any milter-aware MTA, including sendmail,
Postfix, or any other MTA that supports the milter protocol.

%package -n %{name}-tools
Summary: An open source DKIM library

%description -n %{name}-tools
This package contains the tools necessary to create artifacts needed
by opendkim.

%package -n lib%{name}
Summary: An open source DKIM library
Obsoletes: %{name}-sysvinit < 2.10.1-5

%description -n lib%{name}
This package contains the library files required for running services built
using libopendkim.

%package -n lib%{name}-devel
Summary: Development files for lib%{name}
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-devel
This package contains the static libraries, headers, and other support files
required for developing applications against libopendkim.

%prep
%autosetup -p1 -n %{upname}-%{full_version}

%build
autoreconf -iv
# Always use system libtool instead of pacakge-provided one to
# properly handle 32 versus 64 bit detection and settings
%define LIBTOOL LIBTOOL=`which libtool`

%configure --with-odbx --with-db --with-libmemcached --with-openldap --enable-query_cache --with-lua

# Remove rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
install -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_sysconfdir}/sysconfig
install -m 0755 contrib/init/redhat/%{name}-default-keygen %{buildroot}%{_sbindir}/%{name}-default-keygen

install -d -m 0755 %{buildroot}%{_unitdir}

# fix service file for rundir
sed -i -e "s:PIDFile=/var/run/opendkim/opendkim.pid:PIDFile=%{_rundir}/opendkim/opendkim.pid:" contrib/systemd/%{name}.service
install -m 0644 contrib/systemd/%{name}.service %{buildroot}%{_unitdir}/%{name}.service

install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{name}.conf

install -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}

mkdir -p %{buildroot}%{_sysconfdir}/%{name}
install -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/%{name}/SigningTable

install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/%{name}/KeyTable

install -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/%{name}/TrustedHosts

cp %{SOURCE6} ./README.fedora

%if %{tmpfiles}
install -p -d %{buildroot}/usr/lib/tmpfiles.d
cat > %{buildroot}/usr/lib/tmpfiles.d/%{name}.conf <<'EOF'
D %{_rundir}/%{name} 0750 %{name} %{name} -
EOF
%endif

rm -r %{buildroot}%{_prefix}/share/doc/%{name}
rm %{buildroot}%{_libdir}/*.a
rm %{buildroot}%{_libdir}/*.la

mkdir -p %{buildroot}%{_localstatedir}/spool/%{name}
mkdir -p %{buildroot}%{_rundir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir %{buildroot}%{_sysconfdir}/%{name}/keys

install -m 0755 stats/%{name}-reportstats %{buildroot}%{_prefix}/sbin/%{name}-reportstats
sed -i 's|^%{bigname}STATSDIR="/var/db/%{name}"|%{bigname}STATSDIR="%{_localstatedir}/spool/%{name}"|g' %{buildroot}%{_prefix}/sbin/%{name}-reportstats
sed -i 's|^%{bigname}DATOWNER="mailnull:mailnull"|%{bigname}DATOWNER="%{name}:%{name}"|g' %{buildroot}%{_prefix}/sbin/%{name}-reportstats

chmod 0644 contrib/convert/convert_keylist.sh

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
	useradd -r -g %{name} -G mail -d %{_rundir}/%{name} -s /sbin/nologin \
	-c "%{upname} Milter" %{name}
exit 0

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service
# For the switchover from initscript to service file
%triggerun -- %{name} < 2.8.0-1
%systemd_post %{name}.service
/sbin/chkconfig --del %{name} >/dev/null 2>&1 || :
%systemd_postun_with_restart %{name}.service


%ldconfig_scriptlets -n libopendkim

%files
%license LICENSE LICENSE.Sendmail
%doc FEATURES KNOWNBUGS RELEASE_NOTES RELEASE_NOTES.Sendmail
%doc contrib/convert/convert_keylist.sh %{name}/*.sample
%doc %{name}/%{name}.conf.simple-verify %{name}/%{name}.conf.simple
%doc %{name}/README contrib/lua/*.lua
%doc README.fedora
%config(noreplace) %{_sysconfdir}/%{name}.conf
%if %{tmpfiles}
%config(noreplace) /usr/lib/tmpfiles.d/%{name}.conf
%endif
%config(noreplace) %attr(0640,%{name},%{name}) %{_sysconfdir}/%{name}/SigningTable
%config(noreplace) %attr(0640,%{name},%{name}) %{_sysconfdir}/%{name}/KeyTable
%config(noreplace) %attr(0640,%{name},%{name}) %{_sysconfdir}/%{name}/TrustedHosts
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_bindir}/miltertest
%{_sbindir}/opendkim
%{_sbindir}/opendkim-reportstats
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_mandir}/man8/miltertest.8.gz
%{_mandir}/man8/opendkim.8.gz
%dir %attr(-,%{name},%{name}) %{_localstatedir}/spool/%{name}
%dir %attr(0750,%{name},%{name}) %{_rundir}/%{name}
%dir %attr(-,root,%{name}) %{_sysconfdir}/%{name}
%dir %attr(0750,root,%{name}) %{_sysconfdir}/%{name}/keys
%attr(0755,root,root) %{_sbindir}/%{name}-default-keygen

%attr(0644,root,root) %{_unitdir}/%{name}.service

%files -n libopendkim
%license LICENSE LICENSE.Sendmail
%doc README
%{_libdir}/lib%{name}.so.*

%files -n opendkim-tools
%license LICENSE LICENSE.Sendmail
%{_mandir}/man8/opendkim-genkey.8.gz
%{_mandir}/man8/opendkim-genzone.8.gz
%{_mandir}/man8/opendkim-testkey.8.gz
%{_mandir}/man8/opendkim-testmsg.8.gz
%{_sbindir}/opendkim-genkey
%{_sbindir}/opendkim-genzone
%{_sbindir}/opendkim-testkey
%{_sbindir}/opendkim-testmsg

%files -n libopendkim-devel
%license LICENSE LICENSE.Sendmail
%doc lib%{name}/docs/*.html
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-0.40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-0.39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-0.38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-0.37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 15 2023 Diego Herrera <dherrera@redhat.com> - 2.11.0-0.36
- Add upstream PR that filters Authentication-Results headers correctly.

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-0.35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Apr 16 2023 Matt Domsch <mdomsch@fedoraproject.org> 2.11.0-0.34
- remove failing systemd protections

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-0.33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep  5 2022 Matt Domsch <mdomsch@fedoraproject.org> 2.11.0-0.32
- fix systemd service type=simple patch to apply cleanly
- Use systemd RuntimeDirectory for socket file

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-0.30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 24 2022 Matt Domsch <mdomsch@fedoraproject.org> 2.11.0-0.29
- Use systemd service type=simple rather than forking, avoids PID race

* Sat Feb 19 2022 Matt Domsch <mdomsch@fedoraproject.org> 2.11.0-0.28
- Make systemd delay a second before checking for the PID file. BZ#2056209

* Sun Jan 23 2022 Matt Domsch <mdomsch@fedoraproject.org> 2.11.0-0.27
- Use libmemcached-awesome-devel for F35+ and EPEL 9+

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-0.26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Matt Domsch <mdomsch@fedoraproject.org> 2.11.0-0.25
- add comment separator upstream PR

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.11.0-0.24
- Rebuilt with OpenSSL 3.0.0

* Sat Jul 31 2021 Matt Domsch <mdomsch@fedoraproject.org> - 2.11.0-0.23
- replace libmemcached-devel with libmemcached-awesome-devel as the former is removed from F35

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-0.22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 19 2021 W. Michael Petullo <mike@flyn.org> - 2.11.0-0.21
- Move management utilities to opendkim-tools
- remove useless INSTALL doc

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.11.0-0.20
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Mon Mar  1 2021 Matt Domsch <mdomsch@fedoraproject.org> - 2.11.0-0.19
- Fix service PIDFile for rundir (Red Hat Bugzilla #1915469)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-0.18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-0.17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Tomas Korbar <tkorbar@redhat.com> - 2.11.0-0.16
- Change location of tmpfiles definiton (#1736767)

* Wed Jun 24 2020 Tomas Korbar <tkorbar@redhat.com> - 2.11.0-0.15
- Change permissions of /var/run/opendkim directory (#1744391)

* Wed Jun 24 2020 Tomas Korbar <tkorbar@redhat.com> - 2.11.0-0.14
- Change ownership of the keys directory to root (#1711713)

* Wed Jun 24 2020 Tomas Korbar <tkorbar@redhat.com> - 2.11.0-0.13
- Change /run/opendkim permissions to group writable
- Improve the patch which adds support for lua
- Credit: mdomsch

* Mon Jun 22 2020 Tomas Korbar <tkorbar@redhat.com> - 2.11.0-0.12
- Rebase to 2.11.0-beta2 version
- Clean specfile and move configuration to their own files

* Fri Apr 24 2020 Tomas Korbar <tkorbar@redhat.com> - 2.11.0-0.11
- Rebuilt with lua support
- Credit: Breno Brand Fernandes brandfbb@gmail.com

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-0.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.11.0-0.6
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Steve Jenkins <steve@stevejenkins.com> - 2.11.0-0.1
- Updated to 2.11.0.Alpha0 upstream source
- Rediffed, combined, and applied patch for SF #35 + #37
- Modernized spec slightly (thanks to EPEL 5 getting a bit more modern)

* Mon Aug 01 2016 Steve Jenkins <steve@stevejenkins.com> - 2.10.3-9
- Changed sendmail-milter-devel BuildRequires to > F25

* Mon Aug 01 2016 Steve Jenkins <steve@stevejenkins.com> - 2.10.3-8
- Updated BuildRequires to sendmail-milter-devel for F25+ (RH Bugzilla #891288)

* Mon Aug 01 2016 Steve Jenkins <steve@stevejenkins.com> - 2.10.3-7
- Added compile-time support for QUERY_CACHE (RH Bugzilla #1361038)

* Fri Jul 22 2016 Steve Jenkins <steve@stevejenkins.com> - 2.10.3-6
- Patched for From: field wrapping issue (SF Ticket #226)

* Wed Jul 20 2016 Steve Jenkins <steve@stevejenkins.com> - 2.10.3-5
- Fixed OpenLDAP support for all targets except EL5 (required version not available)
- Updated spec file to more modern conventions

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 25 2015 Steve Jenkins <steve@stevejenkins.com> - 2.10.3-3
- Added OpenLDAP support for systemd branches in response to RH Bugzilla #1293279

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 12 2015 Steve Jenkins <steve@stevejenkins.com> - 2.10.3-1
- Updated to use newer upstream 2.10.3 source code

* Mon May 11 2015 Steve Jenkins <steve@stevejenkins.com> - 2.10.2-1
- Updated to use newer upstream 2.10.2 source code
- Removed patches for bugs fixed in upstream source
- Included support for systemd macros
- Added deprecated options notice to default configuration file
- Added new options to default configuration file
- Updated README.fedora with additional SQL useage info

* Mon Apr 13 2015 Steve Jenkins <steve@stevejenkins.com> - 2.10.1-13
- Obsoleted sysvinit subpackage via libopendkim subpackage
- Added more macros
- Updated README.fedora

* Mon Apr 06 2015 Steve Jenkins <steve@stevejenkins.com> - 2.10.1-12
- BuildRequires opendbx-devel instead of opendbx
- Fixed typo in configure flag

* Mon Apr 06 2015 Steve Jenkins <steve@stevejenkins.com> - 2.10.1-11
- All branches now require opendbx
- All branches now configure with --with-obdx flag
- Added comments to README.Fedora to address Bug #1209009
- Cleaned up some spacing

* Fri Apr 03 2015 Steve Jenkins <steve@stevejenkins.com> - 2.10.1-10
- policycoreutils now only required for EL5

* Thu Apr 02 2015 Steve Jenkins <steve@stevejenkins.com> - 2.10.1-9
- policycoreutils* now only required for Fedora and EL6+
- Added --with-obdx configure support for Fedora builds
- Changed a few macros
- Added additional %%license support

* Sun Mar 29 2015 Steve Jenkins <steve@stevejenkins.com> - 2.10.1-8
- removed unecessary Requires packages
- moved libbsd back to BuildRequires
- removed unecessary %%defattr
- added support for %%license in place of %%doc
- Changed some %%{name} macro usages

* Sat Mar 28 2015 Steve Jenkins <steve@stevejenkins.com> - 2.10.1-7
- added %%{?_isa} to Requires where necessary
- added sendmail-milter to Requires
- added libtool to BuildRequires
- moved libbsd from BuildRequires to Requires
- added policycoreutils and policycoreutils-python to Requires(post)

* Sat Mar 28 2015 Steve Jenkins <steve@stevejenkins.com> - 2.10.1-6
- Remove global _pkgdocdir variable
- Use defaultdocdir variable in default config file
- Setting permissions special mode bit explicitly in all cases for consistency
- Change /var/run/opendkim permissions to group writable for Bug #1120080

* Wed Mar 25 2015 Steve Jenkins <steve@stevejenkins.com> - 2.10.1-5
- Combined systemd and SysV spec files using conditionals
- Drop sysvinit subpackage completely

* Tue Mar 24 2015 Steve Jenkins <steve@stevejenkins.com> - 2.10.1-4
- Fixed typo in Group name
- Added updated libtool definition
- Additional comments in spec file
- Patch SysV initscript to stop default key generation on startup

* Thu Mar 05 2015 Adam Jackson <ajax@redhat.com> 2.10.1-3
- Drop sysvinit subpackage from F23+

* Tue Mar 03 2015 Steve Jenkins <steve@stevejenkins.com> - 2.10.1-2
- Added IPv6 ::1 support to TrustedHosts (RH Bugzilla #1049204)

* Tue Mar 03 2015 Steve Jenkins <steve@stevejenkins.com> - 2.10.1-1
- Updated to use newer upstream 2.10.1 source code

* Tue Dec 09 2014 Steve Jenkins <steve@stevejenkins.com> - 2.10.0-1
- Updated to use newer upstream 2.10.0 source code
- Removed unbound compile option due to orphaned upstream dependency
- Removed AUTOCREATE_DKIM_KEYS option
- Added README.fedora with basic key generation and config instructions

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 04 2014 Steve Jenkins <steve@stevejenkins.com> - 2.9.2-2
- Change file ownerships/permissions to fix https://bugzilla.redhat.com/show_bug.cgi?id=891292
- Default keys no longer created on startup. Privileged user must run opendkim-default-keygen or create manually (after install)

* Wed Jul 30 2014 Steve Jenkins <steve@stevejenkins.com> - 2.9.2-1
- Updated to use newer upstream 2.9.2 source code
- Fixed invalid date in changelog

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 18 2013 Steve Jenkins <steve stevejenkins com> - 2.9.0-2
- Patch adds user and group to systemd service file (Thx jcosta@redhat.com)
- Changed default ownership of /etc/opendkim/keys directory to opendkim user

* Wed Dec 18 2013 Steve Jenkins <steve stevejenkins com> - 2.9.0-1
- Updated to use newer upstream 2.9.0 source code
- Added libbsd-devel to Build Requires
- Removed listrl references from libopendkim files section (handled by libbsd-devel)

* Sun Nov 3 2013 Steve Jenkins <steve stevejenkins com> - 2.8.4-4
- Rebuild of all release packages to sync version numbers

* Sun Nov 3 2013 Ville Skytta ville.skytta@iki.fi> - 2.8.4-3
- Fix path to docs in sample config when doc dir is unversioned (#993997).

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 2.8.4-2
- Perl 5.18 rebuild

* Tue Jul 23 2013 Steve Jenkins <steve stevejenkins com> 2.8.4-1
- Updated to use newer upstream 2.8.4 source code
- Added libbsd build requirement

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 2.8.3-3
- Perl 5.18 rebuild

* Fri May 17 2013 Steve Jenkins <steve stevejenkins com> 2.8.3-2
- Removed libmemcached support from SysV version (requires > v0.36)

* Sun May 12 2013 Steve Jenkins <steve stevejenkins com> 2.8.3-1
- Updated to use newer upstream 2.8.3 source code
- Added unbound, libmcached, and db support on configure

* Mon Apr 29 2013 Steve Jenkins <steve stevejenkins com> 2.8.2-1
- Updated to use newer upstream 2.8.2 source code

* Tue Mar 19 2013 Steve Jenkins <steve stevejenkins com> 2.8.1-1
- Updated to use newer upstream 2.8.1 source code
- Removed patches for bugs fixed in upstream source

* Wed Feb 27 2013 Steve Jenkins <steve stevejenkins com> 2.8.0-4
- Added patch from upstream to fix libdb compatibility issues

* Tue Feb 26 2013 Steve Jenkins <steve stevejenkins com> 2.8.0-3
- Split into two spec files: systemd (F17+) and SysV (EL5-6)
- Removed leading / from unitdir variables
- Removed commented source lines
- Created comment sections for easy switching between systemd and SysV

* Mon Feb 25 2013 Steve Jenkins <steve stevejenkins com> 2.8.0-2
- Added / in front of unitdir variables

* Thu Feb 21 2013 Steve Jenkins <steve stevejenkins com> 2.8.0-1
- Happy Birthday to me! :)
- Updated to use newer upstream 2.8.0 source code
- Migration from SysV initscript to systemd unit file
- Added systemd build requirement
- Edited comments in default configuration files
- Changed default Canonicalization to relaxed/relaxed in config file
- Changed default values in EnvironmentFile
- Moved program startup options into EnvironmentFile
- Moved default key check and generation on startup to external script
- Removed AutoRestart directives from default config (systemd will handle)
- Incorporated additional variable names throughout spec file
- Added support for new opendkim-sysvinit package for legacy SysV systems

* Tue Jan 08 2013 Steve Jenkins <steve stevejenkins com> 2.7.4-1
- Updated to use newer upstream 2.7.4 source code
- Added AutoRestart and AutoRestartRate directives to default configuration
- Changed default SigningTable directive to include refile: for wildcard support

* Tue Dec 04 2012 Steve Jenkins <steve stevejenkins com> 2.7.3-2
- Set /etc/opendkim/keys default permissions to 750 (Thanks patrick at puzzled.xs4al.nl)

* Thu Nov 29 2012 Steve Jenkins <steve stevejenkins com> 2.7.3-1
- Updated to use newer upstream 2.7.3 source code

* Mon Nov 19 2012 Steve Jenkins <steve stevejenkins com> 2.7.2-1
- Updated to use newer upstream 2.7.2 source code

* Tue Oct 30 2012 Steve Jenkins <steve stevejenkins com> 2.7.1-1
- Updated to use newer upstream 2.7.1 source code
- Updated to reflect source code move of files from /usr/bin to /usr/sbin
- Removed --enable-stats configure option to avoid additional dependencies
- Added support for strlcat() and strlcopy() previously in libopendkim
- Added new MinimumKeyBits configuration option with default of 1024

* Wed Aug 22 2012 Steve Jenkins <steve stevejenkins com> 2.6.7-1
- Updated to use newer upstream 2.6.7 source code
- Removed patches from 2.4.2 which were incorporated upstream
- Updated install directory of opendkim-reportstats

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 22 2011 Steve Jenkins <steve stevejenkins com> 2.4.2-5
- Changed ownernship of directories to comply with selinux-policy
- Added default KeyTable and TrustedHosts files
- Added config(noreplace) to sysconfig file

* Mon Sep 19 2011 Steve Jenkins <steve stevejenkins com> 2.4.2-4
- Use Fedora standard method to fix pkg supplied libtool (Todd Lyons)
- Updated Summary and Description
- Fixed default stats file location in sample config file
- Install opendkim-reportstats and README.opendkim-reportstats
- Changed default stop priority in init script
- Added example SigningTable
- Added sysconfig support for AUTOCREATE_DKIM_KEYS, DKIM_SELECTOR, DKIM_KEYDIR
- Enabled SysLogSuccess and LogWhy by default

* Mon Aug 22 2011 Steve Jenkins <steve stevejenkins com> 2.4.2-3
- Mad props to Matt Domsch for sponsoring and providing feedback
- Removed {?OSshort} variable in Release: header
- Removed explicit Requires: in header
- Added support for tmpfiles.d
- Replaced opendkim with {name} variable throughout
- Replaced RPM_BUILD_ROOT with {buildroot}
- Moved changelog to bottom of file
- Removed "All Rights Reserved" from top of spec file
- Removed Prefix: line in header
- Pointed Source*: to the upstream tarballs
- Changed BuildRoot: format
- Changed makeinstall to make install
- Moved creation of working dirs to install
- Moved ownership of working dirs to files
- Moved user and group creation to pre
- Moved permissions setting to files with attr
- Created directory for user keys
- Removed testing for working directories; mkdir -p will suffice
- Revised Summary
- Removed static libraries from -devel package
- Removed extra spaces
- Removed usermod command to add opendkim to mail group
- Removed echo in post
- General tidying up
- Moved INSTALL readme information into patch
- Removed CPPFLAGS from configure
- Added _smp_mflags to make
- Changed which README from source is written to doc directory
- Added licenses to all subpackages
- Changed default runlevel in init script

* Tue Aug 16 2011  Steve Jenkins <steve stevejenkins com> 2.4.2-2
- Added -q to setup -a 1
- Added x86_64 libtool support (Mad props to Todd Lyons)
- Added {?dist} variable support in Release: header
- Changed Statistics storage location
- Statistics option now commented in opendkim.conf by default
- Check for existing private key before attempting to build keys
- Check for domain name before attempting to build keys

* Mon Aug 15 2011  Steve Jenkins <steve stevejenkins com> 2.4.2-1
- Initial Packaging of opendkim
