# Add option to build as static libraries (--without shared)
%bcond_without shared
# Add option to build without examples
%bcond_with examples
# Add option to build without tools
%bcond_without tools

# Avoid architecture-specific name of build-dir to fix per-arch reproducibility with doxygen
%global _vpath_builddir %{_vendor}-%{_target_os}-build

Name: dpdk
Version: 22.11.1
Release: 2%{?dist}
Epoch: 2
URL: http://dpdk.org
Source: https://fast.dpdk.org/rel/dpdk-%{version}.tar.xz

BuildRequires: meson
BuildRequires: python3-pyelftools

Summary: Set of libraries and drivers for fast packet processing

#
# Note that, while this is dual licensed, all code that is included with this
# Pakcage are BSD licensed. The only files that aren't licensed via BSD is the
# kni kernel module which is dual LGPLv2/BSD, and thats not built for fedora.
#
License: BSD and LGPLv2 and GPLv2

#
# The DPDK is designed to optimize througput of network traffic using, among
# other techniques, carefully crafted assembly instructions.  As such it
# needs extensive work to port it to other architectures.
#
ExclusiveArch: x86_64 i686 aarch64 ppc64le

BuildRequires: gcc
BuildRequires: kernel-headers, libpcap-devel, doxygen, /usr/bin/sphinx-build, zlib-devel
BuildRequires: numactl-devel
BuildRequires: rdma-core-devel
BuildRequires: openssl-devel
BuildRequires: libbpf-devel
BuildRequires: libfdt-devel
BuildRequires: libatomic
BuildRequires: libarchive-devel

%description
The Data Plane Development Kit is a set of libraries and drivers for
fast packet processing in the user space.

%package devel
Summary: Data Plane Development Kit development files
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release} python3
%if ! %{with shared}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
Requires: rdma-core-devel

%description devel
This package contains the headers and other files needed for developing
applications with the Data Plane Development Kit.

%package doc
Summary: Data Plane Development Kit API documentation
BuildArch: noarch

%description doc
API programming documentation for the Data Plane Development Kit.

%if %{with tools}
%package tools
Summary: Tools for setting up Data Plane Development Kit environment
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: kmod pciutils findutils iproute python3-pyelftools

%description tools
%{summary}
%endif

%if %{with examples}
%package examples
Summary: Data Plane Development Kit example applications
BuildRequires: libvirt-devel
BuildRequires: make

%description examples
Example applications utilizing the Data Plane Development Kit, such
as L2 and L3 forwarding.
%endif

%define sdkdir  %{_datadir}/%{name}
%define docdir  %{_docdir}/%{name}
%define incdir %{_includedir}/%{name}
%define pmddir %{_libdir}/%{name}-pmds

%pretrans -p <lua>
-- This is to clean up directories before links created
-- See https://fedoraproject.org/wiki/Packaging:Directory_Replacement

directories = {
    "/usr/share/dpdk/mk/exec-env/bsdapp",
    "/usr/share/dpdk/mk/exec-env/linuxapp"
}
for i,path in ipairs(directories) do
  st = posix.stat(path)
  if st and st.type == "directory" then
    status = os.rename(path, path .. ".rpmmoved")
    if not status then
      suffix = 0
      while not status do
        suffix = suffix + 1
        status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
      end
      os.rename(path, path .. ".rpmmoved")
    end
  end
end
%prep
%setup -q -n dpdk%(awk -F. '{ if (NF > 2) print "-stable" }' <<<%{version})-%{version}

%build
CFLAGS="$(echo %{optflags} -fcommon)" \
%meson --includedir=include/dpdk \
       -Ddrivers_install_subdir=dpdk-pmds \
       -Denable_docs=true \
       -Dmachine=generic \
%if %{with examples}
       -Dexamples=all \
%endif
%if %{with shared}
  --default-library=shared
%else
  --default-library=static
%endif

%meson_build

%install
%meson_install

