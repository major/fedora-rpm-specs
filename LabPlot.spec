# Features in Fedora/Free Electronic Lab

# Known Bugs fixed:
# S#2759043 Segfault in TableModel::handleAspectRemoved() - can't reproduce

%global genname labplot

Name:           LabPlot
Version:        2.10.1
Release:        %autorelease
Summary:        Data Analysis and Visualization

License:        GPL-2.0-or-later
URL:            https://labplot.kde.org/

Source0:        https://download.kde.org/stable/labplot/labplot-%{version}.tar.xz
Patch0:         labplot-fix-liborigin-cmake.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules

# Qt6 support seems to be in the future new release
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5SerialPort)

BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KF5NewStuffCore)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Purpose)
BuildRequires:  cmake(KF5SyntaxHighlighting)

BuildRequires:  poppler-qt5-devel

BuildRequires:  gsl-devel
BuildRequires:  gettext-devel
%ifarch %{qt5_qtwebengine_arches}
BuildRequires:  cantor-devel
%endif
BuildRequires:  bison
BuildRequires:  cfitsio-devel
BuildRequires:  fftw-devel
BuildRequires:  hdf5-devel
BuildRequires:  libcerf-devel
BuildRequires:  libspectre-devel
BuildRequires:  lz4-devel
BuildRequires:  netcdf-devel
BuildRequires:  readstat-devel
BuildRequires:  kuserfeedback-devel
BuildRequires:  liborigin-devel
# QXlsx is built against Qt6
#BuildRequires:  QXlsx-devel
BuildRequires:  matio-devel
BuildRequires:  libmarkdown-devel

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

ExcludeArch:  sparc64 s390 s390x

Requires:  electronics-menu

%description
LabPlot is a FREE, open source and cross-platform Data Visualization and
Analysis software accessible to everyone.

- High-quality Data Visualization and Plotting with just a few clicks
- Reliable and easy Data Analysis and Statistics, no coding required!
- Intuitive and fast Computing with Interactive Notebooks
- Effortless Data Extraction from plots and support for Live Data
- Smooth Data Import and Export to and from multiple formats
- Available for Windows, macOS, Linux and FreeBSD

%prep
%autosetup -p1 -n %{genname}-%{version}

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release

%cmake_build

%install
%cmake_install

%find_lang %{genname}2 --all-name --with-html


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.xml


%files -f %{genname}2.lang
%license LICENSES/*
%doc README.md ChangeLog AUTHORS INSTALL
%{_datadir}/icons/hicolor/*/apps/%{genname}*
%{_bindir}/%{genname}2
%{_datadir}/kxmlgui5/%{genname}2/
%{_datadir}/mime/packages/%{genname}2.xml
%{_datadir}/%{genname}2/
%{_datadir}/applications/org.kde.%{genname}2.desktop
%{_datadir}/metainfo/org.kde.%{genname}2.appdata.xml
%{_mandir}/man1/labplot2.1.gz
%{_mandir}/*/man1/labplot2.1.gz

%changelog
%autochangelog
