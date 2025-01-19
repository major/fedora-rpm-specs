%{?mingw_package_header}

Name:           mingw-gsl
Version:        1.16
Release:        24%{?dist}
Summary:        MinGW Windows port of the GNU Scientific Library

# info part of this package is under GFDL license
# eigen/nonsymmv.c and eigen/schur.c
# contains rutiens which are part of LAPACK - under BSD style license
# Automatically converted from old format: GPLv3 and GFDL and BSD - review is highly recommended.
License:        GPL-3.0-only AND LicenseRef-Callaway-GFDL AND LicenseRef-Callaway-BSD
URL:            http://www.gnu.org/software/gsl/
Source0:        ftp://ftp.gnu.org/gnu/gsl/gsl-%{version}.tar.gz
Patch0:         gsl-1.15-lib64.patch

BuildArch: noarch

BuildRequires: make
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw64-binutils

%description
The GNU Scientific Library (GSL) is a collection of routines for
numerical analysis, written in C.


# Mingw32
%package -n mingw32-gsl
Summary: MinGW Windows port of the GNU Scientific Library for the win32 target

%description -n mingw32-gsl
The GNU Scientific Library (GSL) is a collection of routines for
numerical analysis, written in C.

%package -n mingw32-gsl-static
Summary: Static version of MinGW Windows port of the GNU Scientific Library
Requires: mingw32-gsl = %{version}-%{release}

%description -n mingw32-gsl-static
Static version of MinGW Windows port of the GNU Scientific Library
for the win32 target.

# Mingw64
%package -n mingw64-gsl
Summary: MinGW Windows port of the GNU Scientific Library for the win64 target

%description -n mingw64-gsl
The GNU Scientific Library (GSL) is a collection of routines for
numerical analysis, written in C.

%package -n mingw64-gsl-static
Summary: Static version of MinGW Windows port of the GNU Scientific Library
Requires: mingw64-gsl = %{version}-%{release}

%description -n mingw64-gsl-static
Static version of MinGW Windows port of the GNU Scientific Library
for the win32 target.

%{?mingw_debug_package}


%prep
%setup -q -n gsl-%{version}
%patch -P0 -p1 -b .lib64
iconv -f windows-1252 -t utf-8 THANKS > THANKS.aux
touch -r THANKS THANKS.aux
mv THANKS.aux THANKS


%build
# Native package has:
#   configure ... CFLAGS="$CFLAGS -fgnu89-inline"
# but that destroys the original CFLAGS setting.
%mingw_configure

%mingw_make %{?_smp_mflags}


%install
%mingw_make install "DESTDIR=$RPM_BUILD_ROOT"

# Libtool files don't need to be bundled
find $RPM_BUILD_ROOT -name "*.la" -delete

# Remove info files and man pages which duplicate native package.
rm -r $RPM_BUILD_ROOT%{mingw32_mandir}
rm -r $RPM_BUILD_ROOT%{mingw32_infodir}
rm -r $RPM_BUILD_ROOT%{mingw64_mandir}
rm -r $RPM_BUILD_ROOT%{mingw64_infodir}


# Mingw32
%files -n mingw32-gsl
%doc COPYING AUTHORS BUGS ChangeLog NEWS README THANKS TODO
%{mingw32_bindir}/libgslcblas-0.dll
%{mingw32_bindir}/libgsl-0.dll
%{mingw32_bindir}/gsl-config
%{mingw32_bindir}/gsl-histogram.exe
%{mingw32_bindir}/gsl-randist.exe
%{mingw32_libdir}/libgslcblas.dll.a
%{mingw32_libdir}/libgsl.dll.a
%{mingw32_libdir}/pkgconfig/gsl.pc
%{mingw32_datadir}/aclocal/gsl.m4
%{mingw32_includedir}/gsl

%files -n mingw32-gsl-static
%{mingw32_libdir}/libgslcblas.a
%{mingw32_libdir}/libgsl.a

# Mingw64
%files -n mingw64-gsl
%doc COPYING AUTHORS BUGS ChangeLog NEWS README THANKS TODO
%{mingw64_bindir}/libgslcblas-0.dll
%{mingw64_bindir}/libgsl-0.dll
%{mingw64_bindir}/gsl-config
%{mingw64_bindir}/gsl-histogram.exe
%{mingw64_bindir}/gsl-randist.exe
%{mingw64_libdir}/libgslcblas.dll.a
%{mingw64_libdir}/libgsl.dll.a
%{mingw64_libdir}/pkgconfig/gsl.pc
%{mingw64_datadir}/aclocal/gsl.m4
%{mingw64_includedir}/gsl

%files -n mingw64-gsl-static
%{mingw64_libdir}/libgslcblas.a
%{mingw64_libdir}/libgsl.a

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.16-23
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.16-16
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct  4 2013 Alexey Kurov <nucleo@fedoraproject.org> - 1.16-1
- GSL 1.16

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun  3 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.15-2
- subpackages specific summaries
- no cleanup needed in %%install section
- removed %%defattr

* Tue May  8 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.15-1
- GSL 1.15
- mingw64 support

* Sun Mar 21 2010 Keiichi Takahashi <bitwalk@users.sourceforge.net> -   1.14-1
- update GSL to 1.14.

* Mon Oct 26 2009 Keiichi Takahashi <bitwalk@users.sourceforge.net> -   1.13-2
- Added -static subpackage

* Sun Oct 25 2009 Keiichi Takahashi <bitwalk@users.sourceforge.net> -   1.13-1
- update GSL to 1.13.

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 1.11-4
- Rebuild for mingw32-gcc 4.4

* Fri Feb  6 2009 Richard W.M. Jones <rjones@redhat.com> - 1.11-3
- Include license.

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.11-2
- Use _smp_mflags.

* Fri Oct 24 2008 Richard W.M. Jones <rjones@redhat.com> - 1.11-1
- Initial RPM release.
