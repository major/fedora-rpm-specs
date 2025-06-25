%global mfx_major 2
%global mfx_minor 15

Name:           libvpl
Epoch:          1
Version:        2.15.0
Release:        %autorelease
Summary:        Intel Video Processing Library
License:        MIT
URL:            https://intel.github.io/libvpl/latest/index.html
ExclusiveArch:  x86_64

Source0:        https://github.com/intel/libvpl/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libdrm) >= 2.4.91
BuildRequires:  pkgconfig(libva) >= 1.2
BuildRequires:  pkgconfig(libva-drm) >= 1.2
BuildRequires:  pkgconfig(libva-x11) >= 1.10.0
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.15
BuildRequires:  pkgconfig(x11)

Recommends:     intel-mediasdk
Recommends:     intel-vpl-gpu-rt

Obsoletes:      oneVPL <= 2023.4.0
Provides:       oneVPL%{?_isa} == %{?epoch:%{epoch}:}%{version}-%{release}

%description
The oneAPI Video Processing Library (oneVPL) provides a single video processing
API for encode, decode, and video processing that works across a wide range of
accelerators.

The base package is limited to the dispatcher and samples. To use oneVPL for
video processing you need to install at least one implementation. Current
implementations:

- intel-vpl-gpu-rt for use on Intel Xe graphics and newer
- intel-mediasdk for use on legacy Intel graphics

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:      oneVPL-devel <= 2023.4.0
Provides:       oneVPL-devel%{?_isa} == %{?epoch:%{epoch}:}%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package        samples
Summary:        Sample programs and source code for %{name}
Requires:       %{name}-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:      oneVPL-samples <= 2023.4.0
Provides:       oneVPL-samples%{?_isa} == %{?epoch:%{epoch}:}%{version}-%{release}

%description    samples
This package contains sample programs and applications that use %{name}.

%prep
%autosetup -p1 -n libvpl-%{version}

%build
%cmake -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}
%cmake_build

%install
%cmake_install

# Let RPM pick up documents in the files section
rm -fr %{buildroot}%{_datadir}/vpl/licensing

%files
%license LICENSE
%doc README.md CONTRIBUTING.md third-party-programs.txt
%dir %{_sysconfdir}/vpl
%{_sysconfdir}/vpl/vars.sh
%{_libdir}/libvpl.so.%{mfx_major}
%{_libdir}/libvpl.so.%{mfx_major}.%{mfx_minor}

%files devel
%{_includedir}/vpl
%dir %{_libdir}/cmake/vpl
%{_libdir}/cmake/vpl/VPLConfig.cmake
%{_libdir}/cmake/vpl/VPLConfigVersion.cmake
%{_libdir}/libvpl.so
%{_libdir}/pkgconfig/vpl.pc

%files samples
%dir %{_datadir}/vpl
%{_datadir}/vpl/examples

%changelog
%autochangelog
