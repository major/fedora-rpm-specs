%global gitdate 20260105
%global commit 70d26fbca881b99a0a58c16f3802339e38c924eb
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           zegrapher
Summary:        Free and opensource math graphing software
Version:        3.1.1^%{gitdate}git%{shortcommit}
Release:        %autorelease
License:        AGPL-3.0-or-later

URL:            https://www.zegrapher.com/
Source0:        https://github.com/AdelKS/ZeGrapher/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        https://github.com/AdelKS/ZeCalculator/archive/v0.12.3/ZeCalculator-v0.12.3.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  boost-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QuickWidgets)

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

# License: AGPL-3.0-or-later
Provides:       bundled(zecalculator) = 0.12.3

%description
ZeGrapher is a plotting program for functions, sequences, parametric equations,
and tabular data. It has been designed to be as easy to use as possible.

ZeGrapher supports importing and exporting of tabular data from and to CSV files
and polynomial (regression) fits, plotting of tangents (the point can be
selected interactively). Calculation and plotting of derivatives and integrals
is also possible.

Plots can be exported in various image formats and as PDF files.

%prep
%autosetup -p1 -C
mkdir -p subprojects/zecalculator
tar xf %{SOURCE1} -C subprojects/zecalculator --strip-components=1

sed -i "s|meson.project_version()|'%{version}'|" meson.build

%build
%meson --buildtype=debugoptimized -Dtest=true
%meson_build

%install
%meson_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%meson_test

%files
%doc README.md
%license LICENSE
%{_bindir}/ZeGrapher
%{_datadir}/applications/ZeGrapher.desktop
%{_datadir}/icons/hicolor/*/apps/ZeGrapher.png
%{_datadir}/icons/hicolor/scalable/apps/ZeGrapher.svg
%{_datadir}/metainfo/ZeGrapher.metainfo.xml

%changelog
%autochangelog
