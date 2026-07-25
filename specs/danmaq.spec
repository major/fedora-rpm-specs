%global reponame danmaQ

Name:		danmaq
Version:	0.3.0
Release:	%autorelease
Summary:	A small client side Qt program to play danmaku on any screen
License:	GPL-3.0-only
URL:		https://github.com/TUNA/%{reponame}
Source0:	%{url}/archive/v%{version}/%{reponame}-v%{version}.tar.gz
ExclusiveArch:  %{qt6_qtwebengine_arches}

BuildRequires:	appstream
BuildRequires:	cmake
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	desktop-file-utils
BuildRequires:	gcc-c++

%description
DanmaQ is a small client side Qt program to play danmaku on any screen.

%prep
%autosetup -n %{reponame}-%{version}
sed -i 's|<description>\(.*\)</description>|<description><p>\1</p></description>|' src/resource/moe.tuna.danmaq.metainfo.xml

%build
%cmake -DCMAKE_SKIP_RPATH=ON -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{reponame}.desktop
appstreamcli validate --no-net %{buildroot}%{_datadir}/metainfo/moe.tuna.danmaq.metainfo.xml

%files
%license LICENSE
%doc README.md
%{_bindir}/%{reponame}
%{_datadir}/applications/%{reponame}.desktop
%{_datadir}/icons/hicolor/*/apps/%{reponame}.*
%{_datadir}/metainfo/moe.tuna.danmaq.metainfo.xml
%{_mandir}/man1/%{reponame}.1*

%changelog
%autochangelog
