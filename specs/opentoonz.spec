%undefine __cmake_in_source_build
%define _vpath_srcdir toonz/sources

Name:           opentoonz
Version:        1.8.0
Release:        %autorelease
Summary:        2D animation software

License:        BSD-3-Clause
URL:            https://opentoonz.github.io/
Source0:        https://github.com/opentoonz/opentoonz/archive/refs/tags/v%{version}.tar.gz

Patch:          0001-lzo-fix.patch
# https://github.com/opentoonz/opentoonz/issues/4199
Patch:          0002-tiff-fix.patch
Patch:          0003-exr-fix.patch
# https://github.com/opentoonz/opentoonz/pull/4239
Patch:          0004-gethostbyname.patch
Patch:          0005-install-path-fix.patch
Patch:          0006-kissfft-fix.patch       
Patch:          0007-toonzrle-rm.patch
Patch:          0008-tzp-tiffiop-fix.patch
Patch:          0009-appdata.patch

BuildRequires:  flexiblas-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  freeglut-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  kiss-fft-devel
BuildRequires:  libappstream-glib
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libmypaint-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  lz4-devel
BuildRequires:  lzo-devel
BuildRequires:  opencv-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qtserialport-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  SuperLU-devel
BuildRequires:  tinyexr-devel
BuildRequires:  turbojpeg-devel
BuildRequires:  xz-devel

BuildRequires:  qt5-qttools-static

Requires:       opencv
Requires:       hicolor-icon-theme
Requires:       %{name}-data = %{version}-%{release}

%description
OpenToonz is a 2D animation software published by DWANGO. It is based on 
Toonz Studio Ghibli Version, originally developed in Italy by 
Digital Video, Inc., and customized by Studio Ghibli over many years of 
production.
This version was packaged for Fedora using the latest stable libraries
available in the distribution, in exchange some features were disabled.


%package data
Summary: OpenToonz data files
BuildArch: noarch

%description data
Data files for the OpenToonz application.


%package doc
Summary: OpenToonz doc files
BuildArch: noarch

%description doc
Documentation about the OpenToonz application.


%prep
%autosetup -p1

# Remove all thirdparty libraries
rm -rf thirdparty
find stuff/doc/LICENSE/ -type f -not -name 'LICENSE.txt' -delete

# add flexiblas
sed -i 's/OPENBLAS_LIB NAMES/& flexiblas/' toonz/sources/CMakeLists.txt


%build
%cmake \
    -DWITH_SYSTEM_LZO:BOOL=ON \
    -DCMAKE_SKIP_RPATH:BOOL=YES \
    -DWITH_TRANSLATION:BOOL=OFF
    
%cmake_build


%install
%cmake_install
chmod 0755 ${RPM_BUILD_ROOT}%{_libdir}/%{name}/*.so
desktop-file-validate \
    ${RPM_BUILD_ROOT}%{_datadir}/applications/io.github.OpenToonz.desktop
appstream-util validate-relax --nonet \
    ${RPM_BUILD_ROOT}%{_metainfodir}/io.github.OpenToonz.appdata.xml

%files
%license LICENSE.txt
%{_bindir}/OpenToonz
%{_bindir}/opentoonz
%{_bindir}/tcleanup
%{_bindir}/tcomposer
%{_bindir}/tconverter
%{_bindir}/tfarmcontroller
%{_bindir}/tfarmserver
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/*.so
%{_datadir}/applications/io.github.OpenToonz.desktop
%{_metainfodir}/io.github.OpenToonz.appdata.xml
%{_datadir}/icons/hicolor/256x256/apps/io.github.OpenToonz.png

%files data
%license LICENSE.txt
%{_datadir}/%{name}/


%files doc
%doc doc/*.md
%doc doc/*.JPG


%changelog
%autochangelog
