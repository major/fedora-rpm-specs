Name:    messagelib
Version: 24.12.1
Release: 1%{?dist}
Summary: KDE Message libraries

License: BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/pim/%{name}/

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  openssl-devel

BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qca-qt6)

BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(Gpgmepp)
BuildRequires:  cmake(QGpgmeQt6)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6TextTemplate)

BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6AkonadiMime)
BuildRequires:  cmake(KPim6AkonadiContactWidgets)
BuildRequires:  cmake(KPim6GrantleeTheme)
BuildRequires:  cmake(KPim6Gravatar)
BuildRequires:  cmake(KPim6IdentityManagementWidgets)
BuildRequires:  cmake(KPim6Libkleo)
BuildRequires:  cmake(KPim6MailTransport)
BuildRequires:  cmake(KPim6Mbox)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KPim6PimCommonAkonadi)
BuildRequires:  cmake(KPim6TextEdit)
BuildRequires:  cmake(KPim6Libkdepim)
BuildRequires:  cmake(KF6TextEditTextToSpeech)
BuildRequires:  cmake(KF6TextAutoCorrectionWidgets)
BuildRequires:  cmake(KF6TextUtils)
BuildRequires:  cmake(KF6TextCustomEditor)
BuildRequires:  cmake(KF6TextAddonsWidgets)
BuildRequires:  cmake(KPim6AkonadiSearch)

Obsoletes:      kf5-messagelib < 24.01.80

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KPim6Akonadi)
Requires:       cmake(KPim6AkonadiMime)
Requires:       cmake(KF6Contacts)
Requires:       cmake(KPim6IdentityManagementWidgets)
Requires:       cmake(KPim6Libkleo)
Requires:       cmake(KPim6Mime)
Requires:       cmake(KPim6PimCommonAkonadi)
Requires:       cmake(Qt6WebEngineWidgets)
%description    devel
%{summary}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/config.kcfg/customtemplates_kfg.kcfg
%{_kf6_datadir}/config.kcfg/templatesconfiguration_kfg.kcfg
%{_kf6_datadir}/knotifications6/messageviewer.notifyrc
%{_kf6_datadir}/knsrcfiles/messageviewer_header_themes.knsrc
%{_kf6_datadir}/libmessageviewer/
%{_kf6_datadir}/messagelist/
%{_kf6_datadir}/messageviewer/
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6MessageComposer.so.*
%{_kf6_libdir}/libKPim6MessageCore.so.*
%{_kf6_libdir}/libKPim6MessageList.so.*
%{_kf6_libdir}/libKPim6MessageViewer.so.*
%{_kf6_libdir}/libKPim6MimeTreeParser.so.*
%{_kf6_libdir}/libKPim6TemplateParser.so.*
%{_kf6_libdir}/libKPim6WebEngineViewer.so.*
%{_kf6_qtplugindir}/pim6/messageviewer/kf6/ktexttemplate/messageviewer_ktexttemplate_extension.so
%{_kf6_qtplugindir}/pim6/messageviewer/headerstyle/messageviewer_defaultgrantleeheaderstyleplugin.so
%dir %{_kf6_datadir}/org.kde.syntax-highlighting/
%{_kf6_datadir}/org.kde.syntax-highlighting/syntax/kmail-template.xml

%files devel
%{_includedir}/KPim6/MessageComposer/
%{_kf6_libdir}/cmake/KPim6MessageComposer/
%{_kf6_libdir}/libKPim6MessageComposer.so

%{_includedir}/KPim6/MessageCore/
%{_kf6_libdir}/cmake/KPim6MessageCore/
%{_kf6_libdir}/libKPim6MessageCore.so

%{_includedir}/KPim6/MessageList/
%{_kf6_libdir}/cmake/KPim6MessageList/
%{_kf6_libdir}/libKPim6MessageList.so

%{_includedir}/KPim6/MessageViewer/
%{_kf6_libdir}/cmake/KPim6MessageViewer/
%{_kf6_libdir}/libKPim6MessageViewer.so

%{_includedir}/KPim6/MimeTreeParser/
%{_kf6_libdir}/cmake/KPim6MimeTreeParser/
%{_kf6_libdir}/libKPim6MimeTreeParser.so

%{_includedir}/KPim6/TemplateParser/
%{_kf6_libdir}/cmake/KPim6TemplateParser/
%{_kf6_libdir}/libKPim6TemplateParser.so

%{_includedir}/KPim6/WebEngineViewer/
%{_kf6_libdir}/cmake/KPim6WebEngineViewer/
%{_kf6_libdir}/libKPim6WebEngineViewer.so

%{_qt6_docdir}/*.tags
 
%files doc
%{_qt6_docdir}/*.qch

%changelog
* Tue Jan 07 2025 Steve Cossette <farchord@gmail.com> - 24.12.1-1
- 24.12.1

* Sat Dec 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.12.0-1
- 24.12.0

* Fri Nov 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.90-1
- 24.11.90

* Fri Nov 15 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.80-1
- 24.11.80

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 24.08.3-1
- 24.08.3

* Tue Oct 08 2024 Steve Cossette <farchord@gmail.com> - 24.08.2-1
- 24.08.2

* Wed Sep 25 2024 Alessandro Astone <ales.astone@gmail.com> - 24.08.1-1
- 24.08.1

* Thu Aug 22 2024 Steve Cossette <farchord@gmail.com> - 24.08.0-1
- 24.08.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.05.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.2-1
- 24.05.2

* Fri Jun 14 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.1-1
- 24.05.1

* Fri May 17 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.0-1
- 24.05.0

* Fri Apr 12 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.2-1
- 24.02.2

* Fri Mar 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.1-1
- 24.02.1

* Sat Mar 09 2024 Marie Loise Nolden <loise@kde.org> - 24.02.0-2
- add missing BuildArch: noarch to -doc package

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.0-1
- 24.02.0

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Tue Jan 09 2024 Marie Loise Nolden <loise@kde.org> - 24.01.85-3
- add doc package for KF6 API

* Fri Dec 29 2023 Steve Cossette <farchord@gmail.com> - 24.01.85-2
- Added patch that changes the ugly HTML message bar into a button

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Wed Dec 20 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.80-4
- Obsolete kf5-messagelib

* Wed Dec 13 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-3
- Updated devel requirements

* Wed Dec 13 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-2
- Updated devel requirements

* Wed Dec 13 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
