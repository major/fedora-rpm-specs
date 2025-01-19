Name:		ipmctl
Version:	03.00.00.0468
Release:	8%{?dist}
Summary:	Utility for managing Intel Optane DC persistent memory modules
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/intel/ipmctl
Source:		https://github.com/intel/ipmctl/archive/v%{version}/%{name}-%{version}_with_edk2.tar.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=1628752
ExclusiveArch:	x86_64

Requires:	libipmctl%{?_isa} = %{version}-%{release}
BuildRequires:	pkgconfig(libndctl)
BuildRequires:	cmake
BuildRequires:	python3
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	asciidoctor
BuildRequires:	systemd
Obsoletes:	ixpdimm-cli < 01.00.00.3000

Patch1: ipmctl-remove-uefi-spec-code.patch
Patch2: ipmctl-remove-always-true-conditional.patch
Patch3: ipmctl_remove_unused_functions.patch

%description
Utility for managing Intel Optane DC persistent memory modules
Supports functionality to:
Discover DCPMMs on the platform.
Provision the platform memory configuration.
View and update the firmware on DCPMMs.
Configure data-at-rest security on DCPMMs.
Track health and performance of DCPMMs.
Debug and troubleshoot DCPMMs.

%prep
%setup -q -n %{name}-%{version}
%patch -P1 -p1 
%patch -P2 -p1 
%patch -P3 -p1 

%package -n libipmctl
Summary:	Library for Intel DCPMM management
Obsoletes:	ixpdimm_sw < 01.00.00.3000
Obsoletes:	libixpdimm-common < 01.00.00.3000
Obsoletes:	libixpdimm-core < 01.00.00.3000
Obsoletes:	libixpdimm-cli < 01.00.00.3000
Obsoletes:	libixpdimm-cim < 01.00.00.3000
Obsoletes:	libixpdimm < 01.00.00.3000
Obsoletes:	ixpdimm-data < 01.00.00.3000

%description -n libipmctl
An Application Programming Interface (API) library for managing Intel Optane DC
persistent memory modules.

%package -n libipmctl-devel
Summary:	Development packages for libipmctl
Requires:	libipmctl%{?_isa} = %{version}-%{release}
Obsoletes:	ixpdimm-devel < 01.00.00.3000
Obsoletes:	ixpdimm_sw-devel < 01.00.00.3000

%description -n libipmctl-devel
API for development of Intel Optane DC persistent memory management utilities.

%build
%cmake -DBUILDNUM=%{version} -DCMAKE_INSTALL_PREFIX=/ \
    -DLINUX_PRODUCT_NAME=%{name} \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir} \
    -DCMAKE_INSTALL_BINDIR=%{_bindir} \
    -DCMAKE_INSTALL_DATAROOTDIR=%{_datarootdir} \
    -DCMAKE_INSTALL_MANDIR=%{_mandir} \
    -DCMAKE_INSTALL_LOCALSTATEDIR=%{_localstatedir} \
    -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
    -DRELEASE=ON \
    -DRPM_BUILD=ON
%cmake_build

%install
%{!?_cmake_version: cd build}
%cmake_install

%post -n libipmctl -p /sbin/ldconfig

%postun -n libipmctl -p /sbin/ldconfig

%files -n ipmctl
%{_bindir}/ipmctl
%{_mandir}/man1/ipmctl*

%files -n libipmctl
%{_libdir}/libipmctl.so.5*
%dir %{_datadir}/doc/ipmctl
%doc %{_datadir}/doc/ipmctl/ipmctl_default.conf
%doc %{_datadir}/doc/ipmctl/LICENSE
%doc %{_datadir}/doc/ipmctl/edk2_License.txt
%doc %{_datadir}/doc/ipmctl/thirdpartynotice.txt
%config(noreplace) %{_datadir}/ipmctl/ipmctl.conf
%dir %{_localstatedir}/log/ipmctl
%config(noreplace) %{_sysconfdir}/logrotate.d/ipmctl

%files -n libipmctl-devel
%{_libdir}/libipmctl.so
%{_includedir}/nvm_types.h
%{_includedir}/nvm_management.h
%{_includedir}/export_api.h
%{_includedir}/NvmSharedDefs.h
%{_libdir}/pkgconfig/libipmctl.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 03.00.00.0468-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 03.00.00.0468-7
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 03.00.00.0468-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 03.00.00.0468-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 03.00.00.0468-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 03.00.00.0468-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 03.00.00.0468-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 28 2022 Steven Pontsler <steven.pontsler@intel.com> - 03.00.00.0468-1
- Release 03.00.00.0468

* Thu Aug 25 2022 Steven Pontsler <steven.pontsler@intel.com> - 03.00.00.0453-3
- Add patch to remove unused functions that have compilation issues

* Wed Aug 24 2022 Steven Pontsler <steven.pontsler@intel.com> - 03.00.00.0453-2
- Add patch to remove conditional that is always true

* Fri Aug 12 2022 Steven Pontsler <steven.pontsler@intel.com> - 03.00.00.0453-1
- Release 03.00.00.0453

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 02.00.00.3885-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 01 2022 Steven Pontsler <steven.pontsler@intel.com> - 02.00.00.3885-3
- Add patch files to clear up compiler warnings for Fedora 36 Mass Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 02.00.00.3885-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 24 2021 Steven Pontsler <steven.pontsler@intel.com> - 02.00.00.3885-1
- Release 02.00.00.3885

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 02.00.00.3878-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 13 2021 Steven Pontsler <steven.pontsler@intel.com> - 02.00.00.3878-1
- Release 02.00.00.3878

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 02.00.00.3833-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 03 2020 Steven Pontsler <steven.pontsler@intel.com> - 02.00.00.3833-2
- Correct date in change log

* Thu Dec 03 2020 Steven Pontsler <steven.pontsler@intel.com> - 02.00.00.3833-1
- Release 02.00.00.3833

* Wed Nov 04 2020 Steven Pontsler <steven.pontsler@intel.com> - 02.00.00.3830-1
- Release 02.00.00.3830

* Thu Oct 15 2020 Jeff Law <law@redhat.com> - 02.00.00.3825-2
- Fix mismatched array sizes for argument to os_mkdir caught by gcc-11

* Wed Sep 30 2020 Steven Pontsler <steven.pontsler@intel.com> - 02.00.00.3825-1
- Release 02.00.00.3825

* Sun Aug 30 2020 Steven Pontsler <steven.pontsler@intel.com> - 02.00.00.3809-2
- Change to use cmake macros

* Sun Aug 30 2020 Steven Pontsler <steven.pontsler@intel.com> - 02.00.00.3809-1
- Release 02.00.00.3809

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 02.00.00.3791-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 02.00.00.3791-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Juston Li <juston.li@intel.com> - 02.00.00.3791-1
- Release 02.00.00.3791

* Tue Jun 30 2020 Jeff Law <law@redhat.com> - 02.00.00.3764-2
- Fix latent type mismatch problem exposed by LTO

* Fri May 01 2020 Juston Li <juston.li@intel.com> - 02.00.00.3764-1
- Release 02.00.00.3764

* Fri Apr 24 2020 Juston Li <juston.li@intel.com> - 02.00.00.3759-1
- Inital 2.x Release 02.00.00.3759
- Removed ipmctl-monitor
- Removed libsafec dependency

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 01.00.00.3474-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed May 02 2018 Juston Li <juston.li@intel.com> - 01.00.00.3000-1
- initial spec
