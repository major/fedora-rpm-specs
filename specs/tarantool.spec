BuildRequires: cmake >= 2.8
BuildRequires: gcc >= 4.5
BuildRequires: gcc-c++ >= 4.5
BuildRequires: coreutils
BuildRequires: sed
BuildRequires: readline-devel
BuildRequires: openssl-devel
BuildRequires: libcurl-devel
BuildRequires: libicu-devel
BuildRequires: libzstd-devel
BuildRequires: perl-podlators
Requires(pre): %{_sbindir}/useradd
Requires(pre): %{_sbindir}/groupadd
Requires: logrotate

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires: systemd

Name: tarantool
Version: 2.4.2.68
Release: 21%{?dist}
Summary: In-Memory Database
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: https://tarantool.org/
# Add dependency on network configuration files used by `socket` module
# https://github.com/tarantool/tarantool/issues/1794
Requires: /etc/protocols
Requires: /etc/services
# Deps for built-in package manager
# https://github.com/tarantool/tarantool/issues/2612
Requires: openssl
Requires: curl
Recommends: tarantool-devel
Recommends: git-core
Recommends: cmake >= 2.8
Recommends: make
Recommends: gcc >= 4.5
Recommends: gcc-c++ >= 4.5
Source0: http://download.tarantool.org/tarantool/2.4/src/tarantool-%{version}.tar.gz
Patch0: 10-rundir.patch
ExclusiveArch: %{ix86} x86_64
%description
Tarantool is an open-source database that can store everything in RAM.
You can use it as a cache with on-disk persistence. Tarantool is able to
process up to 1 million RPS and supports SQL and secondary index searching.

In Tarantool, you can run your code at the same place where your data is.
That speeds up all the operations. Apply any business logic in Lua programming
language. Get rid of the outdated database records. Synchronize with other
data sources. Implement HTTP-service.

This package provides the server daemon and admin tools.

%package devel
Summary: Server development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Tarantool is an open-source database that can store everything in RAM.
You can use it as a cache with on-disk persistence. Tarantool is able to
process up to 1 million RPS and supports SQL and secondary index searching.

In Tarantool, you can run your code at the same place where your data is.
That speeds up all the operations. Apply any business logic in Lua programming
language. Get rid of the outdated database records. Synchronize with other
data sources. Implement HTTP-service.

This package provides server development files needed to create
C and Lua/C modules.

%prep
%setup -q -n %{name}-%{version}
%patch -P0 -p1

%build
# RHBZ #1301720: SYSCONFDIR an LOCALSTATEDIR must be specified explicitly
%cmake . -DCMAKE_BUILD_TYPE=RelWithDebInfo \
         -DCMAKE_INSTALL_LOCALSTATEDIR:PATH=%{_localstatedir} \
         -DCMAKE_INSTALL_SYSCONFDIR:PATH=%{_sysconfdir} \
         -DENABLE_BUNDLED_LIBYAML:BOOL=ON \
         -DENABLE_BUNDLED_MSGPUCK:BOOL=ON \
         -DENABLE_BUNDLED_LIBCURL:BOOL=OFF \
         -DENABLE_BUNDLED_ZSTD:BOOL=OFF \
         -DENABLE_BACKTRACE:BOOL=OFF \
         -DWITH_SYSTEMD:BOOL=ON \
         -DSYSTEMD_UNIT_DIR:PATH=%{_unitdir} \
         -DSYSTEMD_TMPFILES_DIR:PATH=%{_tmpfilesdir} \
         -DENABLE_DIST:BOOL=ON
%cmake_build --target tarantool api man-tarantool man-tarantoolctl

%install
%cmake_install
# %%doc and %%license macroses are used instead
rm -rf %{buildroot}%{_datarootdir}/doc/tarantool/

%check
%ctest

%pre
/usr/sbin/groupadd -r tarantool > /dev/null 2>&1 || :
/usr/sbin/useradd -M -N -g tarantool -r -d /var/lib/tarantool -s /sbin/nologin\
    -c "Tarantool Server" tarantool > /dev/null 2>&1 || :

%post
%tmpfiles_create tarantool.conf
%systemd_post 'tarantool@.service'

%preun
# Sic: doesn't work
#systemd_preun 'tarantool@*.service'

%postun
%systemd_postun_with_restart 'tarantool@*.service'

