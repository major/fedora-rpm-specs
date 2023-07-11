Name:           kaidan
Version:        0.9.1
Release:        %autorelease
Summary:        A XMPP client based on KDE Framework

# https://invent.kde.org/network/kaidan/-/raw/master/LICENSE
License:        GPL-3.0-or-later AND MIT AND Apache-2.0 AND CC-BY-SA-4.0
URL:            https://www.kaidan.im
Source0:        https://invent.kde.org/network/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

%if 0%{?fedora} || 0%{?epel} > 7
# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
# Package doesn't build on arches that qtwebengine is not built on.
ExclusiveArch: %{qt5_qtwebengine_arches}
%endif

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Positioning)
BuildRequires:  cmake(Qt5Location)

BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KQuickImageEditor)
BuildRequires:  cmake(KF5KirigamiAddons)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  kf5-rpm-macros
BuildRequires:  cmake(ZXing)
BuildRequires:  cmake(QXmpp)
# optional dependencies
BuildRequires:  cmake(KF5QQC2DesktopStyle)

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

# QML module dependencies
Requires:       kf5-kirigami2%{?_isa}
Requires:       kf5-kirigami2-addons%{?_isa}
Requires:       kf5-kquickcharts%{?_isa}
Requires:       qt5-qtgraphicaleffects%{?_isa}
Requires:       qt5-qtquickcontrols2%{?_isa}
Requires:       qt5-qtwebchannel%{?_isa}
Requires:       qt5-qtwebengine%{?_isa}
Requires:       hicolor-icon-theme

%description
Kaidan is a simple, user-friendly and modern chat client. It uses the open
communication protocol XMPP (Jabber). The user interface makes use of Kirigami
and QtQuick, while the back-end of Kaidan is entirely written in C++ using Qt
and the Qt-based XMPP library QXmpp.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%cmake_kf5 \
    -GNinja \
    -DUSE_KNOTIFICATIONS=ON \
    -DBUILD_TESTING=ON \
    -DBUILD_TESTS=ON \

%cmake_build

%install
%cmake_install

%find_lang %{name} --with-qt

%check
# https://koji.fedoraproject.org/koji/taskinfo?taskID=102424233
# https://kojipkgs.fedoraproject.org/work/tasks/4248/102424248/build.log
%ctest -E 'PublicGroupChatTest'

desktop-file-validate %{buildroot}%{_datadir}/applications/im.kaidan.kaidan.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/im.kaidan.kaidan.appdata.xml

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/applications/im.kaidan.kaidan.desktop
%{_metainfodir}/im.kaidan.kaidan.appdata.xml
%{_datadir}/icons/hicolor/128x128/apps/kaidan.png
%{_datadir}/icons/hicolor/scalable/apps/kaidan.svg
%{_datadir}/knotifications5/kaidan.notifyrc
%{_datadir}/%{name}/images
%{_datadir}/%{name}/providers.json

%changelog
%autochangelog
