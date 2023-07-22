#http://lists.fedoraproject.org/pipermail/devel/2011-August/155358.html
%global _hardened_build 1
%global sysrepo 0

#%%global prever P1

Name:           kea
Version:        2.4.0
Release:        2%{?dist}
Summary:        DHCPv4, DHCPv6 and DDNS server from ISC

License:        MPL-2.0 AND BSL-1.0
URL:            http://kea.isc.org
Source0:        https://downloads.isc.org/isc/kea/%{version}%{?prever:-%{prever}}/kea-%{version}%{?prever:-%{prever}}.tar.gz
Source5:        https://downloads.isc.org/isc/kea/%{version}%{?prever:-%{prever}}/kea-%{version}%{?prever:-%{prever}}.tar.gz.asc
# Obtained from https://www.isc.org/pgpkey/
Source6:        isc-keyblock.asc
Source1:        kea-dhcp4.service
Source2:        kea-dhcp6.service
Source3:        kea-dhcp-ddns.service
Source4:        kea-ctrl-agent.service

Patch3:         kea-openssl-version.patch

# autoreconf
BuildRequires: autoconf automake libtool
BuildRequires: boost-devel
BuildRequires: gcc-c++
# %%configure --with-openssl
BuildRequires: openssl-devel
# %%configure --with-dhcp-mysql
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires: mariadb-connector-c-devel
# TODO: propose upstream fix so this is not needed (no server-side related
# headers nor configuration should be needed)
BuildRequires: postgresql-server-devel
%else
# %%configure --with-dhcp-mysql
BuildRequires: mariadb-devel
# %%configure --with-dhcp-pgsql
BuildRequires: postgresql-devel
%endif
BuildRequires: log4cplus-devel
%if %{sysrepo}
# %%configure --with-sysrepo
BuildRequires: sysrepo-devel
%endif

%ifnarch s390 %{mips}
BuildRequires: valgrind-devel
%endif
# src/lib/testutils/dhcp_test_lib.sh
BuildRequires: procps-ng
# %%configure --enable-generate-parser
BuildRequires: bison
BuildRequires: flex
# %%configure --enable-shell
BuildRequires: python3-devel
# in case you ever wanted to use %%configure --enable-generate-docs
#BuildRequires: elinks asciidoc plantuml
BuildRequires: systemd
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: make
BuildRequires: gnupg2

Requires: kea-libs%{?_isa} = %{version}-%{release}
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd


%description
DHCP implementation from Internet Systems Consortium, Inc. that features fully
functional DHCPv4, DHCPv6 and Dynamic DNS servers.
Both DHCP servers fully support server discovery, address assignment, renewal,
rebinding and release. The DHCPv6 server supports prefix delegation. Both
servers support DNS Update mechanism, using stand-alone DDNS daemon.


%package devel
Summary: Development headers and libraries for Kea DHCP server
Requires: kea-libs%{?_isa} = %{version}-%{release}
# to build hooks (#1335900)
Requires: boost-devel
Requires: openssl-devel
Requires: pkgconfig

%description devel
Header files and API documentation.


%package hooks
Summary: Hooks libraries for kea
Requires: kea-libs%{?_isa} = %{version}-%{release}

%description hooks
Hooking mechanism allow Kea to load one or more dynamically-linked libraries
(known as "hooks libraries") and, at various points in its processing
("hook points"), call functions in them.  Those functions perform whatever
custom processing is required.


%package libs
Summary: Shared libraries used by Kea DHCP server

%description libs
This package contains shared libraries used by Kea DHCP server.


%prep
%if 0%{?fedora}
%{gpgverify} --keyring='%{SOURCE6}' --signature='%{SOURCE5}' --data='%{SOURCE0}'
%endif
rm -rf doc/sphinx/_build
%autosetup -p1 -n kea-%{version}%{?prever:-%{prever}}

# to be able to build on ppc64(le)
# https://sourceforge.net/p/flex/bugs/197
# https://lists.isc.org/pipermail/kea-dev/2016-January/000599.html
sed -i -e 's|ECHO|YYECHO|g' src/lib/eval/lexer.cc


%build
autoreconf --verbose --force --install

%configure \
    --disable-dependency-tracking \
    --disable-rpath \
    --disable-silent-rules \
    --disable-static \
    --enable-debug \
    --enable-generate-parser \
    --enable-shell \
    --enable-generate-docs \
    --enable-generate-messages \
    --enable-perfdhcp \
    --with-mysql \
    --with-pgsql \
    --with-gnu-ld \
    --with-log4cplus \
%if %{sysrepo}
    --with-sysrepo \
%endif
    --with-openssl

%make_build


%install
%make_install docdir=%{_pkgdocdir}

