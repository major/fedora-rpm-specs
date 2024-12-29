Name:          ruqola
Version:       2.4.0
Release:       1%{?dist}
Summary:       Qt-based client for Rocket Chat

License:       BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:           https://invent.kde.org/network/%{name}

Source:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

# Qt
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6WebSockets)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6NetworkAuth)
BuildRequires: cmake(Qt6MultimediaWidgets)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Keychain)
BuildRequires: cmake(Qt6Test)

# KDE Frameworks
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6SyntaxHighlighting)
BuildRequires: cmake(KF6NotifyConfig)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6IdleTime)
BuildRequires: cmake(KF6Prison)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6TextTranslator)
BuildRequires: cmake(KF6TextAutoCorrectionWidgets)
BuildRequires: cmake(KF6TextEditTextToSpeech)
BuildRequires: cmake(KF6TextEmoticonsWidgets)
BuildRequires: cmake(KF6TextUtils)
BuildRequires: cmake(KF6TextCustomEditor)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6Purpose)
BuildRequires: cmake(KF6DocTools)
# Not in Fedora
# BuildRequires: cmake(KLLMWidgets)
BuildRequires: cmake(KF6UserFeedback)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6NetworkManagerQt)
BuildRequires: cmake(KF6StatusNotifierItem)

BuildRequires: cmake(PlasmaActivities)

Requires: hicolor-icon-theme

Provides: bundled(cmark-rc)

%description
Ruqola is a Rocket chat client for the KDE desktop.

%package       doc
Summary:       HTML documentation for %{name}
BuildArch:     noarch
%description   doc
%{summary}.

%prep
%autosetup -p1

%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.ruqola.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.ruqola.appdata.xml

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/ruqola
%{_kf6_datadir}/applications/org.kde.ruqola.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/ruqola.png
%{_kf6_datadir}/knotifications6/ruqola.notifyrc
%{_kf6_datadir}/messageviewer/openurlwith/ruqola.openurl
%{_kf6_datadir}/qlogging-categories6/ruqola.{categories,renamecategories}
%{_kf6_libdir}/{librocketchatrestapi-qt,libruqolacore,libruqolawidgets}.so.%{version}
%{_kf6_libdir}/{librocketchatrestapi-qt,libruqolacore,libruqolawidgets}.so.0
%{_kf6_metainfodir}/org.kde.ruqola.appdata.xml
%{_kf6_qtplugindir}/ruqolaplugins/
%{_kf6_libdir}/libcmark-rc-copy.so.*

%files doc
%dir %{_docdir}/HTML/en/ruqola
%{_docdir}/HTML/en/ruqola/index.cache.bz2
%{_docdir}/HTML/en/ruqola/index.docbook

%changelog
* Sat Dec 28 2024 Steve Cossette <farchord@gmail.com> - 2.4.0-1
- 2.4.0

* Sun Dec 01 2024 Alessandro Astone <ales.astone@gmail.com> - 2.3.2-1
- new version

* Mon Nov 18 2024 Alessandro Astone <ales.astone@gmail.com> - 2.3.1-1
- new version

* Wed Oct 09 2024 Alessandro Astone <ales.astone@gmail.com> - 2.3.0-1
- new version

* Sat Sep 14 2024 Pavel Solovev <daron439@gmail.com> - 2.2.0-1
- new version

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Mar 12 2024 Steve Cossette <farchord@gmail.com> - 2.1.0-1
- v2.1.0
