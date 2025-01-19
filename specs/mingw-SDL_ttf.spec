%?mingw_package_header

Name:           mingw-SDL_ttf
Version:        2.0.11
Release:        17%{?dist}

%global  pkg_summary  MinGW Windows port of the TrueType font handling library for SDL
Summary: %{pkg_summary}

License:        Zlib
URL:            https://www.libSDL.org/projects/SDL_ttf/release-1.2.html
Source0:        https://www.libSDL.org/projects/SDL_ttf/release/SDL_ttf-%{version}.tar.gz

# Upstream bug #830: TTF_RenderGlyph_Shaded is broken
# Patch taken from upstream Bugzilla:
#   https://bugzilla-attachments.libsdl.org/attachments/830/renderglyph_shaded.patch.txt
Patch0:         renderglyph_shaded.patch

BuildArch:      noarch

BuildRequires:  freetype-devel >= 2.0
BuildRequires:  %{_bindir}/iconv
BuildRequires:  make

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-freetype
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-SDL >= 1.2

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-freetype
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-SDL >= 1.2


%global  pkg_description  Simple DirectMedia Layer (SDL) is a cross-platform multimedia library \
designed to provide fast access to the graphics frame buffer and audio device. \
This package contains a library that allows you to use TrueType fonts \
to render text in SDL 1.2 applications.

%description
%{pkg_description}


# Win32
%package -n mingw32-SDL_ttf
Summary: %{pkg_summary}

%description -n mingw32-SDL_ttf
%{pkg_description}


# Win64
%package -n mingw64-SDL_ttf
Summary: %{pkg_summary}

%description -n mingw64-SDL_ttf
%{pkg_description}


%?mingw_debug_package


%prep
%setup -q -n SDL_ttf-%{version}
%patch -P0 -p0

# Convert file encoding
for FILE in CHANGES; do
  iconv -f ISO-8859-1 -t UTF-8 < "${FILE}" > "${FILE}--UTF8"
  mv "${FILE}--UTF8" "${FILE}"
done


%build
%mingw_configure \
  --disable-static \
  --disable-dependency-tracking \

# The configure script for this library doesn't fully work with MinGW,
# so we have to edit the resulting Makefiles a bit.
sed \
  -e 's| -I%{_includedir}/freetype2 | -I%{mingw32_includedir}/freetype2 |g' \
  -e 's| -I%{_includedir}/libpng16 | -I%{mingw32_includedir}/libpng16 |g'   \
  -i build_win32/libtool build_win32/Makefile

sed \
  -e 's| -I%{_includedir}/freetype2 | -I%{mingw64_includedir}/freetype2 |g' \
  -e 's| -I%{_includedir}/libpng16 | -I%{mingw64_includedir}/libpng16 |g'   \
  -i build_win64/libtool build_win64/Makefile

%mingw_make %{?smp_mflags}


%install
%mingw_make DESTDIR=%{buildroot} install


# Drop all .la files
find %{buildroot} -name "*.la" -delete


# Win32
%files -n mingw32-SDL_ttf
%doc CHANGES README
%license COPYING
%{mingw32_bindir}/SDL_ttf.dll
%{mingw32_libdir}/libSDL_ttf.dll.a
%{mingw32_libdir}/pkgconfig/SDL_ttf.pc
%{mingw32_includedir}/SDL

# Win64
%files -n mingw64-SDL_ttf
%doc CHANGES README
%license COPYING
%{mingw64_bindir}/SDL_ttf.dll
%{mingw64_libdir}/libSDL_ttf.dll.a
%{mingw64_libdir}/pkgconfig/SDL_ttf.pc
%{mingw64_includedir}/SDL


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 08 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.0.11-16
- Fix License tag (project relicensed from LGPL-2.1-or-later to Zlib)
- Add a patch to fix a broken function

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.0.11-9
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Artur Iwicki <fedora@svgames.pl> - 2.0.11-2
- Convert COPYING.txt to UTF-8 encoding during %%prep

* Sun Jul 07 2019 Artur Iwicki <fedora@svgames.pl> - 2.0.11-1
- Initial packaging
