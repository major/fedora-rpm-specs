%global py_prefix python3
%global py_binary %{py_prefix}

# CRIU's parasite/restorer code (criu/pie/) is compiled with its own CFLAGS
# that already disable hardening (-fno-stack-protector, -U_FORTIFY_SOURCE,
# -D_FORTIFY_SOURCE=0, -nostdlib). Standard RHEL hardening flags (PIE, RELRO,
# FORTIFY_SOURCE, stack protector) only affect the main criu binary and libs.
#
# Annobin remains disabled because its instrumentation gets injected into
# every compilation unit including parasite code, and there is no per-target
# way to exclude it through the Makefile.
%undefine _annotated_build

Name: criu
Version: 4.3.1
Release: %autorelease
Summary: Tool for Checkpoint/Restore in User-space
License: GPL-2.0-only AND LGPL-2.1-only AND MIT
URL: http://criu.org/
Source0: https://github.com/checkpoint-restore/criu/archive/v%{version}/criu-%{version}.tar.gz

# Add protobuf-c as a dependency.
# We use this patch because the protobuf-c package name
# in RPM and DEB is different.
Patch99: criu.pc.patch

Source5: criu-tmpfiles.conf

BuildRequires: gcc
BuildRequires: systemd
BuildRequires: libnet-devel
BuildRequires: protobuf-devel protobuf-c-devel %{py_prefix}-devel libnl3-devel libcap-devel
BuildRequires: %{py_prefix}-pip
BuildRequires: %{py_prefix}-setuptools
BuildRequires: (%{py_prefix}-wheel if %{py_prefix}-setuptools < 71)
BuildRequires: %{py_prefix}-protobuf
BuildRequires: asciidoctor
BuildRequires: perl-interpreter
BuildRequires: libselinux-devel
BuildRequires: gnutls-devel
BuildRequires: libdrm-devel
BuildRequires: libuuid-devel
BuildRequires: nftables-devel
BuildRequires: lz4-devel
# Checkpointing containers with a tmpfs requires tar
Recommends: tar
%if 0%{?fedora}
BuildRequires: libbsd-devel
%endif
BuildRequires: make

# user-space and kernel changes are only available for x86_64, arm,
# ppc64le, aarch64 and s390x
# https://bugzilla.redhat.com/show_bug.cgi?id=902875
ExclusiveArch: x86_64 %{arm} ppc64le aarch64 s390x riscv64

%description
criu is the user-space part of Checkpoint/Restore in User-space
(CRIU), a project to implement checkpoint/restore functionality for
Linux in user-space.

%package devel
Summary: Header files and libraries for %{name}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libs = %{version}-%{release}

%description devel
This package contains header files and libraries for %{name}.

%package libs
Summary: Libraries for %{name}
Requires: %{name} = %{version}-%{release}

%description libs
This package contains the libraries for %{name}

%package amdgpu-plugin
Summary: AMD GPU plugin for %{name}
Requires: %{name} = %{version}-%{release}

%description amdgpu-plugin
This package contains the AMD GPU plugin for %{name}

%package cuda-plugin
Summary: CUDA plugin for %{name}
Requires: %{name} = %{version}-%{release}

%description cuda-plugin
This package contains the CUDA plugin for %{name}

%package -n %{py_prefix}-%{name}
%{?python_provide:%python_provide %{py_prefix}-%{name}}
Summary: Python bindings for %{name}
Requires: %{py_prefix}-protobuf

%description -n %{py_prefix}-%{name}
%{py_prefix}-%{name} contains Python bindings for %{name}.

%package -n crit
Summary: CRIU image tool
Requires: %{py_prefix}-%{name} = %{version}-%{release}
Requires: %{py_prefix}-lz4

%description -n crit
crit is a tool designed to decode CRIU binary dump files and show
their content in human-readable form.

%package -n criu-ns
Summary: Tool to run CRIU in different namespaces
Requires: %{name} = %{version}-%{release}

%description -n criu-ns
The purpose of the criu-ns wrapper script is to enable restoring a process
tree that might require a specific PID that is already used on the system.
This script can help to workaround the so called "PID mismatch" problem.

