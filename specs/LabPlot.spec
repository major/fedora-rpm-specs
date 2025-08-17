%global genname labplot

#global gitcommit 4e770ae2d988362dca637aef2b74610a4a1456c2
#global gitdate 20241117.082905
#global shortcommit %%(c=%%{gitcommit}; echo ${c:0:7})

# No libcerf-3 on s390x
%ifarch s390x
%bcond libcerf 0
%else
%bcond libcerf 1
%endif

Name:           LabPlot
Version:        2.12.1%{?gitdate:~%{gitdate}.%{shortcommit}}
Release:        %autorelease
Summary:        Data Analysis and Visualization
License:        GPL-2.0-or-later
URL:            https://labplot.kde.org/

# REASON: cantor
# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

Source0:        https://download.kde.org/stable/labplot/labplot-%{version}.tar.xz
#Source0:        https://invent.kde.org/education/labplot/-/archive/%%{version}/labplot-%%{version}.tar.bz2
#Source0:        https://invent.kde.org/education/labplot/-/archive/%%{gitcommit}/labplot-%%{gitcommit}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  bison
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6SerialPort)

BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6NewStuffCore)
BuildRequires:  cmake(KF6NewStuff)
# Optional
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6UserFeedback)

BuildRequires:  cmake(qtadvanceddocking-qt6)
BuildRequires:  gsl-devel
BuildRequires:  gettext-devel

BuildRequires:  cantor-devel
BuildRequires:  pkgconfig(poppler-qt6)
BuildRequires:  fftw-devel
BuildRequires:  hdf5-devel
BuildRequires:  netcdf-devel

BuildRequires:  cmake(Qt6Mqtt)
BuildRequires:  cfitsio-devel
%if %{with cerf}
BuildRequires:  libcerf-devel
%endif
BuildRequires:  libspectre-devel
BuildRequires:  libzstd-devel
BuildRequires:  zlib-devel
BuildRequires:  lz4-devel
BuildRequires:  readstat-devel

BuildRequires:  liborigin-devel
BuildRequires:  QXlsx-devel
BuildRequires:  qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

BuildRequires:  matio-devel
BuildRequires:  libmarkdown-devel
BuildRequires:  liborcus-devel
BuildRequires:  libixion-devel
BuildRequires:  boost-devel
BuildRequires:  eigen3-devel

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%if %{undefined flatpak}
Requires:       electronics-menu
%endif

%description
LabPlot is a FREE, open source and cross-platform Data Visualization and
Analysis software accessible to everyone.

- High-quality Data Visualization and Plotting with just a few clicks
- Reliable and easy Data Analysis and Statistics, no coding required!
- Intuitive and fast Computing with Interactive Notebooks
- Effortless Data Extraction from plots and support for Live Data
- Smooth Data Import and Export to and from multiple formats
- Available for Windows, macOS, Linux and FreeBSD

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(Qt6Widgets)

%description devel
This package contains the LabPlot Software Development Kit.


%prep
%autosetup -p1 -n %{genname}-%{!?gitcommit:%{version}}%{?gitcommit}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{genname} --all-name --with-html --with-man

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml

%files -f %{genname}.lang
%license LICENSES/*
%doc README.md ChangeLog AUTHORS INSTALL
%{_datadir}/icons/hicolor/*/apps/%{genname}*
%{_datadir}/icons/hicolor/*/apps/org.kde.%{genname}.*
%{_bindir}/%{genname}
%{_libdir}/liblabplot.so.*
%{_datadir}/mime/packages/%{genname}.xml
%{_datadir}/%{genname}/
%{_datadir}/applications/org.kde.%{genname}.desktop
%{_metainfodir}/org.kde.%{genname}.appdata.xml
%{_mandir}/man1/%{genname}.1*

%files devel
%{_includedir}/labplot/
%{_libdir}/cmake/%{genname}/
%{_libdir}/liblabplot.so


%changelog
%autochangelog
