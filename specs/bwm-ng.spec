Name:           bwm-ng
Version:        0.6.3
Release:        5%{?dist}
Summary:        Bandwidth Monitor NG
License:        GPL-2.0-or-later
URL:            https://github.com/vgropp/bwm-ng
Source0:        https://github.com/vgropp/%{name}/archive/v%{version}.tar.gz
Source1:        bwm-ng.conf
Patch0:         0001-fix-format-not-a-string-literal.patch
Patch1:         0002-fix-use-after-free-in-proc_diskstats-on-error.patch
Patch2:         0003-fix-missing-device-number-in-fbsd-devstat-input.patch
Patch3:         0004-fix-multiple-fflush-might-miss-some-branch-and-html-.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  make
Requires:       hostname
Requires:       procps

%description
A small and simple console-based live network and disk io bandwidth monitor.

Features:
- Supports /proc/net/dev, netstat, getifaddr, sysctl, kstat, /proc/diskstats 
/proc/partitions, IOKit, devstat and libstatgrab
- Unlimited number of interfaces/devices supported
- Interfaces/devices are added or removed dynamically from list
- White-/blacklist of interfaces/devices
- Output of KB/s, Kb/s, packets, errors, average, max and total sum
- Output in curses, plain console, CSV or HTML
- Configfile

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
./autogen.sh
%configure --enable-64bit \
           --enable-netstatbyte \
           --enable-netstatlink \
           --with-ncurses \
           --with-time \
           --with-getopt_long \
           --with-getifaddrs \
           --with-sysctl \
           --with-procnetdev \
           --with-netstatlinux \
           --without-strip
make %{?_smp_mflags}

%install
install -pDm755 src/bwm-ng %{buildroot}%{_bindir}/bwm-ng
install -pDm644 %{SOURCE1} %{buildroot}%{_sysconfdir}/bwm-ng.conf
install -pDm644 bwm-ng.1 %{buildroot}%{_mandir}/man1/bwm-ng.1

%files
%doc AUTHORS README ChangeLog bwm-ng.conf-example bwm-ng.css
%config(noreplace) %{_sysconfdir}/bwm-ng.conf
%{_bindir}/bwm-ng
%{_mandir}/man1/bwm-ng.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Feb 24 2023 Tim Orling <ticotimo@gmail.com> - 0.6.3-1
- Update to 0.6.3 (rhbz 2113135)
- Drop C99 patch (was https://github.com/vgropp/bwm-ng/pull/25)
- Add patch from 'fix-wsecurity' PR (https://github.com/vgropp/bwm-ng/pull/37)
- Add patches from 'fix-freebsd' PR (https://github.com/vgropp/bwm-ng/pull/42)
- Drop .rpmlint (filters not used)

* Fri Feb 24 2023 Tim Orling <ticotimo@gmail.com> - 0.6.2-9
- migrated to SPDX license

* Thu Feb 02 2023 Jonathan Wakely <jwakely@redhat.com> - 0.6.2-8
- Patched configure checks for C99 compatibility

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 2020 Sven Lankes <sven@lank.es> - 0.6.2-1
- new upstream release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Tim Orling <ticotimo@gmail.com> - 0.6.1-7
- Add BuildRequires: autoconf automake gcc
- Add static inline patch
- Add .rpmlint
Resolves: rhbz#1423286 bwm-ng: FTBFS in rawhide

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 16 2016 Sven Lankes <sven@lank.es> - 0.6.1-2
- update conf to reflect default input change

* Tue Feb 16 2016 Sven Lankes <sven@lank.es> - 0.6.1-1
- new upstream release
- remove upstreamed patch
- remove dependency on libstatgrab (no longer default upstream)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 17 2015 Kalev Lember <klember@redhat.com> - 0.6-19
- Rebuilt for libstatgrab soname bump

* Fri Jun 19 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.6-18
- Append --stdc=gnu89 to CFLAGS (Work-around to c11/inline compatibility
  issues. Fix FTBFS).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 03 2014 Christopher Meng <rpm@cicku.me> - 0.6-14
- Fix gcc dumb security check issue.

* Sun Oct 13 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.6-13
- Fix spec-file corruption caused by previous patch.

* Mon Sep 16 2013 Christopher Meng <rpm@cicku.me> - 0.6-12
- Rebuild for libstatgrab(BZ#1008278).

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 24 2012 Oliver Falk <oliver@linux-kernel.at> - 0.6-8
- Require hostname instead of net-tools (BZ#784368)

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 13 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> - 0.6-3
- Bump-n-build for GCC 4.3

* Tue Aug 21 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> - 0.6-2
- Rebuild for BuildID
- License clarification 

* Fri Mar 16 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> - 0.6-1
- Update
- Filename change: changelog -> ChangeLog
- Removed tag at start of spec (since I don't use it)

* Thu Jan 25 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> - 0.5-9
- Added noreplace to config, as per rpmlint warning
- Removed a couple spaces which triggered spaces/tabs rpmlint warning
- Fixed project URL

* Wed Oct 04 2006 Patrick "Jima" Laughton <jima@beer.tclug.org> - 0.5-8
- Bump-n-build

* Tue Sep 19 2006 Patrick "Jima" Laughton <jima@beer.tclug.org> - 0.5-7
- Bump for FC6 rebuild

* Fri Aug 12 2005 Oliver Falk <oliver@linux-kernel.at> - 0.5-6
- Rebuild against libstatgrab 0.12

* Thu Jul 14 2005 Oliver Falk <oliver@linux-kernel.at> - 0.5-5
- Integrated Matthias changes, after his review

* Thu May 19 2005 Oliver Falk <oliver@linux-kernel.at> - 0.5-4.2
- Specfile cleanup

* Fri Mar 25 2005 Oliver Falk <oliver@linux-kernel.at> - 0.5-4.1
- Check with lint says: bwm-ng hardcoded-packager-tag Oliver: FIXED

* Wed Mar 16 2005 Oliver Falk <oliver@linux-kernel.at> - 0.5-4
- Fix, still build pre1 :-/

* Wed Mar 16 2005 Oliver Falk <oliver@linux-kernel.at> - 0.5-3
- Update to real 0.5, not only 0.5pre1

* Tue Feb 15 2005 Oliver Falk <oliver@linux-kernel.at> - 0.5-2
- Make use of libstatgrab, by using it in the default config

* Tue Feb 15 2005 Oliver Falk <oliver@linux-kernel.at> - 0.5-1
- Fix warnings spotted by rpmlint
- Update
- Update dependencies and add various configure switches, so this
  little thingy is no longer _little_ :-)

* Tue Oct 19 2004 Oliver Falk <oliver@linux-kernel.at> - 0.4-pre1-1
- Initial package

