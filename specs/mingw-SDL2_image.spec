%{?mingw_package_header}

Name:           mingw-SDL2_image
Version:        2.8.4
Release:        1%{?dist}
Summary:        MinGW Windows port of the Image loading library for SDL2

License:        LGPL-2.0-or-later
URL:            https://github.com/libsdl-org/SDL_image
Source0:        https://github.com/libsdl-org/SDL_image/releases/download/release-%{version}/SDL2_image-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-SDL2
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-libjpeg-turbo
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw32-libwebp


BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-SDL2
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-libjpeg-turbo
BuildRequires:  mingw64-libtiff
BuildRequires:  mingw64-libwebp


%description
Simple DirectMedia Layer (SDL2) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.  This package contains a simple library for loading images of
various formats (BMP, PPM, PCX, GIF, JPEG, PNG) as SDL2 surfaces.


# Win32
%package -n mingw32-SDL2_image
Summary:        MinGW Windows port of the Image loading library for SDL2

%description -n mingw32-SDL2_image
Simple DirectMedia Layer (SDL2) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.  This package contains a simple library for loading images of
various formats (BMP, PPM, PCX, GIF, JPEG, PNG) as SDL2 surfaces.


# Win64
%package -n mingw64-SDL2_image
Summary:        MinGW Windows port of the Image loading library for SDL2

%description -n mingw64-SDL2_image
Simple DirectMedia Layer (SDL2) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.  This package contains a simple library for loading images of
various formats (BMP, PPM, PCX, GIF, JPEG, PNG) as SDL2 surfaces.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n SDL2_image-%{version}


%build
# the --disabled-*-shared lines below stops SDL2_image from loading those
# libraries at link time. Instead they are loaded when needed.
%mingw_configure \
    --disable-jpg-shared \
    --disable-png-shared \
    --disable-tif-shared \
    --disable-webp-shared \
    --disable-static
#    --disable-dependency-tracking \
%mingw_make_build


%install
%mingw_make_install

# Drop all .la files
find %{buildroot} -name "*.la" -delete


# Win32
%files -n mingw32-SDL2_image
%license LICENSE.txt
%{mingw32_bindir}/SDL2_image.dll
%{mingw32_libdir}/libSDL2_image.dll.a
%{mingw32_libdir}/cmake/SDL2_image/
%{mingw32_libdir}/pkgconfig/SDL2_image.pc
%{mingw32_includedir}/SDL2

# Win64
%files -n mingw64-SDL2_image
%license LICENSE.txt
%{mingw64_bindir}/SDL2_image.dll
%{mingw64_libdir}/libSDL2_image.dll.a
%{mingw64_libdir}/cmake/SDL2_image/
%{mingw64_libdir}/pkgconfig/SDL2_image.pc
%{mingw64_includedir}/SDL2


%changelog
* Mon Jan 06 2025 Sandro Mani <manisandro@gmail.com> - 2.8.4-1
- Update to 2.8.4

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 10 2024 Sandro Mani <manisandro@gmail.com> - 2.8.2-1
- Update to 2.8.2

* Mon Dec 18 2023 Sandro Mani <manisandro@gmail.com> - 2.8.1-1
- Update to 2.8.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 19 2023 Sandro Mani <manisandro@gmail.com> - 2.6.3-1
- Update to 2.6.3

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 05 2022 Sandro Mani <manisandro@gmail.com> - 2.6.2-1
- Update to 2.6.2

* Thu Aug 04 2022 Sandro Mani <manisandro@gmail.com> - 2.6.1-1
- Update to 2.6.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.0.5-8
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Pete Walter <pwalter@fedoraproject.org> - 2.0.5-1
- Update to 2.0.5

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 06 2018 Pete Walter <pwalter@fedoraproject.org> - 2.0.4-1
- Update to 2.0.4

* Thu Sep 27 2018 Kalev Lember <klember@redhat.com> - 2.0.3-1
- Update to 2.0.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 2.0.1-2
- Rebuild (libwebp)

* Mon Oct 24 2016 Kalev Lember <klember@redhat.com> - 2.0.1-1
- Update to 2.0.1
- Don't set group tags

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 29 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0.0-6
- Rebuild against mingw-libwebp-0.5.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 06 2015 maci <maci@satgnu.net> - 2.0.0-4
- Strip wrong end of line encoding
- Fedora 21 rebuild

* Mon Jul 21 2014 maci <maci@satgnu.net> - 2.0.0-3
- Fix homepage URL

* Tue May 13 2014 Marcel Wysocki <maci@satgnu.net> - 2.0.0-2
- Removed redundant BuildRequires

* Mon May 12 2014 Marcel Wysocki <maci@satgnu.net> - 2.0.0-1
- Initial rpm
