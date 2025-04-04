Name:           gattlib
Version:        0.7.2
Release:        %autorelease
Summary:        Library to access GATT information from BLE (Bluetooth Low Energy) devices
# See "License" in README.md for the breakdown:
License:        GPL-2.0-or-later AND BSD-3-Clause
URL:            https://github.com/labapart/gattlib

Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Upstream fixes:
Patch0:         https://github.com/labapart/gattlib/commit/a074af0d6a21665d3dfbd785ffd788146afeacef.patch
Patch1:         https://github.com/labapart/gattlib/commit/0d2d629b84573f2e7f2186c973a3124c4db5c630.patch
Patch2:         https://github.com/labapart/gattlib/commit/fec94997dde6a1f33efbd15f920eb7566c7be72a.patch
Patch3:         https://github.com/labapart/gattlib/commit/1580056bce260f0d8ad7ccc8b105c34057cd1fbd.patch
# Fix error during document building:
Patch4:         %{name}-docs.patch
# Use libpcre2-8 instead of libpcre:
Patch5:         https://patch-diff.githubusercontent.com/raw/labapart/gattlib/pull/292.patch

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  python3-breathe
BuildRequires:  python3-sphinx
BuildRequires:  sed

%description
GattLib is a library used to access Generic Attribute Profile (GATT) protocol of
BLE (Bluetooth Low Energy) devices.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconf-pkg-config      

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        examples
Summary:        Example programs using %{name}

%description    examples
This package provides various demonstration programs that leverage %{name}.

%prep
%autosetup -p1

# Remove bluez source:
rm -fr bluez

# Set shared library version
sed -i dbus/CMakeLists.txt \
  -e '/add_library(%{name} SHARED/a\ \ set_target_properties(%{name} PROPERTIES VERSION 0 SOVERSION %{version})'

%build
%cmake \
  -DCMAKE_SKIP_RPATH=YES \
  -DGATTLIB_BUILD_EXAMPLES=YES \
  -DGATTLIB_SHARED_LIB=YES \
  -DGATTLIB_BUILD_DOCS=YES \
  -DGATTLIB_PYTHON_INTERFACE=NO

%cmake_build

mv %{_vpath_builddir}/docs/docs/gattlib/sphinx/ html

%install
%cmake_install

# Install the examples
for p in %{_vpath_builddir}/examples/*; do
  install -Dpm0755 ${p}/$(basename $p) %{buildroot}%{_bindir}/gatt_$(basename $p)
done

%files
# License file is missing: https://github.com/labapart/gattlib/issues/128
%doc README.md
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.%{version}

%files devel
%doc html
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files examples
%{_bindir}/gatt_advertisement_data
%{_bindir}/gatt_ble_scan
%{_bindir}/gatt_discover
%{_bindir}/gatt_find_eddystone
%{_bindir}/gatt_nordic_uart
%{_bindir}/gatt_notification
%{_bindir}/gatt_read_write

%changelog
%autochangelog
