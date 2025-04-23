%global commit f790e134bd71bf45a9fbfc23ef36b7ca30b55ec0
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20250313

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
Source:         https://download.kde.org/%{stable_kf6}/%{name}/%{version}/%{name}-%{version}.tar.xz
%endif

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6DocTools)

BuildRequires:  cmake(KDEGames6)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description
Purpose of the Atlantic board game is to acquire land in major cities in
North America and Europe while being a transatlantic traveller. One of the
game modes plays like the popular real estate board game based on Atlantic
City street names.

%package libs
Summary:        KDE monopd client libraries
License:        LGPL-2.1-only
# no KDE4 or KF5 port, was last built for KDE3
Obsoletes:      kdeaddons-atlantikdesigner < 4

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
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang %{name} --with-html --with-man


%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/%{app_id}.appdata.xml


%files -f %{name}.lang
%license COPYING
%doc ChangeLog README.md TODO
%{_kf6_bindir}/atlantik
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/applications/%{app_id}.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/atlantik.*
%{_kf6_datadir}/knotifications6/atlantik.notifyrc
%{_kf6_datadir}/qlogging-categories6/atlantik.categories
%{_kf6_mandir}/man6/atlantik.6*
%{_kf6_metainfodir}/%{app_id}.appdata.xml

%files libs
%license COPYING.LIB
%{_kf6_libdir}/libatlanti[ck]*.so.5{,.*}

%files devel
%{_includedir}/atlanti[ck]/
%{_kf6_libdir}/cmake/Atlantik/
%{_kf6_libdir}/libatlanti[ck]*.so


%changelog
%autochangelog
