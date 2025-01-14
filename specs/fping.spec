%global _hardened_build 1
#global snapshot 0
%global OWNER schweikert
%global PROJECT fping
%global commit cb832861742f4af5fcadfaf6b2dd19ee0a4b4143
%global commitdate 20250102
%global gittag v5.3
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: fping
Version: 5.3%{?snapshot:^%{commitdate}git%{shortcommit}}
Release: 2%{?dist}
Summary: Scriptable, parallelized ping-like utility
License: BSD-4.3TAHOE
URL: http://www.fping.org/
%if 0%{?snapshot}
Source0: https://github.com/%{OWNER}/%{PROJECT}/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildRequires: autoconf automake
%else
Source0: http://fping.org/dist/%{name}-%{version}.tar.gz
%endif

BuildRequires: gcc
BuildRequires: make

%if "%{_sbindir}" == "%{_bindir}"
# We rely on filesystem to create the compat symlinks for us
Requires: filesystem(unmerged-sbin-symlinks)
Provides: /usr/sbin/fping
%endif

%description
fping is a ping-like program which can determine the accessibility of
multiple hosts using ICMP echo requests. fping is designed for parallelized
monitoring of large numbers of systems, and is developed with ease of
use in scripting in mind.

%prep
%if 0%{?snapshot}
%autosetup -p1 -n %{name}-%{commit}
%else
%autosetup -p1
%endif

%build
%if 0%{?snapshot}
./autogen.sh
%endif
%configure
%make_build

%install
%make_install

