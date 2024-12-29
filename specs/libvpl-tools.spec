Name:           libvpl-tools
Version:        1.3.0
Release:        1%{?dist}
Summary:        Intel Video Processing Library (Intel VPL) Tools
License:        MIT
URL:            https://intel.github.io/libvpl
ExclusiveArch:  x86_64

Source0:        https://github.com/intel/libvpl-tools/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-use-system-gtest.patch
# https://github.com/intel/libvpl-tools/pull/1
Patch1:         %{name}-versioned-library.patch

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
* Fri Dec 27 2024 Simone Caronni <negativo17@gmail.com> - 1.3.0-1
- Update to 1.3.0.

* Tue Sep 10 2024 Simone Caronni <negativo17@gmail.com> - 1.2.0-1
- Update to 1.2.0.

* Sun Aug 25 2024 Simone Caronni <negativo17@gmail.com> - 1.1.0-1
- Update to 1.1.0.

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue May 28 2024 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 1.0.0-4
- Devel and Libs subpackages added

* Fri May 17 2024 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 1.0.0-3
- Bundled googletest removed

* Sat May 04 2024 Simone Caronni <negativo17@gmail.com> - 1.0.0-2
- Require libvpl 2.11.0 for building.

* Sat May 04 2024 Simone Caronni <negativo17@gmail.com> - 1.0.0-1
- First build.
