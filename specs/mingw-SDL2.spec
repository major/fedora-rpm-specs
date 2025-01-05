%{?mingw_package_header}

Name:           mingw-SDL2
Version:        2.30.11
Release:        1%{?dist}
Summary:        MinGW Windows port of SDL2 cross-platform multimedia library

License:        LGPL-2.0-or-later
URL:            http://www.libsdl.org/
Source0:        http://www.libsdl.org/release/SDL2-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  dos2unix

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++

%ifarch %{ix86}
BuildRequires: nasm
%endif

%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.


# Win32
%package -n mingw32-SDL2
Summary:        MinGW Windows port of SDL cross-platform multimedia library

%description -n mingw32-SDL2
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.

# Win32 (static)
%package -n mingw32-SDL2-static
Summary:        MinGW Windows port of SDL cross-platform multimedia library
Requires:       mingw32-SDL2 = %{version}-%{release}

%description -n mingw32-SDL2-static
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.

# Win64
%package -n mingw64-SDL2
Summary:        MinGW Windows port of SDL cross-platform multimedia library

%description -n mingw64-SDL2
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.

# Win64 (static)
%package -n mingw64-SDL2-static
Summary:        MinGW Windows port of SDL cross-platform multimedia library
Requires:       mingw64-SDL2 = %{version}-%{release}

%description -n mingw64-SDL2-static
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n SDL2-%{version}


%build
%mingw_cmake -DSDL_STATIC=ON -DSDL_STATIC_PIC=ON
%mingw_make_build


%install
%mingw_make_install

rm -rf %{buildroot}%{mingw32_datadir}/licenses
rm -rf %{buildroot}%{mingw64_datadir}/licenses


# Win32
%files -n mingw32-SDL2
%license LICENSE.txt
%{mingw32_bindir}/SDL2.dll
%{mingw32_bindir}/sdl2-config
%{mingw32_libdir}/libSDL2.dll.a
%{mingw32_libdir}/libSDL2main.a
%{mingw32_libdir}/libSDL2_test.a
%{mingw32_libdir}/cmake/SDL2/
%exclude %{mingw32_libdir}/cmake/SDL2/*static*
%{mingw32_libdir}/pkgconfig/sdl2.pc
%{mingw32_datadir}/aclocal/sdl2.m4
%{mingw32_includedir}/SDL2

# Win32 (static)
%files -n mingw32-SDL2-static
%{mingw32_libdir}/libSDL2.a
%{mingw32_libdir}/cmake/SDL2/*static*

# Win64
%files -n mingw64-SDL2
%license LICENSE.txt
%{mingw64_bindir}/SDL2.dll
%{mingw64_bindir}/sdl2-config
%{mingw64_libdir}/libSDL2.dll.a
%{mingw64_libdir}/libSDL2main.a
%{mingw64_libdir}/libSDL2_test.a
%{mingw64_libdir}/cmake/SDL2/
%exclude %{mingw64_libdir}/cmake/SDL2/*static*
%{mingw64_libdir}/pkgconfig/sdl2.pc
%{mingw64_datadir}/aclocal/sdl2.m4
%{mingw64_includedir}/SDL2

# Win64 (static)
%files -n mingw64-SDL2-static
%{mingw64_libdir}/libSDL2.a
%{mingw64_libdir}/cmake/SDL2/*static*


%changelog
* Fri Jan 03 2025 Sandro Mani <manisandro@gmail.com> - 2.30.11-1
- Update to 2.30.11

* Sat Dec 07 2024 Sandro Mani <manisandro@gmail.com> - 2.30.9-1
- Update to 2.30.9

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.30.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 22 2024 Sandro Mani <manisandro@gmail.com> - 2.30.3-1
- Update to 2.30.3

* Tue Mar 26 2024 Sandro Mani <manisandro@gmail.com> - 2.30.1-1
- Update to 2.30.1

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 07 2023 Sandro Mani <manisandro@gmail.com> - 2.28.5-1
- Update to 2.28.5

* Tue Oct 03 2023 Sandro Mani <manisandro@gmail.com> - 2.28.4-1
- Update to 2.28.4

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 05 2023 Sandro Mani <manisandro@gmail.com> - 2.26.5-1
- Update to 2.26.5

* Sun Mar 19 2023 Sandro Mani <manisandro@gmail.com> - 2.26.4-1
- Update to 2.26.4

* Wed Feb 15 2023 Sandro Mani <manisandro@gmail.com> - 2.26.3-1
- Update to 2.26.3

* Sun Jan 22 2023 Sandro Mani <manisandro@gmail.com> - 2.26.2-1
- Update to 2.26.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 22 2022 Neal Gompa <ngompa@fedoraproject.org> - 2.26.0-1
- Update to 2.26.0

* Fri Aug 19 2022 Neal Gompa <ngompa@fedoraproject.org> - 2.24.0-1
- Update to 2.24.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 23 2022 Sandro Mani <manisandro@gmail.com> - 2.0.22-2
- Fix packaging static cmake config

* Sat Apr 30 2022 Neal Gompa <ngompa@fedoraproject.org> - 2.0.22-1
- Update to 2.0.22

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.0.20-4
- Rebuild with mingw-gcc-12

* Wed Mar 02 2022 Sandro Mani <manisandro@gmail.com> - 2.0.22-3
- Add mingw-SDL2_lmingw32.patch

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Sandro Mani <manisandro@gmail.com> - 2.0.20-1
- Update to 2.0.20

* Wed Dec 01 2021 Neal Gompa <ngompa@fedoraproject.org> - 2.0.18-1
- Update to 2.0.18
- Switch to building with CMake

* Wed Aug 11 2021 Sandro Mani <manisandro@gmail.com> - 2.0.16-1
- Update to 2.0.16

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Sandro Mani <manisandro@gmail.com> - 2.0.14-1
- Update to 2.0.14

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 11 2020 Pete Walter <pwalter@fedoraproject.org> - 2.0.12-1
- Update to 2.0.12

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Sandro Mani <manisandro@gmail.com> - 2.0.10-1
- Update to 2.0.10

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.0.9-4
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 02 2018 Kalev Lember <klember@redhat.com> - 2.0.9-1
- Update to 2.0.9

* Thu Sep 27 2018 Kalev Lember <klember@redhat.com> - 2.0.8-1
- Update to 2.0.8

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 24 2016 Kalev Lember <klember@redhat.com> - 2.0.5-1
- Update to 2.0.5
- Don't set group tags

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 15 2015 Anonymous Maarten <anonymous.maarten@gmail.com> - 2.0.3-7
- Added static package.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 29 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0.3-5
- Don't try to re-implement D3D11 pieces which are already part of mingw-w64
- Workaround a gcc compatibility issue

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Marcel Wysocki <maci@satgnu.net> - 2.0.3-3
- Fix rpmlint warnings

* Tue May 13 2014 Marcel Wysocki <maci@satgnu.net> - 2.0.3-2
- Removed redundant BuildRequires

* Mon May 12 2014 Marcel Wysocki <maci@satgnu.net> - 2.0.3-1
- Initial rpm
