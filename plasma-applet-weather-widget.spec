%global giturl	https://github.com/kotelnik/
Name:			plasma-applet-weather-widget
Version:		1.6.10
Release:		%autorelease
Summary:		Plasma applet for displaying weather information
License:		GPLv2+
Url:			%{giturl}%{name}
Source0:		%{giturl}%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:	extra-cmake-modules, kf5-rpm-macros, kf5-plasma-devel
BuildRequires:	libappstream-glib, qt5-qtdeclarative-devel, gettext-devel
BuildRequires:	desktop-file-utils, appstream-qt-devel

%description
Plasma 5 applet for displaying weather information from yr.no server

%prep
%setup -qn %{name}-%{version}

%build
%{cmake_kf5}
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name

%check
desktop-file-validate $RPM_BUILD_ROOT%{_kf5_datadir}\
/kservices5/plasma-applet-org.kde.weatherWidget.desktop
#appstream-util validate-relax --nonet \
#$RPM_BUILD_ROOT%{_kf5_metainfodir}/org.kde.weatherWidget.appdata.xml

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_kf5_qmldir}/org/kde/private/weatherWidget/
%{_kf5_metainfodir}/org.kde.weatherWidget.appdata.xml
%{_kf5_datadir}/kservices5/plasma-applet-org.kde.weatherWidget.desktop
%{_kf5_datadir}/plasma/plasmoids/org.kde.weatherWidget/

%changelog
%autochangelog