%files
%{_bindir}/tarantool
%{_mandir}/man1/tarantool.1*
%doc README.md
%license LICENSE AUTHORS
# tarantool package should own module directories
%dir %{_libdir}/tarantool
%dir %{_datadir}/tarantool
%{_datadir}/tarantool/luarocks
%{_bindir}/tarantoolctl
%{_mandir}/man1/tarantoolctl.1*
%config(noreplace) %{_sysconfdir}/sysconfig/tarantool
%dir %{_sysconfdir}/tarantool
%dir %{_sysconfdir}/tarantool/instances.available
%config(noreplace) %{_sysconfdir}/tarantool/instances.available/example.lua
%attr(-,tarantool,tarantool) %dir %{_localstatedir}/lib/tarantool/
%attr(-,tarantool,tarantool) %dir %{_localstatedir}/log/tarantool/
%config(noreplace) %{_sysconfdir}/logrotate.d/tarantool
%{_unitdir}/tarantool@.service
%{_tmpfilesdir}/tarantool.conf

%files devel
%dir %{_includedir}/tarantool
%{_includedir}/tarantool/lauxlib.h
%{_includedir}/tarantool/luaconf.h
%{_includedir}/tarantool/lua.h
%{_includedir}/tarantool/lua.hpp
%{_includedir}/tarantool/luajit.h
%{_includedir}/tarantool/lualib.h
%{_includedir}/tarantool/module.h

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2.68-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Pete Walter <pwalter@fedoraproject.org> - 2.4.2.68-20
- Rebuild for ICU 76

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.2.68-19
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2.68-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 2.4.2.68-17
- Rebuild for ICU 74

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2.68-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2.68-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 2.4.2.68-14
- Rebuilt for ICU 73.2

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2.68-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 2.4.2.68-12
- Rebuild for ICU 72

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.4.2.68-11
- Rebuilt for ICU 71.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2.68-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2.68-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.4.2.68-8
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2.68-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 2.4.2.68-6
- Rebuild for ICU 69

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 2.4.2.68-5
- Rebuild for ICU 69

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.4.2.68-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2.68-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 22 2020 Roman Tsisyk <rtsisyk@fedoraproject.org> - 2.4.2.68-2
- Use 755 for /var/lib/tarantool and /var/log/tarntool.
- Fix /run directory.
- Fix systemd invocations.
- Disable bundled curl.
- Disable bundled zstd.
- Fix rpmlint warnings.
- Speed up build.

* Sat Sep 19 2020 Roman Tsisyk <rtsisyk@fedoraproject.org> - 2.4.2.68-1
- New minor release.
- Use `cmake_build` && `cmake_install` instead of `make` && `make install`.
- Update description from the official web-site.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2.62-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2.62-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 15 2020 Pete Walter <pwalter@fedoraproject.org> - 2.2.2.62-2
- Rebuild for ICU 67

* Thu Mar 19 2020 Roman Tsisyk <rtsisyk@fedoraproject.org> - 2.2.2.62-1
- New minor release.
- Disable python2-based tests.
- Drop ARM support - upstream doesn't support it.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2.54-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 03 2019 Roman Tsisyk <rtsisyk@fedoraproject.org> - 2.1.2.54-1
- New major release.

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.7.5.0-5
- Rebuild for readline 8.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 24 2017 Roman Tsisyk <roman@tarantool.org> 1.7.5.0-1
- Stabilization of Vinyl storage engine.
- Improved MemTX TREE iterators.
- Better replication monitoring.
- WAL tracking for remote replicas on master.
- Automatic snapshots every hour.
- Lua API to create consistent backups.
- Hot code reload for stored C procedures.
- New built-in rocks: 'http.client', 'iconv' and 'pwd'.
- Lua 5.1 command line options.
- LuaRocks-based package manager.
- Stack traces support in fiber.info().
- New names for box.cfg() options.
- Hot standy mode is now off by default.
- Support for UNIX pipes in tarantoolctl.
- Non-blocking syslog logger.
- Improved systemd integration.
- Hundrends of bugs fixed, see GitHub release notes for details:
  https://github.com/tarantool/tarantool/releases/tag/1.7.5

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2.428-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2.428-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2.428-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2.428-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.7.2.428-2
- Rebuild for readline 7.x

* Wed Dec 21 2016 Roman Tsisyk <roman@tarantool.org> 1.7.2.428-1
- Fix failing tests on armv7hl

* Fri Dec 16 2016 Roman Tsisyk <roman@tarantool.org> 1.7.2.396-1
- Add `tarantoolctl cat/play` commands and `xlog` Lua module.
- Add Lua library to manipulate environment variables.
- Allow DML requests from on_replace triggers.
- Allow UPSERT without operations.
- Improve support for the large number of active network clients.
- Fix race conditions during automatic cluster bootstrap.
- Fix calculation of periods in snapshot daemon.
- Fix handling of iterator type in space:pairs() and space:select().
- Fix CVE-2016-9036 and CVE-2016-9037.
- Dozens of bug fixes to Vinyl storage engine.
- Remove broken coredump() Lua function.

