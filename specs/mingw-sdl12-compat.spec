%{?mingw_package_header}

%global origname sdl12-compat

Name:           mingw-%{origname}
Version:        1.2.68
Release:        5%{?dist}
Summary:        MinGW Windows port of SDL 1.2 runtime compatibility library using SDL 2.0
# mp3 decoder code is MIT-0/PD
# SDL_opengl.h is zlib and MIT
License:        Zlib AND MIT AND (MIT-0 OR LicenseRef-Fedora-Public-Domain)
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
Windows programs written against SDL 1.2, but it uses SDL 2.0 behind the scenes.

If you are writing new code, please target SDL 2.0 directly and do not use
this layer.

%package -n mingw32-%{origname}
Summary:        MinGW 32-bit Windows port of SDL 1.2 compatibility library using SDL 2.0
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-SDL2
# This replaces SDL
Obsoletes:      mingw32-SDL < 1.2.15-19
Conflicts:      mingw32-SDL < 1.2.50
Provides:       mingw32-SDL = %{version}
# This dlopens SDL2 (?!), so manually depend on it
Requires:       mingw32-SDL2 >= 2.0.18

%description -n mingw32-%{origname}
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio device.

This code is a compatibility layer; it provides a binary-compatible API for
Windows 32-bit programs written against SDL 1.2, but it uses SDL 2.0 behind
the scenes.

If you are writing new code, please target SDL 2.0 directly and do not use
this layer.

%package -n mingw64-%{origname}
Summary:        MinGW 64-bit Windows port of SDL 1.2 compatibility library using SDL 2.0
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-SDL2
# This replaces SDL
Obsoletes:      mingw64-SDL < 1.2.15-19
Conflicts:      mingw64-SDL < 1.2.50
Provides:       mingw64-SDL = %{version}
# This dlopens SDL2 (?!), so manually depend on it
Requires:       mingw64-SDL2 >= 2.0.18

%description -n mingw64-%{origname}
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio device.

This code is a compatibility layer; it provides a binary-compatible API for
Windows 64-bit programs written against SDL 1.2, but it uses SDL 2.0 behind
the scenes.

If you are writing new code, please target SDL 2.0 directly and do not use
this layer.


%{?mingw_debug_package}


%prep
%autosetup -n %{origname}-release-%{version} -S git_am


%build
%mingw_cmake
%mingw_make_build


%install
%mingw_make_install

# These exist in the native sdl12-compat package
rm -rf %{buildroot}%{mingw32_datadir}/aclocal
rm -rf %{buildroot}%{mingw64_datadir}/aclocal


%files -n mingw32-%{origname}
%license LICENSE.txt
%doc README.md BUGS.md COMPATIBILITY.md
%{mingw32_bindir}/SDL.dll
%{mingw32_bindir}/sdl-config
%{mingw32_libdir}/libSDL.dll.a
%{mingw32_libdir}/libSDLmain.a
%{mingw32_libdir}/pkgconfig/sdl12_compat.pc
%{mingw32_includedir}/SDL/

%files -n mingw64-%{origname}
%license LICENSE.txt
%doc README.md BUGS.md COMPATIBILITY.md
%{mingw64_bindir}/SDL.dll
%{mingw64_bindir}/sdl-config
%{mingw64_libdir}/libSDL.dll.a
%{mingw64_libdir}/libSDLmain.a
%{mingw64_libdir}/pkgconfig/sdl12_compat.pc
%{mingw64_includedir}/SDL/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.68-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.68-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.68-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 26 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.2.68-1
- Update to 1.2.68

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 30 2023 Sandro Mani <manisandro@gmail.com> - 1.2.64-1
- Update to 1.2.64

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Oct 30 2022 Neal Gompa <ngompa@fedoraproject.org> - 1.2.60-2
- Backport fix for SDL12COMPAT_MAX_VIDMODE

* Sun Oct 30 2022 Sandro Mani <manisandro@gmail.com> - 1.2.60-1
- Update to 1.2.60

* Fri Sep 16 2022 Neal Gompa <ngompa@fedoraproject.org> - 1.2.56-1
- Update to 1.2.56

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.52-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.2.52-2
- Rebuild with mingw-gcc-12

* Thu Mar 03 2022 Neal Gompa <ngompa@fedoraproject.org> - 1.2.52-1
- Update to 1.2.52

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1~git.20211125.4e4527a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 27 2021 Neal Gompa <ngompa@fedoraproject.org> - 0.0.1~git.20211125.4e4527a-1
- Update to new snapshot release

* Sun Nov 07 2021 Neal Gompa <ngompa@fedoraproject.org> - 0.0.1~git.20211107.a10d6b6-1
- Update to new snapshot release

* Sun Sep 26 2021 Neal Gompa <ngompa@fedoraproject.org> - 0.0.1~git.20210926.c6cfc8f-1
- Update to new snapshot release

* Mon Sep 13 2021 Neal Gompa <ngompa@fedoraproject.org> - 0.0.1~git.20210909.a98590a-1
- Update to new snapshot release

* Thu Aug 26 2021 Neal Gompa <ngompa@fedoraproject.org> - 0.0.1~git.20210825.b5f7170-1
- Update to new snapshot release

* Sun Aug 22 2021 Neal Gompa <ngompa@fedoraproject.org> - 0.0.1~git.20210814.a3bfcb2-1
- Update to new snapshot release
- Drop upstreamed patch included in this snapshot

* Sun Jul 25 2021 Neal Gompa <ngompa@fedoraproject.org> - 0.0.1~git.20210719.aa9919b-1
- Update to new snapshot release

* Sat Jul 24 2021 Sandro Mani <manisandro@gmail.com> -  - 0.0.1~git.20210709.51254e5-3
- Add -lmingw32 to SDL_LIBS (prevents undefined references to WinMain@16 by consumers)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1~git.20210709.51254e5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 09 2021 Neal Gompa <ngompa13@gmail.com> - 0.0.1~git.20210709.51254e5-1
- Update to new snapshot release

* Tue Jun 29 2021 Neal Gompa <ngompa13@gmail.com> - 0.0.1~git.20210628.cf47f88-1
- Update to new snapshot release

* Sun Jun 20 2021 Neal Gompa <ngompa13@gmail.com> - 0.0.1~git.20210619.4ad7ba6-1
- Update to new snapshot release

* Fri Jun 18 2021 Neal Gompa <ngompa13@gmail.com> - 0.0.1~git.20210618.f44f295-1
- Update to new snapshot release

* Sun Jun 13 2021 Neal Gompa <ngompa13@gmail.com> - 0.0.1~git.20210612.44f299f-1
- Update to new snapshot release
- Update license tag information

* Sat Jun 12 2021 Neal Gompa <ngompa13@gmail.com> - 0.0.1~git.20210612.c0504eb-1
- Initial package based on sdl12-compat package
