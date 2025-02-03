# Disable TCP Wrappers connection filter
%bcond_with rwhoisd_enables_tcpwrappers

Name:       rwhoisd 
Version:    1.5.9.6
Release:    33%{?dist}
Summary:    ARIN's Referral WHOIS server
# common/strerror.c:                GPL-2.0-or-later (libiberty)
# LICENSE:                          GPL-2.0 text
# mkdb/metaphon.c:                  LicenseRef-Fedora-Public-Domain
# mkdb/y.tab.c:                     GPL-2.0-or-later WITH Bison-exception-1.24
# regexp/COPYRIGHT:                 Spencer-86
## Not in any binary package
# configure:                        FSFUL
## Unbundled
# tools/tcpd_wrapper/DISCLAIMER:    TCP-wrappers
# tools/tcpd_wrapper/strcasecmp.c:  BSD-4.3TAHOE
License:    GPL-2.0-or-later AND GPL-2.0-or-later WITH Bison-exception-1.24 AND Spencer-86 AND LicenseRef-Fedora-Public-Domain
SourceLicense:  %{license} AND FSFUL AND TCP-wrappers AND BSD-4.3TAHOE
URL:        http://projects.arin.net/rwhois/
Source0:    %{url}ftp/%{name}-%{version}.tar.gz
Source1:    %{name}.service
# Install database to /var
Patch0:     %{name}-1.5.9.6-Install-database-to-var.patch
# Fix configure script
Patch1:     %{name}-1.5.9.5-Use-configure-options-instead-of-GCC-test.patch
# Fix configure script
Patch2:     %{name}-1.5.9.5-Use-AC_SYS_LARGEFILE-for-large-file-support-check.patch
# Fix configure script
Patch3:     %{name}-1.5.9.5-Respect-without-local-libwrap.patch
# Use system tcpd.h
Patch4:     %{name}-1.5.9.5-Do-not-include-bundled-tcpd.h.patch
# GNU sort requires new syntax
Patch5:     %{name}-1.5.9.5-Select-which-way-to-call-sort.patch
# Change default configuration
Patch6:     %{name}-1.5.9.5-Adjust-sample-configuration.patch
# Disable TCP wrappers, bug #1518781
Patch7:     %{name}-1.5.9.6-Allow-disabling-TCP-wrappers.patch
# Fix building with GCC 13, proposed to na upstream,
# <https://github.com/arineng/rwhoisd/pull/2>
Patch8:     %{name}-1.5.9.6-c99.patch
# Fix a signal handler return value, proposed to an upstream,
# <https://github.com/arineng/rwhoisd/pull/3>
Patch9:     %{name}-1.5.9.6-Fix-a-return-value-of-signal-handlers.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libxcrypt-devel
%if %{with rwhoisd_enables_tcpwrappers}
BuildRequires:  tcp_wrappers-devel
%endif
BuildRequires:  systemd
# cat executed by rwhois_repack
Requires:       %{_bindir}/cat
# sort executed by rwhois_indexer
Requires:       %{_bindir}/sort
Requires(pre):      shadow-utils
%{?systemd_requires}

%description
This server is a reference implementation of the server side of the RWhois
protocol, first described in RFC 1714.  This server attempts to implement
concepts and practices in accordance with version 1.5 of the protocol,
described in RFC 2167.

%package example
License:    GPL-2.0-or-later
Summary:    Sample data for %{name} WHOIS server
BuildArch:  noarch
Requires:   %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description example
This package delivers example configuration and data for %{name} WHOIS server.
Recommended how-to is <http://www.unixadmin.cc/rwhois/>.


%prep
%autosetup -p1
# Remove bundled tcp_wrappers for sure
find tools/tcpd_wrapper -depth -mindepth 1 \! -name Makefile.in -delete
# Keep System V8 regexp library
# TODO: port to GNU glibc
autoreconf

