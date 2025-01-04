# Add option to build as static libraries (--without shared)
%bcond_without shared
# Add option to build without examples
%bcond_with examples
# Add option to build without tools
%bcond_without tools

# Avoid architecture-specific name of build-dir to fix per-arch reproducibility with doxygen
%global _vpath_builddir %{_vendor}-%{_target_os}-build

Name: dpdk
Version: 24.11.1
Release: %autorelease
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
# Automatically converted from old format: BSD and LGPLv2 and GPLv2 - review is highly recommended.
License: LicenseRef-Callaway-BSD AND LicenseRef-Callaway-LGPLv2 AND GPL-2.0-only

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
%ifnarch %{ix86}
BuildRequires: libbpf-devel
%endif
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
%autosetup -p1 -n dpdk%(awk -F. '{ if (NF > 2) print "-stable" }' <<<%{version})-%{version}

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

# Taken from debian/rules
rm -f %{buildroot}%{docdir}/html/.buildinfo
rm -f %{buildroot}%{docdir}/html/objects.inv
rm -rf %{buildroot}%{docdir}/html/.doctrees
find %{buildroot}%{_mandir}/ -type f -a ! -iname "*rte_*" -delete

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
%{_mandir}
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
%ifnarch %{ix86}
%{_bindir}/dpdk-dumpcap
%{_bindir}/dpdk-pdump
%endif
%{_bindir}/dpdk-graph
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
%autochangelog