# Get rid of .la files
find %{buildroot} -type f -name "*.la" -delete -print

# Install systemd units
install -Dpm 0644 %{S:1} %{buildroot}%{_unitdir}/kea-dhcp4.service
install -Dpm 0644 %{S:2} %{buildroot}%{_unitdir}/kea-dhcp6.service
install -Dpm 0644 %{S:3} %{buildroot}%{_unitdir}/kea-dhcp-ddns.service
install -Dpm 0644 %{S:4} %{buildroot}%{_unitdir}/kea-ctrl-agent.service

# Start empty lease databases
mkdir -p %{buildroot}%{_sharedstatedir}/kea/
touch %{buildroot}%{_sharedstatedir}/kea/kea-leases4.csv
touch %{buildroot}%{_sharedstatedir}/kea/kea-leases6.csv

rm -f %{buildroot}%{_pkgdocdir}/COPYING


mkdir -p %{buildroot}/run
install -d -m 0755 %{buildroot}/run/kea/

# install /usr/lib/tmpfiles.d/kea.conf
mkdir -p %{buildroot}%{_tmpfilesdir}
cat > %{buildroot}%{_tmpfilesdir}/kea.conf <<EOF
# kea needs existing /run/kea/ to create logger_lockfile there
# See tmpfiles.d(5) for details

d /run/kea 0755 root root -
EOF


%post
%systemd_post kea-dhcp4.service kea-dhcp6.service kea-dhcp-ddns.service kea-ctrl-agent.service

%preun
%systemd_preun kea-dhcp4.service kea-dhcp6.service kea-dhcp-ddns.service kea-ctrl-agent.service

%postun
%systemd_postun_with_restart kea-dhcp4.service kea-dhcp6.service kea-dhcp-ddns.service kea-ctrl-agent.service


%ldconfig_scriptlets libs


