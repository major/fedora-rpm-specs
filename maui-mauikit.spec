Name:           maui-mauikit
Version:        2.1.1
Release:        3%{?dist}
License:        LGPLv3
Summary:        Kit for developing Maui Apps
Url:            https://invent.kde.org/maui/mauikit
Source0:        https://download.kde.org/stable/maui/mauikit/%{version}/mauikit-%{version}.tar.xz

# Temporarily turn off ppc64le because of build fails - onuralp
ExclusiveArch: %{ix86} s390x aarch64 x86_64 

BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  cmake

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-plasma-devel
BuildRequires:  libxcb-devel
BuildRequires:  pkgconfig(xcb-ewmh)

BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5X11Extras)

BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5SyntaxHighlighting)

Requires: kf5-kirigami
Requires: applet-window-buttons

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
%cmake_kf5
%cmake_build

%install
%cmake_install


%files
%license LICENSES/*
%dir %{_kf5_qmldir}/QtQuick/Controls.2/
%dir %{_kf5_qmldir}/org/

%{_kf5_datadir}/org.mauikit.controls/*
%{_kf5_qmldir}/QtQuick/Controls.2/maui-style/
%{_kf5_qmldir}/org/mauikit/


%files devel
%doc README.md
%{_includedir}/*
%{_libdir}/cmake/MauiKit/
%{_kf5_libdir}/libMauiKit.so


%changelog
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
