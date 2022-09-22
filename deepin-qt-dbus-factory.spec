%global soname dframeworkdbus
%global repo   dde-qt-dbus-factory


Name:           deepin-qt-dbus-factory
Version:        5.5.22
Release:        %autorelease
Summary:        A repository stores auto-generated Qt5 dbus code
# The entire source code is GPLv3+ except
# libdframeworkdbus/qtdbusextended/ which is LGPLv2+
License:        GPLv3+ and LGPLv2+
%if 0%{?fedora}
URL:            https://github.com/linuxdeepin/dde-qt-dbus-factory
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
%else
URL:            http://shuttle.corp.deepin.com/cache/repos/eagle/release-candidate/56qX566h6IGU6LCD5rWL6K-V6aqM6K-BMDUyMTQ5Mg/pool/main/d/dde-qt-dbus-factory/
Source0:        %{name}_%{version}.orig.tar.xz
%endif

BuildRequires:  python3
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
%if 0%{?fedora}
BuildRequires:  qt5-qtbase-private-devel
%endif
BuildRequires:  make

%description
A repository stores auto-generated Qt5 dbus code.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem

%description devel
Header files and libraries for %{name}.

%prep
%autosetup -p1 -n %{repo}-%{version}
sed -i "s/env python$/env python3/g" libdframeworkdbus/generate_code.py

%build
%qmake_qt5 LIB_INSTALL_DIR=%{_libdir}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md CHANGELOG.md technology-overview.md
%license LICENSE
%{_libdir}/lib%{soname}.so.2*

%files devel
%{_includedir}/lib%{soname}-2.0/
%{_libdir}/pkgconfig/%{soname}.pc
%{_libdir}/lib%{soname}.so
%{_libdir}/cmake/DFrameworkdbus/

%changelog
%autochangelog
