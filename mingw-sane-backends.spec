%?mingw_package_header

Name:           mingw-sane-backends
Version:        1.1.1
Release:        3%{?dist}
Summary:        MinGW package for SANE
# lib/ is LGPLv2+, backends are GPLv2+ with exceptions
# Tools are GPLv2+
License:        GPLv2+ and GPLv2+ with exceptions and Public Domain
URL:            http://www.sane-project.org
Source0:        https://gitlab.com/sane-project/backends/uploads/7d30fab4e115029d91027b6a58d64b43/sane-backends-%{version}.tar.gz

Patch0:         %{name}-%{version}-mingw.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-libusbx
BuildRequires:  mingw64-libusbx
BuildRequires:  python3


%description
Scanner Access Now Easy (SANE) is a universal scanner interface.  The
SANE application programming interface (API) provides standardized
access to any raster image scanner hardware (flatbed scanner,
hand-held scanner, video and still cameras, frame-grabbers, etc.).


# Mingw32
%package -n mingw32-sane-backends
Summary:        %{summary}

%description -n mingw32-sane-backends
Scanner Access Now Easy (SANE) is a universal scanner interface.  The
SANE application programming interface (API) provides standardized
access to any raster image scanner hardware (flatbed scanner,
hand-held scanner, video and still cameras, frame-grabbers, etc.).


%package -n mingw32-sane-backends-static
Summary:        Static version of the Scanner Access Now Easy (SANE) universal scanner interface.
Requires:       mingw32-sane-backends = %{version}-%{release}


%description -n mingw32-sane-backends-static
Static version of the Scanner Access Now Easy (SANE) universal scanner interface.


# Mingw64
%package -n mingw64-sane-backends
Summary:        %{summary}


%description -n mingw64-sane-backends
Scanner Access Now Easy (SANE) is a universal scanner interface.  The
SANE application programming interface (API) provides standardized
access to any raster image scanner hardware (flatbed scanner,
hand-held scanner, video and still cameras, frame-grabbers, etc.).


%package -n mingw64-sane-backends-static
Summary:        Static version of the Scanner Access Now Easy (SANE) universal scanner interface.
Requires:       mingw64-sane-backends = %{version}-%{release}


%description -n mingw64-sane-backends-static
Static version of the Scanner Access Now Easy (SANE) universal scanner interface.


%?mingw_debug_package


%prep
%setup -q -n sane-backends-%{version}
%patch0 -p1 -b.mingw
chmod -x COPYING


%build
export BACKENDS=fujitsu \
export PRELOADABLE_BACKENDS=fujitsu \
export LIBS="-lws2_32" \
export DIST_SANELIBS_LDFLAGS="-lsane -lfujitsu" \
%mingw_configure \
                 --with-usb
%mingw_make %{?_smp_mflags}
touch build_win32/backend/.libs/libsane-fujitsu-1.dll
touch build_win32/backend/.libs/libsane-dll-1.dll
touch build_win64/backend/.libs/libsane-fujitsu-1.dll
touch build_win64/backend/.libs/libsane-dll-1.dll


%install
rm -rf $RPM_BUILD_ROOT
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

# Remove documentation which duplicates that found in the native package.
rm -r $RPM_BUILD_ROOT%{mingw32_prefix}/share
rm -r $RPM_BUILD_ROOT%{mingw64_prefix}/share

# Delete temp files
rm -r $RPM_BUILD_ROOT%{mingw32_libdir}/sane
rm -r $RPM_BUILD_ROOT%{mingw64_libdir}/sane
rm -r $RPM_BUILD_ROOT%{mingw32_libdir}/bin
rm -r $RPM_BUILD_ROOT%{mingw64_libdir}/bin


# Win32
%files -n mingw32-sane-backends
%doc COPYING
%{mingw32_bindir}/libsane-1.dll
%{mingw32_bindir}/gamma4scanimage.exe
%{mingw32_bindir}/sane-config
%{mingw32_bindir}/sane-find-scanner.exe
%{mingw32_bindir}/scanimage.exe
%{mingw32_includedir}/sane/
%{mingw32_libdir}/pkgconfig/sane-backends.pc
%{mingw32_sysconfdir}/sane.d/

%files -n mingw32-sane-backends-static
%{mingw32_libdir}/libsane.dll.a


# Win64
%files -n mingw64-sane-backends
%doc COPYING
%{mingw64_bindir}/libsane-1.dll
%{mingw64_bindir}/gamma4scanimage.exe
%{mingw64_bindir}/sane-config
%{mingw64_bindir}/sane-find-scanner.exe
%{mingw64_bindir}/scanimage.exe
%{mingw64_includedir}/sane/
%{mingw64_libdir}/pkgconfig/sane-backends.pc
%{mingw64_sysconfdir}/sane.d/

%files -n mingw64-sane-backends-static
%{mingw64_libdir}/libsane.dll.a


%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 25 2023 Michael Cronenworth <mike@cchtml.com> - 1.1.1-1
- New upstream release

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.30-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.30-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.0.30-6
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 2020 Michael Cronenworth <mike@cchtml.com> - 1.0.30-1
- New upstream release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.27-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Michael Cronenworth <mike@cchtml.com> - 1.0.27-1
- New upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 28 2015 Michael Cronenworth <mike@cchtml.com> - 1.0.25-1
- New upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Nov 07 2013 Michael Cronenworth <mike@cchtml.com> - 1.0.24-1
- New upstream release

* Fri Sep 20 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.23-4
- Rebuild against winpthreads

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Michael Cronenworth <mike@cchtml.com> - 1.0.23-2
- Add patch for winpthreads support.

* Thu Jul 11 2013 Michael Cronenworth <mike@cchtml.com> - 1.0.23-1
- Initial RPM package.

