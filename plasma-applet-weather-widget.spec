%global giturl	https://github.com/kotelnik/
Name:			plasma-applet-weather-widget
Version:		1.6.10
Release:		11%{?dist}
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
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 25 2017 Gerald Cox <gbcox@fedoraproject.org> 1.6.10-1
- Upstream Release:  rhbz#1495031

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 01 2017 Gerald Cox <gbcox@fedoraproject.org> 1.6.9-1
- Upstream Release:  rhbz#1428194

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Gerald Cox <gbcox@fedoraproject.org> 1.6.8-1
- Upstream Release:  rhbz#1409528

* Wed Aug 24 2016 Gerald Cox <gbcox@fedoraproject.org> 1.6.7-4
- Remove changes made in 1.6.7-3; rhbz#1367971

* Wed Aug 24 2016 Gerald Cox <gbcox@fedoraproject.org> 1.6.7-3
- Additional BuildRequires for F25 rhbz#1367971

* Mon Aug 22 2016 Gerald Cox <gbcox@fedoraproject.org> 1.6.7-2
- Remove icon cache processing, not required rhbz#1367971

* Wed Aug 17 2016 Gerald Cox <gbcox@fedoraproject.org> 1.6.7-1
- Initial build for Fedora
