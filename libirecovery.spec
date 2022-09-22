Name:           libirecovery
Version:        1.0.0
Release:        %autorelease
Summary:        Library and utility to talk to iBoot/iBSS via USB

License:        LGPLv2
URL:            https://github.com/libimobiledevice/libirecovery
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
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
./autogen.sh
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

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
