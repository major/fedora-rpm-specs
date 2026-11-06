Name:           bigscreen-ui
Version:        0.1.0
Release:        1%{?dist}
Summary:        Qt UI components targeted towards big screen utilisation

License:        CC-BY-SA-4.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only
URL:            https://invent.kde.org/libraries/bigscreen-ui
# Unstable for now
Source0:        https://download.kde.org/unstable/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)

BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)

%description
Bigscreen UI provides reusable
Qt Quick components designed for applications
targeting TV/console style platforms (i.e.
Plasma Bigscreen).

%prep
%autosetup

%conf
%cmake_kf6 -DBUILD_EXAMPLES=OFF

%build
%cmake_build


%install
%cmake_install


%files
%license LICENSES/*
%doc README.md
%{_kf6_qmldir}/org/kde/bigscreen/ui/


%changelog
* Tue Nov 03 2026 Steve Cossette <farchord@gmail.com> - 0.1.0
- Initial Release
