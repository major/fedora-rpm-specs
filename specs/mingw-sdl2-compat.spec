%{?mingw_package_header}

%global origname sdl2-compat
%global sdl3_minver 3.2.0

Name:           mingw-%{origname}
Version:        2.30.50
Release:        1%{?dist}
Summary:        MinGW Windows port of SDL 2.0 runtime compatibility library using SDL 3.0
# License of SDL-2.0 headers
License:        Zlib and Apache-2.0 and MIT and BSD-3-Clause
URL:            https://github.com/libsdl-org/%{origname}
Source0:        %{url}/archive/release-%{version}/%{origname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  git-core
BuildRequires:  make

BuildArch:      noarch

%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio device.

This code is a compatibility layer; it provides a binary-compatible API for
Windows programs written against SDL 2.0, but it uses SDL 3.0 behind the scenes.

If you are writing new code, please target SDL 3.0 directly and do not use
this layer.

%package -n mingw32-%{origname}
Summary:        MinGW 32-bit Windows port of SDL 2.0 compatibility library using SDL 3.0
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-SDL3 >= %{sdl3_minver}
# This replaces SDL2
Obsoletes:      mingw32-SDL2 < 2.30.11-2
Conflicts:      mingw32-SDL2 < 2.30.50~
Provides:       mingw32-SDL2 = %{version}
# This dlopens SDL3 (?!), so manually depend on it
Requires:       mingw32-SDL3 >= %{sdl3_minver}

%description -n mingw32-%{origname}
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio device.

This code is a compatibility layer; it provides a binary-compatible API for
Windows 32-bit programs written against SDL 2.0, but it uses SDL 3.0 behind
the scenes.

If you are writing new code, please target SDL 3.0 directly and do not use
this layer.

%package -n mingw64-%{origname}
Summary:        MinGW 64-bit Windows port of SDL 2.0 compatibility library using SDL 3.0
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-SDL3 >= %{sdl3_minver}
# This replaces SDL2
Obsoletes:      mingw64-SDL2 < 2.30.11-2
Conflicts:      mingw64-SDL2 < 2.30.50~
Provides:       mingw64-SDL2 = %{version}
# This dlopens SDL3 (?!), so manually depend on it
Requires:       mingw64-SDL3 >= %{sdl3_minver}

%description -n mingw64-%{origname}
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio device.

This code is a compatibility layer; it provides a binary-compatible API for
Windows 64-bit programs written against SDL 2.0, but it uses SDL 3.0 behind
the scenes.

If you are writing new code, please target SDL 3.0 directly and do not use
this layer.


%{?mingw_debug_package}


%prep
%autosetup -n %{origname}-release-%{version} -S git_am


%build
%mingw_cmake
%mingw_make_build


%install
%mingw_make_install

# These don't make sense here
rm -rf %{buildroot}%{mingw32_datadir}/licenses
rm -rf %{buildroot}%{mingw64_datadir}/licenses

# These exist in the native sdl2-compat package
rm -rf %{buildroot}%{mingw32_datadir}/aclocal
rm -rf %{buildroot}%{mingw64_datadir}/aclocal


%files -n mingw32-%{origname}
%license LICENSE.txt
%doc README.md BUGS.md COMPATIBILITY.md
%{mingw32_bindir}/SDL2.dll
%{mingw32_bindir}/sdl2-config
%{mingw32_libdir}/libSDL2.dll.a
%{mingw32_libdir}/libSDL2main.a
%{mingw32_libdir}/libSDL2_test.a
%{mingw32_libdir}/pkgconfig/sdl2_compat.pc
%{mingw32_libdir}/cmake/SDL2/
%{mingw32_includedir}/SDL2/


%files -n mingw64-%{origname}
%license LICENSE.txt
%doc README.md BUGS.md COMPATIBILITY.md
%{mingw64_bindir}/SDL2.dll
%{mingw64_bindir}/sdl2-config
%{mingw64_libdir}/libSDL2.dll.a
%{mingw64_libdir}/libSDL2main.a
%{mingw64_libdir}/libSDL2_test.a
%{mingw64_libdir}/pkgconfig/sdl2_compat.pc
%{mingw64_libdir}/cmake/SDL2/
%{mingw64_includedir}/SDL2/


%changelog
* Wed Jan 22 2025 Neal Gompa <ngompa@fedoraproject.org> - 2.30.50-1
- Update to 2.30.50 GA

* Sun Jan 19 2025 Neal Gompa <ngompa@fedoraproject.org> - 2.30.50~git20250119.1126.208cea9-1
- Bump to new git snapshot

* Sun Jan 19 2025 Neal Gompa <ngompa@fedoraproject.org> - 2.30.50~git20250116.10a9ed3-2
- Fix mingw-SDL2 obsoletes

* Fri Jan 17 2025 Neal Gompa <ngompa@fedoraproject.org> - 2.30.50~git20250116.10a9ed3-1
- Bump to new git snapshot

* Sun Jan 12 2025 Neal Gompa <ngompa@fedoraproject.org> - 2.30.50~git20250107.c368587-1
- Bump to new git snapshot

* Mon Dec 02 2024 Neal Gompa <ngompa@fedoraproject.org> - 2.30.50~git20241130.89e3c65-1
- Bump to a new snapshot

* Mon Dec 02 2024 Neal Gompa <ngompa@fedoraproject.org> - 2.30.50~git20241004.2115.e6b9f31-1
- Initial package

