%?mingw_package_header

Name:           mingw-SDL2_ttf
License:        Zlib

Version:        2.22.0
Release:        3%{?dist}

%global  pkg_summary  MinGW Windows port of the TrueType font handling library for SDL2
Summary: %{pkg_summary}

URL:            https://www.libSDL.org/projects/SDL_ttf/
Source0:        %{URL}release/SDL2_ttf-%{version}.tar.gz

# By default, some example programs are also built - we want only the library.
Patch0:         0000-disable-building-example-programs.patch

BuildArch:      noarch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-freetype
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-harfbuzz
BuildRequires:  mingw32-SDL2

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-freetype
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-harfbuzz
BuildRequires:  mingw64-SDL2


%global  pkg_description  Simple DirectMedia Layer (SDL2) is a cross-platform multimedia library \
designed to provide fast access to the graphics frame buffer and audio device. \
This package contains a library that allows you to use TrueType fonts \
to render text in SDL2 applications.

%description
%{pkg_description}


# Win32
%package -n mingw32-SDL2_ttf
Summary: %{pkg_summary}

%description -n mingw32-SDL2_ttf
%{pkg_description}


# Win64
%package -n mingw64-SDL2_ttf
Summary: %{pkg_summary}

%description -n mingw64-SDL2_ttf
%{pkg_description}


%?mingw_debug_package


%prep
%autosetup -n SDL2_ttf-%{version} -p1


%build
./autogen.sh
%mingw_configure \
	--disable-static \
	--disable-dependency-tracking \
	--enable-freetype-builtin=no \
	--enable-harfbuzz-builtin=no \
	--enable-harfbuzz=yes \

%mingw_make_build


%install
%mingw_make_install

# Drop all .la files
find %{buildroot} -name "*.la" -delete

# Convert CRLF line endings to LF
sed -i 's/\r$//' README.txt CHANGES.txt LICENSE.txt


# Win32
%files -n mingw32-SDL2_ttf
%doc CHANGES.txt README.txt
%license LICENSE.txt
%{mingw32_bindir}/SDL2_ttf.dll
%{mingw32_libdir}/libSDL2_ttf.dll.a
%{mingw32_libdir}/cmake/SDL2_ttf/
%{mingw32_libdir}/pkgconfig/SDL2_ttf.pc
%{mingw32_includedir}/SDL2

# Win64
%files -n mingw64-SDL2_ttf
%doc CHANGES.txt README.txt
%license LICENSE.txt
%{mingw64_bindir}/SDL2_ttf.dll
%{mingw64_libdir}/libSDL2_ttf.dll.a
%{mingw64_libdir}/cmake/SDL2_ttf/
%{mingw64_libdir}/pkgconfig/SDL2_ttf.pc
%{mingw64_includedir}/SDL2


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 06 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.22.0-1
- Update to v2.22.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 18 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.20.2-1
- Update to v2.20.2
- Convert License tag to SPDX

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 11 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.20.1-1
- Update to v2.20.1
- Drop Patch1 (fix faulty Harfbuzz check - no longer needed, issue fixed upstream)
- Drop Patch2 (fix for CVE-2022-27470 - included in this release)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.0.18-3
- Add a patch for CVE-2022-27470

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.0.18-2
- Rebuild with mingw-gcc-12

* Thu Feb 10 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.0.18-1
- Update to v2.0.18

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 07 2019 Artur Iwicki <fedora@svgames.pl> - 2.0.15-2
- Fix wrong License: tag (was "LGPLv2+", should be "zlib")
- Fix COPYING.txt being marked as %%doc instead of %%license
- Fix package description containing a leading newline

* Wed Jul 03 2019 Artur Iwicki <fedora@svgames.pl> - 2.0.15-1
- Initial packaging