* Tue Oct 04 2016 Roman Tsisyk <roman@tarantool.org> 1.7.2.11-1
- Fix failing tests on armv7hl

* Thu Sep 29 2016 Roman Tsisyk <roman@tarantool.org> 1.7.2.4-1
- Vinyl - a new write-optimized storage engine, allowing the amount of
  data stored to exceed the amount of available RAM 10-100x times.
- A new binary protocol command for CALL, which no more restricts a function
  to returning an array of tuples and allows returning an arbitrary
  MsgPack/JSON result, including scalars, nil and void (nothing).
- Automatic replication cluster bootstrap; it's now much easier to configure
  a new replication cluster.
- New indexable data types: unsigned, integer, number and scalar.
- memtx snapshots and xlog files are now compressed on the fly using the
  fast ZStandard compression algorithm. Compression options are configured
  automatically to get an optimal trade-off between CPU utilization and disk
  throughput.
- fiber.cond() - a new synchronization mechanism for fibers.
- Tab-based autocompletion in the interactive console.
- A new implementation of net.box improving performance and solving
  problems with the garbage collection of dead connections.
- Native systemd integration alongside sysvinit.
- A ready-to-use 'example.lua' instance enable by default.
- Dozens of bugfixes:
   https://github.com/tarantool/tarantool/issues?q=milestone%3A1.7.2+is%3Aclosed

* Wed Sep 28 2016 Roman Tsisyk <roman@tarantool.org> 1.6.9.11-1
- Add dependency on network configuration files used by `socket` module

* Mon Sep 26 2016 Roman Tsisyk <roman@tarantool.org> 1.6.9.1-1
- Tab-based autocompletion in the interactive console
- LUA_PATH and LUA_CPATH environment variables taken into account
- A new box.cfg { read_only = true } option
- Upgrade script for 1.6.4 -> 1.6.8 -> 1.6.9
- Bugs fixed:
   https://github.com/tarantool/tarantool/issues?q=milestone%3A1.6.9+is%3Aclosed

* Thu Sep 01 2016 Roman Tsisyk <roman@tarantool.org> 1.6.8.762-1
- Add support for OpenSSL 1.1

* Sun Feb 28 2016 Roman Tsisyk <roman@tarantool.org> 1.6.8.530-2
- Add ExclusiveArch (#1293100)

* Sat Feb 27 2016 Roman Tsisyk <roman@tarantool.org> 1.6.8.530-1
- Update to the latest 1.6.8 release
- Add missing gcc-g++ BuildRequires

* Fri Feb 19 2016 Roman Tsisyk <roman@tarantool.org> 1.6.8.508-1
- Fix stack overflow in Sophia on armv7l

* Thu Feb 18 2016 Roman Tsisyk <roman@tarantool.org> 1.6.8.504-1
- tarantool package now owns module directories

* Tue Feb 09 2016 Roman Tsisyk <roman@tarantool.org> 1.6.8.462-1
- Enable tests

* Fri Feb 05 2016 Roman Tsisyk <roman@tarantool.org> 1.6.8.451-1
- Add coreutils, make and sed to BuildRequires

* Wed Feb 03 2016 Roman Tsisyk <roman@tarantool.org> 1.6.8.433-1
- Obsolete tarantool-common package

* Thu Jan 21 2016 Roman Tsisyk <roman@tarantool.org> 1.6.8.376-1
- Implement proper support of multi-instance management using systemd

* Sat Jan 9 2016 Roman Tsisyk <roman@tarantool.org> 1.6.8.0-1
- Change naming scheme to include a postrelease number to Version
- Fix arch-specific paths in tarantool-common
- Rename tarantool-dev to tarantool-devel
- Use system libyaml
- Remove Vendor
- Remove SCL support
- Remove devtoolkit support
- Remove Lua scripts
- Remove quotes from %%files
- Disable hardening to fix backtraces
- Fix permissions for tarantoolctl directories
- Comply with http://fedoraproject.org/wiki/Packaging:DistTag
- Comply with http://fedoraproject.org/wiki/Packaging:LicensingGuidelines
- Comply with http://fedoraproject.org/wiki/Packaging:Tmpfiles.d
- Comply with the policy for log files
- Comply with the policy for man pages
- Other changes according to #1293100 review

* Tue Apr 28 2015 Roman Tsisyk <roman@tarantool.org> 1.6.5.0-1
- Remove sql-module, pg-module, mysql-module

* Fri Jun 06 2014 Eugine Blikh <bigbes@tarantool.org> 1.6.3.0-1
- Add SCL support
- Add --with support
- Add dependencies

* Mon May 20 2013 Dmitry Simonenko <support@tarantool.org> 1.5.1.0-1
- Initial version of the RPM spec
