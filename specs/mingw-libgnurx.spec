%?mingw_package_header

Name:           mingw-libgnurx
Version:        2.5.1
Release:        38%{?dist}
Summary:        MinGW Regex library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://mingw.sourceforge.net/
Source0:        http://kent.dl.sourceforge.net/sourceforge/mingw/mingw-libgnurx-%{version}-src.tar.gz
Source1:        mingw32-libgnurx-configure.ac
Source2:        mingw32-libgnurx-Makefile.am
Patch0:         mingw32-libgnurx-honor-destdir.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  autoconf automake libtool

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils


%description
MinGW Windows regular expression library.


# Win32
%package -n mingw32-libgnurx
Summary:        MinGW Regex library

%description -n mingw32-libgnurx
MinGW Windows regular expression library.

%package -n mingw32-libgnurx-static
Summary:        Static version of the MinGW Windows regular expression library
Requires:       mingw32-libgnurx = %{version}-%{release}

%description -n mingw32-libgnurx-static
Static version of the MinGW Windows regular expression library.

# Win64
%package -n mingw64-libgnurx
Summary:        MinGW Regex library

%description -n mingw64-libgnurx
MinGW Windows regular expression library.

%package -n mingw64-libgnurx-static
Summary:        Static version of the MinGW Windows regular expression library
Requires:       mingw64-libgnurx = %{version}-%{release}

%description -n mingw64-libgnurx-static
Static version of the MinGW Windows regular expression library.


%?mingw_debug_package


%prep
%setup -q -n mingw-libgnurx-%{version}
%patch -P0 -p0

# The Makefile which is delivered with this package can't create static
# libraries and misnames the resulting import libraries
# So replace the buildsystem by a more proper one
cp %{SOURCE1} configure.ac
cp %{SOURCE2} Makefile.am
touch NEWS
touch AUTHORS
libtoolize --copy
aclocal
autoconf
automake --add-missing

%build
%mingw_configure --enable-static --enable-shared
%mingw_make %{?_smp_mflags}


%install
# make install expects %{mingw32_includedir} to exist
mkdir -p $RPM_BUILD_ROOT%{mingw32_includedir} $RPM_BUILD_ROOT%{mingw64_includedir}

%mingw_make DESTDIR=$RPM_BUILD_ROOT install

# make install installs two import libraries named libgnurx.a and
# libgnurx.dll.a. As most applications requiring regex functions
# try to perform 'gcc -lregex' we rename the import libraries for this to work
mv $RPM_BUILD_ROOT%{mingw32_libdir}/libgnurx.a $RPM_BUILD_ROOT%{mingw32_libdir}/libregex.a
mv $RPM_BUILD_ROOT%{mingw64_libdir}/libgnurx.a $RPM_BUILD_ROOT%{mingw64_libdir}/libregex.a
mv $RPM_BUILD_ROOT%{mingw32_libdir}/libgnurx.dll.a $RPM_BUILD_ROOT%{mingw32_libdir}/libregex.dll.a
mv $RPM_BUILD_ROOT%{mingw64_libdir}/libgnurx.dll.a $RPM_BUILD_ROOT%{mingw64_libdir}/libregex.dll.a

# Drop the man pages
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/man
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/man

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete


# Win32
%files -n mingw32-libgnurx
%doc COPYING.LIB
%{mingw32_bindir}/libgnurx-0.dll
%{mingw32_includedir}/regex.h
%{mingw32_libdir}/libregex.dll.a

%files -n mingw32-libgnurx-static
%{mingw32_libdir}/libregex.a

# Win64
%files -n mingw64-libgnurx
%doc COPYING.LIB
%{mingw64_bindir}/libgnurx-0.dll
%{mingw64_includedir}/regex.h
%{mingw64_libdir}/libregex.dll.a

%files -n mingw64-libgnurx-static
%{mingw64_libdir}/libregex.a


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.5.1-37
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.5.1-30
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr  8 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.5.1-12
- Added win64 support

* Fri Mar 09 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.5.1-11
- Dropped .la files

* Tue Mar 06 2012 Kalev Lember <kalevlember@gmail.com> - 2.5.1-10
- Renamed the source package to mingw-libgnurx (#800429)
- Spec clean up
- Use mingw macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.5.1-9
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.5.1-5
- The wrong RPM variable was overriden for -debuginfo support. Should be okay now

* Mon Jun 22 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.5.1-4
- Split out debug symbols to a -debuginfo subpackage

* Wed Jun  3 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.5.1-3
- The libtool .la file referenced to the wrong file. Fixed

* Tue May 26 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.5.1-2
- Fixed license tag

* Sun May 24 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.5.1-1
- Initial release

