Name:          libtypec
Version:       0.6.1
Release:       2%{?dist}
Summary:       A generic user space library for USB-C port management
License:       MIT and GPL-2.0-only
URL:           https://github.com/libtypec/libtypec
Source0:       %{url}/archive/refs/tags/%{name}-%{version}.tar.gz

BuildRequires: meson
BuildRequires: gcc
BuildRequires: gtk3-devel
BuildRequires: systemd-devel

%description
“libtypec” is aimed to provide a generic interface abstracting all
platform complexity for user space to develop tools for efficient
USB-C port management. The library can also enable development of
diagnostic and debug tools to debug system issues around USB-C/USB
PD topology.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%package utils
Summary: Utilities for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Utilities for USB Type-C.

%package guiutils
Summary: Utilities for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description guiutils
Utilities for USB Type-C.

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}

%build
%meson -Dutils=true
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license README
%{_libdir}/libtypec.so.0*

%files devel
%{_includedir}/libtypec*
%{_libdir}/libtypec.so
%{_libdir}/pkgconfig/libtypec.pc

%files utils
%{_bindir}/lstypec
%{_bindir}/typecstatus
%{_bindir}/ucsicontrol

%files guiutils
%{_bindir}/usbcview

%changelog
* Mon Apr 28 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 0.6.1-2
- Update license and URL

* Mon Apr 28 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 0.6.1-1
- Initial package
