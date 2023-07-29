%global forgeurl https://github.com/libimobiledevice/libusbmuxd
%global commit 8d30a559cf0585625d9d05dc8ce0dd495b1de4f4
%global date 20230620
%{?commit:%global shortcommit %(c=%{commit}; echo ${c:0:7})}

Name:           libusbmuxd
Version:        2.0.2^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Client library USB multiplex daemon for Apple's iOS devices

License:        LGPL-2.0-or-later AND GPL-2.0-or-later
URL:            https://www.libimobiledevice.org/
Source:         %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  make

BuildRequires:  libimobiledevice-glue-devel
BuildRequires:  libplist-devel >= 2.2.0

%description
libusbmuxd is the client library used for communicating with Apple's iPod Touch,
iPhone, iPad and Apple TV devices. It allows multiple services on the device 
to be accessed simultaneously.

%package        utils
Summary:        Utilities for communicating with Apple's iOS devices
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    utils
Utilities for Apple's iOS devices

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Files for development with %{name}.

%prep
%autosetup -p1 -n %{name}-%{commit}

%if %{defined commit}
echo %{version} > .tarball-version
%endif

%build
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static
%make_build

%install
%make_install

%check
make check

%files
%license COPYING
%doc README.md AUTHORS
%{_libdir}/libusbmuxd-2.0.so.6*

%files utils
%{_bindir}/iproxy
%{_bindir}/inetcat
%{_mandir}/man1/iproxy.1*
%{_mandir}/man1/inetcat.1*

%files devel
%{_includedir}/usbmuxd.h
%{_includedir}/usbmuxd-proto.h
%{_libdir}/%{name}-2.0.so
%{_libdir}/pkgconfig/%{name}-2.0.pc

%changelog
%autochangelog