%build
%global _hardened_build 1
%configure \
    --disable-gcc-debug \
    --disable-gprof \
    --enable-ipv6 \
    --enable-largefile \
    --enable-newsort \
    --enable-syslock \
%if %{with rwhoisd_enables_tcpwrappers}
    --enable-tcpwrappers \
%else
    --disable-tcpwrappers \
%endif
    --enable-warnings \
    --without-local-libwrap

# Does not support parallel build
make

%install
%{make_install}
install -d '%{buildroot}%{_mandir}/man8'
install -m 0644 -t '%{buildroot}%{_mandir}/man8' doc/*.8
install -d '%{buildroot}%{_unitdir}'
install -m 0644 -t '%{buildroot}%{_unitdir}' '%{SOURCE1}'
# Default empty configuration
install -d '%{buildroot}%{_sysconfdir}'
install -m 0644 -t '%{buildroot}%{_sysconfdir}' sample.data/rwhoisd.conf
install -m 0644 -t '%{buildroot}%{_sysconfdir}' sample.data/rwhoisd.dir
install -m 0644 -t '%{buildroot}%{_sysconfdir}' sample.data/rwhoisd.x.dir
install -m 0644 -t '%{buildroot}%{_sysconfdir}' sample.data/rwhoisd.root
install -m 0644 -t '%{buildroot}%{_localstatedir}/%{name}/' \
    sample.data/rwhoisd.auth_area
install -d -m 0775 "%{buildroot}%{_localstatedir}/%{name}/register-spool"

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -d %{_localstatedir}/%{name} -s /sbin/nologin \
    -c "rwhoisd daemon" %{name}
exit 0

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service 

%files
%license LICENSE regexp/COPYRIGHT
%doc doc/operations_guide.txt doc/security.txt doc/TODO doc/UPGRADE README
%{_bindir}/rwhois_deleter
%{_bindir}/rwhois_indexer
%{_bindir}/rwhois_repack
%{_sbindir}/rwhoisd
%{_mandir}/man8/rwhois_indexer.*
%{_mandir}/man8/rwhoisd.*
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}.dir
%config(noreplace) %{_sysconfdir}/%{name}.x.dir
%config(noreplace) %{_sysconfdir}/%{name}.root
%dir %{_localstatedir}/%{name}
%config(noreplace) %{_localstatedir}/%{name}/%{name}.auth_area
%attr(775,root,%{name}) %dir %{_localstatedir}/%{name}/register-spool

%files example
%{_localstatedir}/%{name}/samples

%changelog
* Sat Feb 01 2025 Björn Esser <besser82@fedoraproject.org> - 1.5.9.6-33
- Add explicit BR: libxcrypt-devel

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 04 2024 Petr Pisar <ppisar@redhat.com> - 1.5.9.6-29
- Convert license tags to an SPDX format

* Fri Dec 01 2023 Petr Pisar <ppisar@redhat.com> - 1.5.9.6-28
- Fix a signal handler return value (GH#3)
- Correct a license to "Public Domain and HSRL and GPLv2+"

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Florian Weimer <fweimer@redhat.com> - 1.5.9.6-25
- C99 compatibility fixes

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.5.9.6-21
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Petr Pisar <ppisar@redhat.com> - 1.5.9.6-18
- Modernize a spec file

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Björn Esser <besser82@fedoraproject.org> - 1.5.9.6-14
- Rebuilt for libcrypt.so.2 (#1666033)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Petr Pisar <ppisar@redhat.com> - 1.5.9.6-12
- Modernize spec file

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.5.9.6-10
- Rebuilt for switch to libxcrypt

* Thu Nov 30 2017 Petr Pisar <ppisar@redhat.com> - 1.5.9.6-9
- Disable TCP wrappers (bug #1518781)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 24 2013 Petr Pisar <ppisar@redhat.com> - 1.5.9.6-1
- 1.5.9.6 bump

* Thu Oct 03 2013 Petr Pisar <ppisar@redhat.com> - 1.5.9.5-1
- 1.5.9.5 version packaged
