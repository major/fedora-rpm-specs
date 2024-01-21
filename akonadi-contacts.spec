Name:    akonadi-contacts
Version: 24.01.90
Release: 2%{?dist}
Summary: The Akonadi Contacts Library

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{name}

Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Prison)

BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KF6TextUtils)

BuildRequires:  cmake(KPim6AkonadiMime)
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6GrantleeTheme)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KF6IconThemes)

Obsoletes:      kf5-akonadi-contacts < 24.01.80-1

%description
%{summary}.

%package   devel
Summary:   Development files for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
Requires:  cmake(KPim6Akonadi)
Requires:  cmake(KF6Contacts)
Requires:  cmake(KPim6GrantleeTheme)
Recommends:  cmake(KF6CalendarCore)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version} -p1

# Remove together with move-translations.patch once released
find ./po -type f -name akonadicontact5.po -execdir mv {} akonadicontact6.po \;
find ./po -type f -name akonadicontact5-serializer.po -execdir mv {} akonadicontact6-serializer.po \;


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html


%files -f %{name}.lang
%{_kf6_datadir}/akonadi/plugins/serializer/
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6AkonadiContactCore.so.*
%{_kf6_libdir}/libKPim6AkonadiContactWidgets.so.*
%{_kf6_qtplugindir}/akonadi_serializer_*.so
%{_datadir}/kf6/akonadi/contact/

%files devel
%{_includedir}/KPim6/AkonadiContactCore/
%{_includedir}/KPim6/AkonadiContactWidgets/
%{_kf6_libdir}/cmake/KPim6AkonadiContactCore/
%{_kf6_libdir}/cmake/KPim6AkonadiContactWidgets/
%{_kf6_libdir}/libKPim6AkonadiContactCore.so
%{_kf6_libdir}/libKPim6AkonadiContactWidgets.so
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch

%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90
- Add doc package for KF6 API

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Thu Dec 21 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.80-3
- Backport rename translation files

* Sat Dec 16 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-2
- Obsoletes the old version

* Sat Dec 9 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
