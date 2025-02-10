%{?mingw_package_header}

Name:           mingw-SDL3
Version:        3.2.4
Release:        1%{?dist}
Summary:        MinGW Windows port of SDL3 cross-platform multimedia library

License:        Zlib AND MIT AND Apache-2.0 AND (Apache-2.0 OR MIT)
URL:            http://www.libsdl.org/
Source0:        http://www.libsdl.org/release/SDL3-%{version}.tar.gz

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
%package -n mingw32-SDL3
Summary:        MinGW32 Windows port of SDL cross-platform multimedia library
# Long ago forked hidraw customized for SDL
Provides:       bundled(hidraw)

%description -n mingw32-SDL3
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.

# Win32 (static)
%package -n mingw32-SDL3-static
Summary:        MinGW32 Windows port of SDL cross-platform multimedia library
Requires:       mingw32-SDL3 = %{version}-%{release}

%description -n mingw32-SDL3-static
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.

# Win64
%package -n mingw64-SDL3
Summary:        MinGW64 Windows port of SDL cross-platform multimedia library
# Long ago forked hidraw customized for SDL
Provides:       bundled(hidraw)

%description -n mingw64-SDL3
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.

# Win64 (static)
%package -n mingw64-SDL3-static
Summary:        MinGW64 Windows port of SDL cross-platform multimedia library
Requires:       mingw64-SDL3 = %{version}-%{release}

%description -n mingw64-SDL3-static
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n SDL3-%{version}


%build
%mingw_cmake -DSDL_STATIC=ON -DSDL_STATIC_PIC=ON
%mingw_make_build


%install
%mingw_make_install

rm -rf %{buildroot}%{mingw32_datadir}/licenses
rm -rf %{buildroot}%{mingw64_datadir}/licenses


# Win32
%files -n mingw32-SDL3
%license LICENSE.txt
%{mingw32_bindir}/SDL3.dll
%{mingw32_libdir}/libSDL3.dll.a
%{mingw32_libdir}/libSDL3_test.a
%{mingw32_libdir}/cmake/SDL3/
%exclude %{mingw32_libdir}/cmake/SDL3/*static*
%{mingw32_libdir}/pkgconfig/sdl3.pc
%{mingw32_includedir}/SDL3

# Win32 (static)
%files -n mingw32-SDL3-static
%{mingw32_libdir}/libSDL3.a
%{mingw32_libdir}/cmake/SDL3/*static*

# Win64
%files -n mingw64-SDL3
%license LICENSE.txt
%{mingw64_bindir}/SDL3.dll
%{mingw64_libdir}/libSDL3.dll.a
%{mingw64_libdir}/libSDL3_test.a
%{mingw64_libdir}/cmake/SDL3/
%exclude %{mingw64_libdir}/cmake/SDL3/*static*
%{mingw64_libdir}/pkgconfig/sdl3.pc
%{mingw64_includedir}/SDL3

# Win64 (static)
%files -n mingw64-SDL3-static
%{mingw64_libdir}/libSDL3.a
%{mingw64_libdir}/cmake/SDL3/*static*


%changelog
* Sat Feb 08 2025 Neal Gompa <ngompa@fedoraproject.org> - 3.2.4-1
- Update to 3.2.4

* Mon Feb 03 2025 Neal Gompa <ngompa@fedoraproject.org> - 3.2.2-1
- Update to 3.2.2

* Wed Jan 22 2025 Neal Gompa <ngompa@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0 (SDL3 GA)

* Thu Jan 16 2025 Neal Gompa <ngompa@fedoraproject.org> - 3.1.10-1
- Update to 3.1.10

* Thu Jan 09 2025 Neal Gompa <ngompa@fedoraproject.org> - 3.1.8-1
- Update to 3.1.8

* Mon Dec 02 2024 Neal Gompa <ngompa@fedoraproject.org> - 3.1.6-1
- Initial package