%files
# BSD
%{_bindir}/dpdk-testpmd
%{_bindir}/dpdk-proc-info
%if %{with shared}
%{_libdir}/*.so.*
%{pmddir}/*.so.*
%endif

%files doc
#BSD
%{docdir}

%files devel
#BSD
%{incdir}/
%{sdkdir}
%ghost %{sdkdir}/mk/exec-env/bsdapp
%ghost %{sdkdir}/mk/exec-env/linuxapp
%if %{with tools}
%exclude %{_bindir}/dpdk-*.py
%endif
%if %{with examples}
%exclude %{sdkdir}/examples/
%endif
%if ! %{with shared}
%{_libdir}/*.a
%exclude %{_libdir}/*.so
%exclude %{pmddir}/*.so
%else
%{_libdir}/*.so
%{pmddir}/*.so
%exclude %{_libdir}/*.a
%endif
%{_libdir}/pkgconfig/libdpdk.pc
%{_libdir}/pkgconfig/libdpdk-libs.pc

%if %{with tools}
%files tools
%{_bindir}/dpdk-dumpcap
%{_bindir}/dpdk-pdump
%{_bindir}/dpdk-test
%{_bindir}/dpdk-test-*
%{_bindir}/dpdk-*.py
%endif

%if %{with examples}
%files examples
%{_bindir}/dpdk_example_*
%doc %{sdkdir}/examples
%endif

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:22.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Timothy Redaelli <tredaelli@redhat.com> - 2:22.11.1-1
- Update to 22.11.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:21.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Oct 23 2022 Jiri Olsa <jolsa@kernel.org> - 2:21.11.2-2
- Rebuild for libbpf 1.0.0

* Fri Sep 09 2022 Timothy Redaelli <tredaelli@redhat.com> - 2:21.11.2-1
- Update to 21.11.2 (CVE-2022-28199: bz2123550) (CVE-2022-2132: bz2122335)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:21.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 06 2022 Timothy Redaelli <tredaelli@redhat.com> - 2:21.11.1-2
- Support compressed firmwares (bz2104418)

* Fri Apr 29 2022 Timothy Redaelli <tredaelli@redhat.com> - 2:21.11.1-1
- Update to 21.11.1

* Wed Mar 09 2022 Timothy Redaelli <tredaelli@redhat.com> - 2:21.11-1
- Update to 21.11 (bz1991248)
- Add other dependencies in order to build all the possible PMDs

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:20.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:20.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 17 2021 Timothy Redaelli <tredaelli@redhat.com> - 2:20.11-1
- Update to 20.11

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:19.11.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Jeff Law <law@redhat.com> - 2:19.11.3-2
- Re-enable LTO

* Tue Sep 01 2020 Timothy Redaelli <tredaelli@redhat.com> - 2:19.11.3-1
- Update to latest 19.11 LTS (bz1874499)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:19.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 2020 Jeff Law <law@redhat.com> - 2:19.11.1-6
- Disable LTO

* Tue Jun 23 2020 Timothy Redaelli <tredaelli@redhat.com> - 2:19.11.1-5
- Fix missing Requires for dpdk-devel (bz1843590)

* Thu Jun 04 2020 Neil Horman <nhorman@redhat.com> - 2:19.11.1-4
- Fix broken buildrequires (bz1843590)

* Thu Jun 04 2020 Neil Horman <nhorman@redhat.com> - 2:19.11.1-3
- Enable MLX5 PMD (bz 1843590)

* Thu May 07 2020 Neil Horman <nhorman@redhat.com> - 2:19.11.1-2
- Fix error in python interpreter fixup (bz 1832416)

* Mon Apr 06 2020 Timothy Redaelli <tredaelli@redhat.com> - 2:19.11-1
- Update to latest 19.11 LTS (bz1821213)

* Fri Feb 07 2020 Timothy Redaelli <tredaelli@redhat.com> - 2:18.11.6-1
- Update to latest 18.11 LTS (bz1800510)
- Add -fcommon to CFLAGS as workaround in order to make it build on GCC 10
  (bz1799289)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:18.11.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 04 2019 Timothy Redaelli <tredaelli@redhat.com> - 2:18.11.2-5
- Pass the correct LDFLAGS to host apps (dpdk-pmdinfogen) too (bz1768405)

* Wed Sep 11 2019 Than Ngo <than@redhat.com> - 2:18.11.2-4
- Fix multilib issue, different outputs on different arches

* Mon Aug 26 2019 Neil Horman <nhorman@redhat.com> - 2:18.11.2-3
- Fix csh syntax in dpdk-sdk-x86_64.csg (bz1742942)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:18.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Timothy Redaelli <tredaelli@redhat.com> - 2:18.11.2-1
- Update to latest 18.11 LTS (bz1721056)

* Thu Feb 28 2019 Timothy Redaelli <tredaelli@redhat.com> - 2:18.11.0-1
- Update to latest LTS release (bz1684107)

* Wed Feb 13 2019 Neil Horman <nhorman@redhat.com> - 2:17.11.2-6
- Fix some FTBFS errors (1674825)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:17.11.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 27 2018 Neil Horman <nhorman@redhat.com> - 2:17.11.2-4
- Add wdiff to BuildRequires

* Thu Sep 27 2018 Neil Horman <nhorman@tuxdriver.com> - 2:17.11.2-3
- quiet annocheck complaints (bz1548404)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:17.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 24 2018 Neil Horman <nhorman@redhat.com> 2:17.11.2-1
- Update to latest 17.11 LTS (fixes bz 1571361)

* Tue Apr 10 2018 Timothy Redaelli <tredaelli@redhat.com> - 2:17.11.1-3
- Fix Requires dpdk by adding epoch

* Fri Apr 06 2018 Neil Horman <nhorman@redhat.com> 2:17.11.1-2
- Fix aarch64 build issue

* Fri Apr 06 2018 Neil Horman <nhorman@redhat.com> 2:17.11.1-1
- Update to latest LTS release for OVS

* Fri Apr 06 2018 Timothy Redaelli <tredaelli@redhat.com> -  18.02 -6
- Replace "/usr/bin/env python" with "/usr/bin/python3" (bz 1564215)

* Thu Apr 05 2018 Neil Horman <nhorman@redhat.com> - 18.02-5
- Fix compiler flag error (bz 1548404)
- Update spec file to switch to python3

* Wed Mar 14 2018 Neil Horman <nhorman@redhat.com>< -18.02-4
- Fixing date in changelog below

* Thu Mar 08 2018 Neil Horman <nhorman@redhat.com> - 18.02-3
- Fixing missing c/ldflags for pmdinfogen (bz 1548404)

* Tue Feb 27 2018 Neil Horman <nhorman@redhat.com> - 18.02-2
- Fix rpm ldflags usage (bz 1548404)

* Mon Feb 19 2018 Neil Horman <nhorman@redhat.com> - 18.02-1
- update to latest upstream

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Iryna Shcherbina <ishcherb@redhat.com> - 17.11-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Nov 30 2017 Neil Horman <nhorman@redhat.com> - 17.11-2
- Fix dangling symlinks (bz 1519322)
- Fix devtools->usertools conversion (bz 1519332)
- Fix python-pyelftools requirement (bz 1519336)

* Thu Nov 16 2017 Neil Horman <nhorman@redhat.com> - 17.11-1
- Update to latest upstream

* Wed Aug 09 2017 Neil Horman <nhorman@redhat.com> - 17.08-1
- Update to latest upstream

* Mon Jul 31 2017 Neil Horman <nhorman@redhat.com> - 17.05-2
- backport rte_eth_tx_done_cleanup map fix (#1476341)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Neil Horman <nhorman@redhat.com> - 17.05-1
- Update to latest upstream

* Fri Feb 24 2017 Neil Horman <nhorman@redhat.com> - 17-02-2
- Add python dependency (#1426561)

* Wed Feb 15 2017 Fedora Release Monitoring  <release-monitoring@fedoraproject.org> - 17.02-1
- Update to 17.02 (#1422285)

* Mon Feb 06 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 16.11-2
- Enable aarch64, ppc64le (#1419731)

* Tue Nov 15 2016 Neil Horman <nhorman@redhat.com> - 16.11-1
- Update to 16.11

* Tue Aug 02 2016 Neil Horman <nhorman@redhat.com> - 16.07-1
* Update to 16.07

* Thu Apr 14 2016 Panu Matilainen <pmatilai@redhat.com> - 16.04-1
- Update to 16.04
- Drop all patches, they're not needed anymore
- Drop linker script generation, its upstream now
- Enable vhost numa support again

* Wed Mar 16 2016 Panu Matilainen <pmatilai@redhat.com> - 2.2.0-7
- vhost numa code causes crashes, disable until upstream fixes
- Generalize target/machine/etc macros to enable i686 builds

* Tue Mar 01 2016 Panu Matilainen <pmatilai@redhat.com> - 2.2.0-6
- Drop no longer needed bnx2x patch, the gcc false positive has been fixed
- Drop no longer needed -Wno-error=array-bounds from CFLAGS
- Eliminate the need for the enic patch by eliminating second -Wall from CFLAGS
- Disable unmaintained librte_power as per upstream recommendation

* Mon Feb 15 2016 Neil Horman <nhorman@redhat.com> 2.2.0-5
- Fix ftbfs isssue (1307431)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Panu Matilainen <pmatilai@redhat.com> - 2.2.0-3
- Use a different quoting method to avoid messing up vim syntax highlighting
- A string is expected as CONFIG_RTE_MACHINE value, quote it too

* Mon Jan 25 2016 Panu Matilainen <pmatilai@redhat.com> - 2.2.0-2
- Enable librte_vhost NUMA-awareness

* Wed Jan 20 2016 Panu Matilainen <pmatilai@redhat.com> - 2.2.0-1
- Update to 2.2.0
- Establish a driver directory for automatic driver loading
- Move the unversioned pmd symlinks from libdir -devel
- Make option matching stricter in spec setconf
- Spec cleanups
- Adopt upstream standard installation layout

* Thu Oct 22 2015 Aaron Conole <aconole@redhat.com> - 2.1.0-3
- Include examples binaries
- Enable the Broadcom NetXtreme II 10Gb PMD
- Fix up linkages for the dpdk-devel package

* Wed Sep 30 2015 Aaron Conole <aconole@redhat.com> - 2.1.0-2
- Re-enable the IGB, IXGBE, I40E PMDs
- Bring the Fedora and RHEL packages more in-line.

* Wed Aug 26 2015 Neil Horman <nhorman@redhat.com> - 2.1.0-1
- Update to latest version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 06 2015 Neil Horman <nhorman@redhat.com> - 2.0.0-1
- Update to dpdk 2.0
- converted --with shared option to --without shared option

* Wed Jan 28 2015 Panu Matilainen <pmatilai@redhat.com> - 1.7.0-8
- Always build with -fPIC

* Wed Jan 28 2015 Panu Matilainen <pmatilai@redhat.com> - 1.7.0-7
- Policy compliance: move static libraries to -devel, provide dpdk-static
- Add a spec option to build as shared libraries

* Wed Jan 28 2015 Panu Matilainen <pmatilai@redhat.com> - 1.7.0-6
- Avoid variable expansion in the spec here-documents during build
- Drop now unnecessary debug flags patch
- Add a spec option to build a combined library

* Tue Jan 27 2015 Panu Matilainen <pmatilai@redhat.com> - 1.7.0-5
- Avoid unnecessary use of %%global, lazy expansion is normally better
- Drop unused destdir macro while at it
- Arrange for RTE_SDK environment + directory layout expected by DPDK apps
- Drop config from main package, it shouldn't be needed at runtime

* Tue Jan 27 2015 Panu Matilainen <pmatilai@redhat.com> - 1.7.0-4
- Copy the headers instead of broken symlinks into -devel package
- Force sane mode on the headers
- Avoid unnecessary %%exclude by not copying unpackaged content to buildroot
- Clean up summaries and descriptions
- Drop unnecessary kernel-devel BR, we are not building kernel modules

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 - John W. Linville <linville@redhat.com> - 1.7.0-2
- Use EXTRA_CFLAGS to include standard Fedora compiler flags in build
- Set CONFIG_RTE_MACHINE=default to build for least-common-denominator machines
- Turn-off build of librte_acl, since it does not build on default machines
- Turn-off build of physical device PMDs that require kernel support
- Clean-up the install rules to match current packaging
- Correct changelog versions 1.0.7 -> 1.7.0
- Remove ix86 from ExclusiveArch -- it does not build with above changes

* Thu Jul 10 2014 - Neil Horman <nhorman@tuxdriver.com> - 1.7.0-1.0
- Update source to official 1.7.0 release 

* Thu Jul 03 2014 - Neil Horman <nhorman@tuxdriver.com>
- Fixing up release numbering

* Tue Jul 01 2014 - Neil Horman <nhorman@tuxdriver.com> - 1.7.0-0.9.1.20140603git5ebbb1728
- Fixed some build errors (empty debuginfo, bad 32 bit build)

* Wed Jun 11 2014 - Neil Horman <nhorman@tuxdriver.com> - 1.7.0-0.9.20140603git5ebbb1728
- Fix another build dependency

* Mon Jun 09 2014 - Neil Horman <nhorman@tuxdriver.com> - 1.7.0-0.8.20140603git5ebbb1728
- Fixed doc arch versioning issue

* Mon Jun 09 2014 - Neil Horman <nhorman@tuxdriver.com> - 1.7.0-0.7.20140603git5ebbb1728
- Added verbose output to build

* Tue May 13 2014 - Neil Horman <nhorman@tuxdriver.com> - 1.7.0-0.6.20140603git5ebbb1728
- Initial Build

