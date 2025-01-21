Name: wcslib
Version: 8.2.2
Release: 5%{?dist}
Summary: An implementation of the FITS World Coordinate System standard

# Library is under LGPLv3+ utils under GPLv3+
License: LGPL-3.0-or-later
URL: http://www.atnf.csiro.au/people/mcalabre/WCS/wcslib/
Source0: http://www.atnf.csiro.au/people/mcalabre/WCS/wcslib-%{version}.tar.bz2

# General stuff
BuildRequires: make
BuildRequires: flex
BuildRequires: gcc
# Development libraries
BuildRequires: cfitsio-devel
BuildRequires: zlib-devel

%description
WCSLIB is a library that implements the "World Coordinate System" (WCS) 
convention in FITS (Flexible Image Transport System)

%package devel
Summary: Libraries, includes, etc. used to develop an application with %{name}
License: LGPL-3.0-or-later
Requires: wcslib = %{version}-%{release}
%description devel
These are the files needed to develop an application using %{name}.

%package utils
Summary: Utility programs provided by %{name}
License: GPL-3.0-or-later
Requires: wcslib = %{version}-%{release}
%description utils
Utils provided with %{name}

%prep
%setup -q 

%build
%configure --disable-fortran --disable-static
# Does not like multithread builds...
make

%install
make install DESTDIR=%{buildroot}
# fix permissions
rm -rf %{buildroot}%{_datadir}/doc/wcslib*
chmod 755 %{buildroot}%{_includedir}/wcslib-%{version}

%check
make check

%ldconfig_scriptlets

%files
%license COPYING.LESSER
%doc README
%{_libdir}/*.so.*

%files devel
%license COPYING.LESSER
%doc html wcslib.pdf
%{_libdir}/*.so
%exclude %{_libdir}/*.a
%{_libdir}/pkgconfig/wcslib.pc
%{_includedir}/wcslib
%{_includedir}/wcslib-%{version}

%files utils
%license COPYING 
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 8.2.2-3
- convert license to SPDX

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 09 2024 Sergio Pascual <sergiopr@fedoraproject.org> 8.2.2-1
- New upstream version (8.2.2)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 28 2022 Sergio Pascual <sergiopr@fedoraproject.org> 7.12-1
- New upstream version (7.12)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Apr 24 2022 Sergio Pascual <sergiopr@fedoraproject.org> 7.10-1
- New upstream version (7.10)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 16 2021 Sergio Pascual <sergiopr@fedoraproject.org> 7.6-1
- New upstream version (7.6)

* Thu Apr 08 2021 Sergio Pascual <sergiopr@fedoraproject.org> 7.5-1
- New upstream version (7.5)

* Wed Feb 03 2021 Sergio Pascual <sergiopr@fedoraproject.org> 7.4-1
- New upstream version (7.4)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Sergio Pascual <sergiopr@fedoraproject.org> 7.3-1
- New upstream version (7.3)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 09 2020 Sergio Pascual <sergiopr@fedoraproject.org> 7.2-1
- New upstream version (7.2)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 31 2019 Sergio Pascual <sergiopr@fedoraproject.org> 6.4-1
- New upstream version (6.4)

* Mon Jul 29 2019 Sergio Pascual <sergiopr@fedoraproject.org> 6.3-1
- New upstream version (6.3)

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.19.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 02 2018 Christian Dersch <lupinix@mailbox.org> - 5.19.1-1
- new version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 5.18-3
- added BR: flex

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 5.18-2
- rebuilt for cfitsio 3.450

* Fri Feb 23 2018 Christian Dersch <lupinix@mailbox.org> - 5.18-1
- new version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Sergio Pascual <sergiopr@fedoraproject.org> 5.16-7
- Patch all problematic 2775 install permissions to 775

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 01 2017 Christian Dersch <lupinix@mailbox.org> - 5.16-4
- try workaround for #1452893

* Thu Jun 01 2017 Christian Dersch <lupinix@mailbox.org> - 5.16-3
- yet another rebuild for build-id conflicts

* Fri May 19 2017 Christian Dersch <lupinix@mailbox.org> - 5.16-2
- rebuild, to fix #1452893

* Tue May 16 2017 Sergio Pascual <sergiopr@fedoraproject.org> 5.16-1
- New upstream source (5.16)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 15 2016 Sergio Pascual <sergiopr@fedoraproject.org> 5.15-1
- New upstream source (5.15)

* Wed Mar 30 2016 Sergio Pascual <sergiopr@fedoraproject.org> 5.14-1
- New upstream source (5.14), soname bump

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.25.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.25.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 Sergio Pascual <sergiopr@fedoraproject.org> 4.25.1-1
- New upstream source (4.25.1)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Sergio Pascual <sergiopr@fedoraproject.org> 4.23-1
- New upstream source (4.23)

* Sun Apr 13 2014 Sergio Pascual <sergiopr@fedoraproject.org> 4.22-1
- New upstream source (4.22)

* Thu Jan 09 2014 Sergio Pascual <sergiopr@fedoraproject.org> 4.20-1
- New upstream source (4.20)
- Rebuilt for new cfitsio (3.360)

* Wed Oct 23 2013 Sergio Pascual <sergiopr@fedoraproject.org> 4.19-1
- New upstream source (4.19)

* Sat Aug 24 2013 Sergio Pascual <sergiopr@fedoraproject.org> 4.18-3
- Removed reference to versioned docdir (bz #993888)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Sergio Pascual <sergiopr@fedoraproject.org> 4.18-1
- New upstream source (4.18)

* Fri Mar 22 2013 Sergio Pascual <sergiopr@fedoraproject.org> 4.17-2
- Rebuilt for new cfitsio (3.340)

* Wed Mar 20 2013 Sergio Pascual <sergiopr@fedoraproject.org> 4.17-1
- New upstream source

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.13.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 Sergio Pascual <sergiopr at fedoraproject.org> 4.13.4-1
- New upstream source

* Sat Jan 07 2012 Sergio Pascual <sergiopr at fedoraproject.org> 4.8.4-3
- Disable check

* Fri Jan 06 2012 Sergio Pascual <sergiopr at fedoraproject.org> 4.8.4-2
- New upstream source (source added)

* Fri Jan 06 2012 Sergio Pascual <sergiopr at fedoraproject.org> 4.8.4-1
- New upstream source

* Mon Feb 21 2011 Sergio Pascual <sergiopr at fedoraproject.org> 4.7-2
- EVR bump for rebuilding

* Sun Feb 20 2011 Sergio Pascual <sergiopr at fedoraproject.org> 4.7-1
- New upstream source

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 09 2010 Sergio Pascual <sergiopr at fedoraproject.org> 4.6.3-2
- Race condition with parallel make

* Tue Nov 09 2010 Sergio Pascual <sergiopr at fedoraproject.org> 4.6.3-1
- New upstream source
- Patch to fix problems compiling i686 in x86_64

* Tue Nov 09 2010 Sergio Pascual <sergiopr at fedoraproject.org> 4.5.6-1
- New upstream source
- Added pkgconfig file

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 16 2009 Sergio Pascual <sergiopr at fedoraproject.org> 4.3.1-2
- Added patch to link explicitly with libmath.
- Removed duplicate licenses.

* Sat Feb 14 2009 Sergio Pascual <sergiopr at fedoraproject.org> 4.3.1-1
- First version.
