%global qt_module qtcanvaspainter

#global unstable 0
%if 0%{?unstable}
%global prerelease rc
%endif

%global examples 1

Summary: Qt6 - Canvas Painter component
Name:    qt6-%{qt_module}
Version: 6.11.2
Release: 1%{?dist}

License: BSD-3-Clause AND GFDL-1.3-no-invariants-only AND GPL-3.0-only AND (GPL-3.0-only WITH Qt-GPL-exception-1.0) AND OFL-1.1 AND Zlib
Url:     http://www.qt.io
%global  majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
Source0: https://download.qt.io/development_releases/qt/%{majmin}/%{qt_version}/submodules/%{qt_module}-everywhere-src-%{qt_version}-%{prerelease}.tar.xz
%else
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
%endif

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: qt6-rpm-macros
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel >= %{version}
BuildRequires: qt6-qtshadertools-devel >= %{version}

%description
Qt CanvasPainter module provides a hardware-accelerated 2D vector graphics
rendering engine built on top of Qt's RHI (Rendering Hardware Interface).
It supports rendering paths, shapes, gradients, images, and text using
GPU-accelerated pipelines.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
%description devel
%{summary}.

%if 0%{?examples}
%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.
%endif

%prep
%autosetup -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}} -p1


%build
%cmake_qt6 \
  -DQT_BUILD_EXAMPLES:BOOL=%{?examples:ON}%{!?examples:OFF} \
  -DQT_INSTALL_EXAMPLES_SOURCES=%{?examples:ON}%{!?examples:OFF}

%cmake_build


%install
%cmake_install


%files
%license LICENSES/*
%{_qt6_archdatadir}/sbom/%{qt_module}-%{qt_version}.spdx
%{_qt6_bindir}/qcshadergen
%{_qt6_libdir}/libQt6CanvasPainter.so.6{,.*}

%files devel
%{_qt6_headerdir}/QtCanvasPainter/
%{_qt6_libdir}/libQt6CanvasPainter.so
%{_qt6_libdir}/libQt6CanvasPainter.prl
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtCanvasPainterTestsConfig.cmake
%dir %{_qt6_libdir}/cmake/Qt6CanvasPainter/
%{_qt6_libdir}/cmake/Qt6CanvasPainter/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6CanvasPainterPrivate/
%{_qt6_libdir}/cmake/Qt6CanvasPainterPrivate/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6CanvasPainterTools/
%{_qt6_libdir}/cmake/Qt6CanvasPainterTools/*.cmake
%{_qt6_archdatadir}/mkspecs/modules/*
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/pkgconfig/*.pc

%if 0%{?examples}
%files examples
%{_qt6_examplesdir}/
%endif

%changelog
* Tue Sep 15 2026 Jan Grulich <jgrulich@redhat.com> - 6.11.2-1
- 6.11.2
