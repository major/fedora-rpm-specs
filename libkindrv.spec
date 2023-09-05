Name:       libkindrv
Version:    1.0.0
Release:    %autorelease
Summary:    Driver for controlling robotic arms by Kinova
License:    LGPL-3.0-or-later
URL:        https://github.com/fawkesrobotics/libkindrv
Source0:    https://github.com/fawkesrobotics/libkindrv/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  boost-devel
BuildRequires:  boost-system
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libusb1-devel
BuildRequires:  pkgconfig(udev)

%description
This driver allows to navigate robotic arms by Kinova.
It supports different modes for arm navigation and finger control.

%package    devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description  devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1


%build
# we build the doc separately because we only want it in libkindrv-devel
# and 'make install' would install it in the wrong directory
%cmake \
  -DBUILD_DOC=OFF \
  -DUDEV_INSTALL_DIR=%{_udevrulesdir}

%cmake_build

%cmake_build --target apidoc


%install
%cmake_install


%files
%license LICENSE.GPL LICENSE.LGPL
%{_libdir}/libkindrv.so.*
%{_udevrulesdir}/10-libkindrv.rules


%files devel
%doc %{_vpath_builddir}/doc/html
%{_includedir}/*
%{_libdir}/libkindrv.so
%{_libdir}/pkgconfig/libkindrv.pc


%changelog
%autochangelog
