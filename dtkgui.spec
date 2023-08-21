Name:           dtkgui
Version:        5.6.12
Release:        %autorelease
Summary:        Deepin dtkgui
# migrated to SPDX
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dtkgui

Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  dtkcore-devel
BuildRequires:  libqtxdg-devel
BuildRequires:  librsvg2-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel
%if 0%{?fedora}
BuildRequires:  qt5-qtbase-private-devel
%endif
BuildRequires:  %{_bindir}/doxygen
BuildRequires:  make
%description
Dtkgui is the GUI module for DDE look and feel.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dtkcore-devel%{?_isa}

%description devel
Header files and libraries for %{name}.

%prep
%autosetup

%build
export PATH=%{_qt5_bindir}:$PATH
%cmake -DLINUXNAME=fedora \
       -DNOTPACKAGE=OFF \
       -DBUILD_DOCS=OFF
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.5*
%{_libexecdir}/dtk5/DGui/

%files devel
%{_includedir}/dtk5/DGui
%{_libdir}/pkgconfig/dtkgui*.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_dtkgui.pri
%{_libdir}/cmake/DtkGui/
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
