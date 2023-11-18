Name:           photoqt
Version:        3.4
Release:        %autorelease
Summary:        A fast Qt image viewer

# GPL-2.0-or-later: main program
# BSD-3-Clause: cplusplus/scripts/simplecrypt.*
License:        GPL-2.0-or-later AND BSD-3-Clause
URL:            http://photoqt.org/
Source:         http://photoqt.org/pkgs/%{name}-%{version}.tar.gz
# Fix build with exiv2-0.28.0
Patch:          23e03360adefebadbccfb4ac4f1628caeea216f.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  freeimage-plus-devel
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(GraphicsMagick++)
BuildRequires:  pkgconfig(IL)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(phonon4qt5)
BuildRequires:  pkgconfig(poppler-qt5)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-chromecast
BuildRequires:  python3-devel

Requires:       qt5-qtquickcontrols
Requires:       qt5-qtquickcontrols2
Requires:       qt5-qtgraphicaleffects
Requires:       qt5-qtmultimedia
Requires:       qt5-qtcharts
Requires:       python3-chromecast

Recommends:     xcftools
Recommends:     kf5-kimageformats

%description
PhotoQt is a fast and highly configurable image viewer with a simple and
nice interface.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%cmake -DVIDEO_MPV=OFF\
       -DGRAPHICSMAGICK=ON\
       -DIMAGEMAGICK=OFF
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.%{name}.PhotoQt.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.%{name}.PhotoQt.metainfo.xml

%files
%doc CHANGELOG README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.%{name}.PhotoQt.desktop
%{_datadir}/icons/hicolor/*/apps/org.%{name}.PhotoQt.png
%{_datadir}/metainfo/org.%{name}.PhotoQt.metainfo.xml

%changelog
%autochangelog
