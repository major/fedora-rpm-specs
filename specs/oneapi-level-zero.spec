%global srcname level-zero
%global lib_version 1.20
%global patch_version 4

Name:           oneapi-%{srcname}
Version:        %{lib_version}.%{patch_version}
Release:        %{autorelease}
Summary:        OneAPI Level Zero Specification Headers and Loader

License:        MIT
URL:            https://github.com/oneapi-src/%{srcname}
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

ExclusiveArch:  x86_64

BuildRequires:  chrpath
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  spdlog-devel

# Useful for a quick oneAPI Level-Zero testing
Recommends:     %{name}-zello_world

%description
The objective of the oneAPI Level-Zero Application Programming Interface
(API) is to provide direct-to-metal interfaces to offload accelerator
devices. Its programming interface can be tailored to any device needs
and can be adapted to support broader set of languages features such as
function pointers, virtual functions, unified memory,
and I/O capabilities.

%package        devel
Summary:        The oneAPI Level Zero Specification Headers and Loader development package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains library and header files for
developing applications that use %{name}.

%package        zello_world
Summary:        The oneAPI Level Zero quick test package with zello_world binary
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    zello_world
The %{name}-zello_world package contains a zello_world binary which is capable of a quick test
of the oneAPI Level-Zero driver and dumping out the basic device and driver characteristics.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
# spdlog uses fmt, but since this doesn't setup linking, use it in header only mode
export CXXFLAGS="%{build_cxxflags} -DFMT_HEADER_ONLY=1"
%cmake -DSYSTEM_SDPLOG=ON
%cmake_build

%install
%cmake_install
# Install also the zello_world binary to ease up testing of the l0
mkdir -p %{buildroot}%{_bindir}/
install -p -m 755 ./redhat-linux-build/bin/zello_world %{buildroot}%{_bindir}/zello_world
chrpath --delete %{buildroot}%{_bindir}/zello_world

%files
%license LICENSE
%doc README.md SECURITY.md
%{_libdir}/libze_loader.so.%{lib_version}.%{patch_version}
%{_libdir}/libze_loader.so.1
%{_libdir}/libze_validation_layer.so.%{lib_version}.%{patch_version}
%{_libdir}/libze_validation_layer.so.1
%{_libdir}/libze_tracing_layer.so.%{lib_version}.%{patch_version}
%{_libdir}/libze_tracing_layer.so.1

%files zello_world
%{_bindir}/zello_world

%files devel
%{_includedir}/level_zero
%{_libdir}/libze_loader.so
%{_libdir}/libze_validation_layer.so
%{_libdir}/libze_tracing_layer.so
%{_libdir}/pkgconfig/libze_loader.pc
%{_libdir}/pkgconfig/%{srcname}.pc

%changelog
%autochangelog