%files
%doc CHANGELOG.md
%license COPYING
%attr(0755,root,root) %caps(cap_net_raw=ep) %{_sbindir}/fping
%{_mandir}/man8/*

%changelog
* Sun Jan 12 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.3-2
- Rebuilt for the bin-sbin merge (2nd attempt)

* Fri Jan 03 2025 Charles R. Anderson <cra@alum.wpi.edu> - 5.3-1
- Update to 5.3

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 09 2024 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.2-2
- Rebuilt for the bin-sbin merge

* Sun Apr 21 2024 Charles R. Anderson <cra@alum.wpi.edu> - 5.2-1
- Update to 5.2

* Thu Apr 18 2024 Charles R. Anderson <cra@alum.wpi.edu> - 5.1^20231102gita3f4c57-5
- Provide /usr/sbin/fping (pr#1 for Unify bin and sbin change)
- Convert License tag to SPDX format

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1^20231102gita3f4c57-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1^20231102gita3f4c57-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1^20231102gita3f4c57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov 10 2023 Charles R. Anderson <cra@alum.wpi.edu> - 5.1^20231102gita3f4c57-1
- update to latest git snapshot to see if it fixes fping -n with systemd-resolved

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jan 22 2023 Charles R. Anderson <cra@alum.wpi.edu> - 5.1^20221023git8dc0b7f-1
- update to latest git snapshot to see if it fixes fping -n with systemd-resolved

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 06 2022 Charles R. Anderson <cra@alum.wpi.edu> - 5.1-1
- Update to 5.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 08 2020 Charles R. Anderson <cra@alum.wpi.edu> - 5.0-2
- BR make

* Wed Aug 05 2020 Charles R. Anderson <cra@alum.wpi.edu> - 5.0-1
- Update to 5.0

* Sat Jul 25 2020 Charles R. Anderson <cra@alum.wpi.edu> - 4.4-1
- Update to 4.4

* Tue Jul 21 2020 Charles R. Anderson <cra@alum.wpi.edu> - 4.3-1
- Update to 4.3
- No longer need GCC 10 patch

* Sun Feb  2 2020 Charles R. Anderson <cra@wpi.edu> - 4.2-4
- Patch for GCC 10 requirement to use extern in header files when declaring global variables

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Charles R. Anderson <cra@wpi.edu> - 4.2-1
- update to 4.2
- use %%autosetup, %%make_build, %%make_install macros
- mark COPYING as %%license

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 18 2018 Charles R. Anderson <cra@wpi.edu> - 4.1-1
- update to 4.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Charles R. Anderson <cra@wpi.edu> - 4.0-6
- Add BR gcc
- Remove Group: and rm -rf in install section

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 04 2017 Charles R. Anderson <cra@wpi.edu> - 4.0-2
- remove obsolete CFLAGS

* Wed May 03 2017 Charles R. Anderson <cra@wpi.edu> - 4.0-1
- update to 4.0
- remove EL5 and old Fedora compatibility

* Mon Feb 20 2017 Charles R. Anderson <cra@wpi.edu> - 3.16-1
- update to 3.16 (rhbz#1420733)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Charles R. Anderson <cra@wpi.edu> - 3.15-1
- update to 3.15 (rhbz#1412003)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 24 2015 Charles R. Anderson <cra@wpi.edu> - 3.13-1
- update to 3.13 (rhbz#1271420)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Charles R. Anderson <cra@wpi.edu> - 3.10-1
- update to 3.10 (rhbz#1094411)

* Wed Mar 12 2014 Charles R. Anderson <cra@wpi.edu> - 3.9-1
- update to 3.9 (rhbz#1074890)

* Sat Nov 16 2013 Charles R. Anderson <cra@wpi.edu> - 3.8-1
- update to 3.8 (rhbz#1018121)

* Tue Aug 13 2013 Charles R. Anderson <cra@wpi.edu> - 3.5-3
- enable _hardened_build for -fPIE (rhbz#983602)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 24 2013 Charles R. Anderson <cra@wpi.edu> - 3.5-1
- update to 3.5 (rhbz#925355, rhbz#966000)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 24 2012 Charles R. Anderson <cra@wpi.edu> - 3.4-1
- update to 3.4 which fixes rhbz#854572 by restoring previous behavior:
  * Revert "Output statistics to stdout instead of stderr", because it breaks
    tools assuming the output goes to stderr

* Thu Aug 30 2012 Charles R. Anderson <cra@wpi.edu> - 3.3-2
- use configure options to build ipv4 and ipv6 versions simultaneously
  so we can use the standard make install to get the fping6 man page,
  etc.
- build for el6 w/cap_net_raw (el5 still needs traditional setuid)
- use preferred Buildroot tag for el5
- make conditional build with/without ENABLE_F_OPTION actually work

* Thu Aug 30 2012 Charles R. Anderson <cra@wpi.edu> - 3.3-1
- update to 3.3

* Thu Jul 26 2012 Charles R. Anderson <cra@wpi.edu> - 3.2-1
- update to 3.2
- no longer need capnetraw patch

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Feb 18 2012 Charles R. Anderson <cra@wpi.edu> - 3.0-1
- fping-3.0 based on new upstream at http://www.fping.org/
  - Debian patches until version 2.4b2-to-ipv6-16.
  - Modifications by Tobias Oetiker for SmokePing (2.4b2-to4)
  - Reimplemented main loop for improved performance

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4b2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Sep 04 2011 Charles R. Anderson <cra@wpi.edu> - 2.4b2-12
- remove SUID and add CAP_NET_RAW instead on Fedora 15 and newer (rhbz#646466)
- allow -f option for non-root on Fedora 15 and newer
- remove read permissions on binaries for Fedora 14 and older

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4b2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4b2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4b2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 15 2008 Chris Ricker <kaboom@oobleck.net> 2.4b2-8
- Rebuild for GCC 4.3
- Fix license

* Mon Sep 11 2006 Chris Ricker <kaboom@oobleck.net> 2.4b2-7
- Bump and rebuild

* Tue Feb 14 2006 Chris Ricker <kaboom@oobleck.net> 2.4b2-6
- Bump and rebuild

* Wed Jun 29 2005 Chris Ricker <kaboom@oobleck.net> 2.4b2-5
- Clean up changelog and tags

* Wed Jun 01 2005 Chris Ricker <kaboom@oobleck.net> 2.4b2-4
- Bump release and build

* Wed Jun 01 2005 Chris Ricker <kaboom@oobleck.net> 2.4b2-3
- Add dist tag

* Mon May 16 2005 Chris Ricker <kaboom@oobleck.net> 2.4b2-3
- Simplify doc packaging (Matthias Saou)
- Simplify clean (Matthias Saou)
- Don't strip fping6 binary (Matthias Saou)
- Preserve timestamps

* Wed May 11 2005 Chris Ricker <kaboom@oobleck.net> 2.4b2-2
- Fix URL and Source locations

* Wed Mar 23 2005 Chris Ricker <kaboom@oobleck.net> 2.4b2-1
- Initial package for Fedora
- IPv6 patches from Herbert Xu (Debian)
