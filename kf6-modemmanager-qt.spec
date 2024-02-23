%undefine __cmake_in_source_build

%global framework modemmanager-qt

Name:    kf6-%{framework}
Version: 6.0.0
Release: 1%{?dist}
Summary: A Tier 1 KDE Frameworks module wrapping ModemManager DBus API
License: GPL-2.0-only AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}
Source0: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  ModemManager-devel >= 1.0.0
BuildRequires:  qt6-qtbase-devel

Requires:       kf6-filesystem

%description
A Qt 6 library for ModemManager.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ModemManager-devel
Requires:       qt6-qtbase-devel
%description    devel
Qt 6 libraries and header files for developing applications
that use ModemManager.

%package        doc
Summary:        Developer Documentation files for %{name}
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%doc README README.md
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*.categories
%{_kf6_datadir}/qlogging-categories6/*.renamecategories
%{_kf6_libdir}/libKF6ModemManagerQt.so.*

%files devel
%{_kf6_libdir}/libKF6ModemManagerQt.so
%{_kf6_libdir}/cmake/KF6ModemManagerQt/
%{_kf6_includedir}/ModemManagerQt/
%{_qt6_docdir}/*.tags
 
%files doc
%{_qt6_docdir}/*.qch

%changelog
* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.0-1
- 6.0.0

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.249.0-1
- 5.249.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.248.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.248.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.248.0-1
- 5.248.0

* Tue Jan 09 2024 Marie Loise Nolden <loise@kde.org> - 5.247.0-2
- add doc package for KF6 API

* Wed Dec 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.247.0-1
- 5.247.0

* Sat Dec 02 2023 Justin Zobel <justin.zobel@gmail.com> - 5.246.0-1
- Update to 5.246.0

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Wed Sep 27 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359714ce9f4a58b6372b68bd6e3a929886d2-48
- rebuilt

* Wed Sep 27 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359714ce9f4a58b6372b68bd6e3a929886d2-47
- rebuilt

* Tue Sep 26 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359714ce9f4a58b6372b68bd6e3a929886d2-46
- rebuilt

* Tue Sep 26 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359714ce9f4a58b6372b68bd6e3a929886d2-45
- rebuilt

* Tue Sep 26 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359714ce9f4a58b6372b68bd6e3a929886d2-44
- rebuilt

* Tue Sep 26 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359714ce9f4a58b6372b68bd6e3a929886d2-43
- rebuilt

* Mon Sep 25 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359714ce9f4a58b6372b68bd6e3a929886d2-42
- rebuilt

* Sun Sep 24 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359714ce9f4a58b6372b68bd6e3a929886d2-41
- rebuilt

* Sat Sep 23 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359714ce9f4a58b6372b68bd6e3a929886d2-40
- rebuilt

* Fri Sep 22 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359714ce9f4a58b6372b68bd6e3a929886d2-39
- rebuilt

* Thu Sep 21 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359714ce9f4a58b6372b68bd6e3a929886d2-38
- rebuilt

* Thu Sep 21 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359-37
- rebuilt

* Thu Sep 21 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359-36
- rebuilt

* Wed Sep 20 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359-35
- rebuilt

* Tue Aug 29 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230813.164311.fa71a4d-1
- Initial package
