%global mfx_ver_major 2
%global mfx_ver_minor 13

Name:           intel-vpl-gpu-rt
Version:        24.4.4
Release:        1%{?dist}
Summary:        Intel Video Processing Library (Intel VPL) GPU Runtime
License:        MIT
URL:            https://www.intel.com/content/www/us/en/developer/tools/oneapi/onevpl.html
ExclusiveArch:  x86_64

Source0:        https://github.com/intel/vpl-gpu-rt/archive/intel-onevpl-%{version}/intel-onevpl-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libvpl-devel >= 2.11.0
BuildRequires:  pkgconfig(libdrm) >= 2.4
# Should be >= 1.9 but fails with libva < 2.12 (VAProcFilterCap3DLUT):
# https://github.com/oneapi-src/oneVPL-intel-gpu/issues/198
BuildRequires:  pkgconfig(libva) >= 1.12

Requires:       libvpl%{?_isa} >= 1:2.10.1

Obsoletes:      oneVPL-intel-gpu < %{version}-%{release}
Provides:       oneVPL-intel-gpu = %{version}-%{release}

%description
Intel oneVPL GPU Runtime is a Runtime implementation of oneVPL API for Intel Gen
GPUs. Runtime provides access to hardware-accelerated video decode, encode and
filtering.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n vpl-gpu-rt-intel-onevpl-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_libdir}/libmfx-gen.so.1.%{mfx_ver_major}
%{_libdir}/libmfx-gen.so.1.%{mfx_ver_major}.%{mfx_ver_minor}
%dir %{_libdir}/libmfx-gen
%{_libdir}/libmfx-gen/enctools.so

%files devel
%{_libdir}/libmfx-gen.so
%{_libdir}/pkgconfig/libmfx-gen.pc

%changelog
* Fri Dec 27 2024 Simone Caronni <negativo17@gmail.com> - 24.4.4-1
- Update to 24.4.4.

* Thu Nov 28 2024 Simone Caronni <negativo17@gmail.com> - 24.3.4-1
- Update to 24.3.4.

* Tue Sep 10 2024 Simone Caronni <negativo17@gmail.com> - 24.3.3-1
- Update to 24.3.3.

* Mon Aug 05 2024 Simone Caronni <negativo17@gmail.com> - 24.3.1-1
- Update to 24.3.1.

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 04 2024 Simone Caronni <negativo17@gmail.com> - 24.2.4-1
- Update to 24.2.4.

* Thu May 23 2024 Simone Caronni <negativo17@gmail.com> - 24.2.3-1
- Update to 24.2.3.

* Sat May 04 2024 Simone Caronni <negativo17@gmail.com> - 24.2.2-2
- Require libvpl 2.11.0 for building.

* Sat May 04 2024 Simone Caronni <negativo17@gmail.com> - 24.2.2-1
- Rename from oneVPL-intel-gpu.
- Update to 24.2.2.
