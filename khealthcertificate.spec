Name:           khealthcertificate
Version:        23.01.0
Release:        1%{?dist}
License:        Apache2.0 and BSD and CC-BY-4.0 and CC0-1.0 and EUPL-1.2 and LGPL-2.0 and MIT and W3C-20120513
Summary:        Handling of digital vaccination, test and recovery certificates.
Url:            https://invent.kde.org/pim/khealthcertificate
Source:         https://download.kde.org/stable/plasma-mobile/%{version}/khealthcertificate-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: gcc-c++
BuildRequires: openssl-devel
BuildRequires: zlib-devel

BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5I18n)

BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Qml)

%description
%{summary}.

%prep
%autosetup

%build
%cmake_kf5
%cmake_build

%install
%cmake_install

%files
%{_kf5_datadir}/qlogging-categories5/org_kde_khealthcertificate.categories

%{_kf5_libdir}/*.so.*

%{_kf5_qmldir}/org/kde/khealthcertificate/

%license LICENSES/*

%package devel
Summary: Development files for khealthcertificate
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%files devel
%{_includedir}/*

%{_kf5_libdir}/cmake/KHealthCertificate
%{_kf5_libdir}/*.so

%changelog
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
