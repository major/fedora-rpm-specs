# Run the tests by default
%bcond_without tests

Name:           libuv
Epoch:          1
Version:        1.45.0
Release:        %autorelease
Summary:        Platform layer for node.js

# the licensing breakdown is described in detail in the LICENSE file
License:        MIT and BSD and ISC
URL:            http://libuv.org/
Source0:        http://dist.libuv.org/dist/v%{version}/libuv-v%{version}.tar.gz
Source2:        %{name}.pc.in
Source3:        libuv.abignore

BuildRequires:  autoconf automake libtool
BuildRequires:  gcc
BuildRequires: make

# -- Patches -- #

# Disable some tests that fail in the network-free Koji builders
Patch0001: 0001-Fedora-Skip-tests-that-can-t-run-in-Koji.patch

%description
libuv is a new platform layer for Node. Its purpose is to abstract IOCP on
Windows and libev on Unix systems. We intend to eventually contain all platform
differences in this library.

%package devel
Summary:        Development libraries for libuv
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
Development libraries for libuv

%package static
Summary:        Platform layer for node.js - static library
Requires:       %{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}

%description static
Static library (.a) version of libuv.


%prep
%autosetup -n %{name}-v%{version} -p1

%build
./autogen.sh
%configure --disable-silent-rules
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/libuv.la

mkdir -p %{buildroot}%{_libdir}/libuv/
install -Dm0644 -t %{buildroot}%{_libdir}/libuv/ %{SOURCE3}

%check
%if %{with tests}
%make_build check
%endif

%ldconfig_scriptlets

%files
%doc README.md AUTHORS CONTRIBUTING.md MAINTAINERS.md SUPPORTED_PLATFORMS.md
%doc ChangeLog
%license LICENSE
%{_libdir}/%{name}.so.*
%{_libdir}/libuv/libuv.abignore

%files devel
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/uv.h
%{_includedir}/uv/

%files static
%{_libdir}/%{name}.a

%changelog
%autochangelog
