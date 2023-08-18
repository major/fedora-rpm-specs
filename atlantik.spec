%global commit 01397fd60153802cfce6b96af3265ee65079b50b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20230806

%global app_id  org.kde.atlantik

Name:           atlantik
Version:        0.7.80%{?gitdate:~%{gitdate}.git%{shortcommit}}
Release:        %autorelease
Summary:        KDE monopd game client
License:        GPL-2.0-only
URL:            https://apps.kde.org/atlantik/
%if 0%{?gitdate:1}
Source:         https://invent.kde.org/games/atlantik/-/archive/%{commit}/atlantik-%{commit}.tar.bz2
%else
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source:         https://download.kde.org/%{stable}/%{name}/%{version}/%{name}-%{version}.tar.xz
%endif

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5KDEGames)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme
# https://pagure.io/fedora-kde/SIG/issue/378
Requires:       kde-filesystem

# no KDE4 port, was last built for KDE3
Conflicts:      kdegames3 < 3.5.10-47

%description
Purpose of the Atlantic board game is to acquire land in major cities in
North America and Europe while being a transatlantic traveller. One of the
game modes plays like the popular real estate board game based on Atlantic
City street names.

%package libs
Summary:        KDE monopd client libraries
License:        LGPL-2.1-only

%description libs
%{summary}.

%package devel
Summary:        Development files for KDE monopd client libraries
License:        LGPL-2.1-only
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      kdegames3-devel < 3.5.10-47

%description devel
%{summary}.


%prep
%autosetup %{?gitdate:-n %{name}-%{commit}}


%build
%cmake_kf5
%cmake_build


%install
%cmake_install

%find_lang %{name} --with-html --with-man


%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/%{app_id}.appdata.xml


%files -f %{name}.lang
%license COPYING
%doc ChangeLog README TODO
%{_kf5_bindir}/atlantik
%{_kf5_datadir}/%{name}/
%{_kf5_datadir}/applications/%{app_id}.desktop
%{_kf5_datadir}/icons/hicolor/*/apps/atlantik.*
%{_kf5_datadir}/knotifications5/atlantik.notifyrc
%{_kf5_datadir}/kxmlgui5/%{name}/
%{_kf5_datadir}/qlogging-categories5/atlantik.categories
%{_kf5_mandir}/man6/atlantik.6*
%{_kf5_metainfodir}/%{app_id}.appdata.xml

%files libs
%license COPYING.LIB
%{_kf5_libdir}/libatlanti[ck]*.so.5{,.*}

%files devel
%{_includedir}/atlanti[ck]/
%{_kf5_libdir}/cmake/Atlantik/
%{_kf5_libdir}/libatlanti[ck]*.so


%changelog
%autochangelog
