Name:           dtk6core
Version:        6.0.27
Release:        %autorelease
Summary:        Deepin tool kit core modules
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dtk6core
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6ToolsTools)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

BuildRequires:  cmake(Dtk6Log)
BuildRequires:  cmake(DtkBuildHelper)
BuildRequires:  cmake(spdlog)

BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(uchardet)
BuildRequires:  pkgconfig(libsystemd)

BuildRequires:  libasan

Requires:       deepin-desktop-base

%description
Deepin tool kit core modules.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dtkcommon-devel%{_isa}

%description    devel
This package contains development files for %{name}.

%prep
%autosetup -p1
# comply with dtkcore in Fedora and dtk6core in Arch Linux
sed -i 's|/etc/os-version|/etc/dde-version|' src/dsysinfo.cpp

%build
%cmake -GNinja -DDTK_VERSION=%{version}
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libdtk6core.so.6*
%{_libexecdir}/dtk6/DCore/

%files devel
%{_libdir}/libdtk6core.so
%{_includedir}/dtk6/DCore/
%{_libdir}/cmake/Dtk6Core/
%{_libdir}/cmake/Dtk6CMake/
%{_libdir}/cmake/Dtk6DConfig/
%{_libdir}/cmake/Dtk6Tools/
%{_libdir}/pkgconfig/dtk6core.pc
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_archdatadir}/mkspecs/features/*.prf

%changelog
%autochangelog