%files
%license COPYING
%doc AUTHORS ChangeLog README CONTRIBUTING.md examples html platforms.rst code_of_conduct.md
%{_bindir}/kea-msg-compiler
%{_sbindir}/%{name}*
%{_sbindir}/perfdhcp
%{_unitdir}/%{name}*.service
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/kea/%{name}*.conf
%{_datarootdir}/%{name}
%dir %{_sharedstatedir}/%{name}
%config(noreplace) %{_sharedstatedir}/kea/kea-leases*.csv
%{python3_sitelib}/%{name}
%{_mandir}/man8/*
%dir /run/kea/
%{_tmpfilesdir}/kea.conf

%files devel
%license COPYING
%{_includedir}/kea
%{_libdir}/libkea-*.so

%files hooks
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/hooks

%files libs
%license COPYING
%{_libdir}/libkea-*.so.*


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 Martin Osvald <mosvald@redhat.com> - 2.4.0-1
- New version 2.4.0
- Migrated to SPDX license
- Do not export CXXFLAGS with -std=gnu++11 to stop boost warning messages

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 2.2.0-5
- Rebuilt for Python 3.12

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 2.2.0-4
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Ondřej Sloup <osloup@redhat.com> - 2.2.0-2
- Rebuild for new PostgreSQL 15

* Wed Jul 27 2022 Martin Osvald <mosvald@redhat.com> - 2.2.0-1
- New version 2.2.0
- Add source code signature verification

* Thu Jul 21 2022 Martin Osvald <mosvald@redhat.com> - 2.0.2-4
- kea fails to build docs with Sphinx 5+ (#2105931)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.2-3
- Rebuilt for Python 3.11

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 2.0.2-2
- Rebuilt for Boost 1.78

* Thu Mar 03 2022 Martin Osvald <mosvald@redhat.com> - 2.0.2-1
- New version 2.0.2

* Mon Feb 07 2022 Martin Osvald <mosvald@redhat.com> - 2.0.1-1
- New version 2.0.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Filip Januš <fjanus@redhat.com> - 1.9.8-6
- Rebuild for Postgresql 14

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.9.8-5
- Rebuilt with OpenSSL 3.0.0

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 1.9.8-4
- Rebuilt for Boost 1.76

* Tue Jul 27 2021 Filip Januš <fjanus@redhat.com> - 1.9.8-3
- Remove libpq-devel requirement, it conflicts with postgresql-server-devel
  dependencies

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 23 2021 Pavel Zhukov <pzhukov@redhat.com> - 1.9.8-1
- New version 1.9.8

* Wed Jun 23 2021 Pavel Zhukov <pzhukov@redhat.com> - 1.9.6-2
- Make compatible with spinx 4.0

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.9.6-2
- Rebuilt for Python 3.10

* Sun Apr 04 2021 Pavel Zhukov <pzhukov@redhat.com> - 1.9.6-1
- New version v1.9.6

* Thu Mar 11 2021 Pavel Zhukov <pzhukov@redhat.com> - 1.9.5-1
- New version v1.9.5

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.9.4-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Feb 09 2021 Pavel Raiskup <praiskup@redhat.com> - 1.9.4-2
- rebuild all postgresql deps once more, for libpq ABI fix rhbz#1908268

* Mon Feb 08 2021 Pavel Zhukov pzhukov@redhat.com> - 1.9.4-1
- Update to 1.9.4

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 1.9.3-5
- rebuild for libpq ABI fix rhbz#1908268

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Pavel Zhukov pzhukov@redhat.com> - 1.9.3-3
- Update to 1.9.3
- Fix Werror bug

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.9.2-3
- Rebuilt for Boost 1.75

* Sat Dec 05 2020 Jeff Law <law@redhat.com> - 1.9.2-2
- Fix more missing includes for gcc-11

* Thu Nov 26 2020 Pavel Zhukov <pzhukov@redhat.com> - 1.9.2-1
- new version v1.9.2

* Fri Nov 20 2020 Pavel Zhukov <pzhukov@redhat.com> - 1.9.1-3
- Rebuild with new log4cplus

* Thu Oct 15 2020 Jeff Law <law@redhat.com> - 1.8.0-2
- Fix missing #includes for gcc-11

* Wed Sep 16 2020 Pavel Zhukov <pzhukov@redhat.com> - 1.8.0-1
- New version v1.8.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Jonathan Wakely <jwakely@redhat.com> - 1.6.0-4
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 11 2019 Kenneth Topp <toppk@bllue.org> - 1.6.0-1
- update to 1.6.0
- includes fixes for CVE-2019-6472, CVE-2019-6473 and CVE-2019-6474 

* Tue Jul 30 2019 Pavel Zhukov <pzhukov@redhat.com> - 1.5.0-8
- Do not specify openssl version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 22 2019 Felix Kaechele <heffer@fedoraproject.org> - 1.5.0-4
- Update to 1.3.0 release version
- fix PID file path in service files
- clean up spec file
- switched to openssl-devel, now builds with openssl 1.1
- install systemd units manually instead of patching the souce to do it
- enable kea-shell
- add boost patch
- add kea-ctrl-agent unit
- change postgresql-devel to postgresql-server-devel
- update to 1.4.0

* Sun Dec 16 2018 Pavel Zhukov <pzhukov@redhat.com> - 1.5.0-3
- Update to released version

* Tue Dec 11 2018 Pavel Zhukov <pzhukov@redhat.com> - 1.5.0-beta2.2%{?dist}
- Do not require -connectors on RHEL

* Tue Dec  4 2018 Pavel Zhukov <pzhukov@redhat.com> - 1.5.0-beta2.1%{?dist}
- update to beta2

* Tue Nov 20 2018 Pavel Zhukov <pzhukov@redhat.com> - 1.5.0-2
- Update to 1.5.0 beta

* Mon Aug 27 2018 Pavel Zhukov <pzhukov@redhat.com> - 1.3.0-12
- Disable tests again.

* Mon Aug 27 2018 Pavel Zhukov <pzhukov@redhat.com> - 1.3.0-11
- Do not use compat verion of openssl

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Pavel Zhukov <pzhukov@redhat.com> - 1.3.0-9
- Fix config files names (#1579298)

* Mon Feb 19 2018 Pavel Zhukov <pzhukov@redhat.com> - 1.3.0-8
- Add gcc-c++ BR

* Wed Feb 14 2018 Pavel Zhukov <landgraf@fedoraproject.org> - 1.3.0-7
- Package released version (#1545096)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Pavel Zhukov <landgraf@fedoraproject.org> - 1.3.0-4
- Fix build with boost 1.66 (#1540331)

* Thu Nov  2 2017 Pavel Zhukov <pzhukov@redhat.com> - 1.3.0-3
- Add openssl-devel requires
- Do not force pkgconfig(openssl) version

* Mon Oct 23 2017 Pavel Zhukov <pzhukov@redhat.com> - 1.2.0-8
- Require openssl102

* Sun Oct 22 2017 Pavel Zhukov <pzhukov@redhat.com> - 1.2.0-7
- Rebuild with new openssl

* Thu Oct 12 2017 Pavel Zhukov <pzhukov@redhat.com> - 1.2.0-6
- Use mariadb-connector-c-devel instead of mysql-devel (#1493628)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 1.2.0-3
- Rebuilt for Boost 1.64

* Fri May 26 2017 Pavel Zhukov <landgraf@fedoraproject.org> - 1.2.0-2
- New release 1.2.0 (#1440348)

* Tue Apr 04 2017 Pavel Zhukov <landgraf@fedoraproject.org> - 1.1.0-3
- Add patch for OpenSSL 1.1. Fix FTBFS (#1423812)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 04 2016 Jiri Popelka <jpopelka@redhat.com> - 1.1.0-1
- 1.1.0

* Thu Sep 01 2016 Jiri Popelka <jpopelka@redhat.com> - 1.1.0-0.1
- 1.1.0-beta

* Fri Aug 12 2016 Michal Toman <mtoman@fedoraproject.org> - 1.0.0-11
- No valgrind on MIPS

* Wed Aug 03 2016 Jiri Popelka <jpopelka@redhat.com> - 1.0.0-10
- %%{_defaultdocdir}/kea/ -> %%{_pkgdocdir}

* Fri May 13 2016 Jiri Popelka <jpopelka@redhat.com> - 1.0.0-9
- devel subpackage Requires: boost-devel

* Wed Mar 23 2016 Zdenek Dohnal <zdohnal@redhat.com> - 1.0.0-8
- Rebuild for log4cplus-1.2.0-2

* Wed Mar 23 2016 Zdenek Dohnal <zdohnal@redhat.com> - 1.0.0-7
- Rebuilding kea for log4cplus-1.2.0

* Wed Mar 16 2016 Zdenek Dohnal <zdohnal@redhat.com> - 1.0.0-6
- Editing pgsql_lease_mgr.cc according to upstream

* Fri Mar 11 2016 Zdenek Dohnal <zdohnal@redhat.com> - 1.0.0-4
- Fixing bugs created from new C++ standard

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.0.0-2
- Rebuilt for Boost 1.60

* Tue Dec 29 2015 Jiri Popelka <jpopelka@redhat.com> - 1.0.0-1
- 1.0.0

* Wed Dec 23 2015 Jiri Popelka <jpopelka@redhat.com> - 1.0.0-0.3.beta2
- fix compile error

* Wed Dec 23 2015 Jiri Popelka <jpopelka@redhat.com> - 1.0.0-0.2.beta2
- 1.0.0-beta2

* Wed Dec 09 2015 Jiri Popelka <jpopelka@redhat.com> - 1.0.0-0.1.beta
- 1.0.0-beta

* Mon Aug 24 2015 Jiri Popelka <jpopelka@redhat.com> - 0.9.2-3
- fix valgrind-devel availability

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Tue Jul 28 2015 Jiri Popelka <jpopelka@redhat.com> - 0.9.2-1
- 0.9.2

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.9.2-0.2.beta
- rebuild for Boost 1.58

* Thu Jul 02 2015 Jiri Popelka <jpopelka@redhat.com> - 0.9.2-0.1.beta
- 0.9.2-beta

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Wed Apr 01 2015 Jiri Popelka <jpopelka@redhat.com> - 0.9.1-1
- 0.9.1

* Fri Feb 20 2015 Jiri Popelka <jpopelka@redhat.com> - 0.9.1-0.2.beta
- /run/kea/ (for logger_lockfile)

* Thu Feb 19 2015 Jiri Popelka <jpopelka@redhat.com> - 0.9.1-0.1.beta
- 0.9.1-beta

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.9-4
- Rebuild for boost 1.57.0

* Tue Nov 04 2014 Jiri Popelka <jpopelka@redhat.com> - 0.9-3
- do not override @localstatedir@ globally
- include latest upstream kea.conf

* Wed Sep 24 2014 Dan Horák <dan[at]danny.cz> - 0.9-2
- valgrind available only on selected arches

* Mon Sep 01 2014 Jiri Popelka <jpopelka@redhat.com> - 0.9-1
- 0.9

* Thu Aug 21 2014 Jiri Popelka <jpopelka@redhat.com> - 0.9-0.5.beta1
- fix building with PostgreSQL on i686
- redefine localstatedir to sharedstatedir (kea#3523)

* Wed Aug 20 2014 Jiri Popelka <jpopelka@redhat.com> - 0.9-0.4.beta1
- install systemd service units with a proper patch that we can send upstream
- build with MySQL & PostgreSQL & Google Test
- no need to copy sample configuration, /etc/kea/kea.conf already contains one

* Tue Aug 19 2014 Jiri Popelka <jpopelka@redhat.com> - 0.9-0.3.beta1
- comment patches
- use --preserve-timestamps with install

* Mon Aug 18 2014 Jiri Popelka <jpopelka@redhat.com> - 0.9-0.2.beta1
- make it build on armv7
- BuildRequires procps-ng for %%check
- use install instead of cp
- configure.ac: AC_PROG_LIBTOOL -> LT_INIT
- move license files to -libs

* Thu Aug 14 2014 Jiri Popelka <jpopelka@redhat.com> - 0.9-0.1.beta1
- initial spec

