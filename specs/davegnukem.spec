Name: davegnukem
Summary: Side-view scrolling 2D shooter

# README.md says simply "MIT license or GPL".
# The debian/copyright file says "Expat or GPL-2 or GPL-3".
License: MIT OR GPL-2.0-only OR GPL-3.0-only

Version: 1.0.3
Release: 4%{?dist}

URL: https://djoffe.com/gnukem/
Source0: https://github.com/davidjoffe/dave_gnukem/archive/%{version}/dave_gnukem-%{version}.tar.gz
Source1: https://github.com/davidjoffe/gnukem_data/archive/%{version}/gnukem_data-%{version}.tar.gz

# AppStream metainfo file and a 128x128 icon.
# Added to the repo after v1.0.3 was released.
Source90: https://raw.githubusercontent.com/davidjoffe/dave_gnukem/72d05572ef3dbdff9d317df686f44e73a18bc340/debian/appstream/com.djoffe.davegnukem.metainfo.xml
Source91: https://raw.githubusercontent.com/davidjoffe/dave_gnukem/72d05572ef3dbdff9d317df686f44e73a18bc340/debian/icons/hicolor/128x128/apps/davegnukem.png

# Backport some upstream improvements to the Makefile.
# https://github.com/davidjoffe/dave_gnukem/commit/35ddcf783f737176b7190bd0157ec6a1f85e78a3.patch
# https://github.com/davidjoffe/dave_gnukem/commit/a3673af959a51184b6e86d8b256248f59537e83e.patch
# https://github.com/davidjoffe/dave_gnukem/commit/dcb4c3939f0e0d69a840df4313e958924e6b9c22.patch
# https://github.com/davidjoffe/dave_gnukem/commit/547393b84c8744f469ccb7af08b0256dfe3695e5.patch
# https://github.com/davidjoffe/dave_gnukem/commit/11d882c228f55df5c37c74038d0b2eb77e9b512b.patch
# https://github.com/davidjoffe/dave_gnukem/commit/e148befb7c2e4572db730526601f0b392830bb96.patch
# https://github.com/davidjoffe/dave_gnukem/commit/a99a7290016d3cb49d3d765eeb7492ae9818f76b.patch
# https://github.com/davidjoffe/dave_gnukem/commit/412e590de761fcc903e4b2aa10618d85af1fb0cd.patch
Patch0: gnukem--Makefile.patch

# Fix build on big-endian architectures
Patch1: gnukem--BigEndian.patch

%global dave_make_vars PREFIX="%{_prefix}" BIN_DIR="%{_bindir}" DATA_DIR="%{_datadir}/%{name}/"

BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: make
BuildRequires: SDL2-devel
BuildRequires: SDL2_mixer-devel

Requires: %{name}-data = %{version}-%{release}

%description
Dave Gnukem is a retro-style 2D scrolling platform shooter similar to,
and inspired by, Duke Nukem 1 (~1991). The original Duke Nukem 1 had
16-color EGA 320x200 graphics; the aim here is 'similar but different'
gameplay and 'look and feel'. It is kind of a parody of the original.


%package data
Summary: Data files for Dave Gnukem
BuildArch: noarch

# Check debian/copyright for a detailed list
License: CC0-1.0 AND CC-BY-3.0 AND (MIT OR GPL-2.0-only OR GPL-3.0-only)

Requires: hicolor-icon-theme

%description data
This package contains data files (graphics, sounds, et cetera)
required to play Dave Gnukem.


%prep
%setup -q -n dave_gnukem-%{version} -a 1
mv ./gnukem_data-%{version} ./data

mkdir -p debian/appstream/
cp -a %{SOURCE90} debian/appstream/

mkdir -p debian/icons/hicolor/128x128/apps/
cp -a %{SOURCE91} debian/icons/hicolor/128x128/apps/

%autopatch -p1


%build
%make_build %{dave_make_vars}


%install
%make_install %{dave_make_vars}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/com.djoffe.%{name}.metainfo.xml


%files
%doc %{_docdir}/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/com.djoffe.%{name}.metainfo.xml
%{_mandir}/man6/%{name}.6*

%files data
%license debian/copyright COPYING MIT-LICENSE.txt
%doc %{_docdir}/%{name}-data/
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}


%changelog
* Wed Jul 15 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Tue May 19 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.0.3-3
- Change license tag (GPL-2.0-or-later -> GPL-2.0-only or GPL-3.0-only)
- Move license texts to -data subpackage so they're always installed
- Add links to upstream commits for patches

* Sun Aug 31 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.0.3-2
- Backport the AppStream metainfo file and larger icon

* Mon Aug 18 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.0.3-1
- Initial packaging
