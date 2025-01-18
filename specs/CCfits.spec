Name: CCfits
Version: 2.6
Release: 13%{?dist}
Summary: A C++ interface for cfitsio

License: CFITSIO
URL: http://heasarc.gsfc.nasa.gov/docs/software/fitsio/ccfits
Source0: http://heasarc.gsfc.nasa.gov/docs/software/fitsio/ccfits/%{name}-%{version}.tar.gz
Patch0: CCfits-removerpath.patch
Patch1: cfitsio-path.patch

BuildRequires: gcc-c++ cfitsio-devel
BuildRequires: make

%description
CCfits is an object oriented interface to the cfitsio library. It is designed 
to make the capabilities of cfitsio available to programmers working in C++. 
It is written in ANSI C++ and implemented using the C++ Standard Library 
with namespaces, exception handling, and member template functions.

%package devel
Summary: Headers for developing programs that will use %{name}
Requires: cfitsio-devel >= 3.280
Requires: %{name} = %{version}-%{release}
%description devel
These are the header files and libraries needed to develop a %{name} 
application.

%package doc
Summary: Documentation for %{name}, includes full API docs
BuildArch: noarch
 
%description doc
This package contains the full API documentation for %{name}.

%prep
%autosetup

%build
%configure --disable-static --with-cfitsio=%{_prefix} --with-cfitsio-include=%{_includedir}/cfitsio
make %{?_smp_mflags}

%install
make %{?_smp_mflags}  install DESTDIR=%{buildroot}
rm %{buildroot}/usr/bin/cookbook

%ldconfig_scriptlets

