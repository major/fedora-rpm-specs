Name:           libvpl-tools
Version:        1.5.0
Release:        %autorelease
Summary:        Intel Video Processing Library (Intel VPL) Tools
License:        MIT
URL:            https://intel.github.io/libvpl
ExclusiveArch:  x86_64

Source0:        https://github.com/intel/libvpl-tools/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-use-system-gtest.patch
# https://github.com/intel/libvpl-tools/pull/1
Patch1:         %{name}-versioned-library.patch
Patch2:         %{name}-gcc13.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  libvpl-devel >= 2.11.0
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gtkmm-4.0)
BuildRequires:  pkgconfig(libdrm) >= 2.4.91
BuildRequires:  pkgconfig(libva) >= 1.2
BuildRequires:  pkgconfig(libva-drm) >= 1.2
BuildRequires:  pkgconfig(libva-x11) >= 1.10.0
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.15
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-present)

%description
Intel Video Processing Library (Intel VPL) tools provide access to hardware
accelerated video decode, encode, and frame processing capabilities on Intel
GPUs from the command line.

The tools require the Intel VPL base library and a runtime library installed.
Current runtime implementations:

- Intel VPL GPU Runtime for use on Intel Iris Xe graphics and newer
- Intel Media SDK for use on legacy Intel graphics

%package devel
Summary:	Development files for %{name}
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains library and header files for development

%package libs
Summary:	%{name} runtime library
Requires:	%{name} = %{version}-%{release}

%description libs
Runtime library for %{name}

%prep
%autosetup -p1

# delete bundled googletest
rm -rf ext/*

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_TESTS=ON \
    -DTOOLS_ENABLE_OPENCL=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md third-party-programs.txt
%{_bindir}/system_analyzer
%{_bindir}/val-surface-sharing
%{_bindir}/vpl-import-export
%{_bindir}/vpl-inspect
%{_bindir}/sample_decode
%{_bindir}/sample_vpp
%{_bindir}/sample_encode
%{_bindir}/sample_multi_transcode
%{_bindir}/metrics_monitor

%files devel
%dir %{_includedir}/cttmetrics
%{_includedir}/cttmetrics/cttmetrics.h
%{_includedir}/cttmetrics/cttmetrics_utils.h
%{_libdir}/libcttmetrics.so
%{_libdir}/libvpl_wayland.so

%files libs
%{_libdir}/libcttmetrics.so.*
%{_libdir}/libvpl_wayland.so.*

%changelog
%autochangelog
