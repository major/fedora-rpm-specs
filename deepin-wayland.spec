%global repo dde-wayland

Name:           deepin-wayland
Version:        1.0.0
Release:        %autorelease
Summary:        Deepin Wayland libraries

License:        GPLv3+
URL:            https://github.com/linuxdeepin/%{repo}
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt5-qtwayland-devel
BuildRequires:  wayland-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  libxkbcommon-devel


%description
This package provides Wayland libraries with Deepin customization.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel
Header files and libraries for %{name}.

%prep
%autosetup -p1 -n %{repo}-%{version}


%build
%qmake_qt5 LIB_INSTALL_DIR=%_libdir
%make_build


%install
%make_install INSTALL_ROOT=%buildroot


%files
%{_libdir}/lib%{repo}-client.so.0*
%{_libdir}/lib%{repo}-server.so.0*

%files devel
%{_libdir}/lib%{repo}-client.so
%{_libdir}/lib%{repo}-server.so
%{_includedir}/%{repo}-client/
%{_includedir}/%{repo}-server/
%{_libdir}/pkgconfig/%{repo}-client.pc
%{_libdir}/pkgconfig/%{repo}-server.pc


%changelog
%autochangelog
