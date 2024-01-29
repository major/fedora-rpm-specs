Name:    pimcommon
Version: 24.01.90
Release: 3%{?dist}
Summary: PIM common libraries

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://api.kde.org/kdepim/pimcommon/html/

Source0:  https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6TextAutoCorrectionWidgets)
BuildRequires:  cmake(KF6TextAddonsWidgets)
BuildRequires:  cmake(KF6TextCustomEditor)
BuildRequires:  cmake(KF6TextTemplate)

# Pim
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6AkonadiContactWidgets)
BuildRequires:  cmake(KPim6IMAP)
BuildRequires:  cmake(KPim6LdapWidgets)
BuildRequires:  cmake(KPim6Libkdepim)
BuildRequires:  cmake(KPim6AkonadiSearch)

# qt6
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)

%description
%{summary}.

%package        akonadi
Summary:        The PimCommon Akondi runtime library
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description akonadi
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Config)
Requires:       cmake(KF6TextAutoCorrectionWidgets)
# akonadi
Requires:       %{name}-akonadi%{?_isa} = %{version}-%{release}
Requires:       cmake(KPim6Akonadi)
Requires:       cmake(KPim6AkonadiContactWidgets)
Requires:       cmake(KF6Contacts)
Requires:       cmake(KPim6IMAP)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6PimCommon.so.*
%{_kf6_libdir}/libKPim6PimCommonAkonadi.so.*
%{_qt6_plugindir}/designer/pimcommon6widgets.so

%files akonadi
%{_qt6_plugindir}/designer/pimcommon6akonadiwidgets.so

%files devel
%{_kf6_libdir}/libKPim6PimCommon.so
%{_kf6_libdir}/libKPim6PimCommonAkonadi.so
%{_kf6_libdir}/cmake/KPim6PimCommon/
%{_kf6_libdir}/cmake/KPim6PimCommonAkonadi/
%{_includedir}/KPim6/PimCommon/
%{_includedir}/KPim6/PimCommonAkonadi/
%{_qt6_docdir}/*.tags
 
%files doc
%{_qt6_docdir}/*.qch

%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Tue Jan 09 2024 Marie Loise Nolden <loise@kde.org> - 24.01.85-4
- add doc package for KF6 API

* Thu Dec 28 2023 Steve Cossette <farchord@gmail.com> - 24.01.85-3
- Reverted last commit

* Thu Dec 28 2023 Marie Loise Nolden <loise@kde.org> - 24.01.85-2
- Add obsoletes for upgrade path

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Tue Dec 12 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-2
- Updated devel requirements

* Mon Dec 11 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
