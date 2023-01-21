%global __strip %{mingw32_strip}
%global __objdump %{mingw32_objdump}

Name:           mingw-dirac
Version:        1.0.2
Release:        29%{?dist}
Summary:        Dirac is an open source video codec

License:        MPLv1.1 or GPLv2+ or LGPLv2+
URL:            http://dirac.sourceforge.net/
Source0:        http://downloads.sourceforge.net/dirac/dirac-%{version}.tar.gz
Patch0:         dirac-1.0.2-mingw32-gcc44.patch
Patch1:         dirac-1.0.2-mingw-w64-compatibility.patch
BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 23
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils

%description
MinGW Windows dirac compression library.


%package -n mingw32-dirac
Summary:        Dirac is an open source video codec

%description -n mingw32-dirac
MinGW Windows dirac compression library.


%prep
%setup -q -n dirac-%{version}
%patch0 -p1 -b .gcc44
%patch1 -p0 -b .mingw-w64
rm util/conversion/common/setstdiomode.cpp
touch util/conversion/common/setstdiomode.cpp

%build
# Make sure the compilation also succeeds when mingw32-cppunit is installed
export ac_cv_header_cppunit_TestRunner_h=no

%mingw32_configure \
  --program-prefix=dirac_ \
  --program-transform-name=s,dirac_dirac_,dirac_, \
  --enable-overlay \
  --disable-static

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# Remove .la files
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/*.la

# Remove docs
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/doc
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/doc


%files -n mingw32-dirac
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%exclude %{mingw32_bindir}/dirac_create_dirac_testfile.pl
%{mingw32_bindir}/dirac_*.exe
%{mingw32_includedir}/dirac/
%{mingw32_bindir}/libdirac_decoder-0.dll
%{mingw32_bindir}/libdirac_encoder-0.dll
%{mingw32_libdir}/pkgconfig/dirac.pc
%{mingw32_libdir}/libdirac_decoder.dll.a
%{mingw32_libdir}/libdirac_encoder.dll.a

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-24
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.0.2-21
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 09 2012 Kalev Lember <kalevlember@gmail.com> - 1.0.2-8
- Remove .la files

* Wed Mar 07 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.2-7
- Renamed the source package to mingw-dirac (RHBZ #800859)
- Use mingw macros without leading underscore
- Dropped unneeded RPM tags

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.2-6
- Rebuild against the mingw-w64 toolchain
- Dropped BR: mingw32-dlfcn as it's unneeded
- Fix compilation against latest mingw-w64 trunk

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 22 2011 Kalev Lember <kalev@smartlink.ee> - 1.0.2-4
- Rebuilt for pseudo-reloc version mismatch (#698827)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul  9 2009 kwizart < kwizart at gmail.com > - 1.0.2-2
- Fix for mingw32-gcc 4.4.0 and binary mode

* Tue Mar 24 2009 kwizart < kwizart at gmail.com > - 1.0.2-1
- Update to 1.0.2

* Mon Jan  5 2009 kwizart < kwizart at gmail.com > - 1.0.0-1
- Initial package based on original dirac.spec

