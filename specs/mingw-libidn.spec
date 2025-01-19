%{?mingw_package_header}

Name:           mingw-libidn
Version:        1.42
Release:        5%{?dist}
Summary:        MinGW Windows Internationalized Domain Name support library

License:        LGPL-2.0-or-later
URL:            http://www.gnu.org/software/libidn/
Source0:        http://ftp.gnu.org/gnu/libidn/libidn-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-win-iconv

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-win-iconv

BuildRequires:  pkgconfig gettext-devel


%description
GNU Libidn is an implementation of the Stringprep, Punycode and
IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group, used for internationalized domain
names.


# Win32
%package -n mingw32-libidn
Summary:        MinGW Windows zlib compression library for the win32 target
Requires:       pkgconfig

%description -n mingw32-libidn
GNU Libidn is an implementation of the Stringprep, Punycode and
IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group, used for internationalized domain
names.

%package -n mingw32-libidn-static
Summary:        Static version of the MinGW Windows IDN library
Requires:       mingw32-libidn = %{version}-%{release}

%description -n mingw32-libidn-static
Static version of the MinGW Windows IDN library.

# Win64
%package -n mingw64-libidn
Summary:        MinGW Windows zlib compression library for the win64 target
Requires:       pkgconfig

%description -n mingw64-libidn
GNU Libidn is an implementation of the Stringprep, Punycode and
IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group, used for internationalized domain
names.

%package -n mingw64-libidn-static
Summary:        Static version of the MinGW Windows IDN library
Requires:       mingw64-libidn = %{version}-%{release}

%description -n mingw64-libidn-static
Static version of the MinGW Windows IDN library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n libidn-%{version}


%build
%mingw_configure --disable-nls --disable-csharp --enable-static --enable-shared
%mingw_make_build

%install
%mingw_make_install

# Remove documentation which duplicates native Fedora package.
rm -r %{buildroot}%{mingw32_datadir}/emacs
rm -r %{buildroot}%{mingw64_datadir}/emacs
rm -r %{buildroot}%{mingw32_infodir}
rm -r %{buildroot}%{mingw64_infodir}
rm -r %{buildroot}%{mingw32_mandir}/man*
rm -r %{buildroot}%{mingw64_mandir}/man*

# The .def file isn't interesting for other libraries/applications
rm -f %{buildroot}%{mingw32_bindir}/libidn-12.def
rm -f %{buildroot}%{mingw64_bindir}/libidn-12.def

# Drop all .la files
find %{buildroot} -name "*.la" -delete


# Win32
%files -n mingw32-libidn
%license COPYING COPYING.LESSERv2 COPYING.LESSERv3 COPYINGv2 COPYINGv3
%{mingw32_bindir}/idn.exe
%{mingw32_bindir}/libidn-12.dll
%{mingw32_libdir}/libidn.dll.a
%{mingw32_libdir}/pkgconfig/libidn.pc
%{mingw32_includedir}/*.h

%files -n mingw32-libidn-static
%{mingw32_libdir}/libidn.a

# Win64
%files -n mingw64-libidn
%license COPYING COPYING.LESSERv2 COPYING.LESSERv3 COPYINGv2 COPYINGv3
%{mingw64_bindir}/idn.exe
%{mingw64_bindir}/libidn-12.dll
%{mingw64_libdir}/libidn.dll.a
%{mingw64_libdir}/pkgconfig/libidn.pc
%{mingw64_includedir}/*.h

%files -n mingw64-libidn-static
%{mingw64_libdir}/libidn.a


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Sandro Mani <manisandro@gmail.com> - 1.42-1
- Update to 1.42

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Sandro Mani <manisandro@gmail.com> - 1.41-1
- Update to 1.41

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.38-3
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Sandro Mani <manisandro@gmail.com> - 1.38-1
- Update to 1.38

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 19 2021 Sandro Mani <manisandro@gmail.com> - 1.37-1
- Update to 1.37

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Sandro Mani <manisandro@gmail.com> - 1.36-1
- Update to 1.36

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 28 2019 Sandro Mani <manisandro@gmail.com> - 1.35-1
- Update to 1.35

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Kalev Lember <klember@redhat.com> - 1.34-1
- Update to 1.34

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 30 2016 Nikos Mavrogiannopoulos - 1.33-1
- Update to 1.33 (#1374902,#1359147,#1359148)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 13 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.28-1
- Update to 1.28
- Fixes FTBFS against latest mingw-w64
- Dropped BR: autoconf automake libtool

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.25-1
- Update to 1.25
- Fixes FTBFS against latest automake

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 18 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.14-13
- Added win64 support (contributed by Mikkel Kruse Johnsen)

* Wed Mar 07 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.14-12
- Renamed the source package to mingw-libidn (RHBZ #800914)
- Use mingw macros without leading underscore
- Dropped unneeded RPM tags
- Dropped the .la files

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.14-11
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 06 2011 Kalev Lember <kalevlember@gmail.com> - 1.14-9
- Rebuilt against win-iconv

* Wed Apr 27 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.14-8
- Dropped the proxy-libintl pieces

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov  7 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.14-6
- Rebuild in order to have soft dependency on libintl

* Fri Sep 18 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.14-5
- Rebuild because of broken mingw32-gcc/mingw32-binutils

* Sun Aug 30 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.14-4
- Automatically generate debuginfo subpackage

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 22 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.14-2
- Use %%global instead of %%define
- Fixed the Source URL
- Use %%find_lang for the gettext translations
- Dropped the commented out patch

* Sat May  9 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.14-1
- Update to version 1.14

* Fri Apr  3 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.9-5
- Added -static subpackage
- Fixed %%defattr line

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 1.9-4
- Rebuild for mingw32-gcc 4.4

* Fri Feb  6 2009 Richard W.M. Jones <rjones@redhat.com> - 0.6.14-3
- Include license file.

* Fri Jan 30 2009 Richard W.M. Jones <rjones@redhat.com> - 0.6.14-2
- Requires pkgconfig.

* Mon Nov 10 2008 Richard W.M. Jones <rjones@redhat.com> - 0.6.14-1
- Initial RPM release.
