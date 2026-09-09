%global forgeurl https://github.com/AlizaMedicalImaging/AlizaMS

Name:    alizams
Version: 1.10.3

%forgemeta

Release: %autorelease
Summary: Aliza MS DICOM Viewer
# Mixed licensed source files:
# GPL-3.0-only is the main license;
# vectormath/sse/*, vectormath/scalar/* and GUI/qxtspanslider*.h are BSD-3-Clause;
# common/colorspace/colorspace.cpp is BSD 2-Clause License;
# common/codecutils.* are Apache-2.0
License: GPL-3.0-only AND Apache-2.0 AND BSD-3-Clause AND BSD-2-Clause
URL:     %{forgeurl}
Source0: %{forgesource}
Patch0:  alizams-find_CharLS.patch
Patch1:  alizams-find_system_openjpeg_before.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  libuuid-devel
BuildRequires:  zlib-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  vxl-devel
BuildRequires:  openjpeg-devel
BuildRequires:  CharLS-devel
BuildRequires:  cmake(LIBMINC)
BuildRequires:  cmake(ITK)
BuildRequires:  cmake(gdcm)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  bullet-devel
BuildRequires:  lcms2-devel

Requires:       hicolor-icon-theme
Provides:       bundled(vectormath)
Provides:       bundled(colorspace)

# https://github.com/AlizaMedicalImaging/AlizaMS/issues/2
ExcludeArch:      %{power64} %{ix86} s390x

%description
A 2D and 3D DICOM viewer with many tools and very fast directory
scanner and DICOMDIR support. It can consistently remove personal
information from DICOM files.

%prep
%forgeautosetup -p1

# Remove unuseful directories
rm -rf alizalcms/
rm -rf debian-10
rm -rf debian-12-qt5/
rm -rf debian-12-qt6/
rm -rf fedora-34
rm -rf package/apple
rm -rf package/art
rm -fr mdcm/Utilities/mdcmzlib/
rm -fr mdcm/Utilities/mdcmopenjpeg/
rm -fr mdcm/Utilities/mdcmcharls/
rm -fr mdcm/Utilities/mdcmuuid/
rm -fr mdcm/Utilities/pvrg/
rm -fr b/
rm -fr CG/glew/

%build
%cmake \
  -DCMAKE_BUILD_TYPE:STRING=Release \
  -DALIZA_QT_VERSION:STRING=6 \
  -DALIZA_USE_SYSTEM_BULLET:BOOL=ON \
  -DALIZA_USE_SYSTEM_LCMS2:BOOL=ON \
  -DMDCM_USE_SYSTEM_ZLIB:BOOL=ON \
  -DMDCM_USE_SYSTEM_OPENJPEG:BOOL=ON \
  -DMDCM_USE_SYSTEM_CHARLS:BOOL=ON \
  -DMDCM_USE_SYSTEM_UUID:BOOL=ON \
  -DITK_DIR=%{_libdir}/cmake/InsightToolkit \
%ifnarch x86_64
  -DALIZA_DISABLE_SIMDMATH:BOOL=ON \
%endif
%cmake_build -v

%install
%cmake_install

%check
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet \
  %{buildroot}%{_datadir}/metainfo/%{name}.metainfo.xml

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
