Name:          arx-libertatis
Version:       1.2.1
Release:       7%{?dist}
Summary:       Cross-platform, open source port of the Arx Fatalis RPG

# Main source - GPLv3+
# data/core/misc/dejavusansmono.ttf - Bitstream Vera
# data/core/misc/icons.ttf - OFL
# src/util/HandleType.h - BSL-1.0
# src/util/cmdline - BSL-1.0
# tools/crashreporter/qhexedit - LGPLv2+, but not used
# src/math/GtxFunctions.h - MIT
# src/util/MD5.cpp - Public Domain
# cmake/SDL-2.0.9/SDL_syswm.h - zlib
License:       GPLv3+ and Bitstream Vera and OFL and BSL-1.0 and MIT and zlib
URL:           https://arx-libertatis.org/
Source0:       https://arx-libertatis.org/files/%{name}-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: zlib-devel
BuildRequires: boost-devel
BuildRequires: glm-devel
BuildRequires: freetype-devel
BuildRequires: openal-soft-devel
BuildRequires: SDL2-devel
BuildRequires: libepoxy-devel
BuildRequires: desktop-file-utils
Requires: hicolor-icon-theme
Provides: bundled(dejavu-fonts) = 0
Provides: bundled(google-noto-fonts) = 0

%description
Cross-platform port of Arx Fatalis, a first-person role-playing game

Arx Libertatis is based on the publicly released Arx Fatalis source code.

%package devel
Summary: Header files and libraries for Arx Libertatis development
Requires: %{name}%{_isa} = %{version}-%{release}

%description devel
The arx-libertatis-devel package contains header files asnd libraries needed
to develop programs that use Arx Libertatis.

%prep
%autosetup -p1

%build
%cmake -G Ninja
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/arx-libertatis.desktop

%files
%doc AUTHORS CHANGELOG CONTRIBUTING.md README.md
%license COPYING LICENSE LICENSE.DejaVu
%{_bindir}/arx
%{_bindir}/arx-install-data
%{_bindir}/arxsavetool
%{_bindir}/arxunpak
%{_libdir}/libArxIO.so.*
%{_libexecdir}/arxtool
%{_datadir}/applications/arx-libertatis.desktop
%{_datadir}/games/arx/
%{_datadir}/icons/hicolor/*/apps/arx-libertatis.png
%{_mandir}/man1/arx-install-data.1.gz
%{_mandir}/man1/arxsavetool.1.gz
%{_mandir}/man1/arxunpak.1.gz
%{_mandir}/man6/arx.6.gz

%files devel
%{_libdir}/libArxIO.so
%{_includedir}/ArxIO.h
%dir %{_datadir}/blender
%dir %{_datadir}/blender/scripts
%dir %{_datadir}/blender/scripts/addons
%{_datadir}/blender/scripts/addons/arx

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Aug 13 2022 Jonathan Schleifer <js@nil.im> - 1.2.1-1
- Initial package
