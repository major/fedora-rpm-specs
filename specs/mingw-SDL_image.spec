%{?mingw_package_header}

Name:           mingw-SDL_image
Version:        1.2.12
Release:        33%{?dist}
Summary:        MinGW Windows port of the Image loading library for SDL

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.libsdl.org/projects/SDL_image/
Source0:        http://www.libsdl.org/projects/SDL_image/release/SDL_image-%{version}.tar.gz
# Fix incompatible pointer types
Patch0:         sdl-image-incompatible-pointer-types.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-SDL
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-libjpeg-turbo
BuildRequires:  mingw32-libtiff

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-SDL
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-libjpeg-turbo
BuildRequires:  mingw64-libtiff


%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.  This package contains a simple library for loading images of
various formats (BMP, TIF, JPEG, PNG) as SDL surfaces.


# Win32
%package -n mingw32-SDL_image
Summary:        MinGW Windows port of the Image loading library for SDL
Requires:       pkgconfig

%description -n mingw32-SDL_image
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.  This package contains a simple library for loading images of
various formats (BMP, TIF, JPEG, PNG) as SDL surfaces.

# Win64
%package -n mingw64-SDL_image
Summary:        MinGW Windows port of the Image loading library for SDL
Requires:       pkgconfig

%description -n mingw64-SDL_image
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.  This package contains a simple library for loading images of
various formats (BMP, TIF, JPEG, PNG) as SDL surfaces.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n SDL_image-%{version}


%build
# the --disabled-*-shared lines below stops SDL_image from loading those
# libraries at link time. Instead they are loaded when needed.
%mingw_configure \
    --disable-jpg-shared \
    --disable-png-shared \
    --disable-tif-shared \
    --disable-static
#    --disable-dependency-tracking \

%mingw_make_build


%install
%mingw_make_install

# silence rpmlint:
iconv --from=ISO-8859-1 --to=UTF-8 CHANGES > CHANGES.new && \
touch -r CHANGES CHANGES.new && \
mv CHANGES.new CHANGES

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete


# Win32
%files -n mingw32-SDL_image
%doc README CHANGES COPYING
%{mingw32_bindir}/SDL_image.dll
%{mingw32_libdir}/libSDL_image.dll.a
%{mingw32_libdir}/pkgconfig/SDL_image.pc
%{mingw32_includedir}/SDL

# Win64
%files -n mingw64-SDL_image
%doc README CHANGES COPYING
%{mingw64_bindir}/SDL_image.dll
%{mingw64_libdir}/libSDL_image.dll.a
%{mingw64_libdir}/pkgconfig/SDL_image.pc
%{mingw64_includedir}/SDL


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.12-32
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.2.12-25
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 13 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.2.12-9
- Rebuild against libpng 1.6

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 25 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.2.12-7
- Rebuild against latest libtiff

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 14 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.2.12-5
- Added win64 support

* Fri Mar 09 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.2.12-4
- Dropped .la files

* Wed Mar 07 2012 Kalev Lember <kalevlember@gmail.com> - 1.2.12-3
- Renamed the source package to mingw-SDL_image (#801025)
- Use mingw macros without leading underscore

* Tue Feb 28 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.2.12-2
- Rebuild against the mingw-w64 toolchain

* Tue Jan 31 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.2.12-1
- Update to 1.2.12
- Re-enabled png support

* Tue Jan 31 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.2.10-6
- Disabled png support for now as SDL_image isn't compatible with libpng 1.5 yet
- Dropped the dependency extraction overrides as that's done automatically as of RPM 4.9
- Dropped unneeded RPM tags

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 06 2011 Kalev Lember <kalevlember@gmail.com> - 1.2.10-4
- Rebuilt against win-iconv

* Fri Jun 03 2011 Kalev Lember <kalev@smartlink.ee> - 1.2.10-3
- Rebuilt with mingw32-libjpeg-turbo, dropped jpeg_boolean patch (#604702)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 27 2010 Stefan Riemens <fgfs.stefan@gmail.com> - 1.2.10-1
- Include la files
- Fix debuginfo package generation

* Sat Sep 25 2010 Stefan Riemens <fgfs.stefan@gmail.com> - 1.2.10-0
- Update to new upstream release

* Wed Nov 25 2009 Stefan Riemens <fgfs.stefan@gmail.com> - 1.2.7-1
- Remove explicit Requires:
- Add patch for the mingw32-jpeg boolean issue
- Update to 1.2.7 to stay in sync with the native package
- Enable parallel make
- Autogenerate debuginfo subpackage
- Fix non-utf-8 file

* Thu Nov 11 2009 Jason Woofenden <jason@jasonwoof.com> - 1.2.6-2
- use macro global instead of define in this spec file
- added libtiff support
- updated description so it lists the correct supported image formats

* Thu Jun 18 2009 Jason Woofenden <jason@jasonwoof.com> - 1.2.6-1
- Initial RPM release.
