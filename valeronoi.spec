%global srcname Valeronoi

Name:           valeronoi
Version:        0.2.1
Release:        %autorelease
Summary:        WiFi mapping companion app for Valetudo

License:        GPL-3.0-or-later
URL:            https://github.com/ccoors/Valeronoi
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
Source:         %{name}.metainfo.xml

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib

BuildRequires:  catch2-devel
BuildRequires:  CGAL-devel
BuildRequires:  openssl-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel

Requires:       hicolor-icon-theme

%description
Valeronoi (Valetudo + Voronoi) is a companion for Valetudo for generating WiFi
signal strength maps. It visualizes them using a Voronoi diagram.

%prep
%autosetup -n %{srcname}-%{version} -p1

# Replace bundled copy of catch with the system one
ln -sf %{_includedir}/catch2/catch.hpp 3rdparty/

%build
%cmake
%cmake_build

%install
%cmake_install

# Install AppData files
install -Dpm0644 -t %{buildroot}%{_metainfodir} %SOURCE1

# Remove unnecessary license duplicate
rm %{buildroot}%{_datadir}/licenses/valeronoi/LICENSE/COPYING

%check
./%{_vpath_builddir}/valeronoi-tests
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/icons/hicolor/144x144
%dir %{_datadir}/icons/hicolor/144x144/apps
%dir %{_datadir}/icons/hicolor/180x180
%dir %{_datadir}/icons/hicolor/180x180/apps
%dir %{_datadir}/icons/hicolor/1024x1024
%dir %{_datadir}/icons/hicolor/1024x1024/apps
%{_datadir}/icons/hicolor/*/apps/%{name}.{png,svg}
%{_metainfodir}/%{name}.metainfo.xml

%changelog
%autochangelog
