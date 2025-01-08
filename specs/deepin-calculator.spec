Name:           deepin-calculator
Version:        6.5.4
Release:        %autorelease
Summary:        An easy to use calculator for ordinary users
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-calculator
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# fix: don't ignore linker flags specified by system
Patch0:         https://github.com/linuxdeepin/deepin-calculator/pull/82.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  qt5-linguist

BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  pkgconfig(dtkgui)
BuildRequires:  pkgconfig(dtkcore)

BuildRequires:  desktop-file-utils
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel

Requires:       hicolor-icon-theme
Recommends:     deepin-manual

%description
%{summary}.

%prep
%autosetup -p1
sed -i 's|lrelease|lrelease-qt5|g' translate_generation.sh

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
