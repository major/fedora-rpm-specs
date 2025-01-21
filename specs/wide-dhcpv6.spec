#
# spec file for package wide-dhcpv6
#

%global ubuntu_release 23
%global my_release 3
%global _hardened_build 1

Name:           wide-dhcpv6
BuildRequires:  gcc
BuildRequires:  bison flex libfl-static systemd
# The entire source code is BSD except the bison parser code which is GPL
# Automatically converted from old format: BSD and GPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND GPL-2.0-or-later
Summary:        DHCP Client and Server for IPv6
Version:        20080615
Url:            https://launchpad.net/ubuntu/+source/%{name}/%{version}-%{ubuntu_release}
Release:        %{ubuntu_release}.%{my_release}%{dist}.7
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        CHANGELOG-LINUX
Source2:        COPYRIGHT
Source3:        dhcp6c-script
Source4:        dhcp6c.service
Source5:        dhcp6r.service
Source6:        dhcp6s.service
Source7:        RELEASENOTES
Source8:        dhcp6c@.service
Patch1:		wide-dhcpv6-0001-Fix-manpages.patch
Patch2:		wide-dhcpv6-0002-Don-t-strip-binaries.patch
Patch3:		wide-dhcpv6-0003-Close-inherited-file-descriptors.patch
Patch4:		wide-dhcpv6-0004-GNU-libc6-fixes.patch
Patch5:		wide-dhcpv6-0005-Update-ifid-on-interface-restart.patch
Patch6:		wide-dhcpv6-0006-Add-new-feature-dhcp6c-profiles.patch
Patch7:		wide-dhcpv6-0007-Adding-ifid-option-to-the-dhcp6c.conf-prefix-interfa.patch
Patch8:		wide-dhcpv6-0008-Close-file-descriptors-on-exec.patch
Patch9:		wide-dhcpv6-0009-Fix-renewal-of-IA-NA.patch
Patch10:	wide-dhcpv6-0010-Call-client-script-after-interfaces-have-been-update.patch
Patch11:	wide-dhcpv6-0011-resolv-warnings-so-as-to-make-blhc-and-gcc-both-happ.patch
Patch12:	wide-dhcpv6-0012-fix-a-redefined-YYDEBUG-warning-of-gcc-for-the-code-.patch
Patch13:	wide-dhcpv6-0013-added-several-comments-examples-by-Stefan-Sperling.patch
Patch14:	wide-dhcpv6-0014-Support-to-build-on-kFreeBSD-n-GNU-Hurd-platform.patch
Patch15:	wide-dhcpv6-0015-a-bit-info-to-logger-when-get-OPTION_RECONF_ACCEPT.patch
Patch16:	wide-dhcpv6-0016-fix-typo-in-dhcp6c.8-manpage.patch
Patch17:	wide-dhcpv6-0017-Remove-unused-linking-with-libfl.patch
Patch18:	wide-dhcpv6-0018-dhcpv6-ignore-advertise-messages-with-none-of-reques.patch
Patch19:	wide-dhcpv6-0019-Server-should-not-bind-control-port-if-there-is-no-s.patch
Patch20:	wide-dhcpv6-0020-Adding-option-to-randomize-interface-id.patch
Patch21:	wide-dhcpv6-0021-Make-sla-len-config-optional.patch
Patch22:	wide-dhcpv6-0022-Make-sla-id-config-optional.patch
Patch23:	wide-dhcpv6-0023-fix-the-parallel-build-fix.patch
Patch99:	wide-dhcpv6-fedora-c99.patch
Requires(preun): systemd
Requires(postun): systemd

%description
This is the DHCPv6 package from WIDE project. For more information visit the
project web site at http://wide-dhcpv6.sourceforge.net/

DHCPv6 allows prefix delegation and host configuration for the IPv6 network
protocol.

Multiple network interfaces are supported by this DHCPv6 package.

This package contains the server, relay and client.


