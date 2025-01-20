Name:          rtorrent
# OpenSSL exception, see README
# Automatically converted from old format: GPLv2+ with exceptions - review is highly recommended.
License:       LicenseRef-Callaway-GPLv2+-with-exceptions
Version:       0.15.1
Release:       2%{?dist}
Summary:       BitTorrent client based on libtorrent 
URL:           https://github.com/rakshasa/rtorrent
Source0:       https://github.com/rakshasa/rtorrent/releases/download/v%{version}/rtorrent-%{version}.tar.gz
Source1:       rtorrent.1

BuildRequires: make
BuildRequires: curl-devel
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel
BuildRequires: libsigc++20-devel
BuildRequires: libtorrent-devel >= 0.15.1
BuildRequires: ncurses-devel
BuildRequires: pkgconfig
BuildRequires: xmlrpc-c-devel

%description
A BitTorrent client using libtorrent, which on high-bandwidth connections is 
able to seed at 3 times the speed of the official client. Using
ncurses its ideal for use with screen or dtach. It supports 
saving of sessions and allows the user to add and remove torrents and scanning
of directories for torrent files to seed and/or download.

%prep
%autosetup -p0
for file in AUTHORS README doc/rtorrent.rc COPYING
do
    chmod -x "$file"
done

# Avoid an attempt to re-run autoconf.
touch -r aclocal.m4 scripts/common.m4

%build
%configure --with-xmlrpc-c --enable-ipv6
%make_build

%install
%make_install
install -Dpm 0644 %SOURCE1 %{buildroot}/%{_mandir}/man1/rtorrent.1

%files
%doc AUTHORS README doc/rtorrent.rc
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/rtorrent.1.gz

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jan 04 2025 Conrad Meyer <cse.cem@gmail.com> - 0.15.1-1
- Update to 0.15.1

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.8-17
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 08 2023 Florian Weimer <fweimer@redhat.com> - 0.9.8-13
- C compatibility fix for the configure script

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 19 2023 Conrad Meyer <cse.cem@gmail.com> - 0.9.8-11
- Patch for rhbz# 2188136 snprintf misuse

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 05 2021 Denis Fateyev <denis@fateyev.com> - 0.9.8-7
- Add missing "rtorrent.1" man-file

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 09 2019 Denis Fateyev <denis@fateyev.com> - 0.9.8-1
- Update to 0.9.8 version

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 21 2018 Vasiliy N. Glazov <vascom2@gmail.com>  - 0.9.7-4
- Clean spec

