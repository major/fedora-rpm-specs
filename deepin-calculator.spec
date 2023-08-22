Name:           deepin-calculator
Version:        5.8.24
Release:        %autorelease
Summary:        An easy to use calculator for ordinary users
# migrated to SPDX
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-calculator
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# fix ldflags
Patch0:         https://github.com/linuxdeepin/deepin-calculator/pull/82.patch

BuildRequires:  qt5-linguist
BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(dtkwidget) >= 2.0
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  desktop-file-utils
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel
Requires:       hicolor-icon-theme
Recommends:     deepin-manual

%description
%{summary}.

%prep
%autosetup -p1

%build
export PATH=%{_qt5_bindir}:$PATH
%cmake
%cmake_build

%install
export PATH=%{_qt5_bindir}:$PATH
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/deepin-manual/
%{_datadir}/%{name}/

%changelog
%autochangelog
