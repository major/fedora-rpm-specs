Name:           photoqt
Version:        4.3
Release:        %autorelease
Summary:        A fast Qt image viewer

# GPL-2.0-or-later: main program
# BSD-3-Clause: cplusplus/scripts/simplecrypt.*
License:        GPL-2.0-or-later AND BSD-3-Clause
URL:            http://photoqt.org/
Source:         https://photoqt.org/downloads/source/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  freeimage-plus-devel
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(Magick++)
BuildRequires:  pkgconfig(IL)
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(exiv2)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  cmake(phonon4qt6)
BuildRequires:  pkgconfig(poppler-qt6)
BuildRequires:  cmake(pugixml)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(vips)
BuildRequires:  python3-chromecast
BuildRequires:  python3-devel
BuildRequires:  zxing-cpp-devel

Requires:       qt6-qtdeclarative
Requires:       qt6-qtmultimedia
Requires:       qt6-qtcharts
Requires:       python3-chromecast

Recommends:     xcftools
Recommends:     kf6-kimageformats

%description
PhotoQt is a fast and highly configurable image viewer with a simple and
nice interface.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%cmake -DVIDEO_MPV=OFF\
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
