%global forgeurl https://github.com/KDE/latte-dock/

Name:     latte-dock
Version:  0.10.9

%forgemeta

Release:  3%{?dist}
Summary:  Latte is a dock based on plasma frameworks
License:  GPLv2+

URL:      %{forgeurl}
Source0:  https://download.kde.org/stable/latte-dock/%{name}-%{version}.tar.xz
Source1:  %{name}.rpmlintrc

BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-devel
BuildRequires:  libSM-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  kf5-karchive-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kirigami2-devel
BuildRequires:  kf5-kactivities-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-knewstuff-devel
BuildRequires:  kf5-knotifications-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kpackage-devel
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-kwayland-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-kglobalaccel-devel
BuildRequires:  kf5-kguiaddons-devel
BuildRequires:  kf5-kcrash-devel

Recommends:     %{name}-lang

%description
Latte is a dock based on plasma frameworks that provides an elegant and
intuitive experience for your tasks and plasmoids. It animates its contents by
using parabolic zoom effect and tries to be there only when it is needed.

"Art in Coffee"

%package lang
Summary: Translation files for latte-dock
Requires: %{name} = %{version}-%{release}
%description lang
%{summary}.

%prep
%{forgesetup}
%autosetup -n %{archivename}

%build
%cmake_kf5 \
  -Wno-dev

%cmake_build

%install

F36_FILES=$RPM_BUILD_ROOT/F36.list
touch %{F36_FILES}

%if 0%{?fedora} >= 35
echo %{_kf5_datadir}/kservices5/plasma-applet-org.kde.latte.containment.desktop > %{F36_FILES}
echo %{_kf5_datadir}/kservices5/plasma-applet-org.kde.latte.plasmoid.desktop >> %{F36_FILES}
echo %{_kf5_datadir}/kservices5/plasma-shell-org.kde.latte.shell.desktop >> %{F36_FILES}
echo %{_kf5_datadir}/plasma/plasmoids/org.kde.latte.containment/ >> %{F36_FILES}
%else
echo %{_kf5_datadir}/plasma/plasmoids/org.kde.latte.containment/ > %{F36_FILES}
%endif

%cmake_install
%find_lang %{name} --all-name

%files -f %{F36_FILES}
%{_bindir}/latte-dock
%{_datadir}/metainfo/org.kde.latte-dock.appdata.xml
%{_datadir}/metainfo/org.kde.latte.plasmoid.appdata.xml
%{_datadir}/metainfo/org.kde.latte.shell.appdata.xml
%{_kf5_datadir}/applications/org.kde.latte-dock.desktop
%{_kf5_datadir}/dbus-1/interfaces/org.kde.LatteDock.xml
%{_kf5_datadir}/icons/breeze/*/*/*
%{_kf5_datadir}/icons/hicolor/*/*/*
%{_kf5_datadir}/knotifications5/lattedock.notifyrc
%{_kf5_datadir}/kservices5/plasma-containmentactions-lattecontextmenu.desktop
%{_kf5_datadir}/kservicetypes5/latte-indicator.desktop
%{_kf5_datadir}/plasma/plasmoids/org.kde.latte.plasmoid/
%{_kf5_datadir}/plasma/shells/org.kde.latte.shell/
%{_kf5_datadir}/latte
%{_kf5_datadir}/knsrcfiles/latte-indicators.knsrc
%{_kf5_datadir}/knsrcfiles/latte-layouts.knsrc
%{_kf5_qmldir}/org/kde/latte
%{_qt5_plugindir}/plasma_containmentactions_lattecontextmenu.so
%{_qt5_plugindir}/kpackage/packagestructure/latte_packagestructure_indicator.so

%files lang -f %{name}.lang

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 02 2022 Marc Deop <marcdeop@fedoraproject.org> - 0.10.9-1
- 0.10.9

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jan 25 2022 Gerald Cox <gbcox@member.fsf.org> - 0.10.8-1
- Upstream release rhbz#204817

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Gerald Cox <gbcox@member.fsf.org> - 0.10.7-2
- Upstream release rhbz#2039075
- Adjust files check for recent changes to F35

* Mon Jan 10 2022 Gerald Cox <gbcox@member.fsf.org> - 0.10.7-1
- Upstream release rhbz#2039075
- %%build: -Wno-dev (silence dev-only cmake warnings)

* Sat Dec 18 2021 Gerald Cox <gbcox@member.fsf.org> - 0.10.6-1
- Upstream release rhbz#2033869