%prep
%setup -q 
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1
%patch -P13 -p1
%patch -P14 -p1
%patch -P15 -p1
%patch -P16 -p1
%patch -P17 -p1
%patch -P18 -p1
%patch -P19 -p1
%patch -P20 -p1
%patch -P21 -p1
%patch -P22 -p1
%patch -P23 -p1
%patch -P99 -p1


%build
%configure --sysconfdir=%{_sysconfdir}/%{name} --enable-libdhcp=no
make %{?_smp_mflags}	

%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man{8,5}
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
mkdir -p %{buildroot}%{_unitdir}
install -p -m 755 dhcp6c dhcp6s dhcp6relay dhcp6ctl %{buildroot}%{_sbindir}
install -p -m 644 dhcp6c.8 dhcp6s.8 dhcp6relay.8 dhcp6ctl.8 %{buildroot}/%{_mandir}/man8
install -p -m 644 dhcp6c.conf.5 dhcp6s.conf.5 %{buildroot}/%{_mandir}/man5
install -p -m 644 %{SOURCE1} %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 %{SOURCE2} %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 %{SOURCE3} %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 %{SOURCE4} %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 %{SOURCE5} %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 %{SOURCE6} %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 %{SOURCE7} %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 %{SOURCE8} %{buildroot}%{_unitdir}
install -p -m 644 README CHANGES %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 dhcp6c.conf.sample %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 dhcp6s.conf.sample %{buildroot}%{_defaultdocdir}/%{name}

%preun
if [ $1 -lt 1 ] ; then
%systemd_preun dhcp6c@.service
fi
%systemd_preun dhcp6c.service
%systemd_preun dhcp6r.service
%systemd_preun dhcp6s.service

%postun
%systemd_postun_with_restart dhcp6c.service
%systemd_postun_with_restart dhcp6r.service
%systemd_postun_with_restart dhcp6s.service

%files
%dir %{_sysconfdir}/%{name}
%{_defaultdocdir}/%{name}/*
%{_sbindir}/*
%{_mandir}/man?/*
%{_unitdir}/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-23.3.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 20080615-23.3.6
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-23.3.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-23.3.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-23.3.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 10 2023 DJ Delorie <dj@redhat.com> - 20080615-23.2.3
- Fix C99 compatibility issue

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-23.2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-23.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun May 15 2022 dave@bevhost.com - 20080615-23.2
- Change Build Dependancy from flex-devel to libfl-static

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-23.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-23.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jan 03 2021 dave@bevhost.com 20080615-23.1
- Update upstream from 13 to 23 including
- bugfix close file descriptions on exec
- bugfix warning suppression for YYDEBUG
- better logging for Option 20
- added more examples in documentation
- enhancement now able to randomize interface IP

* Fri Aug 14 2020 dave@bevhost.com 20080615-13.2
- Added parameterized systemd unit file for client
- Added more complete usage example to RELEASENOTES

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-13.1.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-13.1.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-13.1.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-13.1.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-13.1.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-13.1.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-13.1.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-13.1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-13.1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20080615-13.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080615-13.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 7 2015 dave@bevhost.com 20080615-13.1
- Added patch 12 from ubuntu version
- Added patch 13 so we can use parallel make

* Tue Jan 14 2014 dave@bevhost.com 20080615-11.1.5
- Added patch 11 provided by Scott Shambarger
- Documentation directory now has no version number

* Thu May 16 2013 dave@bevhost.com 20080615-11.1.4
- Added patches 8 and 9, which simplify configuration
- Added patch 10 which moves client script execution to after IP addr are added.
- Added RELEASENOTES

* Tue May 7 2013 dave@bevhost.com 20080615-11.1.3
- make the build specific to fedora rawhide 

* Mon May 6 2013 dave@bevhost.com 20080615-11.1.2
- use macros in spec file wherever possible
- add support for systemd

* Wed Apr 24 2013 dave@bevhost.com 20080615-11.1.1
- Move sysconfdir from /etc to /etc/wide-dhcpv6 to match man pages

* Tue Apr 02 2013 dave@bevhost.com
- converted from debian package


