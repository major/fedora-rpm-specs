%{?mingw_package_header}

Name:           mingw-libgusb
Version:        0.4.5
Release:        %autorelease
Summary:        GLib wrapper around libusb1 for MinGW

License:        LGPL-2.1-or-later
URL:            https://gitorious.org/gusb/
Source0:        http://people.freedesktop.org/~hughsient/releases/libgusb-%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-json-glib
BuildRequires:  mingw64-json-glib
BuildRequires:  mingw32-libusbx >= 1.0.19
BuildRequires:  mingw64-libusbx >= 1.0.19
BuildRequires:  mingw32-glib2 >= 2.38.0
BuildRequires:  mingw64-glib2 >= 2.38.0
BuildRequires:  gobject-introspection-devel

%description
GUsb is a GObject wrapper for libusb1 that makes it easy to do
asynchronous control, bulk and interrupt transfers with proper
cancellation and integration into a mainloop.

This is the MinGW version of this library.

%package -n mingw32-libgusb
Summary:        MinGW library which allows easy access to USB devices
Requires:       pkgconfig

%description -n mingw32-libgusb
This package contains the header files and libraries needed to develop MinGW
applications that use libgusb.

%package -n mingw32-libgusb-static
Summary:        MinGW static library which allows easy access to USB devices
Requires:       mingw32-libgusb = %{version}-%{release}

%description -n mingw32-libgusb-static
This package contains the static libraries needed to develop MinGW
applications that use libgusb.

%package -n mingw64-libgusb
Summary:        MinGW library which allows easy access to USB devices
Requires:       pkgconfig

%description -n mingw64-libgusb
This package contains the header files and libraries needed to develop MinGW
applications that use libgusb.

%package -n mingw64-libgusb-static
Summary:        MinGW static library which allows easy access to USB devices
Requires:       mingw64-libgusb = %{version}-%{release}

%description -n mingw64-libgusb-static
This package contains the static libraries needed to develop MinGW
applications that use libgusb.

%{?mingw_debug_package}


%prep
%setup -q -n libgusb-%{version}

%build

%mingw_meson \
        --default-library=both \
        -Dvapi=false \
        -Dtests=false \
        -Dintrospection=false \
        -Ddocs=false
%mingw_ninja

%install
%mingw_ninja_install


%files -n mingw32-libgusb
%license COPYING
%doc AUTHORS README.md NEWS
%{mingw32_bindir}/gusbcmd.exe
%{mingw32_bindir}/libgusb-2.dll
%{mingw32_includedir}/gusb-1/
%{mingw32_libdir}/libgusb.dll.a
%{mingw32_libdir}/pkgconfig/gusb.pc

%files -n mingw32-libgusb-static
%{mingw32_libdir}/libgusb.a

%files -n mingw64-libgusb
%license COPYING
%doc AUTHORS README.md NEWS
%{mingw64_bindir}/gusbcmd.exe
%{mingw64_bindir}/libgusb-2.dll
%{mingw64_includedir}/gusb-1/
%{mingw64_libdir}/libgusb.dll.a
%{mingw64_libdir}/pkgconfig/gusb.pc

%files -n mingw64-libgusb-static
%{mingw64_libdir}/libgusb.a


%changelog
%autochangelog
