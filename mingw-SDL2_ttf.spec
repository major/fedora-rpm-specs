%?mingw_package_header

Name:           mingw-SDL2_ttf
License:        zlib

Version:        2.0.18
Release:        4%{?dist}

%global  pkg_summary  MinGW Windows port of the TrueType font handling library for SDL2
Summary: %{pkg_summary}

URL:            https://www.libSDL.org/projects/SDL_ttf/
Source0:        %{URL}release/SDL2_ttf-%{version}.tar.gz

# By default, some example programs are also built - we want only the library.
Patch0:         0000-disable-building-example-programs.patch

# The configure script checks if harfbuzz was built with freetype support,
# but Fedora's harfbuzz.dll uses delayed loading for freetype.dll,
# which causes this check to fail. This patch removes the check entirely.
Patch1:         0001-no-harfbuzz-check.patch

# Fix for CVE-2022-27470
# Backport of upstream commits:
# - https://github.com/libsdl-org/SDL_ttf/commit/09a2294338d7907ae955b07affdac229546f9cc9
# - https://github.com/libsdl-org/SDL_ttf/commit/db1b41ab8bde6723c24b866e466cad78c2fa0448
# See: https://bugzilla.redhat.com/show_bug.cgi?id=2081599
Patch2:		0002-CVE-2022-27470.patch

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
%setup -q -n SDL2_ttf-%{version}
%patch0 -p0
%patch1 -p1
%patch2 -p1


%build
./autogen.sh
%mingw_configure \
	--disable-static \
	--disable-dependency-tracking \
	--enable-freetype-builtin=no \
	--enable-harfbuzz-builtin=no \

%mingw_make_build


%install
%mingw_make_install

# Drop all .la files
find %{buildroot} -name "*.la" -delete

# Convert CRLF line endings to LF
sed -i 's/\r$//' README.txt CHANGES.txt COPYING.txt


# Win32
%files -n mingw32-SDL2_ttf
%doc CHANGES.txt README.txt
%license COPYING.txt
%{mingw32_bindir}/SDL2_ttf.dll
%{mingw32_libdir}/libSDL2_ttf.dll.a
%{mingw32_libdir}/pkgconfig/SDL2_ttf.pc
%{mingw32_includedir}/SDL2

# Win64
%files -n mingw64-SDL2_ttf
%doc CHANGES.txt README.txt
%license COPYING.txt
%{mingw64_bindir}/SDL2_ttf.dll
%{mingw64_libdir}/libSDL2_ttf.dll.a
%{mingw64_libdir}/pkgconfig/SDL2_ttf.pc
%{mingw64_includedir}/SDL2


%changelog
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
