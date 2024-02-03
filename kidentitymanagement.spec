Name:    kidentitymanagement
Version: 24.01.95
Release: 1%{?dist}
Summary: The KIdentityManagement Library

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz


BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6TextEditTextToSpeech)
BuildRequires:  cmake(KPim6TextEdit)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  qt6-qtbase-private-devel

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons)
Requires:       kpimtextedit-devel
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
find ./po -type f -name libkpimidentities5.po -execdir mv {} libkpimidentities6.po \;


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6IdentityManagementQuick.so.*
%{_kf6_libdir}/libKPim6IdentityManagementCore.so.*
%{_kf6_libdir}/libKPim6IdentityManagementWidgets.so.*
%{_kf6_qmldir}/org/kde/kidentitymanagement/


%files devel
%{_datadir}/dbus-1/interfaces/kf6_org.kde.pim.IdentityManager.xml
%{_includedir}/KPim6/KIdentityManagementCore/
%{_includedir}/KPim6/KIdentityManagementQuick/
%{_includedir}/KPim6/KIdentityManagementWidgets/
%{_kf6_libdir}/cmake/KPim6IdentityManagementCore/
%{_kf6_libdir}/cmake/KPim6IdentityManagementQuick/
%{_kf6_libdir}/cmake/KPim6IdentityManagementWidgets/
%{_kf6_libdir}/libKPim6IdentityManagementCore.so
%{_kf6_libdir}/libKPim6IdentityManagementWidgets.so
%{_kf6_libdir}/libKPim6IdentityManagementQuick.so
%{_qt6_docdir}/*.tags
 
%files doc
%{_qt6_docdir}/*.qch

%changelog
* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Tue Jan 09 2024 Marie Loise Nolden <loise@kde.org> - 24.01.85-2
- add doc package for KF6 API

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Thu Dec 21 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.80-2
- Backport rename translation files

* Thu Dec 7 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80