* Fri Jul 20 2018 Conrad Meyer <cemeyer@uw.edu> - 0.9.7-3
- Add now-missing BR on gcc-c++

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 10 2018 Conrad Meyer <cemeyer@uw.edu> - 0.9.7-1
- Bump to latest upstream release (rhbz# 1588472)
- Drop special views patch (# 1354125); now fixed in 0.9.7

* Sun May 06 2018 Conrad Meyer <cemeyer@uw.edu> - 0.9.6-11
- rhbz# 1575228: Enable ipv6 (will be enabled non-optionally in a subsequent release)

* Sat Apr 28 2018 Conrad Meyer <cemeyer@uw.edu> - 0.9.6-10
- rhbz# 1354125: Backport of upstream issue #449 fix

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.9.6-4
- Rebuild for xmlrpc-c

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 22 2015 Conrad Meyer <cemeyer@uw.edu> - 0.9.6-2
- Add explicit BR on libtorrent 0.13.6

* Sat Sep 19 2015 Conrad Meyer <cemeyer@uw.edu> - 0.9.6-1
- Bump to latest upstream release
- Drop now-broken AArch64 patch

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.4-4
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.9.4-1
- Update to latest upstream release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 24 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.9.3-5
- Add patch for ARM 64 build support
- https://bugzilla.redhat.com/show_bug.cgi?id=926462

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 25 2012 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.9.3-3
- Remove traces of man page from spec.

* Thu Oct 25 2012 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.9.3-2
- Upstream removed man page. Removing from files

* Thu Oct 25 2012 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.9.3-1
- Update to latest upstream release (#869534)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.9.2-1
- Update to 0.9.2

* Tue Apr 03 2012 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.9.1-2
- Update patch

* Tue Apr 03 2012 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.9.1-1
- Update to latest upstream release

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-3
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 18 2011 Conrad Meyer <konrad@tylerc.org> - 0.9.0-1
- bump to latest upstream

* Sat Jul 2 2011 Conrad Meyer <konrad@tylerc.org> - 0.8.9-1
- bump to latest upstream

* Thu May 26 2011 Conrad Meyer <konrad@tylerc.org> - 0.8.8-1
- bump to latest upstream

* Sat Mar 5 2011 Conrad Meyer <konrad@tylerc.org> - 0.8.7-6
- Fix bad usage of ncurses

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 12 2011 Conrad Meyer <konrad@tylerc.org> - 0.8.7-4
- Adopt insecure SSL patch (as commandline option) (#669251)

* Thu Oct 28 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.7-3
- manually install the man page to correct location

* Wed Oct 27 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.7-2
- updated FTBFS patch for new version

* Wed Oct 27 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.7-1
- Update to latest upstream release
- #646981

* Fri Oct 15 2010 Michel Salim <salimma@fedoraproject.org> - 0.8.6-4
- document fallocate option (# 466548)
- send patches upstream, link to bug reports in spec file

* Sun Feb 14 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.6-3
- fix FTBFS

* Sun Feb 14 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.6-2
- add patch to add libxmlrpc for FTBFS fix 
- # 564688

* Tue Dec 15 2009 Conrad Meyer <konrad@tylerc.org> - 0.8.6-1
- Bump version.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 3 2009 Conrad Meyer <konrad@tylerc.org> - 0.8.5-1
- Bump version.

* Mon May 11 2009 Conrad Meyer <konrad@tylerc.org> - 0.8.4-4
- Use normal Fedora build flags.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 2 2008 Conrad Meyer <konrad@tylerc.org> - 0.8.4-2
- Add --with-xmlrpc-c to configure.

* Wed Nov 26 2008 Conrad Meyer <konrad@tylerc.org> - 0.8.4-1
- Bump to 0.8.4.

* Tue Nov 18 2008 Conrad Meyer <konrad@tylerc.org> - 0.8.3-1
- Bump version.

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.7.8-4
- fix license tag

* Sat Apr  5 2008 Christopher Aillon <caillon@redhat.com> - 0.7.8-3
- Fix build against newer sigc++
- Fix build against GCC 4.3

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.7.8-2
- Autorebuild for GCC 4.3

* Tue Sep 18 2007 Marek Mahut <mmahut fedoraproject.org> - 0.7.8-1
- New upstream release

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.7.4-3
- Rebuild for selinux ppc32 issue.

* Thu Jun 28 2007 Chris Chabot <chabotc@xs4all.nl> - 0.7.4-2
- Fixed BR

* Thu Jun 28 2007 Chris Chabot <chabotc@xs4all.nl> - 0.7.4-1
- New upstream release

* Sun Nov 26 2006 Chris Chabot <chabotc@xs4all.nl> - 0.6.4-1
- New upstream version
- Compile with -Os to work around a gcc 4.1 incompatibility

* Mon Nov 06 2006 Jindrich Novy <jnovy@redhat.com> - 0.6.2-5
- rebuild against new curl

* Fri Sep 29 2006 Chris Chabot <chabotc@xs4all.nl> - 0.6.2-4
- re-tag

* Fri Sep 29 2006 Chris Chabot <chabotc@xs4all.nl> - 0.6.2-3
- re-tag

* Fri Sep 29 2006 Chris Chabot <chabotc@xs4all.nl> - 0.6.2-2
- New upstream version

* Mon Sep 11 2006 Chris Chabot <chabotc@xs4all.nl> - 0.6.0-2
- FC6 rebuild

* Sun Aug 13 2006 Chris Chabot <chabotc@xs4all.nl> - 0.6.0-1
- Upgrade to 0.6.0

* Sat Jun 17 2006 - Chris Chabot <chabotc@xs4all.nl> - 0.5.3-1
- Upgrade to new upstream version 0.5.3
- And changed libtorrent dependency to >= 0.9.3

* Sat Jan 14 2006 - Chris Chabot <chabotc@xs4all.nl> - 0.4.2-3
- Added ncurses-devel to buildrequirements

* Sat Jan 14 2006 - Chris Chabot <chabotc@xs4all.nl> - 0.4.2-2
- Improved summary & description
- Removed explicit requires, leaving to rpm
- Changed mode of rtorrent.rc.example to 644

* Wed Jan 11 2006 - Chris Chabot <chabotc@xs4all.nl> - 0.4.2-1
- Initial version
