Name:    mailimporter
Version: 24.01.90
Release: 2%{?dist}
Summary: Mail importer library

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LicenseRef-KDE-Accepted-GPL
URL:     https://invent.kde.org/pim/%{name}

Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)

BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KPim6AkonadiMime)
BuildRequires:  cmake(KPim6PimCommon)

%description
%{summary}.

%package        akonadi
Summary:        The MailImporterAkondi runtime library
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description akonadi
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Archive)
# akonadi
Requires:       %{name}-akonadi%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.

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
%find_lang %{name} --all-name


%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6MailImporter.so.*

%files akonadi
%{_kf6_libdir}/libKPim6MailImporterAkonadi.so.*

%files devel
%{_kf6_libdir}/libKPim6MailImporter.so
%{_kf6_libdir}/libKPim6MailImporterAkonadi.so
%{_kf6_libdir}/cmake/KPim6MailImporterAkonadi/
%{_kf6_libdir}/cmake/KPim6MailImporter/
%{_includedir}/KPim6/MailImporterAkonadi/
%{_includedir}/KPim6/MailImporter/
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90
- Add doc package for KF6 API

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Tue Dec 12 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
