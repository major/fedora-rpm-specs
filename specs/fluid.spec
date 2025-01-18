#global snapdate 20160508
#global snaphash 42c2f64d41863a002a14911410a121a5ecb1df1a

Name:           fluid
Summary:        Library for fluid and dynamic applications development with QtQuick
Version:        0.8.0
Release:        23%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://liri.io
Source0:        https://github.com/hawaii-desktop/%{name}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

Requires:       qt5-qtquickcontrols
Requires:       qt5-qtquickcontrols2

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules

%description
Library for fluid and dynamic applications development with QtQuick.


%prep
%setup -q -n %{?snaphash:%{name}-%{snaphash}}%{!?snaphash:%{name}-%{version}}


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%license LICENSE.LGPLv21
%doc AUTHORS.md README.md
%{_kf5_qmldir}/Fluid/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.0-22
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 04 2020 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 0.8.0-12
- Update URL.
- Use new CMake macros.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 22 2016 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 0.8.0-1
- Update to 0.8.0

* Mon Jul 11 2016 Pier Luigi Fiorini <pierluigi.fiorini@hawaiios.org> - 0.7.0-1
- Update to 0.7.0

* Sun May 08 2016 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 0.6.90-1.20160508git42c2f64d41863
- Update to latest snapshot

* Wed Apr 20 2016 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 0.6.90-1.20160328git2fdadf1282bfa
- Update to latest snapshot

* Mon Mar 07 2016 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 0.6.90-0.1.20160307git
- Update to git snapshot

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 24 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.3.0-1
- Update to 0.3 release

* Sun Jun 15 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.2.90-0.2.20140330git6e0a3f7
- A more recent Git snapshot

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.90-0.2.20140101gite9ea587
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 18 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.2.90-0.1.20140101gite9ea587
- A more recent Git snapshot

* Sat Jan 04 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.2.0-1
- Update to a new release tarball

* Mon Oct 28 2013 Lubomir Rintel <lkundrak@v3.sk> - 0.1.90-2.20130723git6d6e0cd
- Drop useless ldconfig (Eduardo Echeverria, #1019435)
- Drop old RPM artifacts (Eduardo Echeverria, #1019435)

* Mon Sep 16 2013 Lubomir Rintel <lkundrak@v3.sk> - 0.1.90-1.20130723git6d6e0cd
- Initial packaging
