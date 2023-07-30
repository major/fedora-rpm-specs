Name:           libirecovery
Version:        1.1.0
Release:        %autorelease
Summary:        Library and utility to talk to iBoot/iBSS via USB

License:        LGPL-2.1-only
URL:            https://github.com/libimobiledevice/libirecovery
Source:         %{url}/releases/download/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libimobiledevice-glue-devel
BuildRequires:  libusb1-devel
BuildRequires:  readline-devel
BuildRequires:  systemd-devel

%description
The libirecovery library allows communication with iBoot/iBSS of iOS devices
via USB.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        utils
Summary:        Utilites for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Suggests:       libimobiledevice-utils

%description    utils
This package contains command line utilities for %{name}.

%prep
%autosetup

%build
%configure --disable-static --with-udev
%make_build

%install
%make_install

%files
%license COPYING
%doc NEWS README.md
%{_libdir}/%{name}*.so.3*
%{_udevrulesdir}/*%{name}.rules

%files devel
%{_includedir}/%{name}.h
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/%{name}*.pc

%files utils
%{_bindir}/irecovery

%changelog
%autochangelog
