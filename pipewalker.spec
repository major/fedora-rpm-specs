Name: pipewalker
Summary: Puzzle game about connecting components into a single circuit
License: GPL-3.0-or-later

Version: 0.9.5
Release: 2%{?dist}

URL: https://github.com/artemsen/pipewalker
Source0: %{URL}/archive/v%{version}/%{name}-v%{version}.tar.gz
Source11: %{name}.metainfo.xml

# Respect XDG Base Directory Specification when storing the config file.
# Backport of upstream commit:
# https://github.com/artemsen/pipewalker/commit/5dbaf4e2c9b20aba2fee21f1d840eb90db7bba1e.patch
Patch1: 0001-follow-xdg-basedir-spec.patch

# Store data files in /usr/share/pipewalker, not /usr/share/games/pipewalker.
# Reverse-patch created from upstream commit:
# https://github.com/artemsen/pipewalker/commit/3927dd99f5cd2037a746b1ff92d6a4fb7480a2d9.patch
Patch2: 0002-no-games-subdir-for-data.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: make
BuildRequires: ImageMagick

BuildRequires: libGL-devel
BuildRequires: libpng-devel
BuildRequires: SDL-devel

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
autoreconf -fiv

# Fix violation of Icon Theme Specification
sed -e 's/^Icon=pipewalker\.xpm$/Icon=pipewalker/' -i extra/%{name}.desktop


%build
%configure
%make_build

convert extra/%{name}.ico extra/%{name}.png


%install
%make_install

install -m 755 -d %{buildroot}%{_mandir}/man6
install -m 644 -p extra/%{name}.6 %{buildroot}%{_mandir}/man6/%{name}.6

install -m 755 -d %{buildroot}%{_metainfodir}
install -m 644 -p %{SOURCE11} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

install -D -m 644 extra/%{name}-0.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -D -m 644 extra/%{name}-1.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -D -m 644 extra/%{name}-2.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -D -m 644 extra/%{name}-3.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

# Not used in Fedora
rm -rf %{buildroot}%{_datadir}/menu
rm -rf %{buildroot}%{_datadir}/pixmaps


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml


%files
%doc %{_datadir}/doc/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_metainfodir}/%{name}.metainfo.xml
%{_mandir}/man6/%{name}.6*

%files data
%license COPYING
%{_datadir}/%{name}


%changelog
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
