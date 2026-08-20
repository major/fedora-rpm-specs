Name:		quic-teec
Version:	1.0.2
Release:	%autorelease
Summary:	Qualcomm qcomtee userspace library

License:	BSD-3-Clause
URL:		https://github.com/qualcomm/quic-teec
Source:		%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/qualcomm/quic-teec/pull/30
Patch0:		30.patch

ExclusiveArch:	%{arm64}

BuildRequires:	cmake >= 3.1
BuildRequires:	gcc
BuildRequires:	pkgconfig(libcbor)

%description
QCOM-TEE library provides an interface for communication to the Qualcomm
Trusted Execution Environment (QTEE) via the QCOM-TEE driver registered with 
the Linux TEE subsystem.

Library supports Object-based IPC with QTEE for user-space clients via the 
TEE_IOC_OBJECT_INVOKE IOCTL from the Linux TEE subsystem.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
applications that use %{name}.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%doc README.md
%{_libdir}/libqcomtee.so.*

%files devel
%{_includedir}/qcomtee_*.h
%{_libdir}/libqcomtee.so
%{_libdir}/pkgconfig/qcomtee.pc

%changelog
%autochangelog
