%{?mingw_package_header}

Name:           mingw-SDL_mixer
Version:        1.2.12
Release:        26%{?dist}
Summary:        MinGW Windows port of Simple DirectMedia Layer's Sample Mixer Library

License:        Zlib
URL:            http://www.libsdl.org/projects/SDL_mixer/
Source0:        http://www.libsdl.org/projects/SDL_mixer/release/SDL_mixer-%{version}.tar.gz
# Fix incompatible pointer types
Patch0:         sdl-mixer-incompatible-pointer-types.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-SDL
BuildRequires:  mingw32-libvorbis

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-SDL
BuildRequires:  mingw64-libvorbis


%description
A simple multi-channel audio mixer for SDL. It supports 4 channels of
16 bit stereo audio, plus a single channel of music, mixed by the popular
MikMod MOD library.


# Win32
%package -n mingw32-SDL_mixer
Summary:        MinGW Windows port of Simple DirectMedia Layer's Sample Mixer Library
Requires:       pkgconfig

%description -n mingw32-SDL_mixer
A simple multi-channel audio mixer for SDL. It supports 4 channels of
16 bit stereo audio, plus a single channel of music, mixed by the popular
MikMod MOD library.

# Win64
%package -n mingw64-SDL_mixer
Summary:        MinGW Windows port of Simple DirectMedia Layer's Sample Mixer Library
Requires:       pkgconfig

%description -n mingw64-SDL_mixer
A simple multi-channel audio mixer for SDL. It supports 4 channels of
16 bit stereo audio, plus a single channel of music, mixed by the popular
MikMod MOD library.


# Automatically create a debuginfo package
%{?mingw_debug_package}


%prep
%autosetup -p1 -n SDL_mixer-%{version}


%build
%mingw_configure \
    --disable-music-flac \
    --disable-static

%mingw_make_build


%install
%mingw_make_install

# Drop all .la files
find %{buildroot} -name "*.la" -delete


# Win32
%files -n mingw32-SDL_mixer
%doc README CHANGES COPYING
%{mingw32_bindir}/SDL_mixer.dll
%{mingw32_libdir}/libSDL_mixer.dll.a
%{mingw32_libdir}/pkgconfig/SDL_mixer.pc
%{mingw32_includedir}/SDL

# Win64
%files -n mingw64-SDL_mixer
%doc README CHANGES COPYING
%{mingw64_bindir}/SDL_mixer.dll
%{mingw64_libdir}/libSDL_mixer.dll.a
%{mingw64_libdir}/pkgconfig/SDL_mixer.pc
%{mingw64_includedir}/SDL


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.2.12-19
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 02 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.2.12-1
- Update to 1.2.12
- Upstream switched license from LGPLv2+ to zlib
- Removed rpath hacks as they are not relevant for the win32/win64 targets
- Removed configure arguments which are not relevant for the win32/win64 targets

* Sat Apr 14 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.2.11-8
- Added win64 support (contributed by Mikkel Kruse Johnsen)
- Use parallel make

* Fri Mar 09 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.2.11-7
- Dropped .la files

* Wed Mar 07 2012 Kalev Lember <kalevlember@gmail.com> - 1.2.11-6
- Renamed the source package to mingw-SDL_mixer (#801027)
- Modernize the spec file
- Use mingw macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.2.11-5
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 06 2011 Kalev Lember <kalevlember@gmail.com> - 1.2.11-3
- Rebuilt against win-iconv

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 19 2010 Stefan Riemens <fgfs.stefan@gmail.com> - 1.2.11-1
- Fix debuginfo package generation
- Fix defattr line

* Sat Sep 25 2010 Stefan Riemens <fgfs.stefan@gmail.com> - 1.2.11-0
- New upstream version

* Wed Nov 25 2009 Stefan Riemens <fgfs.stefan@gmail.com> - 1.2.8-3
- Remove explicit requires: on mingw32-SDL
- Fix non-utf-8 file encoding
- Autogenerate debuginfo subpackage

* Thu Nov 11 2009 Jason Woofenden <jason@jasonwoof.com> - 1.2.8-2
- use macro global instead of define in this spec file
- description no longer (falsely) claims we have midi and .ogg support

* Thu Jun 18 2009 Jason Woofenden <jason@jasonwoof.com> - 1.2.8-1
- Initial RPM release.
