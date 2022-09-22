Name:           deepin-shortcut-viewer
Version:        5.0.6
Release:        %autorelease
Summary:        Deepin Shortcut Viewer
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-shortcut-viewer
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(dtkwidget) >= 2.0.6
BuildRequires: make

%description
The program displays a shortcut key window when a JSON data is passed.

%prep
%setup -q

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT="%{buildroot}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog
