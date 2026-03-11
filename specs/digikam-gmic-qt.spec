%global commit 522d2e64f938bf32b758d5a18e1d0a712ecf7b3c
%global gitdate 20251229

Name:           digikam-gmic-qt
Version:        0^%{gitdate}git%{sub %{commit} 1 7}
Release:        %autorelease
Summary:        DigiKam G'MIC plugin

# build infrastructure is BSD-3-Clause, not installed
# gmic code is CeCILL
# digikam plugin wrapper code is GPL-2.0-or-later
License:        CECILL-2.1 AND CECILL-C AND GPL-2.0-or-later
URL:            https://github.com/cgilles/digikam-gmic-qt
Source:         %{url}/archive/%{commit}/digikam-gmic-qt-%{commit}.tar.gz

# Allow configuring installation prefix (for flatpak builds)
Patch:          qtplugindir.patch

# digikam uses QtWebEngine
ExclusiveArch:  %{qt6_qtwebengine_arches}

BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(DigikamCore)
BuildRequires:  cmake(DigikamGui)
BuildRequires:  cmake(DigikamDatabase)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(libcurl)

Provides:  bundled(CImg) = 3.6.0
Provides:  bundled(gmic) = 3.6.0

%description
This provide the port of G'MIC-Qt plugin as a digiKam/Showfoto Image Editor tool.


%prep
%autosetup -n %{name}-%{commit} -p1


%build
%cmake \
  -DGMIC_QT_HOST=digikam \
  -DBUILD_WITH_QT6=ON \
  -DQT_PLUGINS_DIR=%{_qt6_plugindir} \
  -DENABLE_ASAN=OFF \
  -DENABLE_SYSTEM_GMIC=OFF \
  -DENABLE_FFTW3=ON \
  -DENABLE_CURL=ON
%cmake_build


%install
%cmake_install


%files
%license LICENSES/GPL-2.0-or-later.txt gmicqt/COPYING
%doc README.md
%{_qt6_plugindir}/digikam/bqm/Bqm_Gmic_Plugin.so
%{_qt6_plugindir}/digikam/editor/Editor_GmicQt_Plugin.so
%{_qt6_plugindir}/digikam/generic/Generic_GmicQt_Plugin.so


%changelog
%autochangelog
