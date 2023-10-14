Name:		merkuro
Version:	23.08.2
Release:	1%{?dist}
Summary:	A calendar application using Akonadi to sync with external services (Nextcloud, GMail, ...)

License:	GPL-3.0-or-later
URL:		https://invent.kde.org/pim/%{name}

Source:		https://download.kde.org/%{stable_kf5}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:	kf5-rpm-macros
BuildRequires:	extra-cmake-modules
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5QuickTest)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5QQC2DesktopStyle)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5KirigamiAddons)
BuildRequires:	gpgme-devel
BuildRequires:	cmake(KPim5Akonadi)
BuildRequires:	cmake(KPim5AkonadiCalendar)
BuildRequires:	cmake(KPim5AkonadiContact)
BuildRequires:	cmake(KPim5AkonadiMime)
BuildRequires:	cmake(KPim5CalendarUtils)
BuildRequires:	cmake(KPim5IdentityManagement)
BuildRequires:	cmake(KPim5MailCommon)
BuildRequires:	grantlee-qt5-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib
BuildRequires:	cmake(KPim5Libkdepim)
BuildRequires:	fdupes

# QML module dependencies
Requires:	kf5-kirigami2%{?_isa}
Requires:	kf5-kirigami2-addons%{?_isa}
Requires:	kf5-kquickcharts%{?_isa}
Requires:	qt5-qtgraphicaleffects%{?_isa}
Requires:	qt5-qtquickcontrols2%{?_isa}
Requires:	qt5-qtwebchannel%{?_isa}
Requires:	qt5-qtwebengine%{?_isa}

# kalendar has been renamed to merkuro
Obsoletes:	kalendar < 23.08
Provides:	kalendar = %{version}-%{release}
Provides:	kalendar%{?_isa} = %{version}-%{release}

# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
# Package doesn't build on arches that qtwebengine is not built on.
ExclusiveArch:	%{qt5_qtwebengine_arches}


%description
Merkuro is a application suite designed to make handling your emails, \
calendars, contacts, and tasks simple. Merkuro handles local and \
remote accounts of your choice, keeping changes synchronised across \
your Plasma desktop or phone.


%prep
%autosetup -n %{name}-%{version} -p1

%build
%cmake_kf5
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-kde --with-man --all-name
%fdupes

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.%{name}.contact.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.%{name}.calendar.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.%{name}.mail.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.%{name}.contact.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.%{name}.calendar.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.%{name}.mail.metainfo.xml

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_bindir}/merkuro-calendar
%{_bindir}/merkuro-contact
%{_bindir}/merkuro-mail
%{_kf5_qmldir}/org/kde/akonadi/*
%{_kf5_qmldir}/org/kde/merkuro/*
%{_datadir}/applications/org.kde.merkuro.calendar.desktop
%{_datadir}/applications/org.kde.merkuro.contact.desktop
%{_datadir}/applications/org.kde.merkuro.mail.desktop
%{_datadir}/icons/hicolor/128x128/apps/org.kde.merkuro*.png
%{_datadir}/icons/hicolor/256x256/apps/org.kde.merkuro*.png
%{_datadir}/icons/hicolor/48x48/apps/org.kde.merkuro*.png
%{_kf5_metainfodir}/org.kde.merkuro.*.metainfo.xml
%{_datadir}/qlogging-categories5/akonadi.quick.categories
%{_datadir}/qlogging-categories5/merkuro.categories
%{_datadir}/qlogging-categories5/merkuro.contact.categories

%changelog
* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Sat Sep 16 2023 Steve Cossette <farchord@gmail.com> - 23.08.1-1
- Initial Release
