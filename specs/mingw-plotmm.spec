%?mingw_package_header

Name:           mingw-plotmm
Version:        0.1.2
Release:        43%{?dist}
Summary:        MinGW GTKmm plot widget for scientific applications
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            http://plotmm.sourceforge.net/
Source0:        http://download.sourceforge.net/plotmm/plotmm-%{version}.tar.gz
# Fix code to build against libsigc++20
# Upstream:
# https://sourceforge.net/tracker/?func=detail&atid=632478&aid=2082337&group_id=102665
Patch0:         plotmm-0.1.2-libsigc++20.patch
Patch1:         mingw32-plotmm-ac.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 68
BuildRequires:  mingw64-filesystem >= 68
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-gtkmm24 >= 2.4.0
BuildRequires:  mingw64-gtkmm24 >= 2.4.0
BuildRequires:  mingw32-libpng
BuildRequires:  mingw64-libpng
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  autoconf

%description
This package provides an extension to the mingw32 gtkmm library.  It
contains widgets which are primarily useful for technical and
scientifical purposes.  Initially, this is a 2-D plotting widget.

# Win32
%package -n mingw32-plotmm
Summary:        MinGW GTKmm plot widget for scientific applications for the win32 target
Requires:       pkgconfig

%description -n mingw32-plotmm
This package provides an extension to the mingw32 gtkmm library.  It
contains widgets which are primarily useful for technical and
scientifical purposes.  Initially, this is a 2-D plotting widget.

%package -n mingw32-plotmm-static
Summary:        Static version of the MinGW Windows PlotMM library
Requires:       mingw32-plotmm = %{version}-%{release}

%description -n mingw32-plotmm-static
Static version of the MinGW Windows PlotMM library.

# Win64
%package -n mingw64-plotmm
Summary:        MinGW GTKmm plot widget for scientific applications for the win64 target
Requires:       pkgconfig

%description -n mingw64-plotmm
This package provides an extension to the mingw64 gtkmm library.  It
contains widgets which are primarily useful for technical and
scientifical purposes.  Initially, this is a 2-D plotting widget.

%package -n mingw64-plotmm-static
Summary:        Static version of the MinGW Windows PlotMM library
Requires:       mingw64-plotmm = %{version}-%{release}

%description -n mingw64-plotmm-static
Static version of the MinGW Windows PlotMM library.


%?mingw_debug_package


%prep
%setup -q -n plotmm-%{version}
%patch -P0 -p1 -b .libsigc++20
%patch -P1 -p0 -b .mingw
# update autotools, distributed files are so old they do not
# get compiling dlls right
libtoolize --force --copy
aclocal
autoconf
automake -a -c


%build
export MINGW32_CXXFLAGS="%{mingw32_cflags} -std=gnu++11"
export MINGW64_CXXFLAGS="%{mingw64_cflags} -std=gnu++11"
%mingw_configure
%mingw_make

%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{mingw32_bindir}/curves.exe
rm $RPM_BUILD_ROOT%{mingw64_bindir}/curves.exe
rm $RPM_BUILD_ROOT%{mingw32_bindir}/simple.exe
rm $RPM_BUILD_ROOT%{mingw64_bindir}/simple.exe

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete


%files -n mingw32-plotmm
%doc AUTHORS COPYING ChangeLog README
%{mingw32_bindir}/libplotmm-0.dll
%{mingw32_libdir}/libplotmm.dll.a
%{mingw32_libdir}/pkgconfig/plotmm.pc
%{mingw32_includedir}/plotmm

%files -n mingw32-plotmm-static
%{mingw32_libdir}/libplotmm.a

%files -n mingw64-plotmm
%doc AUTHORS COPYING ChangeLog README
%{mingw64_bindir}/libplotmm-0.dll
%{mingw64_libdir}/libplotmm.dll.a
%{mingw64_libdir}/pkgconfig/plotmm.pc
%{mingw64_includedir}/plotmm

%files -n mingw64-plotmm-static
%{mingw64_libdir}/libplotmm.a


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.2-42
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 0.1.2-35
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 13:44:50 GMT 2020 Sandro Mani <manisandro@gmail.com> - 0.1.2-31
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 0.1.2-28
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 12 2016 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.1.2-21
- build fix (enable C++11 mode)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar  2 2013 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.1.2-16
- build 64bit

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 07 2012 Kalev Lember <kalevlember@gmail.com> - 0.1.2-13
- Renamed the source package to mingw-plotmm (#801014)
- Use mingw macros without leading underscore

* Tue Feb 28 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.1.2-12
- Rebuild against the mingw-w64 toolchain

* Thu Feb  2 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.1.2-11
- Dropped .la files

* Tue Jan 31 2012 Kalev Lember <kalevlember@gmail.com> - 0.1.2-10
- Rebuilt for libpng 1.5
- Spec cleanup for new rpmbuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 07 2011 Kalev Lember <kalevlember@gmail.com> - 0.1.2-8
- Rebuilt against win-iconv

* Thu Apr 28 2011 Kalev Lember <kalev@smartlink.ee> - 0.1.2-7
- Rebuilt for proxy-libintl removal

* Fri Apr 22 2011 Kalev Lember <kalev@smartlink.ee> - 0.1.2-6
- Rebuilt for pseudo-reloc version mismatch (#698827)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.1.2-3
- add debuginfo packages

* Mon Apr 27 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.1.2-2
- add missing BR

* Sun Apr 19 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 0.1.2-1
- copy from native
