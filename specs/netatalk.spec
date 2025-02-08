Name:              netatalk
Epoch:             5
Version:           4.0.8
Release:           3%{?dist}
Summary:           Open Source Apple Filing Protocol(AFP) File Server
# Automatically converted from old format: GPL+ and GPLv2 and GPLv2+ and LGPLv2+ and BSD and FSFUL and MIT - review is highly recommended.
License:           GPL-1.0-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-BSD AND FSFUL AND LicenseRef-Callaway-MIT
# Project is also mirrored at https://github.com/Netatalk/Netatalk
URL:               http://netatalk.sourceforge.net
Source0:           https://download.sourceforge.net/netatalk/netatalk-%{version}.tar.xz
Source1:           netatalk.pam-system-auth

# Per i686 leaf package policy 
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:     avahi-devel
BuildRequires:     bison
BuildRequires:     coreutils
BuildRequires:     cracklib-devel
BuildRequires:     dbus-devel
BuildRequires:     dbus-glib-devel
BuildRequires:     docbook-style-xsl
BuildRequires:     findutils
BuildRequires:     flex
BuildRequires:     gcc
BuildRequires:     grep
BuildRequires:     krb5-devel
BuildRequires:     libacl-devel
BuildRequires:     libattr-devel
BuildRequires:     libdb-devel
BuildRequires:     libevent-devel
BuildRequires:     libgcrypt-devel
BuildRequires:     libretls-devel
BuildRequires:     libtalloc-devel
BuildRequires:     libtdb-devel
BuildRequires:     libxcrypt-devel
BuildRequires:     libxslt
BuildRequires:     mariadb-connector-c-devel
BuildRequires:     meson
BuildRequires:     openldap-devel
BuildRequires:     openssl-devel
BuildRequires:     pam-devel
BuildRequires:     perl-generators
BuildRequires:     perl-interpreter
BuildRequires:     procps
BuildRequires:     procps-ng
BuildRequires:     quota-devel
BuildRequires:     rpm
BuildRequires:     sed
BuildRequires:     systemd
BuildRequires:     systemtap-sdt-devel
BuildRequires:     localsearch
BuildRequires:     tinysparql-devel
BuildRequires:     cups-devel

Requires:     dconf
Requires:     python3-dbus
%{?systemd_requires}

# Netatalk /usr/bin/dbd binary conflicts with binary of the same name in jday package
Conflicts: jday

