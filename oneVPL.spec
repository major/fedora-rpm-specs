%global mfx_major 2
%global mfx_minor 10

Name:           oneVPL
Version:        2023.4.0
Release:        3%{?dist}
Summary:        oneAPI Video Processing Library
License:        MIT
URL:            https://www.intel.com/content/www/us/en/developer/tools/oneapi/onevpl.html
ExclusiveArch:  x86_64

Source0:        https://github.com/intel/libvpl/archive/v%{version}/%{name}-%{version}.tar.gz
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

Recommends:     intel-mediasdk
Recommends:     oneVPL-intel-gpu

# The Python bindings were removed in 2023.0.0
Obsoletes:      python3-%{name} < %{version}-%{release}

%description
The oneAPI Video Processing Library (oneVPL) provides a single video processing
API for encode, decode, and video processing that works across a wide range of
accelerators.

The base package is limited to the dispatcher and samples. To use oneVPL for
video processing you need to install at least one implementation. Current
implementations:

- oneVPL-intel-gpu for use on Intel Xe graphics and newer
- intel-mediasdk for use on legacy Intel graphics

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package        samples
Summary:        Sample programs and source code for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

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
%{_bindir}/system_analyzer
%{_libdir}/libvpl.so.%{mfx_major}
%{_libdir}/libvpl.so.%{mfx_major}.%{mfx_minor}
%dir %{_libdir}/vpl
%{_libdir}/vpl/libvpl_wayland.so

%files devel
%{_includedir}/vpl
%{_libdir}/cmake/vpl
%{_libdir}/libvpl.so
%{_libdir}/pkgconfig/vpl.pc

%files samples
%{_bindir}/sample_decode
%{_bindir}/sample_encode
%{_bindir}/sample_multi_transcode
%{_bindir}/sample_vpp
%{_bindir}/vpl-inspect
%{_datadir}/vpl

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Dec 14 2023 Simone Caronni <negativo17@gmail.com> - 2023.4.0-2
- Drop patch, adjust file section.

* Mon Dec 11 2023 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 2023.4.0-1
- Update to 2023.4.0

* Tue Oct 03 2023 Simone Caronni <negativo17@gmail.com> - 2023.3.1-1
- Update to 2023.3.1.

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2023.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 22 2023 Nicolas Chauvet <kwizart@gmail.com> - 2023.1.3-2
- Rebuilt for libva

* Mon Mar 13 2023 Adam Williamson <awilliam@redhat.com> - 2023.1.3-1
- Update to 2023.1.3
- Drop Python bindings (removed upstream)
- Fix install path for config files (#2177912)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

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
