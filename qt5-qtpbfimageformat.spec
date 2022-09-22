%global project_name QtPBFImagePlugin

%global __provides_exclude_from ^%{_qt5_plugindir}/.*\\.so$

Name:           qt5-qtpbfimageformat
Version:        2.3
Release:        8%{?dist}
Summary:        Qt image plugin for displaying Mapbox vector tiles

License:        GPLv3
URL:            https://github.com/tumic0/QtPBFImagePlugin/

Source0:        https://github.com/tumic0/%{project_name}/archive/%{version}/%{project_name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel
BuildRequires:  protobuf-lite-devel


%description
QtPBFImagePlugin is a Qt image plugin that enables applications capable
of displaying raster MBTiles maps or raster XYZ online maps to also display
PBF(MVT) vector tiles without (almost, see usage) any application modifications.

Standard Mapbox GL Styles are used for styling the maps. Most relevant style
features used by Maputnik are supported. The style is loaded from the
$AppDataLocation/style/style.json file on plugin load. If the style uses
a sprite, the sprite JSON file must be named sprite.json and the sprite image
sprite.png and both files must be placed in the same directory as the style
itself. A default fallback style (OSM-Liberty) for OpenMapTiles is part
of the plugin.

"Plain" PBF files as well as gzip compressed files (as used in MBTiles)
are supported by the plugin.


%prep
%autosetup -n %{project_name}-%{version}


%build
%{qmake_qt5} pbfplugin.pro
%make_build


%install
make install INSTALL_ROOT=%{buildroot}


%files
%license LICENSE
%doc README.md
%{_qt5_plugindir}/imageformats/libpbf.so


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 06 2021 Adrian Reber <adrian@lisas.de> - 2.3-6
- Rebuilt for protobuf 3.19.0

* Mon Oct 25 2021 Adrian Reber <adrian@lisas.de> - 2.3-5
- Rebuilt for protobuf 3.18.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 14:42:41 CET 2021 Adrian Reber <adrian@lisas.de> - 2.3-2
- Rebuilt for protobuf 3.14

* Tue Jan 05 2021 Nikola Forró <nforro@redhat.com> - 2.3-1
- New upstream release 2.3
  resolves: #1911525

* Thu Sep 24 2020 Adrian Reber <adrian@lisas.de> - 2.2-5
- Rebuilt for protobuf 3.13

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 2.2-2
- Rebuilt for protobuf 3.12

* Thu Apr 16 2020 Nikola Forró <nforro@redhat.com> - 2.2-1
- New upstream release 2.2
  resolves: #1824377

* Tue Jan 28 2020 Nikola Forró <nforro@redhat.com> - 2.1-1
- New upstream release 2.1
  resolves: #1795098

* Tue Oct 08 2019 Nikola Forró <nforro@redhat.com> - 2.0-1
- New upstream release 2.0
  resolves: #1758806

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 2019 Nikola Forró <nforro@redhat.com> - 1.4-1
- New upstream release 1.4

* Fri Mar 15 2019 Rex Dieter <rdieter@fedoraproject.org> 1.3-3
- rebuild

* Fri Mar 15 2019 Rex Dieter <rdieter@fedoraproject.org> 1.3-2
- drop versioned Qt5 runtime dependency

* Tue Mar 12 2019 Nikola Forró <nforro@redhat.com> - 1.3-1
- New upstream release 1.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Nikola Forró <nforro@redhat.com> - 1.2-3
- Rebuild against updated qt5-qtbase

* Tue Jan 08 2019 Nikola Forró <nforro@redhat.com> - 1.2-2
- Improve package description
- Use %%autosetup and %%make_build macros
- Explicitly require specific Qt 5 version

* Fri Jan 04 2019 Nikola Forró <nforro@redhat.com> - 1.2-1
- Initial package
