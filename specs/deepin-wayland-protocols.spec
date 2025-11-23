%global debug_package %{nil}

Name:           deepin-wayland-protocols
Epoch:          1
Version:        1.10.0.31
Release:        %autorelease
Summary:        Deepin Specific Protocols for Wayland
License:        LGPL-2.1-or-later AND MIT-CMU AND BSD-3-Clause
URL:            https://github.com/linuxdeepin/deepin-wayland-protocols
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules

%description
%{name} contains Deepin-specific Wayland protocols, which adds
functionality not available in the Wayland core protocol.

%package        devel
Summary:        Development files for %{name}

%description    devel
%{name} contains Deepin-specific Wayland protocols, which
adds functionality not available in the Wayland core protocol.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files devel
%license COPYING.LIB
%{_datadir}/deepin-wayland-protocols/
%{_libdir}/cmake/DeepinWaylandProtocols/

%changelog
%autochangelog
