# To both save infrastrucutre resources and workaround for i686 FTBFS
ExcludeArch: %{ix86}

Name:           galera
Version:        26.4.20
Release:        2%{?dist}
Summary:        Synchronous multi-master wsrep provider (replication engine)

License:        GPL-2.0-only
URL:            http://galeracluster.com/

# Actually, the truth is, we do use galera source tarball provided by MariaDB on
# following URL (without macros):
#   https://archive.mariadb.org/mariadb-10.4.16/galera-26.4.6/src/galera-26.4.6.tar.gz

Source0:        http://releases.galeracluster.com/source/%{name}-%{version}.tar.gz

Patch0:         cmake_paths.patch
Patch1:         docs.patch
Patch2:         network.patch
Patch3:         openssl_engine.patch

BuildRequires:  boost-devel check-devel openssl-devel cmake systemd gcc-c++ asio-devel
Requires(pre):  /usr/sbin/useradd
Requires:       nmap-ncat
Requires:       procps-ng

%{?systemd_requires}


%description
Galera is a fast synchronous multimaster wsrep provider (replication engine)
for transactional databases and similar applications. For more information
about wsrep API see https://github.com/codership/wsrep-API repository. For a
description of Galera replication engine see https://www.galeracluster.com web.


%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
%{set_build_flags}


%cmake \
       -DCMAKE_BUILD_TYPE="%{?with_debug:Debug}%{!?with_debug:RelWithDebInfo}" \
       -DINSTALL_LAYOUT=RPM \
       -DCMAKE_RULE_MESSAGES:BOOL=OFF \
       \
       -DBUILD_SHARED_LIBS:BOOL=OFF \
       \
       -DINSTALL_DOCDIR="share/doc/%{name}/" \
       -DINSTALL_GARBD="sbin" \
       -DINSTALL_GARBD-SYSTEMD="sbin" \
       -DINSTALL_CONFIGURATION="/etc/sysconfig/" \
       -DINSTALL_SYSTEMD_SERVICE="lib/systemd/system" \
       -DINSTALL_LIBDIR="%{_lib}/galera" \
       -DINSTALL_MANPAGE="share/man/man8"

cmake -B %_vpath_builddir -LAH

%cmake_build


%install
%cmake_install

# PATCH 2:
#   Fix the hardcoded paths
#     In the Systemd service file:
sed -i 's;/usr/bin/garb-systemd;/usr/sbin/garb-systemd;g' %{buildroot}%{_unitdir}/garb.service
#     In the wrapper script:
sed -i 's;/usr/bin/garbd;/usr/sbin/garbd;g' %{buildroot}/usr/sbin/garb-systemd

# PATCH 4:
#  Use a dedicated user for the Systemd service
#  To fix an security issue reported by Systemd:
#
## systemd[1]: /usr/lib/systemd/system/garb.service:14: Special user nobody configured, this is not safe!
##   Subject: Special user nobody configured, this is not safe!
##   Defined-By: systemd
##   Support: https://lists.freedesktop.org/mailman/listinfo/systemd-devel
##   Documentation: https://systemd.io/UIDS-GIDS
##
##   The unit garb.service is configured to use User=nobody.
##
##   This is not safe. The nobody user's main purpose on Linux-based
##   operating systems is to be the owner of files that otherwise cannot be mapped
##   to any local user. It's used by the NFS client and Linux user namespacing,
##   among others. By running a unit's processes under the identity of this user
##   they might possibly get read and even write access to such files that cannot
##   otherwise be mapped.
##
##   It is strongly recommended to avoid running services under this user identity,
##   in particular on systems using NFS or running containers. Allocate a user ID
##   specific to this service, either statically via systemd-sysusers or dynamically
##   via the DynamicUser= service setting.
sed -i 's/User=nobody/User=garb/g' %{buildroot}%{_unitdir}/garb.service
# Maintainers from other distributions also tries to resolve it on the upstream:
#   https://github.com/codership/galera/pull/633


%check
%ctest


%pre
/usr/sbin/useradd -M -r -d /dev/null -s /sbin/nologin -c "Galera Arbitrator Daemon" garb >/dev/null 2>&1 || :
# Fixup after upgrading on system before systemd unit rename
unlink /etc/systemd/system/garb.service || :

%post
/sbin/ldconfig
%systemd_post garb.service

%preun
%systemd_preun garb.service

%postun
/sbin/ldconfig
%systemd_postun_with_restart garb.service


%files
%config(noreplace,missingok) %{_sysconfdir}/sysconfig/garb

%dir %{_docdir}/galera
%dir %{_libdir}/galera

%{_sbindir}/garbd

# PATCH 3:
#   Make sure the wrapper script is executable
%attr(755, -, -) %{_sbindir}/garb-systemd

%{_mandir}/man8/garbd.8*

%{_unitdir}/garb.service

%{_libdir}/galera/libgalera_smm.so

%doc %{_docdir}/galera/COPYING
%doc %{_docdir}/galera/LICENSE.asio
%doc %{_docdir}/galera/README-MySQL


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 26.4.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 14 2024 Michal Schorm <mschorm@redhat.com> - 26.4.20-1
- Rebase to 26.4.20

* Fri Oct 18 2024 Michal Schorm <mschorm@redhat.com> - 26.4.19-1
- Rebase to 26.4.19

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 26.4.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Michal Schorm <mschorm@redhat.com> - 26.4.18-3
- Bump release for package rebuild

* Sun Jun 09 2024 Michal Schorm <mschorm@redhat.com> - 26.4.18-2
- Bump release for package rebuild

* Fri Jun 07 2024 Michal Schorm <mschorm@redhat.com> - 26.4.18-1
- Rebase to 26.4.18

* Wed Jan 24 2024 Michal Schorm <mschorm@redhat.com> - 26.4.16-4
- Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 26.4.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 26.4.16-2
- Rebuilt for Boost 1.83

* Fri Nov 17 2023 Michal Schorm <mschorm@redhat.com> - 26.4.16-1
- Rebase to 26.4.16

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 26.4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Apr 29 2023 Michal Schorm <mschorm@redhat.com> - 26.4.14-1
- Rebase to 26.4.14

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 26.4.13-3
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 26.4.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 15 2022 Michal Schorm <mschorm@redhat.com> - 26.4.13-1
- Rebase to 26.4.13

* Wed Aug 24 2022 Michal Schorm <mschorm@redhat.com> - 26.4.12-1
- Rebase to 26.4.12

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 26.4.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 26.4.11-2
- Rebuilt for Boost 1.78

* Sun Feb 20 2022 Michal Schorm <mschorm@redhat.com> - 26.4.11-1
- Rebase to 26.4.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 26.4.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 19 2021 Lukas Javorsky <ljavorsk@redhat.com> - 26.4.9-3
- Explicitly require the 'procps-ng' package
- Otherwise it will not require it in the lightweight systems (e.g. containers)
- and Galera won't work properly

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 26.4.9-2
- Rebuilt with OpenSSL 3.0.0

* Sat Aug 07 2021 Michal Schorm <mschorm@redhat.com> - 26.4.9-1
- Rebase to 26.4.9

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 26.4.8-4
- Rebuilt for Boost 1.76

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 26.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 15 2021 Michal Schorm <mschorm@redhat.com> - 26.4.8-2
- Switch from SCONS build tooling to CMAKE build tooling
- Use upstream variants of Systemd service file and Systemd service file wrapper srcipt

* Thu Jun 03 2021 Lukas Javorsky <ljavorsk@redhat.com> - 26.4.8-1
- Rebase to 26.4.8

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 26.4.7-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Feb 23 2021 Michal Schorm <mschorm@redhat.com> - 26.4.7-1
- Rebase to 26.4.7

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 26.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 26.4.6-2
- Rebuilt for Boost 1.75

* Wed Nov 04 2020 Michal Schorm <mschorm@redhat.com> - 26.4.6-1
- Rebase to 26.4.6

* Thu Sep 17 2020 Michal Schorm <mschorm@redhat.com> - 26.4.5-2
- Extend the workaround also to ELN

* Wed Sep 16 2020 Michal Schorm <mschorm@redhat.com> - 26.4.5-1
- Rebase to 26.4.5

* Wed Sep 16 2020 Michal Schorm <mschorm@redhat.com> - 26.4.4-5
- Apply workaround for FTBFS on F33+

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 26.4.4-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 26.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 08 2020 Michal Schorm <mschorm@redhat.com> - 26.4.4-2
- Second rebuild for Boost 1.73

* Fri Jun 05 2020 Michal Schorm <mschorm@redhat.com> - 26.4.4-1
- Rebase to 26.4.4
  Resolves: rhbz#1546787

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 26.4.3-4
- Rebuilt for Boost 1.73

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 26.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Michal Schorm <mschorm@redhat.com> - 26.4.3-2
- Rebase to 26.4.3

* Wed Nov 06 2019 Michal Schorm <mschorm@redhat.com> - 25.3.28-1
- Rebase to 25.3.28

* Thu Aug 01 2019 Michal Schorm <mschorm@redhat.com> - 25.3.26-3
- Fix for #1735233 and #1737108

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 25.3.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Michal Schorm <mschorm@redhat.com> - 25.3.26-1
- Rebase to 25.3.26

* Fri Jul 19 2019 Michal Schorm <mschorm@redhat.com> - 25.3.25-4
- Use macro for setting up the compiler flags

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 25.3.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Jonathan Wakely <jwakely@redhat.com> - 25.3.25-2
- Rebuilt for Boost 1.69

* Tue Jan 01 2019 Michal Schorm <mschorm@redhat.com> - 25.3.25-1
- Rebase to 25.3.25

* Mon Jul 16 2018 Honza Horak <hhorak@redhat.com> - 25.3.23-5
- Require asio also on rhel

* Fri Jul 13 2018 Honza Horak <hhorak@redhat.com> - 25.3.23-4
- Add explicit gcc-c++ BR
- Use python3-scons

* Fri Jul 13 2018 Honza Horak <hhorak@redhat.com> - 25.3.23-3
- Do not require asio on rhel

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 25.3.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 16 2018 Michal Schorm <mschorm@redhat.com> - 25.3.23-1
- Update to 25.3.23

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 25.3.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 24 2017 Honza Horak <hhorak@redhat.com> - 25.3.22-1
- Update to 25.3.22

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 25.3.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 25.3.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 25.3.16-4
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 25.3.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 18 2017 Jonathan Wakely <jwakely@redhat.com> - 25.3.16-2
- Use asio-devel instead of bundled asio library

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 25.3.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 22 2016 Mike Bayer <mbayer@redhat.com> - 25.3.16-1
- Update to 25.3.16

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 25.3.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 25.3.12-3
- Rebuilt for Boost 1.60

* Wed Sep 30 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 25.3.12-2
- Remove use of -mtune=native which breaks build on secondary architectures

* Fri Sep 25 2015 Richard W.M. Jones <rjones@redhat.com> - 25.3.12-1
- Update to 25.3.12.
- Should fix the build on 32 bit ARM (RHBZ#1241164).
- Remove ExcludeArch (should have read the BZ more closely).

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 25.3.10-5
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 25.3.10-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 25.3.10-3
- rebuild for Boost 1.58

* Wed Jul 08 2015 Ryan O'Hara <rohara@redhat.com> - 25.3.10-2
- Disable ARM builds (#1241164, #1239516)

* Mon Jul 06 2015 Ryan O'Hara <rohara@redhat.com> - 25.3.10-1
- Update to version 25.3.10

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 25.3.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 25.3.5-10
- Rebuild for boost 1.57.0

* Thu Nov 27 2014 Richard W.M. Jones <rjones@redhat.com> - 25.3.5-9
- Add aarch64 support.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 25.3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 25.3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 25.3.5-6
- Rebuild for boost 1.55.0

* Wed Apr 30 2014 Dan Horák <dan[at]danny.cz> - 25.3.5-5
- set ExclusiveArch

* Thu Apr 24 2014 Ryan O'Hara <rohara@redhat.com> - 25.3.5-4
- Use strict_build_flags=0 to avoid -Werror
- Remove unnecessary clean section

* Thu Apr 24 2014 Ryan O'Hara <rohara@redhat.com> - 25.3.5-3
- Include galera directories in file list
- Set CPPFLAGS to optflags

* Wed Apr 23 2014 Ryan O'Hara <rohara@redhat.com> - 25.3.5-2
- Fix client certificate verification (#1090604)

* Thu Mar 27 2014 Ryan O'Hara <rohara@redhat.com> - 25.3.5-1
- Update to version 25.3.5

* Mon Mar 24 2014 Ryan O'Hara <rohara@redhat.com> - 25.3.3-2
- Add systemd service

* Sun Mar 09 2014 Ryan O'Hara <rohara@redhat.com> - 25.3.3-1
- Initial build
