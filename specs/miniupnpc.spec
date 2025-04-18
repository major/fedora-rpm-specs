# Needed for RHEL/CentOS 8
%undefine __cmake_in_source_build

# Set a common one for all architectures and not _target_platform, fixes aarch64
%global __cmake_builddir build

%filter_provides_in %{python3_sitearch}/.*\.so$

Summary:    Library and tool to control NAT in UPnP-enabled routers
Name:       miniupnpc
Version:    2.3.2
Release:    %autorelease
License:    LicenseRef-Callaway-BSD
URL:        http://miniupnp.free.fr/

BuildRequires:  cmake >= 3.5.0
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Source0:    http://miniupnp.free.fr/files/%{name}-%{version}.tar.gz

%description
miniupnpc is an implementation of a UPnP client library, enabling applications
to access the services provided by an UPnP "Internet Gateway Device" present on
the network. In UPnP terminology, it is a UPnP Control Point.

This package includes upnpc, a UPnP client application for configuring  port
forwarding in UPnP enabled routers.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and development documentation for
%{name}.

%package -n python3-%{name}
Summary:    Python3 interface to %{name}

%description -n python3-%{name}
This package contains python3 interfaces to %{name}.

%prep
%autosetup -p2

# Use already built shared object for Python module
# Unversioned link is not enough to avoid a rebuild
sed -i -e 's|build/libminiupnpc.a|build/libminiupnpc.so.%{version}|g' setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%cmake \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
    -DCMAKE_SKIP_RPATH:BOOL=YES \
    -DNO_GETADDRINFO=FALSE \
    -DUPNPC_BUILD_SAMPLE=TRUE \
    -DUPNPC_BUILD_SHARED=TRUE \
    -DUPNPC_BUILD_STATIC=FALSE \
    -DUPNPC_BUILD_TESTS=TRUE \
    -DUPNPC_NO_INSTALL=FALSE

%cmake_build
%pyproject_wheel

%install
%cmake_install
%pyproject_install
%pyproject_save_files -l miniupnpc

mv %{buildroot}%{_bindir}/upnpc-shared %{buildroot}%{_bindir}/upnpc
mv %{buildroot}%{_bindir}/upnp-listdevices-shared %{buildroot}%{_bindir}/upnp-listdevices
rm -f %{buildroot}%{_bindir}/external-ip.sh

%check
make CFLAGS="%{optflags} -DMINIUPNPC_SET_SOCKET_TIMEOUT" check

%files
%license LICENSE
%doc Changelog.txt README
%{_bindir}/upnpc
%{_bindir}/upnp-listdevices
%{_libdir}/libminiupnpc.so.20
%{_libdir}/libminiupnpc.so.%{version}

%files devel
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}/libminiupnpc-shared-noconfig.cmake
%{_libdir}/cmake/%{name}/libminiupnpc-shared.cmake
%{_libdir}/cmake/%{name}/miniupnpc-config.cmake
%{_libdir}/libminiupnpc.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/%{name}.3*

%files -n python3-%{name} -f %{pyproject_files}

%changelog
%autochangelog
