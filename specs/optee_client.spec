Name:      optee_client
Version:   4.4.0
Release:   2%{?dist}
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
%{_libdir}/libteec.so.2*

%files devel
%{_includedir}/ck_debug.h
%{_includedir}/pkcs11*.h
%{_includedir}/se_tee.h
%{_includedir}/tee*.h
%{_libdir}/pkgconfig/tee*.pc
%{_libdir}/libckteec.so
%{_libdir}/libseteec.so
%{_libdir}/libteeacl.so
%{_libdir}/libteec.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 21 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 4.4.0-1
- Update to 4.4.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 4.3.0-1
- Update to 4.3.0

* Fri Apr 12 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 4.2.0-1
- Update to 4.2.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 4.1.0-1
- Update to 4.1.0

* Thu Nov 02 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 4.0.0-1
- Update to 4.0.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 3.22.0-1
- Update to 3.22.0

* Tue Apr 18 2023 Peter Robinson <pbrobinson@fedoraproject.org> - 3.21.0-1
- Update to 3.21.0

* Thu Feb 03 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 3.16.0-1
- Initial package
