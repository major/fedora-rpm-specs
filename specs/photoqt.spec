Name:           photoqt
Version:        4.8.1
Release:        %autorelease
Summary:        A fast Qt image viewer

# GPL-2.0-or-later: main program
# BSD-3-Clause: cplusplus/scripts/simplecrypt.*
License:        GPL-2.0-or-later AND BSD-3-Clause
URL:            http://photoqt.org/
Source:         https://photoqt.org/downloads/source/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(exiv2)
BuildRequires:  cmake(phonon4qt6)
BuildRequires:  cmake(pugixml)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  freeimage-plus-devel
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(IL)
BuildRequires:  pkgconfig(Magick++)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(poppler-qt6)
BuildRequires:  pkgconfig(vips)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-chromecast
BuildRequires:  python3-devel
BuildRequires:  zxing-cpp-devel
BuildRequires: qt6-qtbase-private-devel

Requires:       python3-chromecast
Requires:       qt6-qtcharts
Requires:       qt6-qtdeclarative
Requires:       qt6-qtmultimedia

Recommends:     kf6-kimageformats
Recommends:     xcftools

%description
PhotoQt is a fast and highly configurable image viewer with a simple and
nice interface.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%cmake -DVIDEO_MPV=OFF
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
