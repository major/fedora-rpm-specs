Name:    libdfx
Version: 2025.2
Release: 2%{?dist}
Summary: A lightweight user-space library that provides APIs to configure the PL
License: MIT
URL:     https://github.com/Xilinx/libdfx
Source:  %{url}/archive/refs/tags/xilinx_v%{version}.tar.gz#/%{name}-xilinx_v%{version}.tar.gz

ExcludeArch: %{ix86}
BuildRequires: cmake
BuildRequires: gcc-g++

%description
The library is a lightweight user-space library that provides APIs
for application to configure the PL (programable logic) AKA FPGA.

%package devel
Summary: Development files for using PL (programable logic)
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header and static library files for
development applications using PL (programable logic).

%package static
Summary: Static libraries for using PL (programable logic)
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description static
This package contains the static library files for %{name}
for building PL (programable logic) applications.

%prep
%autosetup -p1 -n %{name}-xilinx_v%{version}


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%license LICENSE.md
%{_libdir}/libdfx.so.1*

%files devel
%{_includedir}/libdfx.h
%{_libdir}/libdfx.so

%files static
%{_libdir}/libdfx.a


%changelog
* Mon Dec 01 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 2025.2-2
- Don't build for i686

* Mon Dec 01 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 2025.2.0-1
- Update to 2025.2, update source URL

* Tue May 27 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 2024.2.0-2
- Split out static library from devel

* Sun May 18 2025 Peter Robinson <pbrobinson@fedoraproject.org> - 2024.2.0-1
- Initial package
