Name:           oneVPL
Version:        2022.2.2
Release:        1%{?dist}
Summary:        oneAPI Video Processing Library
License:        MIT
URL:            https://www.intel.com/content/www/us/en/developer/tools/oneapi/onevpl.html
ExclusiveArch:  x86_64

Source0:        https://github.com/oneapi-src/oneVPL/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-system-analyzer.patch

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
BuildRequires:  python3dist(pybind11)
BuildRequires:  python3-devel

Recommends:     intel-mediasdk
Recommends:     oneVPL-cpu
Recommends:     oneVPL-intel-gpu

%description
The oneAPI Video Processing Library (oneVPL) provides a single video processing
API for encode, decode, and video processing that works across a wide range of
accelerators.

The base package is limited to the dispatcher and samples. To use oneVPL for
video processing you need to install at least one implementation. Current
implementations:

- oneVPL-cpu for use on CPU
- oneVPL-intel-gpu for use on Intel Xe graphics and newer
- Media SDK for use on legacy Intel graphics

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package -n python3-%{name}
Summary:    Python3 interface to %{name}

%description -n python3-%{name}
This package contains python3 interfaces to %{name}.

%package        samples
Summary:        Sample programs and source code for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    samples
This package contains sample programs and applications that use %{name}.

%prep
%autosetup -p1

%build
%cmake \
    -DBUILD_PYTHON_BINDING:BOOL=ON \
    -DPYTHON_INSTALL_DIR:STRING=%{python3_sitearch}
%cmake_build

%install
%cmake_install

find %{buildroot} -name '*.la' -delete

# Let RPM pick up documents in the files section
rm -fr %{buildroot}%{_datadir}/vpl/licensing

%files
%license LICENSE
%doc README.md CONTRIBUTING.md third-party-programs.txt
%dir %{_prefix}/etc/vpl
%{_prefix}/etc/vpl/vars.sh
%dir %{_prefix}/etc/modulefiles
%{_prefix}/etc/modulefiles/vpl
%dir %{_libdir}/vpl
%{_libdir}/vpl/libvpl_wayland.so
%{_bindir}/system_analyzer
%{_libdir}/libvpl.so.2
%{_libdir}/libvpl.so.2.7

%files devel
%{_includedir}/vpl
%dir %{_libdir}/cmake/vpl
%{_libdir}/cmake/vpl/VPLConfig.cmake
%{_libdir}/cmake/vpl/VPLConfigVersion.cmake
%{_libdir}/libvpl.so
%{_libdir}/pkgconfig/vpl.pc

%files -n python3-%{name}
%{python3_sitearch}/*

%files samples
%{_bindir}/decvpp_tool
%{_bindir}/sample_decode
%{_bindir}/sample_encode
%{_bindir}/sample_multi_transcode
%{_bindir}/sample_vpp
%{_bindir}/vpl-inspect
%dir %{_datadir}/vpl
%{_datadir}/vpl/examples

%changelog
* Wed Aug 24 2022 Simone Caronni <negativo17@gmail.com> - 2022.2.2-1
- Update to 2022.2.2.
- Patch system_analyzer so it works without devel subpackage installed.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Simone Caronni <negativo17@gmail.com> - 2022.1.5-1
- Update to 2022.1.5.

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2022.1.3-2
- Rebuilt for Python 3.11

* Wed May 25 2022 Simone Caronni <negativo17@gmail.com> - 2022.1.3-1
- Update to 2022.1.3.

* Tue Apr 26 2022 Simone Caronni <negativo17@gmail.com> - 2022.1.1-1
- Update to 2022.1.1.
- Recommend implementations (at least one must be installed).

* Sat Mar 19 2022 Simone Caronni <negativo17@gmail.com> - 2022.1.0-1
- Update to 2022.1.0.

* Sun Mar 13 2022 Simone Caronni <negativo17@gmail.com> - 2022.0.6-1
- Update to 2022.0.6.

* Wed Mar 02 2022 Simone Caronni <negativo17@gmail.com> - 2022.0.5-2
- Rebuild for updated libva.

* Wed Mar 02 2022 Simone Caronni <negativo17@gmail.com> - 2022.0.5-1
- Update to 2022.0.5.

* Tue Feb 08 2022 Simone Caronni <negativo17@gmail.com> - 2022.0.4-1
- Update to 2022.0.4.

* Mon Feb 07 2022 Simone Caronni <negativo17@gmail.com> - 2022.0.0-2
- Enable Python binding.

* Sat Feb 05 2022 Simone Caronni <negativo17@gmail.com> - 2022.0.0-1
- First build.