%prep
%setup -q
%patch -P 99 -p1

%build
# This package calls LD directly without specifying the LTO plugins.  Until
# that is fixed, disable LTO.
%define _lto_cflags %{nil}

# CRIU's nmk build system calls ld directly for intermediate partial linking
# (ld -r). RHEL LDFLAGS contain -specs= options that only gcc understands;
# raw ld rejects them. Create a wrapper that strips -specs= for direct ld
# calls. The final criu binary link uses gcc (CC), not ld, so it still gets
# full hardening (-pie, -z relro, -z now) from the spec files.
mkdir -p %{_builddir}/bin
cat > %{_builddir}/bin/ld << 'LDWRAPPER'
#!/bin/sh
for arg do
  shift
  case "$arg" in -specs=*) continue ;; esac
  set -- "$@" "$arg"
done
exec /usr/bin/ld "$@"
LDWRAPPER
chmod +x %{_builddir}/bin/ld

# %{?_smp_mflags} does not work
CFLAGS+="%{optflags}" make V=1 WERROR=0 LD=%{_builddir}/bin/ld PREFIX=%{_prefix} RUNDIR=/run/criu PYTHON=%{py_binary} PLUGINDIR=%{_libdir}/criu NETWORK_LOCK_DEFAULT=NETWORK_LOCK_NFTABLES
make V=1 WERROR=0 PREFIX=%{_prefix} PLUGINDIR=%{_libdir}/criu amdgpu_plugin
make docs V=1


%install
sed -e "s,--upgrade --ignore-installed,--no-index --no-deps -v --no-build-isolation,g" -i lib/Makefile -i crit/Makefile
make install-criu LD=%{_builddir}/bin/ld DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} LIBDIR=%{_libdir} BINDIR=%{_bindir} SBINDIR=%{_sbindir}
make install-lib LD=%{_builddir}/bin/ld DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} LIBDIR=%{_libdir} PYTHON=%{py_binary} PIPFLAGS="--no-build-isolation --no-index --no-deps --progress-bar off --upgrade --ignore-installed"
make install-amdgpu_plugin LD=%{_builddir}/bin/ld DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} LIBDIR=%{_libdir} PLUGINDIR=%{_libdir}/criu
make install-cuda_plugin LD=%{_builddir}/bin/ld DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} LIBDIR=%{_libdir} PLUGINDIR=%{_libdir}/criu
make install-crit LD=%{_builddir}/bin/ld DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} LIBDIR=%{_libdir}  BINDIR=%{_bindir} SBINDIR=%{_sbindir} PYTHON=%{py_binary} PIPFLAGS="--no-build-isolation --no-index --no-deps --progress-bar off --upgrade --ignore-installed"
make install-man LD=%{_builddir}/bin/ld DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} LIBDIR=%{_libdir}
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/compel.1

mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -d -m 0755 %{buildroot}/run/%{name}/

# remove static lib
rm -f $RPM_BUILD_ROOT%{_libdir}/libcriu.a

%files
%{_sbindir}/%{name}
%doc %{_mandir}/man8/criu.8*
%{_libexecdir}/%{name}
%dir /run/%{name}
%{_tmpfilesdir}/%{name}.conf
%doc README.md COPYING

%files devel
%{_includedir}/criu
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files libs
%{_libdir}/*.so.*

%files amdgpu-plugin
%{_libdir}/%{name}/amdgpu_plugin.so
%doc %{_mandir}/man1/criu-amdgpu-plugin.1*

%files cuda-plugin
%{_libdir}/%{name}/cuda_plugin.so
%doc plugins/cuda/README.md

%files -n %{py_prefix}-%{name}
%{python3_sitelib}/pycriu*

%files -n crit
%{_bindir}/crit
%{python3_sitelib}/crit-%{version}.dist-info/
%{python3_sitelib}/crit
%doc %{_mandir}/man1/crit.1*

%files -n criu-ns
%{_sbindir}/criu-ns
%doc %{_mandir}/man1/criu-ns.1*

%post
%tmpfiles_create %{name}.conf

%changelog
%autochangelog
