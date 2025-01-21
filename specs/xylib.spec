Name: xylib
Summary: Library for reading x-y data from several file formats
Version: 1.6
Release: 11%{?dist}
License: LGPL-2.1-only
Url: http://xylib.sourceforge.net/
Source0: https://github.com/wojdyr/xylib/releases/download/v%{version}/%{name}-%{version}.tar.bz2
BuildRequires: make
BuildRequires: gcc-c++, boost-devel, zlib-devel, bzip2-devel, wxGTK-devel

%description
C++ library for reading files that contain x-y data from powder diffraction, 
spectroscopy or other experimental methods. The supported formats include:
VAMAS, pdCIF, Bruker UXD and RAW, Philips UDF and RD, Rigaku DAT, 
Sietronics CPI, DBWS/DMPLOT, Koalariet XDD and others.

%package devel
Summary: Development files for xylib
Requires: %{name} = %{version}-%{release}
Requires: boost-devel

%description devel
Files needed for developing apps using xylib.
xylib is a C++ library for reading files that contain x-y data from 
powder diffraction, spectroscopy or other experimental methods.

%prep
%setup -q

%build
%configure --disable-static --with-wx-config=wx-config-3.2
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc README.rst COPYING TODO sample-urls
%{_libdir}/libxy.so.*
%{_bindir}/*
%{_mandir}/man1/*

%files devel
%{_includedir}/xylib/
%{_libdir}/libxy.so

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 04 2022 Scott Talbert <swt@techie.net> - 1.6-6
- Rebuild with wxWidgets 3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 25 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.6-1
- Update to 1.6

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-22
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 1.4-13
- Rebuilt for s390x binutils bug

* Tue Jul 04 2017 Jonathan Wakely <jwakely@redhat.com> - 1.4-12
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.4-9
- Rebuilt for Boost 1.63

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 1.4-7
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.4-6
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.4-4
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.4-2
- Rebuilt for GCC 5 C++11 ABI change

* Wed Apr 01 2015 Marcin Wojdyr <wojdyr@gmail.com> - 1.4-1
- Update to 1.4. Closes Red Hat Bugzilla bug #1100787.

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.2-5
- Rebuild for boost 1.57.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.2-2
- Rebuild for boost 1.55.0

* Fri Aug 2 2013 Marcin Wojdyr <wojdyr@gmail.com> - 1.2-1
- update to 1.2. Closes Red Hat Bugzilla bug #926849.
- removed patch that is not needed with this version

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.8-8
- Rebuild for boost 1.54.0

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.8-7
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.8-6
- Rebuild for Boost-1.53.0

* Fri Feb  8 2013 Petr Machata <pmachata@redhat.com> - 0.8-5
- Add a patch for compilation with Boost.Spirit V2

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 15 2011 Marcin Wojdyr <wojdyr@gmail.com> - 0.8-1
- updated to 0.8

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 11 2010 Marcin Wojdyr <wojdyr@gmail.com> - 0.7-1
- updated to 0.7
- changed URL and Source0
- added zlib-devel and bzip2-devel to BuildRequires
- removed manual installation of xyconv, it is installed by make install now
- added man page and sample-urls to files

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Marcin Wojdyr <wojdyr@gmail.com> - 0.4-4
- added "Requires: boost-devel" to -devel package

* Mon Jul 06 2009 Marcin Wojdyr <wojdyr@gmail.com> - 0.4-3
- install xyconv manually instead of changing Makefile.am

* Fri Jun 26 2009 Marcin Wojdyr <wojdyr@gmail.com> - 0.4-2
- add INSTALL="install -p"
- change Makefile.am instead of calling libtool manually
- use SMP make flags
- replace %%defattr(-,root,root) with %%defattr(-,root,root,-)
- use a more recommended version of the BuildRoot tag

* Sat Jun 13 2009 Marcin Wojdyr <wojdyr@gmail.com> - 0.4-1
- Initial build

