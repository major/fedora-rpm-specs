Name: merkuro
Version: 24.01.90
Release: 3%{?dist}
Summary: A calendar application using Akonadi to sync with external services (Nextcloud, GMail, ...)

License: GPL-3.0-or-later
URL:     https://invent.kde.org/pim/%{name}

Source:  https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake
BuildRequires:  cmake(QGpgmeQt6)
BuildRequires:  cmake(Plasma)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickTest)

BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6QQC2DesktopStyle)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)

BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  gpgme-devel

BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6AkonadiCalendar)
BuildRequires:  cmake(KPim6AkonadiContactCore)
BuildRequires:  cmake(KPim6AkonadiMime)
BuildRequires:  cmake(KPim6CalendarUtils)
BuildRequires:  cmake(KPim6IdentityManagementQuick)
BuildRequires:  cmake(KPim6MailCommon)
BuildRequires:  cmake(KPim6MailTransport)
BuildRequires:  cmake(KPim6MimeTreeParserCore)
BuildRequires:  cmake(KPim6Mbox)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KPim6Libkdepim)

BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib



# kalendar has been renamed to merkuro
Obsoletes:	kalendar < 23.08
Provides:	kalendar = %{version}-%{release}
Provides:	kalendar%{?_isa} = %{version}-%{release}

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
# Package doesn't build on arches that qtwebengine is not built on.
ExclusiveArch:	%{qt6_qtwebengine_arches}


%description
Merkuro is a application suite designed to make handling your emails, \
calendars, contacts, and tasks simple. Merkuro handles local and \
remote accounts of your choice, keeping changes synchronised across \
your Plasma desktop or phone.


%prep
%autosetup -n %{name}-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-kde --with-man --all-name

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.%{name}.contact.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.%{name}.calendar.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.%{name}.mail.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.contact.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.merkuro.contact.appdata.xml ||:
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.calendar.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.mail.metainfo.xml

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_bindir}/merkuro-calendar
%{_bindir}/merkuro-contact
%{_bindir}/merkuro-mail
%{_kf6_qmldir}/org/kde/akonadi/*
%{_kf6_qmldir}/org/kde/merkuro/*
%{_datadir}/plasma/plasmoids/org.kde.merkuro.contact/
%{_datadir}/applications/org.kde.merkuro.calendar.desktop
%{_datadir}/applications/org.kde.merkuro.contact.desktop
%{_datadir}/applications/org.kde.merkuro.mail.desktop
%{_datadir}/icons/hicolor/128x128/apps/org.kde.merkuro*.png
%{_datadir}/icons/hicolor/256x256/apps/org.kde.merkuro*.png
%{_datadir}/icons/hicolor/48x48/apps/org.kde.merkuro*.png
%{_kf6_metainfodir}/org.kde.merkuro.*.metainfo.xml
%{_kf6_metainfodir}/org.kde.merkuro.contact.appdata.xml
%{_datadir}/qlogging-categories6/akonadi.quick.categories
%{_datadir}/qlogging-categories6/merkuro.categories
%{_datadir}/qlogging-categories6/merkuro.contact.categories

%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Sun Jan 07 2024 Justin Zobel <justin.zobel@gmail.com> - 24.01.85-2
- Add patch to fix Adding a new task

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Thu Dec 14 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Sat Sep 16 2023 Steve Cossette <farchord@gmail.com> - 23.08.1-1
- Initial Release
