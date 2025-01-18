Summary:        Open Programmable Acceleration Engine (OPAE) SDK
Name:           opae
Vendor:         Intel Corporation
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD

Version:        2.13.0
%define opae_release 3
%define patch_level 1
Release:        %{opae_release}.%{patch_level}%{?dist}

URL:            https://github.com/OPAE/%{name}-sdk
Source0:        https://github.com/OPAE/opae-sdk/archive/refs/tags/%{version}-%{opae_release}.tar.gz

Group:          Development/Libraries
ExclusiveArch:  x86_64

BuildRequires:  cli11-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  hwloc-devel
BuildRequires:  json-c-devel
BuildRequires:  libedit-devel
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  numactl-devel
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  python3-jsonschema
BuildRequires:  python3-pip
BuildRequires:  python3-pybind11
BuildRequires:  python3-pyyaml
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  rpm-build
BuildRequires:  spdlog-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  tbb-devel


%description
Open Programmable Acceleration Engine (OPAE) is a software framework
for managing and accessing programmable accelerators (FPGAs).
Its main parts are:

* OPAE Software Development Kit (OPAE SDK) (this package)
* OPAE Linux driver for Intel(R) PAC with Arria(R) 10 GX FPGA
* Intel(R) PAC N6000/D5005, Silicom FPGA SmartNIC N5010 Series,
* Intel FPGA Programmable Acceleration Card N6000

OPAE SDK is a collection of libraries and tools to facilitate the
development of software applications and accelerators using OPAE.
It provides a library implementing the OPAE C API for presenting a
streamlined and easy-to-use interface for software applications to
discover, access, and manage FPGA devices and accelerators using
the OPAE software stack.

%package devel
Summary:    OPAE headers, sample source, and documentation
Requires:   opae
Requires:   libuuid-devel, %{name}%{?_isa} = %{version}-%{release}
Requires:   openssl-devel

%description devel
OPAE headers, tools, sample source, and documentation


%package extra-tools
Summary:    Additional OPAE tools
Requires:   opae-devel

%description extra-tools
This package contains OPAE extra tools binaries, 
software tools for accelerators


%prep
%setup -q -n %{name}-sdk-%{version}-%{opae_release}

# No Werror's please
sed -i -e 's@-Werror @ @' cmake/modules/OPAECompiler.cmake

%build
%cmake -DCMAKE_INSTALL_PREFIX=/usr \
       -DOPAE_PRESERVE_REPOS=ON \
       -DOPAE_BUILD_PYTHON_DIST=ON \
       -DOPAE_BUILD_FPGABIST=ON

# Tell pip install to use pre-installed build dependencies, instead of
# trying to download and install the build dependencies, which fails
# when building without network access, e.g., using Fedora's mock.
#
# https://github.com/OFS/meta-ofs/issues/1
# https://pip.pypa.io/en/stable/cli/pip_install/#cmdoption-no-build-isolation
#
# PIP_NO_CACHE_DIR and PIP_NO_BUILD_ISOLATION behave opposite to how they read
# https://github.com/pypa/pip/issues/5735
export PIP_NO_BUILD_ISOLATION=off
%cmake_build


%install
mkdir -p %{buildroot}%{_datadir}/opae
cp RELEASE_NOTES.md %{buildroot}%{_datadir}/opae/RELEASE_NOTES.md
cp LICENSE %{buildroot}%{_datadir}/opae/LICENSE
cp COPYING %{buildroot}%{_datadir}/opae/COPYING

export PIP_NO_BUILD_ISOLATION=off
%cmake_install

# Make rpmlint happy about install permissions

for file in %{buildroot}%{python3_sitelib}/opae/admin/tools/{fpgaflash,fpgaotsu,fpgaport,fpgasupdate,ihex2ipmi,rsu,super_rsu,bitstream_info,opaevfio,pci_device,fpgareg,n5010tool}.py; do
   chmod a+x $file
done

for file in %{buildroot}%{python3_sitelib}/ethernet/{hssicommon,hssiloopback,hssimac,hssistats}.py; do
   chmod a+x $file
done

for file in %{buildroot}%{python3_sitearch}/opae/diag/{common,fecmode,fpgadiag,fpgalpbk,fpgamac,fpgastats,fvlbypass,mactest,mux}.py; do
   chmod a+x $file
