%global kf5_min_version 5.96.0

Name:           kalendar
%global uuid    org.kde.%{name}
%global suuid   %{uuid}ac
Version:        22.12.1
Release:        1%{?dist}
Summary:        A calendar application using Akonadi to sync with external services
License:        GPLv3+
URL:            https://invent.kde.org/pim/%{name}
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
Source1:        %{name}.rpmlintrc

%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

# Upstream patches


BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules >= %{kf5_min_version}
BuildRequires:  kf5-rpm-macros      >= %{kf5_min_version}

BuildRequires:  cmake(QGpgme)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Location)

BuildRequires:  cmake(KF5CalendarCore)     >= %{kf5_min_version}
BuildRequires:  cmake(KF5ConfigWidgets)    >= %{kf5_min_version}
BuildRequires:  cmake(KF5Contacts)         >= %{kf5_min_version}
BuildRequires:  cmake(KF5CoreAddons)       >= %{kf5_min_version}
BuildRequires:  cmake(KF5DBusAddons)       >= %{kf5_min_version}
BuildRequires:  cmake(KF5I18n)             >= %{kf5_min_version}
BuildRequires:  cmake(KF5ItemModels)       >= %{kf5_min_version}
BuildRequires:  cmake(KF5Kirigami2)        >= %{kf5_min_version}
BuildRequires:  cmake(KF5Libkdepim)
BuildRequires:  cmake(KF5MailCommon)
BuildRequires:  cmake(KF5People)           >= %{kf5_min_version}
BuildRequires:  cmake(KF5PimCommonAkonadi)
BuildRequires:  cmake(KF5Service)          >= %{kf5_min_version}
BuildRequires:  cmake(KF5WindowSystem)     >= %{kf5_min_version}
BuildRequires:  cmake(KF5XmlGui)           >= %{kf5_min_version}

BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiContact)
BuildRequires:  cmake(KF5CalendarSupport)
BuildRequires:  cmake(KF5EventViews)
BuildRequires:  cmake(KF5GrantleeTheme)
BuildRequires:  cmake(Grantlee5)
BuildRequires:  qqc2-desktop-style


BuildRequires:  gettext-devel

Requires:       kf5-kirigami2-addons-treeview
Requires:       akonadi-calendar-tools
Requires:       kdepim-addons
Requires:       kdepim-runtime
Requires:       kf5-calendarsupport
Requires:       kf5-kirigami2
Requires:       kf5-kirigami2-addons
Requires:       hicolor-icon-theme

%description
Kalendar is a Kirigami-based calendar application that uses Akonadi. It lets
you add, edit and delete events from local and remote accounts of your choice,
while keeping changes syncronised across your Plasma desktop or phone.


%prep
%autosetup -p1


%build
%cmake_kf5
%cmake_build


%install
%cmake_install
%find_lang %{name}
%find_lang plasma_applet_org.kde.kalendar.contact


%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/%{uuid}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/%{uuid}.appdata.xml


%files -f %{name}.lang -f plasma_applet_org.kde.kalendar.contact.lang
%license LICENSES/*.txt
%doc README.md
%{_kf5_bindir}/%{name}
%{_kf5_datadir}/applications/%{uuid}.desktop
%{_kf5_metainfodir}/%{uuid}.appdata.xml
%{_kf5_metainfodir}/%{uuid}.contact.appdata.xml
%{_kf5_datadir}/icons/hicolor/scalable/apps/%{uuid}.svg
%{_kf5_datadir}/qlogging-categories5/%{name}.categories
%{_kf5_datadir}/qlogging-categories5/%{name}.contact.categories
%{_kf5_datadir}/qlogging-categories5/akonadi.quick.categories
%{_qt5_qmldir}/org/kde/akonadi
%{_qt5_qmldir}/org/kde/kalendar
%dir %{_kf5_datadir}/plasma/plasmoids/org.kde.kalendar.contact/
%{_kf5_datadir}/plasma/plasmoids/org.kde.kalendar.contact/*


%changelog
* Sat Jan 07 2023 Marc Deop <marcdeop@fedoraproject.org> - 22.12.1-1
- 22.12.1

* Tue Jan 03 2023 Justin Zobel <justin@1707.io> - 22.12.1-1
- Update to 22.12.1

* Tue Jan 03 2023 Justin Zobel <justin@1707.io> - 22.12.1-1
- Update to 22.12.1

* Mon Dec 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.12.0-1
- 22.12.0

* Fri Nov 04 2022 Marc Deop i Argemí (Private) <marc@marcdeop.com> - 22.08.3-1
- 22.08.3

* Fri Oct 14 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.2-1
- 22.08.2

* Wed Oct 12 2022 Marc Deop marcdeop@fedoraproject.org - 22.08.1-2
- Backport upstream patch

* Thu Sep 08 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.1-1
- 22.08.1

* Fri Aug 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.0-1
- 22.08.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Than Ngo <than@redhat.com> - 22.04.3-1
- 22.04.3

* Sun May 15 2022 Justin Zobel <justin@1707.io> - 22.04.1-1
- Update to 22.04.1

* Mon Apr 25 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.04.0-1
- 22.04.0

* Mon Feb 21 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 1.0.0-2
- Kalendar html escape partial fix patch added.

* Sun Feb 13 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 1.0.0-1
- Version 1.0.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 26 2021 Justin Zobel <justin@1707.io> - 0.4.0-1
- Verison bump to 0.4.0

* Thu Dec 02 2021 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0.3.1-1
- Version bump to 0.3.1

* Tue Nov 30 2021 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0.2.1-2
- ExclusiveArch : s390 and ppc64le

* Tue Nov 30 2021 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 0.2.1-1
- initial upload and version 0.2.1
- Fixes rhbz#2020883
