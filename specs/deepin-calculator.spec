Name:           deepin-calculator
Version:        6.5.30
Release:        %autorelease
Summary:        An easy to use calculator for ordinary users
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-calculator
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6LinguistTools)

BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  cmake(Dtk6Core)

BuildRequires:  desktop-file-utils

Requires:       hicolor-icon-theme
Recommends:     deepin-manual

%description
%{summary}.

%prep
%autosetup -p1

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/deepin-manual/manual-assets/application/deepin-calculator/
%{_datadir}/deepin-calculator/
%{_datadir}/dbus-1/services/com.deepin.Calculator.service

%changelog
%autochangelog
