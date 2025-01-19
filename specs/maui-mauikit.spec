Name:           maui-mauikit
Version:        4.0.0
Release:        3%{?dist}
License:        LGPL-2.0-or-later AND GPL-3.0-or-later AND BSD-3-Clause AND LGPL-3.0-only AND LGPL-2.1-only AND CC0-1.0 AND MIT
Summary:        Kit for developing Maui Apps
Url:            https://invent.kde.org/maui/mauikit
Source0:        https://download.kde.org/stable/maui/mauikit/%{version}/mauikit-%{version}.tar.xz

# Steve (05/23/2024): Not sure if this still required... Leaving
# here and will completely remove later if builds succeed.

# Temporarily turn off ppc64le because of build fails - onuralp
#ExclusiveArch: %%{ix86} s390x aarch64 x86_64

BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  cmake

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  libxcb-devel
BuildRequires:  pkgconfig(xcb-ewmh)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  qt6-qt5compat-devel

BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  cmake(MauiMan4)

Requires: kf6-kirigami
Requires: kf6-purpose
Requires: qt6-qtmultimedia

%description
Kit for developing MAUI Apps. MauiKit is a set of utilities
and "templated" controls based on Kirigami and QCC2 that
follow the ongoing work on the Maui HIG. It let you quickly
create a Maui application and access utilities and widgets
shared among the other Maui apps.

%package devel
Summary:        MauiKit development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Required headers to build components based
on the MauKit framework.

%prep
%autosetup -n mauikit-%{version} -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build

%install
%cmake_install
%find_lang mauikit

%files -f mauikit.lang
%license LICENSES/*
%{_kf6_datadir}/org.mauikit.controls
%{_kf6_qmldir}/org/mauikit
%{_libdir}/libMauiKit4.so.4*

%files devel
%doc README.md
%{_includedir}/MauiKit4
%{_libdir}/cmake/MauiKit4/
%{_libdir}/libMauiKit4.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 04 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 4.0.0-2
- Update QML dependencies

* Wed Sep 18 2024 Steve Cossette <farchord@gmail.com> - 4.0.0-1
- 4.0.0

* Sat Aug 10 2024 Steve Cossette <farchord@gmail.com> - 3.1.0-4
- Rebuild against the new mauiman version having a different soname

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.1.0-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May 23 2024 Steve Cossette <farchord@gmail.com> - 3.1.0-1
- 3.1.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 20 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 2.1.1-1
- 2.1.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 09 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 1.2.2-1
- initial package