%files
%license License.txt
%{_libdir}/*so.*

%files devel
%doc CHANGES 
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

%files doc
%license License.txt 
%doc html

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Sergio Pascual <sergiopr@fedoraproject.org> 2.6-7
- Use SPDX License
- License name is CFITSIO

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 28 2022 Sergio Pascual <sergiopr@fedoraproject.org> 2.6-5
- Rebuilt for cfitsio 4.2

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 21 2021 Sergio Pascual <sergiopr@fedoraproject.org> 2.6-1
- New upstream release (2.6)

* Wed Feb 03 2021 Sergio Pascual <sergiopr@fedoraproject.org> 2.5-18
- Rebuilt for cfitsio 3.490

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Sergio Pascual <sergiopr@fedoraproject.org> 2.5-13
- Apply the patch (bz #1676568)

* Wed Feb 13 2019 Sergio Pascual <sergiopr@fedoraproject.org> 2.5-12
- Patch headers with the correct cfistio path (bz #1676568)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 2.5-9
- rebuilt for cfitsio 3.450

* Thu Mar 08 2018 Sergio Pascual <sergiopr@fedoraproject.org> 2.5-8
- Include gcc-c++ in Build Requires

* Fri Feb 23 2018 Christian Dersch <lupinix@mailbox.org> - 2.5-7
- rebuilt for cfitsio 3.420 (so version bump)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Sergio Pascual <sergiopr@fedoraproject.org> 2.5-1
- New upstream release (2.5)

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.4-14
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 09 2014 Sergio Pascual <sergiopr@fedoraproject.org> 2.4-11
- Using new cfitsio 3.360
- Fix bad date in changelog

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Sergio Pascual <sergiopr@fedoraproject.org> 2.4-9
- Using new cfitsio 3.350

* Fri Mar 22 2013 Sergio Pascual <sergiopr@fedoraproject.org> 2.4-8
- Using new cfitsio 3.340

* Wed Mar 20 2013 Sergio Pascual <sergiopr@fedoraproject.org> 2.4-7
- Using new cfitsio 3.330

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 24 2012 Sergio Pascual <sergiopr at fedoraproject.org> 2.4-5
- Rebuilt after mass rebuild failled

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-3
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jan 06 2012 Sergio Pascual <sergiopr at fedoraproject.org> 2.4-1
- New upstream source 2.4
- Removing obsoletes for doc package
- Rebuilt to match new cfitsio 3.290

* Fri Jun 10 2011 Sergio Pascual <sergiopr at fedoraproject.org> 2.3-4
- Rebuilt to match new cfitsio 3.280

* Sun Apr 24 2011 Sergio Pascual <sergiopr at fedoraproject.org> 2.3-3
- Rebuilt to match new cfitsio 3.270

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 09 2010 Sergio Pascual <sergiopr at fedoraproject.org> 2.3-1
- New upstream source

* Fri Jul 09 2010 Sergio Pascual <sergiopr at fedoraproject.org> 2.2-4
- Include license as documentation in -doc subpackages
- Rebuilt to match new cfitsio 3.250

* Wed Jan 27 2010 Sergio Pascual <sergiopr at fedoraproject.org> 2.2-3
- Renamed subpackage -docs to -doc, according to guidelines

* Wed Jan 27 2010 Sergio Pascual <sergiopr at fedoraproject.org> 2.2-2
- Rebuilt to match new cfitsio 3.240
- Removed require pkgconfig
- Using upstream pkgconfig file
- Minor fixes

* Thu Sep 10 2009 Sergio Pascual <sergiopr at fedoraproject.org> - 2.2-1
- New upstream version, includes pkgconfig file

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 16 2009 Sergio Pascual <sergiopr at fedoraproject.org> - 2.1-4
- Noarch subpackage for docs

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 06 2009 Sergio Pascual <sergiopr at fedoraproject.org> 2.1-2
- Rebuilt to match new cfitsio 3.130

* Wed Dec 03 2008 Sergio Pascual <sergiopr at fedoraproject.org> 2.1-1
- New upstream source
- Rebuilt needed to fix bz #474087

* Sat Feb 09 2008 Sergio Pascual <sergiopr at fedoraproject.org> 2.0-1
- New upstream source

* Tue Nov 13 2007 Sergio Pascual <sergiopr at fedoraproject.org> 1.8-1
- New upstream source

* Mon Aug 27 2007 Sergio Pascual <spr at astrax.fis.ucm.es> 1.7-1.1
- Rebuild for Fedora 8 by bad binutils in ppc32

* Sun Jul 22 2007 Sergio Pascual <spr at astrax.fis.ucm.es> 1.7-1
- New upstream source 1.7

* Thu Feb 01 2007 Sergio Pascual <spr at astrax.fis.ucm.es> 1.6-2
- Patch to fix the include directives of cfitsio in header files.

* Mon Dec 11 2006 Sergio Pascual <spr at astrax.fis.ucm.es> 1.6-1
- New upstream version 1.6. Only compiles with cfitsio >= 3.020.

* Tue Sep 12 2006 Sergio Pascual <spr at astrax.fis.ucm.es> 1.5-3
- Rebuild for FC6.

* Fri Jul 28 2006 Sergio Pascual <spr at astrax.fis.ucm.es> 1.5-2
- Removed perl files in the documentation (bug #200517).

* Thu Jul 27 2006 Sergio Pascual <spr at astrax.fis.ucm.es> 1.5-1
- New upstream source 1.5.
- Removed patch CCfits-1.4-g++4.patch (integrated in the source)
- Perl files in docs removed in the source.

* Wed Mar 08 2006 Sergio Pascual <spr at astrax.fis.ucm.es> 1.4-4
- Removed explicit Buildrequires gcc-c++.

* Tue Mar 07 2006 Sergio Pascual <spr at astrax.fis.ucm.es> 1.4-3
- Rebuilt with new upstream source.

* Mon Mar 06 2006 Sergio Pascual <spr at astrax.fis.ucm.es> 1.4-2
- Removed Source with license file License.txt.

* Mon Feb 20 2006 Sergio Pascual <spr at astrax.fis.ucm.es> 1.4-1
- Removed perl files in documentation.
- Changed license type to BSD.
- Main summary changed and trailing dots removed.
- Removed -rpath in the shared library.

* Thu Feb 16 2006 Sergio Pascual <spr at astrax.fis.ucm.es> 1.4-0
- Initial spec file.
