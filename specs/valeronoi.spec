%global srcname Valeronoi
%global rtld_name de.ccoors.valeronoi

Name:           valeronoi
Version:        0.4.2
Release:        %autorelease
Summary:        WiFi mapping companion app for Valetudo

# The code is all GPL3, except "3rdparty/mdns.h", which is Public Domain.
#
# While mdns is unbundled in favour of the Fedora version, it is still
# a single-header static library, so its license must be included here.
License:        GPL-3.0-or-later AND LicenseRef-Fedora-Public-Domain

URL:            https://github.com/ccoors/Valeronoi
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib

BuildRequires:  catch2-devel
BuildRequires:  CGAL-devel
BuildRequires:  mdns-devel
BuildRequires:  openssl-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel

Requires:       hicolor-icon-theme

%description
Valeronoi (Valetudo + Voronoi) is a companion for Valetudo for generating WiFi
signal strength maps. It visualizes them using a Voronoi diagram.

%prep
%autosetup -n %{srcname}-%{version} -p1

# Replace bundled libraries with system versions
ln -sf %{_includedir}/catch2/catch.hpp 3rdparty/catch.hpp
ln -sf %{_includedir}/mdns.h 3rdparty/mdns.h

%build
%cmake
%cmake_build

%install
%cmake_install

# Remove unnecessary license duplicate
rm %{buildroot}%{_datadir}/licenses/valeronoi/LICENSE/COPYING

%check
./%{_vpath_builddir}/valeronoi-tests
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{rtld_name}.desktop
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/%{rtld_name}.metainfo.xml

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{rtld_name}.desktop
%dir %{_datadir}/icons/hicolor/144x144
%dir %{_datadir}/icons/hicolor/144x144/apps
%dir %{_datadir}/icons/hicolor/180x180
%dir %{_datadir}/icons/hicolor/180x180/apps
%dir %{_datadir}/icons/hicolor/1024x1024
%dir %{_datadir}/icons/hicolor/1024x1024/apps
%{_datadir}/icons/hicolor/*/apps/%{rtld_name}.{png,svg}
%{_metainfodir}/%{rtld_name}.metainfo.xml

%changelog
%autochangelog
