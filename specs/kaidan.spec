%bcond check 0

Name:           kaidan
Version:        0.12.0
Release:        %autorelease
Summary:        A XMPP client based on KDE Framework
License:        GPL-3.0-or-later AND MIT AND Apache-2.0 AND CC-BY-SA-4.0 AND LGPL-2.0-or-later
URL:            https://invent.kde.org/network/kaidan
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

%if 0%{?fedora} || 0%{?epel} > 7
# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
# Package doesn't build on arches that qtwebengine is not built on.
ExclusiveArch: %{qt6_qtwebengine_arches}
%endif

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(Qt6Location)
BuildRequires:  cmake(Qt6Test)


BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6Prison)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6QQC2DesktopStyle)

BuildRequires:  cmake(QXmppQt6)
BuildRequires:  cmake(KDSingleApplication-qt6)
BuildRequires:  libicu-devel

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

# src/hsluv-c directory
# https://github.com/hsluv/hsluv-c
Provides:       bundled(hsluv-c)
# src/singleapp directory
# https://github.com/itay-grudev/SingleApplication
Provides:       bundled(SingleApplication)

# QML module dependencies
Requires:       kf6-kirigami2%{?_isa}
Requires:       kf6-kirigami2-addons%{?_isa}
Requires:       kf6-kquickcharts%{?_isa}
Requires:       qt6-qtwebchannel%{?_isa}
Requires:       qt6-qtwebengine%{?_isa}
Requires:       kquickimageeditor-qt6%{?_isa}
Requires:       hicolor-icon-theme

%description
Kaidan is a simple, user-friendly and modern chat client. It uses the open
communication protocol XMPP (Jabber). The user interface makes use of Kirigami
and QtQuick, while the back-end of Kaidan is entirely written in C++ using Qt
and the Qt-based XMPP library QXmpp.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%cmake \
    -GNinja \
    -DUSE_KNOTIFICATIONS=ON \
%if %{with check}
    -DBUILD_TESTING=ON \
%else
    -DBUILD_TESTS=OFF \
%endif

%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt

%check
%if %{with check}
%ctest -E 'PublicGroupChatTest'
%endif

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_bindir}/kaidan
%{_datadir}/applications/im.kaidan.kaidan.desktop
%{_datadir}/icons/hicolor/128x128/apps/kaidan.png
%{_datadir}/icons/hicolor/scalable/apps/kaidan.svg
%{_datadir}/kaidan/
%{_datadir}/knotifications6/kaidan.notifyrc
%{_datadir}/metainfo/im.kaidan.kaidan.appdata.xml
%{_datadir}/qlogging-categories6/kaidan.categories

%changelog
%autochangelog