* Thu Dec 16 2021 Gerald Cox <gbcox@member.fsf.org> - 0.10.5-1
- Upstream release rhbz#2033383

* Wed Nov 17 2021 Gerald Cox <gbcox@member.fsf.org> - 0.10.4-1
- Upstream release rhbz#2024392

* Mon Oct 25 2021 Gerald Cox <gbcox@member.fsf.org> - 0.10.3-1
- Upstream release rhbz#2003391
- Previous ticket wasn't closed, hopefully this will correct automation
- with anitya, instead of opening new ticket


* Sat Oct 23 2021 Marc Deop marcdeop@fedoraproject.org - 0.10.2-3
- Use official download to include translations
- Add translations
- Add -lang package

* Sun Sep 12 2021 Marc Deop marcdeop@fedoraproject.org - 0.10.2-2
- Fix changelog

* Sun Sep 12 2021 Marc Deop marcdeop@fedoraproject.org - 0.10.2-1
- Release 0.10.2
- Upstream release rhbz#2003391
- Remove unneeded global commit

* Sat Aug 28 2021 Gerald Cox <gbcox@fedoraproject.org> - 0.10.1-2.20210828git6c17279
- Upstream release rhbz#1991021

* Sat Aug 28 2021 Gerald Cox <gbcox@fedoraproject.org> - 0.10.1-1
- Upstream release rhbz#1991021

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Marc Deop <marcdoep@fedoraproject.org> - 0.9.12-1
- Release 0.9.12

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 18 10:01:14 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.9.11-4
- Make compatible with out of source cmake build

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Marc Deop marc@marcdeop.com - 0.9.11-1
- Upgrade to version 0.9.11
- Update URL and Source links

* Fri Mar 27 2020 Marc Deop marc@marcdeop.com - 0.9.10-1
- Upgrade to version 0.9.10

* Tue Mar 03 2020 Marc Deop marc@marcdeop.com - 0.9.9-1
- Upgrade to version 0.9.9

* Wed Jan 29 2020 Marc Deop marc@marcdeop.com - 0.9.8.1-1
- Upgrade to version 0.9.8.1
- Drop libksysguard-devel dependency

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 05 2019 Marc Deop marc@marcdeop.com - 0.9.1-2
- Fix BuildRequires

* Mon Aug 05 2019 Marc Deop marc@marcdeop.com - 0.9.1-1
- Upgrade to version 0.9.1
- Remove sed workaround on org.kde.latte-dock.desktop file
- Sort %%files alphabetically

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 29 2019 Marc Deop marc@marcdeop.com - 0.8.7-1
- Upgrade to version 0.8.7

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 Marc Deop marc@marcdeop.com - 0.8.3-1
- Upgrade to version 0.8.3

* Sun Oct 28 2018 Marc Deop marc@marcdeop.com - 0.8.2-1
- Upgrade to version 0.8.2
- Small enhancements to spec file

* Wed Oct 17 2018 Marc Deop marc@marcdeop.com - 0.8.1-1
- Upgrade to version 0.8.1
- Add BuildRequires kf5-knewstuff-devel
- Remove nameInCapitals
- Change URL and Source0 to point to github mirror

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Marc Deop <marc@marcdeop.com> - 0.7.3-1
- Upgrade to version 0.7.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.2-2
- Remove obsolete scriptlets

* Mon Nov 13 2017 Marc Deop <marc@marcdeop.com> - 0.7.2-1
- Upgrade to version 0.7.2

* Mon Oct 16 2017 Marc Deop <marc@marcdeop.com> - 0.7.1-1
- Upgrade to version 0.7.1

* Sat Aug 12 2017 Marc Deop <marc@marcdeop.com> - 0.7.0-1
- Upgrade to version 0.7.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Marc Deop <marc@marcdeop.com> - 0.6.2-3
- Fix spelling on %%description
- Escape macros on changelog
- Make description lines shorter
- Remove size 0 files

* Thu May 25 2017 Marc Deop <marc@marcdeop.com> - 0.6.2-2
- Follow Fedora's naming guidelines
- Remove unneeded Requires
- Drop deprecated stuff
- Do not use %%{make_install}
- Be more specific in %%files
- Add missing popd

* Wed May 10 2017 Marc Deop <marc@marcdeop.com> - 0.6.2-1
- Upgrade to version 0.6.2

* Mon May 08 2017 Marc Deop <marc@marcdeop.com> - 0.6.1-1
- Upgrade to version 0.6.1

* Fri Apr 7 2017 Marc Deop <marc@marcdeop.com> - 0.6.0-1
- Initial package.

