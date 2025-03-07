Name:           deepin-calculator
Version:        6.5.8
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
BuildRequires:  qt6-linguist

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
sed -i 's|lrelease|lrelease-qt6|g' translate_generation.sh

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install
%find_lang deepin-calculator --with-qt
rm %{buildroot}%{_datadir}/deepin-calculator/translations/deepin-calculator.qm

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f deepin-calculator.lang
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/deepin-manual/

%changelog
%autochangelog
