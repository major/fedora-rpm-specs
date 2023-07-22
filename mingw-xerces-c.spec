%{?mingw_package_header}

Name:           mingw-xerces-c
Version:        3.2.4
Release:        3%{?dist}
Summary:        MingGW Windows validating XML parser

License:        ASL 2.0
URL:            http://xml.apache.org/xerces-c/
Source0:        http://www.apache.org/dist/xerces/c/3/sources/xerces-c-%{version}.tar.gz
# MinGW build fixes
Patch0:         xerces-c_mingw.patch

BuildArch:      noarch

BuildRequires:  cmake

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils


%description
Xerces-C is a validating XML parser written in a portable subset of
C++. Xerces-C makes it easy to give your application the ability to
read and write XML data. A shared library is provided for parsing,
generating, manipulating, and validating XML documents. Xerces-C is
faithful to the XML 1.0 recommendation and associated standards (DOM
1.0, DOM 2.0. SAX 1.0, SAX 2.0, Namespaces).


%package -n mingw32-xerces-c
Summary:        MingGW x86 Windows validating XML parser
Requires:       pkgconfig

%description -n mingw32-xerces-c
Xerces-C is a validating XML parser written in a portable subset of
C++. Xerces-C makes it easy to give your application the ability to
read and write XML data. A shared library is provided for parsing,
generating, manipulating, and validating XML documents. Xerces-C is
faithful to the XML 1.0 recommendation and associated standards (DOM
1.0, DOM 2.0. SAX 1.0, SAX 2.0, Namespaces).


%package -n mingw64-xerces-c
Summary:        MingGW x64 Windows validating XML parser
Requires:       pkgconfig

%description -n mingw64-xerces-c
Xerces-C is a validating XML parser written in a portable subset of
C++. Xerces-C makes it easy to give your application the ability to
read and write XML data. A shared library is provided for parsing,
generating, manipulating, and validating XML documents. Xerces-C is
faithful to the XML 1.0 recommendation and associated standards (DOM
1.0, DOM 2.0. SAX 1.0, SAX 2.0, Namespaces).


%{?mingw_debug_package}


%prep
%autosetup -p1 -n xerces-c-%{version}


%build
%mingw_cmake
%mingw_make_build


%install
%mingw_make_install

rm -f %{buildroot}%{mingw32_bindir}/*.exe
rm -f %{buildroot}%{mingw64_bindir}/*.exe
rm -rf %{buildroot}%{mingw32_datadir}/doc/
rm -rf %{buildroot}%{mingw64_datadir}/doc/


%files -n mingw32-xerces-c
%license LICENSE
%{mingw32_includedir}/xercesc/
%{mingw32_bindir}/libxerces-c-3.2.dll
%{mingw32_libdir}/libxerces-c.dll.a
%{mingw32_libdir}/pkgconfig/xerces-c.pc
%{mingw32_libdir}/cmake/XercesC/

%files -n mingw64-xerces-c
%license LICENSE
%{mingw64_includedir}/xercesc/
%{mingw64_bindir}/libxerces-c-3.2.dll
%{mingw64_libdir}/libxerces-c.dll.a
%{mingw64_libdir}/pkgconfig/xerces-c.pc
%{mingw64_libdir}/cmake/XercesC/


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 3.2.1-10
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 3.2.1-4
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Pete Walter <pwalter@fedoraproject.org> - 3.2.1-1
- Update to 3.2.1 (CVE-2017-12627)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 30 2016 Kalev Lember <klember@redhat.com> - 3.1.4-1
- Update to 3.1.4, fixing CVE-2016-2099 and CVE-2016-4463

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 11 2015 Kalev Lember <kalevlember@gmail.com> - 3.1.2-2
- Rebuild against latest mingw-gcc

* Fri Mar 20 2015 Kalev Lember <kalevlember@gmail.com> - 3.1.2-1
- Update to 3.1.2, fixing CVE-2015-0252
- Use the license macro for the LICENSE file

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 02 2014 Yaakov Selkowitz <yselkowitz@users.sourceforge.net> - 3.1.1-9
- Added mingw64 package.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 09 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.1.1-5
- Dropped .la files

* Wed Mar 07 2012 Kalev Lember <kalevlember@gmail.com> - 3.1.1-4
- Renamed the source package to mingw-xerces-c (#801039)
- Modernize the spec file
- Use mingw macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.1.1-3
- Rebuild against the mingw-w64 toolchain
- Replaced the LDFLAGS override by a patch as it's needed
  to be compatible with GCC 4.6

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Apr 26 2011 Antti Andreimann <Antti.Andreimann@mail.ee> - 3.1.1-1
- Update to 3.1.1
- Dropped CVE-2009-1885 patch.

* Fri Apr 22 2011 Kalev Lember <kalev@smartlink.ee> - 3.0.1-3
- Rebuilt for pseudo-reloc version mismatch (#698827)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 14 2009 Antti Andreimann <Antti.Andreimann@mail.ee> - 3.0.1-1
- Initial RPM release.
