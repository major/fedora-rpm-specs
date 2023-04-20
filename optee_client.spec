Name:      optee_client
Version:   3.21.0
Release:   1%{?dist}
Summary:   OP-TEE Client API and supplicant
License:   BSD
URL:       https://www.trustedfirmware.org/
Source:    https://github.com/OP-TEE/optee_client/archive/%{version}/%{name}-%{version}.tar.gz

# TrustZone is an ARM specific technology
ExclusiveArch: aarch64
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: libuuid-devel
BuildRequires: make

%description
OP-TEE is an open source Trusted Execution Enviroment (TEE) implementing the
Arm TrustZone technology.

The optee client provides the Linux userspace client APIs and supplicant for
communicating with OPTEE in the Arm TrustZone TEE.

%package devel
Summary:        Development files for optee_client
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development file for optee_client

%prep
%autosetup -p1

%build
%cmake -DRPMB_EMU=0
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%license LICENSE
%{_sbindir}/tee-supplicant
%{_libdir}/libckteec.so.0*
%{_libdir}/libseteec.so.0*
%{_libdir}/libteeacl.so.0*
%{_libdir}/libteec.so.1*

%files devel
%{_includedir}/ck_debug.h
%{_includedir}/pkcs11*.h
%{_includedir}/se_tee.h
%{_includedir}/tee*.h
%{_libdir}/libckteec.so
%{_libdir}/libseteec.so
%{_libdir}/libteeacl.so
%{_libdir}/libteec.so

%changelog
* Tue Apr 18 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 3.21.0-1
- Update to 3.21.0

* Thu Feb 03 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 3.16.0-1
- Initial package
