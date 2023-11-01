Name: pipewalker
Summary: Puzzle game about connecting components into a single circuit
License: GPL-3.0-or-later

Version: 0.9.4
Release: 8%{?dist}

URL: http://pipewalker.sourceforge.net
Source0: https://downloads.sourceforge.net/project/pipewalker/pipewalker/%{version}/pipewalker-%{version}.tar.gz
Source10: %{name}.man
Source11: %{name}.metainfo.xml

Patch0: %{name}--format-security.patch

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

# Fix violation of Icon Theme Specification
sed -e 's/^Icon=pipewalker\.xpm$/Icon=pipewalker/' -i extra/%{name}.desktop


%build
%configure
%make_build

convert extra/%{name}.ico extra/%{name}.png


%install
%make_install

install -m 755 -d %{buildroot}%{_mandir}/man6
install -m 644 -p %{SOURCE10} %{buildroot}%{_mandir}/man6/%{name}.6

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
