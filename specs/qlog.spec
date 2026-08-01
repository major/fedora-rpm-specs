Name:           qlog
Version:        0.51.1
Release:        %autorelease
Summary:        Qt Logging program for ham-radio operators

# QLog is generally GPL 3+, with the following exceptions:
# core/csv.hpp (MIT)
# core/zonedetect.c (BSD 3 clause)
# core/zonedetect.h (BSD 3 clause)
# devtools/timezones/builder/builder.cpp (BSD 3 clause)
# devtools/timezones/timezone_DATA_LICENSE (ODbL)
License:        GPL-3.0-or-later AND BSD-3-Clause AND MIT AND ODbL-1.0
Url:            https://github.com/foldynl/QLog
ExclusiveArch:  %{qt6_qtwebengine_arches}
Source0:        https://github.com/foldynl/QLog/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Source1:        LICENSE.BSD-3-Clause
Source2:        LICENSE.MIT

BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  hamlib-devel
BuildRequires:  libappstream-glib
BuildRequires:  openssl-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtcharts-devel
BuildRequires:  qt6-qtserialport-devel
BuildRequires:  qt6-qtwebchannel-devel
BuildRequires:  qt6-qtwebengine-devel
BuildRequires:  qt6-qtwebsockets-devel
BuildRequires:  qtkeychain-qt6-devel
BuildRequires:  sqlite-devel
BuildRequires:  zlib-ng-compat-devel
Requires:       hicolor-icon-theme

%description
QLog is an Amateur Radio logging application for Linux, Windows and Mac OS. It
is based on the Qt framework and uses SQLite as database backend.

%prep
%autosetup -n QLog-%{version}
cp -p %{SOURCE1} %{SOURCE2} .

%build
export LC_ALL=C.UTF-8
%{qmake_qt6} PREFIX=%{_prefix} -r %{_qt6_qmake_flags} QMAKE_CFLAGS+="-fPIC -fPIE" QMAKE_CXXFLAGS+="-fPIC -fPIE" QMAKE_LFLAGS="%{build_ldflags} -pie -Wl,--as-needed"
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/io.github.foldynl.QLog.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license LICENSE
%license LICENSE.BSD-3-Clause
%license LICENSE.MIT
%license devtools/timezones/timezone_DATA_LICENSE
%doc README.md Changelog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_metainfodir}/io.github.foldynl.QLog.metainfo.xml
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
