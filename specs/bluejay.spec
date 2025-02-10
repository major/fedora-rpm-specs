%global rdnn_name io.github.ebonjaeger.bluejay

Name:           bluejay
Version:        1.0.2
Release:        1%{?dist}
Summary:        Bluetooth manager written in Qt

# The main code is MPL-2.0, the icon file is CC-BY-SA-4.0, the desktop and metainfo files are CC0-1.0, and pin-code-database.xml is GPL-2.0-or-later
License:        MPL-2.0 and CC0-1.0 and CC-BY-SA-4.0 and MIT and GPL-2.0-or-later
URL:            https://github.com/EbonJaeger/bluejay
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6UiTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(KF6BluezQt)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6QQC2DesktopStyle)
BuildRequires:  kf6-rpm-macros
# For check
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

# Extra runtime dependencies
Requires:       kf6-kirigami%{?_isa}
Requires:       hicolor-icon-theme

%description
This is a Bluetooth manager and Bluez front-end. With it, you can pair devices,
connect to and remove devices, turn Bluetooth on and off, and more.
Bluejay is powered by the Qt6 graphical toolkit and KDE Frameworks.

Bluejay is meant to be functional and look good.

%prep
%autosetup -S git_am


%conf
%cmake_kf6


%build
%cmake_build


%install
%cmake_install

%find_lang %{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnn_name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{rdnn_name}.metainfo.xml


%files -f %{name}.lang
%license LICENSE
%license LICENSES/*
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{rdnn_name}.desktop
%{_metainfodir}/%{rdnn_name}.metainfo.xml
%{_datadir}/icons/hicolor/*/*/%{rdnn_name}.svg


%changelog
* Sat Feb 08 2025 Evan Maddock <maddock.evan@vivaldi.net> - 1.0.2-1
- Initial package
