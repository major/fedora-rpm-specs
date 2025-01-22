Name: pipewalker
Summary: Puzzle game about connecting components into a single circuit
License: MIT

Version: 1.1
Release: 4%{?dist}

URL: https://github.com/artemsen/pipewalker
Source0: %{URL}/archive/v%{version}/%{name}-v%{version}.tar.gz
Source11: %{name}.metainfo.xml

# Store data files in /usr/share/pipewalker, not /usr/share/games/pipewalker.
# Reverse-patch created from upstream commit:
# https://github.com/artemsen/pipewalker/commit/3927dd99f5cd2037a746b1ff92d6a4fb7480a2d9.patch
Patch2: 0002-no-games-subdir-for-data.patch

# Disable a debug feature where the game generates the levels already solved.
Patch3: 0003-fix-levels-being-already-solved.patch

# Fix missing includes.
# Submitted upstream: https://github.com/artemsen/pipewalker/pull/12
Patch4: 0004-missing-includes.patch

BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: meson

BuildRequires: SDL2-devel
BuildRequires: SDL2_image-devel

Requires: hicolor-icon-theme

Requires: %{name}-data = %{version}-%{release}

%description
PipeWalker is a puzzle game in which you need to combine the components
into a single circuit: connect all computers to a network server,
bring water to the taps, etc.


%package data
Summary: Data files for PipeWalker
BuildArch: noarch

%description data
This package provides data files (themes and sounds effects)
required to play PipeWalker.


%prep
%autosetup -p1

# Fix violation of Icon Theme Specification
sed -e 's/^Icon=pipewalker\.xpm$/Icon=pipewalker/' -i extra/%{name}.desktop


%build
%meson -Dversion=%{version}
cat %{_vpath_builddir}/buildcfg.h

%meson_build


%install
%meson_install

install -m 755 -d %{buildroot}%{_metainfodir}
install -m 644 -p %{SOURCE11} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml


%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_metainfodir}/%{name}.metainfo.xml
%{_mandir}/man6/%{name}.6*

%files data
%license LICENSE
%{_datadir}/%{name}


%changelog
* Mon Jan 20 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.1-4
- Add a patch to fix FTBFS due to missing includes

* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 02 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.1-1
- Update to v1.1
- Drop Patch10 and Patch20 (32-bit specific issues - fixed upstream)

* Thu Feb 08 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.0-3
- Fix levels always being already solved

* Wed Feb 07 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.0-2
- Add two patches from Debian to fix build failure on i686

* Tue Feb 06 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.0-1
- Update to v1.0
- Drop Patch1 (comply with XDG directory spec - backport from this release)
- Update License tag (relicensed from GPL-3.0-or-later to MIT)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 28 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.5-1
- Update to v0.9.5
- Drop Patch0 (format string security - fixed upstream)
- Drop custom man page in favour of one provided by upstream

* Mon Oct 30 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.4-8
- Convert license tag to SPDX
- Move themes and sound effects to a -data subpackage
- Add a man page

* Mon Oct 30 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 0.9.4-7
- Install icons to hicolor theme

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 24 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.4-2
- Add a metainfo file
- Fix error in desktop file

* Fri Nov 19 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.4-1
- Initial packaging
