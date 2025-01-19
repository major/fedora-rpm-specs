%{?mingw_package_header}

%global name1 libxml++

Name:           mingw-%{name1}
Version:        2.40.1
Release:        24%{?dist}
Summary:        MinGW Windows C++ wrapper for the libxml2 XML parser library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://libxmlplusplus.sourceforge.net/
Source:         http://ftp.gnome.org/pub/GNOME/sources/libxml++/2.40/libxml++-%{version}.tar.xz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-libxml2 >= 2.6.1
BuildRequires:  mingw64-libxml2 >= 2.6.1
BuildRequires:  mingw32-glibmm24 >= 2.4.0
BuildRequires:  mingw64-glibmm24 >= 2.4.0
BuildRequires:  mingw32-filesystem >= 68
BuildRequires:  mingw64-filesystem >= 68
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-gettext
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-gettext
BuildRequires:  perl

%description
libxml++ is a C++ wrapper for the libxml2 XML parser library.

%package -n mingw32-%{name1}
Summary:        MinGW Windows C++ wrapper for the libxml2 XML parser library
Requires:       pkgconfig

%description -n mingw32-%{name1}
libxml++ is a C++ wrapper for the libxml2 XML parser library.

%package -n mingw64-%{name1}
Summary:        MinGW Windows C++ wrapper for the libxml2 XML parser library
Requires:       pkgconfig

%description -n mingw64-%{name1}
libxml++ is a C++ wrapper for the libxml2 XML parser library.

%{?mingw_debug_package}

%prep
%setup -q -n %{name1}-%{version}

%build
%{mingw_configure} --disable-static --disable-documentation
%{mingw_make} %{?_smp_mflags}


%install
%{mingw_make} install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{mingw32_docdir}
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{mingw64_docdir}
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/*.la


%files -n mingw32-%{name1}
%license COPYING
%doc AUTHORS NEWS README ChangeLog
%{mingw32_bindir}/libxml++-2.6-2.dll
%{mingw32_includedir}/*
%{mingw32_libdir}/libxml++-2.6.dll.a
%{mingw32_libdir}/pkgconfig/*
%dir %{mingw32_libdir}/%{name1}-2.6
%dir %{mingw32_libdir}/%{name1}-2.6/include
%{mingw32_libdir}/%{name1}-2.6/include/*.h

%files -n mingw64-%{name1}
%license COPYING
%doc AUTHORS NEWS README ChangeLog
%{mingw64_bindir}/libxml++-2.6-2.dll
%{mingw64_includedir}/*
%{mingw64_libdir}/libxml++-2.6.dll.a
%{mingw64_libdir}/pkgconfig/*
%dir %{mingw64_libdir}/%{name1}-2.6
%dir %{mingw64_libdir}/%{name1}-2.6/include
%{mingw64_libdir}/%{name1}-2.6/include/*.h


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.40.1-23
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.40.1-16
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.40.1-10
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 28 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.40.1-6
- New BR

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.40.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov  9 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.40.1-1
- Update to 2.40.1

* Fri Sep 25 2015 Kalev Lember <klember@redhat.com> - 2.40.0-1
- Update to 2.40.0
- Use license macro for COPYING

* Thu Jul  2 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.38.1-1
- Update to 2.38.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.38.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May  4 2015 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.38.0-1
- Update to 2.38.0

* Thu Dec  4 2014 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.37.2-1
- Update to 2.37.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.37.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec  3 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.37.1-1
- Update to 2.37.1

* Mon Jul 29 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.36.0-3
- Rebuild for mingw64 unresolved symbols

* Sun Jan 27 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.36.0-2
- Rebuild against mingw-gcc 4.8 (win64 uses SEH exceptions now)

* Thu Nov 29 2012 Kalev Lember <kalevlember@gmail.com> - 2.36.0-1
- Update to 2.36.0

* Fri Aug  3 2012 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.34.2-7
- enable 64bit build

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.34.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 07 2012 Kalev Lember <kalevlember@gmail.com> - 2.34.2-5
- Renamed the source package to mingw-libxml++ (#800926)
- Use mingw macros without leading underscore

* Tue Feb 28 2012 Kalev Lember <kalevlember@gmail.com> - 2.34.2-4
- Remove the .la files

* Tue Feb 28 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.34.2-3
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.34.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 02 2011 Kalev Lember <kalevlember@gmail.com> - 2.34.2-1
- Update to 2.34.2
- Spec cleanup for recent rpmbuild

* Wed Jul 06 2011 Kalev Lember <kalevlember@gmail.com> - 2.34.1-3
- Rebuilt against win-iconv

* Thu Apr 28 2011 Kalev Lember <kalev@smartlink.ee> - 2.34.1-2
- Rebuilt for proxy-libintl removal

* Fri Apr 22 2011 Kalev Lember <kalev@smartlink.ee> - 2.34.1-1
- Update to 2.34.1
- Dropped the autotools examples patch which didn't apply cleanly and
  isn't useful for the mingw build as we don't build the examples.

* Tue Apr 12 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.33.2-1
- update to 2.33.2

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.33.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec  8 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.33.1-1
- update to 2.33.1

* Thu Aug  5 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.30.0-1
- update to 2.30.0

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.26.0-2
- add debuginfo packages

* Fri Apr 17 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.26.0-1
- update to 2.26.0
- remove docs cruft from install section
- remove dos2unix BR

* Wed Mar 25 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.24.2-4
- add BR's and R's
- remove docs, as they duplicate the native package

* Mon Mar 23 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.24.2-3
- unify main and devel subpackages

* Mon Mar 23 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.24.2-2
- copy from native package
