Name:    dfx-mgr
Version: 2025.2
Release: 1%{?dist}
Summary: A tool for managing programable logic accelerators
License: MIT
URL:     https://github.com/Xilinx/dfx-mgr
Source:  %{url}/archive/refs/tags/xilinx_v%{version}.tar.gz#/%{name}-xilinx_v%{version}.tar.gz

ExcludeArch: %{ix86}
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: libdfx-devel
BuildRequires: libdrm-devel
BuildRequires: systemd-devel

%description
DFX-MGR provides infrastructure to abstract configuration and
hardware resource management for dynamic deployment of Xilinx
based accelerators (AKA FPGA) across different platforms.

%package devel
Summary: Development files for using PL (programable logic)
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: glib2-devel

%description devel
This package contains the header and static library files for
development applications using PL (programable logic).


%prep
%autosetup -p1 -n %{name}-xilinx_v%{version}


%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build


%install
%cmake_install


%files
%license LICENSE
%doc README.md
%{_bindir}/accel*
%{_bindir}/dfx-mgr*
%{_bindir}/load_accel*
%{_libdir}/libdfx-mgr.so.*

%files devel
%{_libdir}/libdfx-mgr.a
%{_libdir}/libdfx-mgr.so


%changelog
* Mon Dec 01 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 2025.2-1
- Update to 2025.2, update source URL

* Sun May 18 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 2024.2.0-1
- Initial package