%description
Netatalk is a freely-available Open Source AFP file server. A *NIX/*BSD
system running Netatalk is capable of serving many Macintosh clients
simultaneously as an AppleShare file server (AFP).

In addition to the AFP file server daemon, the following utility programs
are also included:
 * ad          - AppleDouble file utility suite
 * afpldaptest - validate Netatalk LDAP parameters
 * afppasswd   - RandNum UAM password management
 * afpstats    - inquire AFP server usage stats
 * apple_dump  - dump AppleSingle/AppleDouble metadata
 * asip-status - inquire AFP server capabilities
 * dbd         - CNID database maintenance
 * macusers    - list connected AFP server users

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%package        afptest
Summary:        Afp test suite for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    afptest
Apple Filing Protocol service test tools.

This package contains the following AFP functional test runners,
benchmarks, and supporting tools:
 * afp_lantest   - AFP benchmark akin to HELIOS LanTest
 * afp_logintest - test authentication over DSI
 * afp_spectest  - AFP specification functional test suite
 * afp_speedtest - AFP read/write/copy benchmark
 * afparg        - AFP CLI client

%if 0%{?fedora}
# The following subpackage needs the appletalk module, which is part of kernel-modules-extra
# Unfortunately, the appletalk module is only available in Fedora
%package        appletalk
Summary:        Appletalk support for classic macintoshes
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       kernel-modules-extra

%description    appletalk
This package contains Netatalk's services and tools for networking
with very old Macs and Apple IIs.

This package contains the daemon and utility programs
for the Netatalk AppleTalk network suite, which can be used
with the Netatalk AFP file server, and other services.

In addition to the atalkd network management daemon,
the following utility programs are installed:
 * aecho      - send AppleTalk Echo Protocol pings
 * getzones   - list available AppleTalk zones
 * nbplkup    - list registered AppleTalk entities
 * nbprgstr   - register an AppleTalk entity
 * nbpunrgstr - release a registered AppleTalk entity
 * a2boot     - allows you to boot an Apple II over the network
                from an AFP volume
 * macipgw    - MacIP gateway which enables pre-TCP/IP Macs to browse the web
                and use other TCP/IP resources
 * papd       - allows Mac OS and Apple II clients to print to modern
                AirPrint / CUPS enabled printers
 * pap        - print from the host to a LocalTalk printer
 * papstatus  - inquire the status of a LocalTalk printer
 * timelord   - time server for Mac OS and Apple II
%endif

%package doc
Summary:        HTML Documentation for %{name}
BuildArch:      noarch

%description doc
Netatalk is a freely-available Open Source AFP file server. A *NIX/*BSD
system running Netatalk is capable of serving many Macintosh clients
simultaneously as an AppleShare file server (AFP).

This package contains the HTML documentation for %{name}.

%prep
%autosetup -p 1

# Don't build the japanese docs and put the english docs into a subfolder
sed -i 's\install: true\install: false\' doc/ja/manual/meson.build
sed -i 's\doc/netatalk\doc/netatalk/htmldoc\' doc/manual/meson.build

# Set RuntimeDirectory in the service file rather than use a tmpfiles.d config
sed -E -i 's|^(ExecStart=.*)|\1\nRuntimeDirectory=lock/netatalk|' distrib/initscripts/systemd.netatalk.service.in

%build
%meson \
        --localstatedir=%{_localstatedir}/lib                                  \
        -Ddefault_library=shared                                               \
        -Dwith-manual=local                                                    \
        -Dwith-rpath=false                                                     \
        -Dwith-overwrite=true                                                  \
        -Dwith-lockfile-path=%{_rundir}/lock/netatalk/netatalk                 \
        -Dwith-tcp-wrappers=false                                              \
        -Dwith-dbus-sysconf-path=%{_sysconfdir}/dbus-1/system.d                \
        -Dwith-pkgconfdir-path=%{_sysconfdir}/netatalk                         \
        -Dwith-init-style=systemd                                              \
        -Dwith-init-hooks=false                                                \
        -Dwith-uams-path=%{_libdir}/netatalk                                   \
        -Dwith-cups=true                                                       \
        -Dwith-tests=true                                                      \
        -Dwith-testsuite=true                                                  \
        %{?fedora:-Dwith-appletalk=true}                                       \

%meson_build

%install
%meson_install

# Use specific pam conf.
install -Dpm644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/netatalk

# Bundled pam config gets installed into non-standard folder. 
# Remove the bundled pam config and it parent folders as we supply our own pam config
rm -rf %{buildroot}%{_prefix}%{_sysconfdir}

# make sure all static libraries are deleted
find %{buildroot} \( -name '*.la' -o -name '*.a' \) -type f -delete -print

%check
%meson_test

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%if 0%{?fedora}
%post appletalk
%systemd_post a2boot.service atalkd.service macipgw.service papd.service timelord.service

%preun appletalk
%systemd_preun a2boot.service atalkd.service macipgw.service papd.service timelord.service

%postun appletalk
%systemd_postun_with_restart a2boot.service atalkd.service macipgw.service papd.service timelord.service
%endif

%files
%license COPYING COPYRIGHT
%doc CONTRIBUTORS NEWS INSTALL.md README.md SECURITY.md

%dir %{_sysconfdir}/netatalk
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/netatalk-dbus.conf
%config(noreplace) %{_sysconfdir}/netatalk/afp.conf
%config(noreplace) %{_sysconfdir}/netatalk/dbus-session.conf
%config(noreplace) %{_sysconfdir}/netatalk/extmap.conf
%config(noreplace) %{_sysconfdir}/pam.d/netatalk

%{_sbindir}/afpd
%{_sbindir}/cnid_dbd
%{_sbindir}/cnid_metad
%{_sbindir}/netatalk

%{_bindir}/ad
%{_bindir}/afpldaptest
%{_bindir}/afppasswd
%{_bindir}/afpstats
%{_bindir}/apple_dump
%{_bindir}/asip-status
%{_bindir}/dbd
%{_bindir}/macusers

%dir %{_libdir}/netatalk
%{_libdir}/netatalk/uams_*.so
%{_libdir}/libatalk.so.19{,.*}

%{_mandir}/man1/ad.1*
%{_mandir}/man1/afpldaptest.1*
%{_mandir}/man1/afppasswd.1*
%{_mandir}/man1/afpstats.1*
%{_mandir}/man1/apple_dump.1*
%{_mandir}/man1/asip-status.1*
%{_mandir}/man1/dbd.1*
%{_mandir}/man1/macusers.1*

%{_mandir}/man5/afp.conf.5*
%{_mandir}/man5/afp_signature.conf.5*
%{_mandir}/man5/afp_voluuid.conf.5*
%{_mandir}/man5/extmap.conf.5*

%{_mandir}/man8/afpd.8*
%{_mandir}/man8/cnid_dbd.8*
%{_mandir}/man8/cnid_metad.8*
%{_mandir}/man8/netatalk.8*

%{_unitdir}/netatalk.service

%{_localstatedir}/lib/netatalk

%files devel
%doc %{_pkgdocdir}/DEVELOPER
%dir %{_includedir}/atalk
%{_includedir}/atalk/*.h
%{_libdir}/libatalk.so

%if 0%{?fedora}
%dir %{_includedir}/netatalk
%{_includedir}/netatalk/*.h
%endif

%{_mandir}/man3/atalk_aton.3*
%{_mandir}/man3/nbp_name.3*

%{_mandir}/man4/atalk.4*

%files afptest
%license test/testsuite/COPYING
%doc test/testsuite/README
%{_bindir}/afp_lantest
%{_bindir}/afp_logintest
%{_bindir}/afp_spectest
%{_bindir}/afp_speedtest
%{_bindir}/afparg

%dir %{_datarootdir}/netatalk
%{_datarootdir}/netatalk/test-data/test431_data

%{_mandir}/man1/afp_lantest.1*
%{_mandir}/man1/afp_logintest.1*
%{_mandir}/man1/afp_spectest.1*
%{_mandir}/man1/afp_speedtest.1*
%{_mandir}/man1/afptest.1*
%{_mandir}/man1/afparg.1*

%if 0%{?fedora}
%files appletalk
%doc %{_pkgdocdir}/README.AppleTalk
%config(noreplace) %{_sysconfdir}/netatalk/atalkd.conf
%config(noreplace) %{_sysconfdir}/netatalk/papd.conf

%{_sbindir}/a2boot
%{_sbindir}/atalkd
%{_sbindir}/macipgw
%{_sbindir}/papd
%{_sbindir}/timelord

%{_bindir}/aecho
%{_bindir}/getzones
%{_bindir}/nbplkup
%{_bindir}/nbprgstr
%{_bindir}/nbpunrgstr
%{_bindir}/pap
%{_bindir}/papstatus

%{_mandir}/man1/aecho.1*
%{_mandir}/man1/getzones.1*
%{_mandir}/man1/nbplkup.1*
%{_mandir}/man1/nbp.1*
%{_mandir}/man1/nbprgstr.1*
%{_mandir}/man1/nbpunrgstr.1*
%{_mandir}/man1/pap.1*

%{_mandir}/man5/atalkd.conf.5*
%{_mandir}/man5/papd.conf.5*

%{_mandir}/man8/a2boot.8*
%{_mandir}/man8/atalkd.8*
%{_mandir}/man8/macipgw.8*
%{_mandir}/man8/papd.8*
%{_mandir}/man8/papstatus.8*
%{_mandir}/man8/timelord.8*

%{_unitdir}/a2boot.service
%{_unitdir}/atalkd.service
%{_unitdir}/macipgw.service
%{_unitdir}/papd.service
%{_unitdir}/timelord.service
%endif

%files doc
%license COPYING COPYRIGHT
%doc %{_pkgdocdir}/htmldocs

%changelog
* Thu Feb 06 2025 Adam Williamson <awilliam@redhat.com> - 5:4.0.8-3
- Update dependencies for rename of tracker to tinysparql

* Sat Feb 01 2025 Björn Esser <besser82@fedoraproject.org>
- Add explicit BR: libxcrypt-devel

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5:4.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 30 2024 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:4.0.8-1
- 4.0.8 release
- custom docbook xsl stylesheet path no longer needed

* Fri Nov 15 2024 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:4.0.6-1
- 4.0.6 release
- only build appletalk documentation for fedora

* Tue Nov 12 2024 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:4.0.5-2
- improve descriptions of each subpackage
- only build appletalk subpackage for fedora

* Mon Nov 11 2024 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:4.0.5-1
- 4.0.5 release
- new afptest, appletalk, and doc subpackages

* Sun Sep 22 2024 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.2.9-2
- Revert license tag caused by incorrect rpmlint output

* Sun Sep 15 2024 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.2.9-1
- 3.2.9 release
- adjust License per rpmlint
- use systemd RuntimeDirectory rather than tmpfiles.d config

* Thu Sep 05 2024 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.2.7-4
- Add wolfssl build option with default off

* Wed Sep 04 2024 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.2.7-3
- fix lockfile path

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 5:3.2.7-2
- convert license to SPDX

* Mon Aug 26 2024 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.2.7-1
- 3.2.7 release RHBZ#2304010
- Build against wolfssl

* Fri Aug 02 2024 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.2.5-1
- remove support for el7 and el8
- replace autotools with meson
- 3.2.5 release

* Mon Jul 15 2024 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.2.3-1
- 3.2.3 release

* Thu Jul 11 2024 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.2.2-2
- Exclude i686 builds per Fedora leaf package policy

* Mon Jul 08 2024 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.2.2-1
- 3.2.2 release

* Sun Jun 30 2024 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.2.1-1
- 3.2.1 release, fixes CVE-2024-38439, CVE-2024-38440, and CVE-2024-38441

* Wed Jun 05 2024 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.2.0-1
- 3.2.0 release

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5:3.1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5:3.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 05 2023 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.1.18-1
- 3.1.18 release
- Fixes CVE-2022-22995

* Thu Sep 28 2023 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.1.17-2
- buildrequire mariadb-connector-c-devel for all but el7
- minor changes to other specfile conditionals

* Sun Sep 17 2023 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.1.17-1
- 3.1.17 release
- Fixes CVE-2023-42464
- upstream removed bundled libevent back in 3.1.13 release

* Tue Sep 12 2023 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.1.16-1
- autoconf, automake, and libtool are no longer required
- force gnu99 cflag on el7 builds
- 3.1.16 release

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5:3.1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 15 2023 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.1.15-1
- 3.1.15 release

* Sun Apr  9 2023 Florian Weimer <fweimer@redhat.com> - 5:3.1.14-4
- C99 compatibility fixes

* Mon Apr 03 2023 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.1.14-3
- fix CVE-2022-45188

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5:3.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.1.14-1
- 3.1.14 release

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5:3.1.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 5:3.1.13-4
- Perl 5.36 rebuild

* Tue May 17 2022 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.1.13-3
- apply latest pr174 as possible fix for bz 2074586

* Fri Apr 15 2022 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.1.13-2
- possible fix for bz 2074586

* Tue Mar 22 2022 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.1.13-1
- 3.1.13 release

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5:3.1.12-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 5:3.1.12-27
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5:3.1.12-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 5:3.1.12-25
- Perl 5.34 rebuild

* Wed May 19 2021 Michal Josef Å paÄek <mspacek@redhat.com> - 5:3.1.12-24
- Rewrite deprecated perl dependency (IO::Socket::INET6)

* Sat Mar 13 2021 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.1.12-23
- build against tracker3 on fedora 

* Tue Mar 02 2021 Zbigniew JÄ™drzejewski-Szmek <zbyszek@in.waw.pl> - 5:3.1.12-22
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5:3.1.12-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 2020 Zbigniew JÄ™drzejewski-Szmek <zbyszek@in.waw.pl> - 5:3.1.12-20
- Rebuilt for libevent 2.1.12

* Fri Aug 21 2020 Jeff Law <law@redhat.com> - 5:3.1.12-19
- Re-enable LTO

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5:3.1.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Jeff Law <law@redhat.com> - 5:3.1.12-17
- Disable LTO

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5:3.1.12-16
- Perl 5.32 re-rebuild of bootstrapped packages

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5:3.1.12-15
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5:3.1.12-14
- remove pam_console dependency RHBZ 1822216
- Exclude aarch64 and s390x on el8 https://pagure.io/epel/issue/87

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5:3.1.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.1.12-12
- BZ1793912 fix multiple definition of invalid_dircache_entries

* Tue Oct 22 2019 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.1.12-11
- conflicts with jday

* Tue Oct 22 2019 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.1.12-10
- build against mariadb-devel, rather than mysql-devel
- add with_python2 global
- remove trailing slash from pkgconfdir

* Mon Oct 21 2019 Miro HronÄok <mhroncok@redhat.com> - 5:3.1.12-9
- Require Python 3 version of dbus-python on Fedora

* Sun Oct 06 2019 Miro HronÄok <mhroncok@redhat.com> - 5:3.1.12-8
- Switch back to Python 3 on Fedora

* Sun Oct 06 2019 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.1.12-7
- Set the following global vars correctly for el8: 
- without_tcp_wrappers, ldconfig, python_bin

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5:3.1.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 5:3.1.12-5
- Perl 5.30 rebuild

* Sun Mar 10 2019 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.1.12-4
- use python2 binary for el7 compat, use python3 binary everywhere else

* Sun Mar 03 2019 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.1.12-3
- execstartpre instead of runtimedirectory in service file for el7 compat

* Sun Feb 03 2019 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.1.12-2
- fix license
- buildrequire perl-generators, require perl version
- fix epoch

* Wed Jan 09 2019 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.1.12-1
- Netatalk 3.1.12 release

* Wed Dec 12 2018 Andrew Bauer <zonexpertconsulting@outlook.com> - 5:3.1.11-2
- Refactor specfile
- remove sysv init support
- let systemd manage lockfile folder
- call ldconfig only for el7
- patch afpstats for python3

* Wed Oct 31 2018 HAT <hat@fa2.so-net.ne.jp> - 5:3.1.11-1.4
- always buildrequres gcc

* Tue Apr 03 2018 HAT <hat@fa2.so-net.ne.jp> - 5:3.1.11-1.3
- always buildrequres perl-interpreter

* Thu Mar 22 2018 HAT <hat@fa2.so-net.ne.jp> - 5:3.1.11-1.2
- If Fedora >=28, don't use tcp_wrappers
- If Fedora >=28, buildrequres perl-interpreter

* Tue Mar 20 2018 HAT <hat@fa2.so-net.ne.jp> - 5:3.1.11-1.1
- pam_ck_connector.so isn't always installed (RHBZ#1246465)
- require dconf package (RHBZ#1248157)
- require perl-IO-Socket-INET6 for asip-status.pl script
- define with_ldap (RHBZ#1249403)
- The UAM path should be netatalk, not atalk (RHBZ#1249404)
- fix multilib conflict of tracker-devel (SF BUG#637)
- If el6, use "make %%{?_smp_mflags}", not "%%make_build" macro
- If el6, disable tracker
- If el6, use db4-devel, not libdb-devel
- If el6, use bundled libevent2, not libevent1 package
- If el6, use procps, not procps-ng

* Fri Dec 01 2017 Ryan Breaker <ryan@breaker.rocks> - 3.1.11-1
- Revival of package from abandonment.
- Update to 3.1.11
- Remove patch previously applied to 3.1.7, is now applied to upstream of project

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5:3.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 23 2015 Ralf Corsï¾ƒï½©pius <corsepiu@fedoraproject.org> - 5:3.1.7-1
- Increment epoch. Missed to reset %%release in previous change.

* Thu Jul 23 2015 Ralf Corsï¾ƒï½©pius <corsepiu@fedoraproject.org> - 4:3.1.7-7
- Upstream update to 3.1.7 (RHBZ#1134783).
- Remove doc from *-devel.
- Add %%license.
- Update %%description from
  http://www003.upp.so-net.ne.jp/hat/files/netatalk-3.1.7-0.1.fc22.src.rpm.

* Thu Jul 23 2015 Ralf Corsï¾ƒï½©pius <corsepiu@fedoraproject.org> - 4:3.1.3-4
- Address F23FTBFS, RHBZ#1239711:
  - Add netatalk-3.1.7-autotools.patch (Fix RHBZ#1160730). 
  - Remove ICDumpSuffixMap, netatalk-2.0.2-uams_no_pie.patch,
    netatalk-2.0.4-extern_ucreator.patch, netatalk-2.2.3-libdb4.patch,
    netatalk-2.2.3-sigterm.patch (Unused)
  - Add netatalk-3.0.1-basedir.patch.
  - Mark %%{_sysconfdir}/dbus-1/system.d/netatalk-dbus.conf noreplace.
  - Fix permissions on include-files.
  - Remove duplicate %%global with_mysql.
  - Enable dbus.
  - Add missing "fi" in %%preun.
  - Run /sbin/ldconfig in %%postun, %%preun.
  - Reflect /var/lock/netatalk is hard-coded into the sources.
  - Set --localstatedir=/var/lib (/var/netatalk violates FHS).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:3.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 04 2014 Christopher Meng <rpm@cicku.me> - 4:3.1.3-1
- Update to 3.1.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:2.2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Tomï¾ƒï½¡ï¾…ï½¡ Mrï¾ƒï½¡z <tmraz@redhat.com> - 4:2.2.3-10
- Rebuild for new libgcrypt

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:2.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 4:2.2.3-8
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:2.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 23 2012 Lukï¾ƒï½¡ï¾…ï½¡ Nykrï¾ƒï½½n <lnykryn@redhat.com> - 4:2.2.3-6
- Scriptlets replaced with new systemd macros

* Fri Jul 27 2012 Lukï¾ƒï½¡ï¾…ï½¡ Nykrï¾ƒï½½n <lnykryn@redhat.com> - 4:2.2.3-5
- fixed build issue on f18

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:2.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Lukï¾ƒï½¡ï¾…ï½¡ Nykrï¾ƒï½½n <lnykryn@redhat.com> - 4:2.2.3-3
- fixes: #835714 - Netatalk 2.2.2-1: Unable to unmount afpd share from OSX
  client, crashes Finder netatalk-2.2.2-1

* Tue Jun 12 2012 Lukï¾ƒï½¡ï¾…ï½¡ Nykrï¾ƒï½½n <lnykryn@redhat.com> - 4:2.2.3-2
- fixes: #831001 - netatalk pam configuration has invalid entry

* Mon Jun 04 2012 Lukas Nykryn <lnykryn@redhat.com> 4:2.2.3-1
- fixes #828205 - update to latest upstream netatalk-2.2.3

* Mon Jan 16 2012 Jiri Skala <jskala@redhat.com> - 4:2.2.2-1
- fixes #782049 - update to latest upstream netatalk-2.2.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 29 2011 Jiri Skala <jskala@redhat.com> - 4:2.2.1-2
- fixes #501144 - updated and redirected pam config

* Tue Nov 29 2011 Jiri Skala <jskala@redhat.com> - 4:2.2.1-1
- update to latest upstream netatalk-2.2.1

* Fri Aug 19 2011 Jiri Skala <jskala@redhat.com> - 4:2.2.0-4
- fixes #726928 - BuildRequires: avahi-devel libacl-devel openldap-devel

* Fri Aug 05 2011 Jiri Skala <jskala@redhat.com> - 4:2.2.0-3
- fixed missing epoch in sysvinit subpackage and triggers

* Thu Aug 04 2011 Jiri Skala <jskala@redhat.com> - 4:2.2.0-2
- fixes #714448 - systemd-service
- moves SysV initscript to subpackage

* Fri Jul 29 2011 Jiri Skala <jskala@redhat.com> - 4:2.2.0-1
- update to latest upstream netatalk-2.2.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 03 2011 Jiri Skala <jskala@redhat.com> - 4:2.1.5-1
- updated to latest upstream version netatalk-2.1.5

* Mon Oct 18 2010 Jiri Skala <jskala@redhat.com> - 4:2.1.4-1
- updated to latest upstream version

* Mon Jul 12 2010 Jiri Skala <jskala@redhat.com> - 4:2.1.3-1
- updated to latest upstream version
- added license texts to devel subpackage

* Wed Jun 30 2010 Jiri Skala <jskala@redhat.com> - 4:2.1.2-1
- updated to latest upstream version

* Fri May 28 2010 Jiri Skala <jskala@redhat.com> - 4:2.1.1-1
- updated to latest upstream version
- fixes #594999 - Summary and Description are old-fashioned
- renamed initscript
- initscript modified to be POSIX compliant

* Wed May 12 2010 Jiri Skala <jskala@redhat.com> - 4:2.1-1
- updated to latest upstream version

* Tue Nov 24 2009 Jiri Skala <jskala@redhat.com> - 4:2.0.5-2
- oops forgot upload new sources => shifted release number

* Tue Nov 24 2009 Jiri Skala <jskala@redhat.com> - 4:2.0.5-1
- updated to latest upstream version

* Mon Nov 23 2009 Jiri Skala <jskala@redhat.com> - 4:2.0.4-5
- added BuildRequires: ... libgcrypt-devel
- removed outdated atalk.init

* Tue Sep 15 2009 Jiri Skala <jskala@redhat.com> - 4:2.0.4-4
- fixed #473943

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 4:2.0.4-3
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Jiri Skala <jskala@redhat.com> - 4:2.0.4-1
- updated to latest upstream version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:2.0.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Jiri Skala <jskala@redhat.com> -4:2.0.3-26
- Resolves #480641 - CVE-2008-5718 netatalk: papd command injection vulnerability

* Tue Jan 27 2009 Jiri Skala <jskala@redhat.com> -4:2.0.3-25
- fixed epoch in the subpackage requires

* Fri Jan 23 2009 Jiri Skala <jskala@redhat.com> -4:2.0.3-24
- fix #473186 conflict timeout with coreutils

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 4:2.0.3-23
- rebuild with new openssl

* Wed Dec 03 2008 Jiri Skala <jskala@redhat.com> -4:2.0.3-22
- fix #473939 netatalk-2.0.3-21.fc10 disable quota

* Mon Oct 13 2008 Jiri Skala <jskala@redhat.com> - 4:2.0.3-21
- fix #465050 - FTBFS netatalk-2.0.3-19 - regenerated patches

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4:2.0.3-20
- fix license tag

* Thu Mar 06 2008 Martin Nagy <mnagy@redhat.com> - 4:2.0.3-19
- fix chmod o+x (#225085)
- increase the maximum number of cnid_dbd processes to 512 (#232805)
- papd now writes debugging output to stderr when invoked with -d (#150021)
- fix multiarch conflict for netatalk-devel (#342681)

* Mon Feb 25 2008 Martin Nagy <mnagy@redhat.com> - 4:2.0.3-18
- make init script LSB compliant (#246993)

* Mon Feb 25 2008 Martin Nagy <mnagy@redhat.com> - 4:2.0.3-17
- fix unowned directories (#233889)

* Mon Feb 11 2008 Martin Nagy <mnagy@redhat.com> - 4:2.0.3-16
- rebuild for gcc-4.3

* Tue Dec 04 2007 Martin Nagy <mnagy@redhat.com> - 4:2.0.3-15.1
- rebuild

* Wed Sep 12 2007 Maros Barabas <mbarabas@redhat.com> -4:2.0.3-15
- patch to build on FC, bad open call 

* Tue Sep 11 2007 Maros Barabas <mbarabas@redhat.com> - 4:2.0.3-13
- rebuild

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 4:2.0.3-12
- Rebuild for selinux ppc32 issue.

* Thu May 10 2007 Maros Barabas <mbarabas@redhat.com> - 4:2.0.4-11
- fix from merge review
- Resolves #226190

* Tue Apr 17 2007 Maros Barabas <mbarabas@redhat.com> - 4:2.0.3-10
- fix fiew problems in spec

* Tue Jan 23 2007 Jindrich Novy <jnovy@redhat.com> - 4:2.0.3-9
- rebuild against new db4

* Mon Dec 04 2006 Maros Barabas        <mbarabas@redhat.com> - 4:2.0.3-8
- BuildRequires changed from cracklib to cracklib-devel

* Fri Aug 18 2006 Jesse Keating <jkeating@redhat.com> - 4:2.0.3-7
- rebuilt with latest binutils to pick up 64K -z commonpagesize on ppc*
  (#203001)
- Add dist tag

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 4:2.0.3-6.fc6.1
- rebuild

* Fri Jun 09 2006 Jason Vas Dias <jvdias@redhat.com> - 4:2.0.3-6.fc6
- rebuild for broken libgssapi deps and brew build

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 4:2.0.3-4.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jason Vas Dias <jvdias@redhat.com>
- rebuild for new gcc, glibc, glibc-kernheaders

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 09 2005 Jason Vas Dias <jvdias@redhat.com>
- Rebuild for new openssl dependencies

* Thu Oct 13 2005 Tomas Mraz <tmraz@redhat.com>
- use include instead of pam_stack in pam config

* Wed Jul 20 2005 Bill Nottingham <notting@redhat.com>
- don't run by default

* Thu Jun 16 2005 Jason Vas Dias <jvdias@redhat.com>
- Upgrade to upstream version 2.0.3
- fix bug 160486: use netatalk's initscript

* Wed Mar 30 2005 Florian La Roche <laroche@redhat.com>
- quick fix: rm -f /usr/include/netatalk/at.h until this
  is resolved the correct way

* Mon Mar 07 2005 Jason Vas Dias <jvdias@redhat.com>
- Fix for gcc4 compilation: extern_ucreator.patch

* Mon Feb 21 2005 Jason Vas Dias <jvdias@redhat.com>
- Upgraded to upstream version 2.0.2 .

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 07 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- 1.6.4

* Fri Aug 1 2003 Charlie Bennett <ccb@redhat.com>
- Update with 1.6.3 upstream sources

* Tue Jul 29 2003 Elliot Lee <sopwith@redhat.com>
- Rebuild
- Fix perl multilib path editing
- Add pathcat patch

* Thu May  1 2003 Elliot Lee <sopwith@redhat.com> 1.5.5-7
- Make multilib generic
- Add builddep on quota (for rpcsvc/rquota.h)

* Tue Feb 18 2003 Bill Nottingham <notting@redhat.com> 1.5.5-5
- fix initscript error (#82118)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan  7 2003 Nalin Dahyabhai <nalin@redhat.com> 1.5.5-3
- patch for compile errors with new ssl libs
- rebuildfedora

* Mon Dec 02 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- postun should never fail

* Thu Nov 28 2002 Phil Knirsch <pknirsch@redhat.com> 1.5.5-1
- Updated to 1.5.5

* Tue Jun 25 2002 Phil Knirsch <pknirsch@redhat.com> 1.5.3.1-4
- Fixed dependancy problem on /usr/bin/rc by removing acleandir.[1|rc] (#67243)
- Fixed missing /usr/share/netatalk dir (#67222)

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 1.5.3.1-2
- automated rebuild

* Tue Jun 18 2002 Phil Knirsch <pknirsch@redhat.com> 1.5.3.1-1
- Updated to latest version 1.5.3.1.
- Fixed bug for nls file lookup (#66300).

* Mon May 27 2002 Phil Knirsch <pknirsch@redhat.com> 1.5.2-4
- Fixed initscript bug where you can't use blanks inside of names (#64926).

* Wed Apr 10 2002 Phil Knirsch <pknirsch@redhat.com> 1.5.2-3
- Fixed initscript to use correct config files from /etc/atalk (#62803)
- Changed initscript to use $0 instead of direct string (#61734)
- Change Copyright to Licencse and switch from BSD to GPL (#61746)

* Thu Mar 14 2002 Bill Nottingham <notting@redhat.com>
- don't run by default

* Wed Mar 13 2002 Bill Nottingham <notting@redhat.com>
- it's back 

* Fri Mar  2 2001 Tim Powers <timp@redhat.com>
- rebuilt against openssl-0.9.6-1

* Sun Feb 25 2001 Tim Powers <timp@redhat.com>
- fixed bug 29370. This package is trying to include a file glibc already includes

* Tue Jan 23 2001 Tim Powers <timp@redhat.com>
- updated initscript

* Thu Jan 04 2001 Than Ngo <than@redhat.com>
- fixed uams-path
- added noreplace to %%config

* Mon Nov 20 2000 Tim Powers <timp@redhat.com>
- rebuilt to fix bad dir perms

* Fri Nov 10 2000 Than Ngo <than@redhat.com>
- update to 1.5pre2 (bug #19737, #20397)
- update Url and ftp site
- clean up specfile
- netatalk-1.4b2+asun obsolete

* Mon Aug 07 2000 Than Ngo <than@redhat.de>
- fix dependency with glibc-devel (Bug #15589)
- fix typo in description (Bug #15479)

* Wed Aug 2 2000 Tim Powers <timp@redhat.com>
- fix symlinks not being relative.

* Fri Jul 28 2000 Than Ngo <than@redhat.de>
- add missing restart function in startup script

* Fri Jul 28 2000 Tim Powers <timp@redhat.com>
- fixed initscripts so that condrestart doesn't return 1 when the test fails

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Sun Jul 23 2000 Tim Powers <timp@redhat.com>
- rebuilt 

* Mon Jul 17 2000 Tim Powers <timp@redhat.com>
- inits back to rc.d/init.d, using service to start inits

* Wed Jul 12 2000 Than Ngo <than@redhat.de>
- rebuilt

* Thu Jul 06 2000 Tim Powers <timp@redhat.com>
- fixed broken PreReq, now PreReq's /etc/init.d

* Tue Jun 27 2000 Than Ngo <than@redhat.de>
- remove prereq initscripts, add requires initscripts
- clean up specfile

* Mon Jun 26 2000 Than Ngo <than@redhat.de>
- /etc/rc.d/init.d -> /etc/init.d
- add condrestart directive
- fix post/preun/postun scripts
- prereq initscripts >= 5.20

* Tue Jun 20 2000 Tim Powers <timp@redhat.com>
- fixed bug 11420 concerning the building with -O2.

* Thu Jun 8 2000 Tim Powers <timp@redhat.com>
- fix bug #11978 
- fix man page locations to be FHS compliant

* Thu Jun  1 2000 Nalin Dahyabhai <nalin@redhat.com>
- modify PAM setup to use system-auth

* Thu Dec 16 1999 Tim Powers <timp@redhat.com>
- renewed source so it is pristine, delete the problematic files in spec file
        instead
- general spec file cleanups, create buildroot and dirs in the %%install
        section
- strip binaries
- gzip man pages
- fixed netatalk-asun.librpcsvc.patch, -lnss_nis too
- changed group
- added %%defattr to %%files section

* Tue Aug 3 1999 iNOUE Koich! <inoue@ma.ns.musashi-tech.ac.jp>
- rpm-3.0 needs to remove vogus files from source.
  Removed files: etc/papd/.#magics.c, etc/.#diff

* Fri Jul 30 1999 iNOUE Koich! <inoue@ma.ns.musashi-tech.ac.jp>
- Change Copyright tag to BSD.
  Add /usr/bin/adv1tov2.

* Thu Apr 22 1999 iNOUE Koich! <inoue@ma.ns.musashi-tech.ac.jp>
- Correct librpcsvc.patch.  Move %%changelog section last.
  Uncomment again -DNEED_QUOTA_WRAPPER in sys/linux/Makefile since
  LinuxPPC may need.

* Wed Mar 31 1999 iNOUE Koich! <inoue@ma.ns.musashi-tech.ac.jp>
- Comment out -DNEED_QUOTA_WRAPPER in sys/linux/Makefile.

* Sat Mar 20 1999 iNOUE Koich! <inoue@ma.ns.musashi-tech.ac.jp>
- Correct symbolic links to psf.

  Remove asciize function from nbplkup so as to display Japanese hostname.
* Thu Mar 11 1999 iNOUE Koich! <inoue@ma.ns.musashi-tech.ac.jp>

- Included MacPerl 5 script ICDumpSuffixMap which dumps suffix mapping
  containd in Internet Config Preference.

* Tue Mar 2 1999 iNOUE Koich! <inoue@ma.ns.musashi-tech.ac.jp>
- [asun2.1.3]

* Mon Feb 15 1999 iNOUE Koich! <inoue@ma.ns.musashi-tech.ac.jp>
- [pre-asun2.1.2-8]

* Sun Feb 7 1999 iNOUE Koich! <inoue@ma.ns.musashi-tech.ac.jp>
- [pre-asun2.1.2-6]

* Mon Jan 25 1999 iNOUE Koichi <inoue@ma.ns.musashi-tech.ac.jp>
- [pre-asun2.1.2-3]

* Thu Dec 17 1998 INOUE Koichi <inoue@ma.ns.musashi-tech.ac.jp>
- [pre-asun2.1.2]
  Remove crlf patch. It is now a server's option.

* Thu Dec 3 1998 INOUE Koichi <inoue@ma.ns.musashi-tech.ac.jp>
- Use stable version source netatalk-1.4b2+asun2.1.1.tar.gz
  Add uams directory

* Sat Nov 28 1998 INOUE Koichi <inoue@ma.ns.musashi-tech.ac.jp>
- Use pre-asun2.1.1-3 source.

* Mon Nov 23 1998 INOUE Koichi <inoue@ma.ns.musashi-tech.ac.jp>
- Use pre-asun2.1.1-2 source.

* Mon Nov 16 1998 INOUE Koichi <inoue@ma.ns.musashi-tech.ac.jp>
- Fix rcX.d's symbolic links.

* Wed Oct 28 1998 INOUE Koichi <inoue@ma.ns.musashi-tech.ac.jp>
- Use pre-asun2.1.0a-2 source. Remove '%%exclusiveos linux' line.

* Sat Oct 24 1998 INOUE Koichi <inoue@ma.ns.musashi-tech.ac.jp>
- Use stable version source netatalk-1.4b2+asun2.1.0.tar.gz.

* Mon Oct 5 1998 INOUE Koichi <inoue@ma.ns.musashi-tech.ac.jp>
- Use pre-asun2.1.0-10a source.

* Sat Sep 19 1998 INOUE Koichi <inoue@ma.ns.musashi-tech.ac.jp>
- Use pre-asun2.1.0-8 source. Add chkconfig support.

* Sat Sep 12 1998 INOUE Koichi <inoue@ma.ns.musashi-tech.ac.jp>
- Comment out -DCRLF. Use RPM_OPT_FLAGS.

* Tue Sep 8 1998 INOUE Koichi <inoue@ma.ns.musashi-tech.ac.jp>
- Use pre-asun2.1.0-7 source. Rename atalk.init to atalk.

* Sat Aug 22 1998 INOUE Koichi <inoue@ma.ns.musashi-tech.ac.jp>
- Use pre-asun2.1.0-6 source.

* Mon Jul 27 1998 INOUE Koichi <inoue@ma.ns.musashi-tech.ac.jp>
- Use pre-asun2.1.0-5 source.

* Tue Jul 21 1998 INOUE Koichi <inoue@ma.ns.musashi-techa.c.jp>
- Use pre-asun2.1.0-3 source.

* Tue Jul 7 1998 INOUE Koichi <inoue@ma.ns.musashi-tech.ac.jp>
- Add afpovertcp entries to /etc/services
- Remove BuildRoot in man8 pages

* Mon Jun 29 1998 INOUE Koichi <inoue@ma.ns.musashi-tech.ac.jp>
- Use modified sources 1.4b2+asun2.1.0 produced by Adrian Sun
  <asun@saul9.u.washington.edu> to provide an AppleShareIP file server

- Included AppleVolumes.system file maintained by Johnson
  <johnson@stpt.usf.edu>

* Mon Aug 25 1997 David Gibson <D.Gibson@student.anu.edu.au>
- Used a buildroot
- Use RPM_OPT_FLAGS
- Moved configuration parameters/files from atalk.init to /etc/atalk
- Separated devel package
- Built with shared libraries

* Sun Jul 13 1997 Paul H. Hargrove <hargrove@sccm.Stanford.EDU>
- Updated sources from 1.3.3 to 1.4b2
- Included endian patch for Linux/SPARC
- Use all the configuration files supplied in the source.  This has the
  following advantages over the ones in the previous rpm release:
        + The printer 'lp' isn't automatically placed in papd.conf
        + The default file conversion is binary rather than text.
- Automatically add and remove DDP services from /etc/services
- Placed the recommended /etc/services in the documentation
- Changed atalk.init to give daemons a soft kill
- Changed atalk.init to make configuration easier

* Wed May 28 1997 Mark Cornick <mcornick@zorak.gsfc.nasa.gov>
- Updated for /etc/pam.d

