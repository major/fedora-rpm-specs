Name:           dtk6log
Version:        0.0.2
Release:        %autorelease
Summary:        Simple, convenient and thread safe logger for Qt-based C++ apps
License:        LGPL-2.1-or-later
URL:            https://github.com/linuxdeepin/dtk6log
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

Patch0:         dtk6log-fix-qt6.9-build.patch
Patch1:         dtk6log-fix-build-against-qt-6-10.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake

BuildRequires:  cmake(Qt6Core)
BuildRequires:  qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
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
%autosetup -p1

%build
%cmake \
    -DBUILD_WITH_SYSTEMD=ON \
    -DBUILD_WITH_QT6=ON \
    -DDLOG_VERSION=%{version} \

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
