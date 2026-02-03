Name:           dtk6log
Version:        6.7.32
Release:        %autorelease
Summary:        Simple, convenient and thread safe logger for Qt-based C++ apps
License:        LGPL-2.1-or-later
URL:            https://github.com/linuxdeepin/dtklog
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6CorePrivate)
BuildRequires:  cmake(spdlog)
BuildRequires:  pkgconfig(libsystemd)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%autosetup -p1 -C

%build
%cmake -DDTK5=OFF -DBUILD_WITH_SYSTEMD=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE.LGPL
%doc README.md
%{_libdir}/libdtk6log.so.0*

%files devel
%{_libdir}/libdtk6log.so
%{_includedir}/dtk6/DLog/
%{_libdir}/cmake/Dtk6Log/
%{_libdir}/pkgconfig/dtk6log.pc
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_dtklog.pri

%changelog
%autochangelog
