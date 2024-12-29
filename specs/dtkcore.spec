Name:           dtkcore
Version:        5.7.5
Release:        %autorelease
Summary:        Deepin tool kit core modules
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dtkcore
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5Help)
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

BuildRequires:  cmake(DtkLog)
#BuildRequires:  cmake(DtkBuildHelper) >= %{version}
BuildRequires:  dtkcommon-devel >= %{version}

BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(uchardet)
BuildRequires:  pkgconfig(icu-uc)

BuildRequires:  doxygen

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
sed -i 's|/etc/os-version|/etc/dde-version|' src/dsysinfo.cpp

%build
%cmake -GNinja \
    -DDTK_VERSION=%{version} \
    -DQCH_INSTALL_DESTINATION=%{_qt5_docdir}
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_libdir}/libdtkcore.so.5*
%{_libexecdir}/dtk5/DCore/

%files devel
%{_libdir}/libdtkcore.so
%{_includedir}/dtk5/
%{_libdir}/cmake/DtkCore/
%{_libdir}/cmake/DtkCMake/
%{_libdir}/cmake/DtkDConfig/
%{_libdir}/cmake/DtkTools/
%{_libdir}/pkgconfig/dtkcore.pc
%{_qt5_archdatadir}/mkspecs/modules/*.pri
%{_qt5_archdatadir}/mkspecs/features/*.prf
%{_qt5_docdir}/dtkcore.qch

%changelog
%autochangelog
