Name:           qwlroots
Version:        0.5.2
Release:        %autorelease
Summary:        Qt and QML bindings for wlroots
License:        Apache-2.0 OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
URL:            https://github.com/vioken/qwlroots
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         https://github.com/vioken/qwlroots/pull/293.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  wlroots-devel
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wlr-protocols)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Test)

%description
qwlroots is a binding of wlroots, which provides a Qt style development
interface. It aims to simplify wlroots API calling methods with Qt, and serve
the needs of calling wlroots within Qt projects. In qwlroots, each wlroots
struct is wrapped as a C++ class with its corresponding functions. At the same
time, wl_singals in Wayland are wrapped as Qt signals.

%package        devel
Summary:        Development Files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%autosetup -p1

%build
%cmake -GNinja

%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc README.md
%license LICENSES/*
%{_libdir}/libqwlroots.so.0*

%files devel
%{_includedir}/qwlroots/
%{_libdir}/cmake/QWlroots/
%{_libdir}/libqwlroots.so
%{_libdir}/pkgconfig/qwlroots.pc

%changelog
%autochangelog
