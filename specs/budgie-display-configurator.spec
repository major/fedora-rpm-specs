Name: budgie-display-configurator
Version: 0.0.1
Release: 1%{?dist}
Summary: Graphical display configuration tool for Budgie Desktop

License: MPL-2.0
URL:     https://forge.moderndesktop.dev/BuddiesOfBudgie/budgie-display-configurator
Source0: %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: cmake(KF6ColorScheme)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6QQC2DesktopStyle)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6UiTools)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros

Requires:      budgie-desktop-services
Requires:      kf6-kirigami%{?_isa}

%description
Graphical display configuration tool for Budgie Desktop

%prep
%autosetup -n %{name}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/org.buddiesofbudgie.DisplayConfig
%{_datadir}/applications/org.buddiesofbudgie.DisplayConfig.desktop

%changelog
* Sun Nov 23 2025 Joshua Strobl <joshua@buddiesofbudgie.org> - 0.0.1-1
- Initial inclusion of budgie-display-configurator
