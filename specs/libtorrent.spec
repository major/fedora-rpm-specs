Name:          libtorrent
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
Version:       0.15.1
Release:       1%{?dist}
Summary:       BitTorrent library with a focus on high performance & good code
URL:           https://github.com/rakshasa/libtorrent/
Source0:       https://github.com/rakshasa/rtorrent/releases/download/v%{version}/libtorrent-%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libsigc++20-devel
BuildRequires: libtool
BuildRequires: openssl-devel
BuildRequires: pkgconfig
BuildRequires: zlib-devel
BuildRequires: make

%description
LibTorrent is a BitTorrent library written in C++ for *nix, with a focus 
on high performance and good code. The library differentiates itself 
from other implementations by transfering directly from file pages to 
the network stack. On high-bandwidth connections it is able to seed at 
3 times the speed of the official client.

%package devel
Summary: Libtorrent development environment
Requires: %{name} = %{version}-%{release}

%description devel
Header and library definition files for developing applications
with the libtorrent libraries.

%prep
%autosetup -p1

%build
%configure --with-posix-fallocate
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc AUTHORS README
%license COPYING
%{_libdir}/libtorrent.so.*

%files devel
%{_libdir}/pkgconfig/libtorrent.pc
%{_includedir}/torrent
%{_libdir}/*.so

%changelog
* Sat Jan 04 2025 Conrad Meyer <cse.cem@gmail.com> - 0.15.1-1
- Update to 0.15.1

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.13.8-17
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 19 2023 Florian Weimer <fweimer@redhat.com> - 0.13.8-13
- Fix another C compatibility issue in the configure script

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Florian Weimer <fweimer@redhat.com> - 0.13.8-10
- Port configure script to C99

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.13.8-7
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 28 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 0.13.8-4
- Clean spec

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 09 2019 Denis Fateyev <denis@fateyev.com> - 0.13.8-1
- Update to 0.13.8 version
- Dropped obsolete openssl patch

* Thu Aug 8 2019 Conrad Meyer <cemeyer@uw.edu> - 0.13.7-6
- Add missing zlib-devel BR after removal from buildroot (rhbz# 1736052)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Conrad Meyer <cemeyer@uw.edu> - 0.13.7-3
- Add missing gcc-c++ BR after removal from buildroot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 8 2018 Conrad Meyer <cemeyer@uw.edu> - 0.13.7-1
- Bump to latest upstream release (rhbz# 1588472)
- Upstream failed to include the OpenSSL 1.1 patch in this release, but it may
  be included in master for the next release:
  https://github.com/rakshasa/libtorrent/issues/171
  So, we must retain the patch for now.

* Sun Mar 11 2018 Conrad Meyer <cemeyer@uw.edu> - 0.13.6-9
- Fix rawhide build with patch for OpenSSL 1.1. (rhbz #1554036)

* Sat Mar 10 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.13.6-8
- Add gcc to BR
- Use license macro
- Remove defattr

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 19 2015 Conrad Meyer <cemeyer@uw.edu> - 0.13.6-1
- Bump to latest upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.13.4-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.13.4-1
- Update to 0.13.4
- Drop patch - no longer needed

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 23 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.13.3-4
- Bad patch name. Paste error

* Sat Mar 23 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.13.3-3
- Add patch to support ARM 64 support

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 25 2012 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.13.3-1
- Update to latest upstream version

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.13.2-1
- Update to 0.13.2

* Tue Apr 03 2012 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.13.1-1
- Update to 0.13.1

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-3
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 18 2011 Conrad Meyer <konrad@tylerc.org> - 0.13.0-1
- Bump to latest upstream release

* Sat Jul 2 2011 Conrad Meyer <konrad@tylerc.org> - 0.12.9-1
- Bump to latest upstream release

* Thu May 26 2011 Conrad Meyer <konrad@tylerc.org> - 0.12.8-1
- Bump to latest upstream release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 27 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.12.7-1
- update to latest upstream release

* Fri Oct 15 2010 Michel Salim <salimma@fedoraproject.org> - 0.12.6-2
- Compile with support for pre-allocating files (# 466548)

* Tue Dec 15 2009 Conrad Meyer <konrad@tylerc.org> - 0.12.6-1
- Bump version.

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.12.5-3
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 3 2009 Conrad Meyer <konrad@tylerc.org> - 0.12.5-1
- Bump version.

* Fri Feb 27 2009 Conrad Meyer <konrad@tylerc.org> - 0.12.4-4
- Fix FTBFS.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 0.12.4-2
- rebuild with new openssl

* Wed Nov 26 2008 Conrad Meyer <konrad@tylerc.org> - 0.12.4-1
- Bump to 0.12.4.

* Tue Nov 18 2008 Conrad Meyer <konrad@tylerc.org> - 0.12.3-1
- Bump to 0.12.3.

* Thu Aug  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.11.8-5
- fix license tag

* Sat Apr  5 2008 Christopher Aillon <caillon@redhat.com> - 0.11.8-4
- Add missing #includes so this compiles against GCC 4.3

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.11.8-3
- Autorebuild for GCC 4.3

* Fri Dec 07 2007 Release Engineering <rel-eng at fedoraproject dot org> - 0.11.8-2
- Rebuild for deps

* Tue Sep 18 2007 Marek Mahut <mmahut at fedoraproject dot org> - 0.11.8-1
- New upstream version

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.11.4-2
- Rebuild for selinux ppc32 issue.

* Thu Jun 28 2007 Chris Chabot <chabotc@xs4all.nl> - 0.11.4-1
- New upstream version

* Sun Nov 26 2006 Chris Chabot <chabotc@xs4all.nl> - 0.10.4-1
- New upstream version
- Compile with -Os to work around a gcc 4.1 incompatibility

* Mon Oct 02 2006 Chris Chabot <chabotc@xs4all.nl> - 0.10.2-3
- Bump EVR to fix broken upgrade path (BZ #208985)

* Fri Sep 29 2006 Chris Chabot <chabotc@xs4all.nl> - 0.10.2-1
- New upstream release

* Mon Sep 11 2006 Chris Chabot <chabotc@xs4all.nl> - 0.10.0-3
- FC6 rebuild, re-tag

* Mon Sep 11 2006 Chris Chabot <chabotc@xs4all.nl> - 0.10.0-2
- FC6 rebuild

* Sun Aug 13 2006 Chris Chabot <chabotc@xs4all.nl> - 0.10.0-1
- Upgrade to 0.10.0

* Sat Jun 17 2006 - Chris Chabot <chabotc@xs4all.nl> - 0.9.3-1
- Upgrade to new upstream version 0.9.3

* Sat Jan 14 2006 - Chris Chabot <chabotc@xs4all.nl> - 0.8.2-2
- Improved general summary & devel package description 
- Simplified devel package includedir files section
- Removed openssl as requires, its implied by .so dependency
- Correct devel package Group

* Wed Jan 11 2006 - Chris Chabot <chabotc@xs4all.nl> - 0.8.2-1
- Initial version
