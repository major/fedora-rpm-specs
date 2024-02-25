Name:           khealthcertificate
Version:        24.02.0
Release:        1%{?dist}
License:        Apache2.0 and BSD and CC-BY-4.0 and CC0-1.0 and EUPL-1.2 and LGPL-2.0 and MIT and W3C-20120513
Summary:        Handling of digital vaccination, test and recovery certificates.
Url:            https://invent.kde.org/pim/khealthcertificate
Source:         https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: gcc-c++
BuildRequires: openssl-devel
BuildRequires: zlib-devel

BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6I18n)

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)

%description
%{summary}.

%prep
%autosetup

%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build

%install
%cmake_install

%files
%{_kf6_datadir}/qlogging-categories6/org_kde_khealthcertificate.categories
%{_kf6_libdir}/*.so.*
%{_kf6_qmldir}/org/kde/khealthcertificate/

%license LICENSES/*

%package devel
Summary: Development files for khealthcertificate
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%files devel
%{_includedir}/*
%{_kf6_libdir}/cmake/KHealthCertificate
%{_kf6_libdir}/*.so

%changelog
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

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Mon Dec 18 2023 Steve cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.01.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jan 30 2023 Justin Zobel <justin@1707.io> - 23.01.0-1
- Update to 23.01.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Justin Zobel <justin@1707.io> - 22.11-1
- Update to 22.11

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09-1
- Update to 22.09

* Thu Aug 25 2022 Justin Zobel <justin@1707.io> - 22.06-1
- Update to 22.06

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb 09 2022 Justin Zobel <justin@1707.io> - 22.02-1
- Update to 22.02

* Wed Dec 22 2021 Justin Zobel <justin@1707.io> - 21.12-1
- Initial version of package