done

for file in %{buildroot}%{python3_sitearch}/opae/fpga/tools/opae_mem.py; do
   chmod a+x $file
done

for file in %{buildroot}%{python3_sitelib}/packager/tools/{afu_json_mgr,packager}.py; do
   chmod a+x $file
done

for file in %{buildroot}%{python3_sitelib}/platmgr/tools/{afu_platform_config,afu_platform_info,afu_synth_setup,rtl_src_config}.py; do
   chmod a+x $file
done

for file in %{buildroot}%{python3_sitelib}/uio/ofs_uio.py; do
   chmod a+x $file
done

chmod a+x %{buildroot}%{_usr}/src/opae/cmake/modules/*.cmake
chmod a+x %{buildroot}%{_usr}/lib/opae-%{version}/modules/*.cmake

%files
%dir %{_datadir}/opae
%doc %{_datadir}/opae/RELEASE_NOTES.md
%license %{_datadir}/opae/LICENSE
%license %{_datadir}/opae/COPYING

%config(noreplace) %{_sysconfdir}/opae/opae.cfg*
%config(noreplace) %{_sysconfdir}/sysconfig/fpgad.conf*

%{_bindir}/fpgaconf
%{_bindir}/fpgad
%{_bindir}/fpgainfo
%{_bindir}/fpgasupdate
%{_bindir}/pci_device
%{_bindir}/rsu

%{_libdir}/libbitstream.so.*
%{_libdir}/libfpgad-api.so.*
%{_libdir}/libmml-srv.so.*
%{_libdir}/libmml-stream.so.*
%{_libdir}/libofs_cpeng.so.*
%{_libdir}/libofs.so.*
%{_libdir}/libopae-c++-nlb.so.*
%{_libdir}/libopae-c.so.*
%{_libdir}/libopae-c++-utils.so.*
%{_libdir}/libopae-cxx-core.so.*
%{_libdir}/libopaemem.so.*
%{_libdir}/libopaeuio.so.*
%{_libdir}/libopaevfio.so.*
%{_libdir}/opae/libboard_a10gx.so
%{_libdir}/opae/libboard_c6100.so
%{_libdir}/opae/libboard_cmc.so
%{_libdir}/opae/libboard_d5005.so
%{_libdir}/opae/libboard_jtag_pci_dk.so
%{_libdir}/opae/libboard_n3000.so
%{_libdir}/opae/libboard_n5010.so
%{_libdir}/opae/libboard_n6000.so
%{_libdir}/opae/libfpgad-vc.so
%{_libdir}/opae/libfpgad-xfpga.so
%{_libdir}/opae/libmodbmc.so
%{_libdir}/opae/libopae-u.so
%{_libdir}/opae/libopae-v.so
%{_libdir}/opae/libxfpga.so
%{_unitdir}/fpgad.service

%{python3_sitelib}/opae.admin*
%{python3_sitelib}/opae/admin*

%post
%systemd_post fpgad.service
/sbin/ldconfig

%preun
%systemd_preun fpgad.service

%files devel
%dir %{_includedir}/opae
%dir %{_usr}/src/opae

%{_bindir}/afu_json_mgr
%{_bindir}/afu_platform_config
%{_bindir}/afu_platform_info
%{_bindir}/afu_synth_setup
%{_bindir}/bitstreaminfo
%{_bindir}/fpgaflash
%{_bindir}/fpgametrics
%{_bindir}/fpgaotsu
%{_bindir}/fpgaport
%{_bindir}/fpgareg
%{_bindir}/hello_cxxcore
%{_bindir}/hello_events
%{_bindir}/hello_fpga
%{_bindir}/hssiloopback
%{_bindir}/hssimac
%{_bindir}/hssistats
%{_bindir}/mmlink
%{_bindir}/n5010-ctl
%{_bindir}/n5010-test
%{_bindir}/n5010tool
%{_bindir}/nlb0
%{_bindir}/nlb3
%{_bindir}/nlb7
%{_bindir}/object_api
%{_bindir}/opae-mem
%{_bindir}/opaeuiotest
%{_bindir}/opaevfio
%{_bindir}/opaevfiotest
%{_bindir}/pac_hssi_config.py
%{_bindir}/packager
%{_bindir}/PACSign
%{_bindir}/regmap-debugfs
%{_bindir}/rtl_src_config
%{_bindir}/super-rsu
%{_bindir}/userclk
%{_bindir}/vabtool
%{_includedir}/mock/opae_std.h
%{_includedir}/opae/cxx/core.h
%{_includedir}/opae/cxx/core/*.h
%{_includedir}/opae/*.h
%{_includedir}/opae/plugin/*.h
%{_libdir}/libbitstream.so
%{_libdir}/libfpgad-api.so
%{_libdir}/libmml-srv.so
%{_libdir}/libmml-stream.so
%{_libdir}/libofs_cpeng.so
%{_libdir}/libofs.so
%{_libdir}/libopae-c++-nlb.so
%{_libdir}/libopae-c.so
%{_libdir}/libopae-c++-utils.so
%{_libdir}/libopae-cxx-core.so
%{_libdir}/libopaemem.so
%{_libdir}/libopaeuio.so
%{_libdir}/libopaevfio.so
%{_prefix}/lib/opae-%{version}
%{_usr}/share/opae/*
%{_usr}/src/opae/argsfilter/argsfilter.c
%{_usr}/src/opae/argsfilter/argsfilter.h
%{_usr}/src/opae/cmake/modules/*
%{_usr}/src/opae/samples/hello_events/hello_events.c
%{_usr}/src/opae/samples/hello_fpga/hello_fpga.c
%{_usr}/src/opae/samples/n5010-ctl/n5010-ctl.c
%{_usr}/src/opae/samples/n5010-test/n5010-test.c
%{_usr}/src/opae/samples/object_api/object_api.c

%{python3_sitearch}/libvfio*
%{python3_sitearch}/opae.fpga*
%{python3_sitearch}/opae/fpga*
%{python3_sitelib}/ethernet*
%{python3_sitelib}/hssi_ethernet*
%{python3_sitelib}/packager*
%{python3_sitelib}/pacsign*
%{python3_sitelib}/platmgr*

%files extra-tools

%{_bindir}/bist
%{_bindir}/bist_app
%{_bindir}/bist_app.py
%{_bindir}/bist_common.py
%{_bindir}/bist_def.py
%{_bindir}/bist_dma.py
%{_bindir}/bist_nlb0.py
%{_bindir}/bist_nlb3.py
%{_bindir}/cxl_hello_fpga
%{_bindir}/cxl_host_exerciser
%{_bindir}/cxl_mem_tg
%{_bindir}/dummy_afu
%{_bindir}/fecmode
%{_bindir}/fpgabist
%{_bindir}/fpgadiag
%{_bindir}/fpga_dma_N3000_test
%{_bindir}/fpga_dma_test
%{_bindir}/fpgalpbk
%{_bindir}/fpgamac
%{_bindir}/fpgastats
%{_bindir}/fvlbypass
%{_bindir}/host_exerciser
%{_bindir}/hps
%{_bindir}/hssi
%{_bindir}/mactest
%{_bindir}/mem_tg
%{_bindir}/ofs.uio
%{_bindir}/opae.io

%{python3_sitearch}/opae.diag*
%{python3_sitearch}/opae/diag*
%{python3_sitearch}/opae.io*
%{python3_sitearch}/opae/io*
%{python3_sitearch}/pyopaeuio*
%{python3_sitelib}/ofs.uio*
%{python3_sitelib}/uio*

%changelog
* Thu Jan 16 2025 Tom Rix <Tom.Rix@amd.com> - 2.13.0-3.1
- Update to 2.13.0-3

* Tue Nov 26 2024 František Zatloukal <fzatlouk@redhat.com> - 2.12.0-4.1.6
- Rebuilt for spdlog 1.15.0

* Wed Nov 6 2024 Tom Rix <Tom.Rix@amd.com> - 2.12.0-4.1.5
- Rebuild for json-c

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.12.0-4.1.4
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-4.1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2.12.0-4.1.2
- Rebuilt for Python 3.13

* Tue May 21 2024 František Zatloukal <fzatlouk@redhat.com> - 2.12.0-4.1.1
- Rebuilt for spdlog 1.14.1

* Mon Feb 26 2024 Peter Colberg <peter.colberg@intel.com> - 2.12.0-4.1
- Update tarball to 2.12.0-4
- Add numactl-devel and python3-wheel to BuildRequires
- Set PIP_NO_BUILD_ISOLATION=off during build and install
- Drop redundant install of cmake modules, opae samples, and python modules

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-1.1.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-1.1.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 2.2.0-1.1.6
- Rebuilt for TBB 2021.11

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-1.1.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2.2.0-1.1.4
- Rebuilt due to spdlog 1.12 update.

* Sat Jul 01 2023 Python Maint <python-maint@redhat.com> - 2.2.0-1.1.3
- Rebuilt for Python 3.12

* Wed Jun 28 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2.2.0-1.1.2
- Rebuilt due to fmt 10 update.

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 2.2.0-1.1.1
- Rebuilt for Python 3.12

* Fri Mar 3 2023 Tom Rix <trix@redhat.com> - 2.2.0-1.1
- Update tarball to 2.2.0-1
- glob the cmake files to install
- disable a broken python module

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 03 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 2.1.0-2.2
- Rebuilt due to spdlog update.

* Thu Aug 18 2022 Tom Rix <trix@redat.com> - 2.1.0-2.1
- Upstate tarball to 2.1.0-2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.1.0-1.1
- Rebuilt for Python 3.11

* Tue Mar 15 2022 The OPAE Dev Team <opae@lists.01.org> - 2.1.0-1
- Update OPAE spec file and tarball generation script.
- Added support to Intel FPGA DFL Driver that has been upstreamed to Linux Kernel v5.7-5.17.
- Added support to Intel FPGA PCIe N6000/D5005/N3000 series.
- Removed OPAE-SIM from OPAE-SDK.
- Various bug fixes
- Various Static code scan bug fixes.
- Updated OPAE documentation.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 04 2021 Tom Rix <trix@redhat.com> - 2.0.0-2.7
- Disable pacsign, the user user of the local libcrypto
- Remove the whole libcrypto directory in prep
- Remove python3-sphinx, doxygen from BuildRequires

* Fri Dec 03 2021 Tom Rix <trix@redhat.com> - 2.0.0-2.6
- Fix Source0 url
- Remove git from BuildRequires
- Remove libcrypto.so in prep stage

* Fri Dec 03 2021 Miro Hroncok <mhroncok@redhat.com> - 2.0.0-2.5
- Do not provide libcrypto.so.1.1()(64bit)
- Fixes rhbz#2028852

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Bjorn Esser <besser82@fedoraproject.org> - 2.0.0-2.2
- Rebuild for versioned symbols in json-c

* Thu Jul 08 2021 Bjorn Esser <besser82@fedoraproject.org> - 2.0.0-2.1
- Fix automatic bump of the release tag
- Add a patch to replace the deprecated pthread_yield function
- Whitespace cleanup
- Use new-style cmake macros

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-2.2
- Rebuilt for Python 3.10

* Mon May 10 2021 Jonathan Wakely <jwakely@redhat.com> - 2.0.0-2.1
- Rebuilt for removed libstdc++ symbols (#1937698)

* Mon Dec 14 2020 The OPAE Dev Team <opae@lists.01.org> - 2.0.0-2
- Update OPAE spec file and tarball generation script
- Fix build errors

* Thu Sep 17 2020 Ananda Ravuri <ananda.ravuri@intel.com> 2.0.0-1
- Various Static code scan bug fixes
- Added support to FPGA Linux kernel Device Feature List (DFL) driver.
- Added support to PAC card N3000 series.
- Added PACSign, bitstream_info, fpgasudpate, rsu, fpgaotsu, fpgaport  python tools.
- Added ethernet tools for PAC card N3000.
- Various bug fixes
- Various memory leak fixes.
- Various Static code scan bug fixes
- Added python3 support.
- OPAE USMG API are deprecated.
- Updated OPAE documentation.

* Tue Dec 17 2019 Korde Nakul <nakul.korde@intel.com> 1.4.0-1
- Added support to FPGA Linux kernel Device Feature List (DFL) driver patch set2.
- Increased test cases and test coverage
- Various bug fixes
- Various compiler warning fixes
- Various memory leak fixes
- Various Static code scan bug fixes
- Added new FPGA MMIO API to write 512 bits
