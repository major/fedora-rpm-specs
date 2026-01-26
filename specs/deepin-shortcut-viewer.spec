Name:           deepin-shortcut-viewer
Version:        5.5.6
Release:        %autorelease
Summary:        Deepin Shortcut Viewer
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-shortcut-viewer
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Widget)

%description
The program displays a shortcut key window when a JSON data is passed.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog
