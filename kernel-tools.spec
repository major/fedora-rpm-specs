# Much of this is borrowed from the original kernel.spec
# It needs a bunch of the macros for rawhide vs. not-rawhide builds.

# For a stable, released kernel, released_kernel should be 1. For rawhide
# and/or a kernel built from an rc or git snapshot, released_kernel should
# be 0.
%global released_kernel 1
%global baserelease 1
%global fedora_build %{baserelease}

# base_sublevel is the kernel version we're starting with and patching
# on top of -- for example, 3.1-rc7-git1 starts with a 3.0 base,
# which yields a base_sublevel of 0.
%global base_sublevel 4

%global base_major 6

## If this is a released kernel ##
%if 0%{?released_kernel}

# Do we have a -stable update to apply?
%global stable_update 0
# Set rpm version accordingly
%if 0%{?stable_update}
%global stablerev %{stable_update}
%global stable_base %{stable_update}
%endif
%global rpmversion %{base_major}.%{base_sublevel}.%{stable_update}

## The not-released-kernel case ##
%else
# The next upstream release sublevel (base_sublevel+1)
%global upstream_sublevel %(echo $((%{base_sublevel} + 1)))
%global upstream_major 6

# The rc snapshot level
%global rcrev 0
# Set rpm version accordingly
%global rpmversion %{upstream_major}.%{upstream_sublevel}.0
%endif
# Nb: The above rcrev values automagically define Patch00 and Patch01 below.

# pkg_release is what we'll fill in for the rpm Release: field
%if 0%{?released_kernel}

%global pkg_release %{fedora_build}%{?buildid}%{?dist}

%else

# non-released_kernel
%if 0%{?rcrev}
%global rctag .rc%rcrev
%else
%global rctag .rc0
%endif
%global gittag .git0
%global pkg_release 0%{?rctag}%{?gittag}.%{fedora_build}%{?buildid}%{?dist}

%endif

# The kernel tarball/base version
%global kversion %{base_major}.%{base_sublevel}
%global KVERREL %{version}-%{release}.%{_target_cpu}

# perf needs this
%undefine _strict_symbol_defs_build

BuildRequires: kmod, patch, bash, tar, git-core
BuildRequires: bzip2, xz, findutils, gzip, m4, perl-interpreter, perl(Carp), perl-devel, perl-generators, make, diffutils, gawk
BuildRequires: gcc, binutils, redhat-rpm-config, hmaccalc
BuildRequires: net-tools, hostname, bc, elfutils-devel
BuildRequires: zlib-devel binutils-devel newt-devel python3-docutils perl(ExtUtils::Embed) bison flex xz-devel
BuildRequires: audit-libs-devel glibc-devel glibc-headers glibc-static python3-devel java-devel
BuildRequires: asciidoc xmlto libcap-devel python3-setuptools
BuildRequires: openssl-devel libbabeltrace-devel
BuildRequires: libtracefs-devel libtraceevent-devel
BuildRequires: libbpf-devel
BuildRequires: clang llvm
%ifnarch s390x %{arm}
BuildRequires: numactl-devel
%endif
%ifarch aarch64
BuildRequires: opencsd-devel >= 1.0.0
%endif
%ifarch i686 x86_64
BuildRequires: libnl3-devel
%endif
BuildRequires: pciutils-devel gettext ncurses-devel
BuildConflicts: rhbuildsys(DiskFree) < 500Mb
BuildRequires: rpm-build, elfutils
BuildRequires: elfutils-debuginfod-client-devel
%{?systemd_requires}
BuildRequires: systemd

Source0: https://www.kernel.org/pub/linux/kernel/v5.x/linux-%{kversion}.tar.xz

# Sources for kernel-tools
Source2000: cpupower.service
Source2001: cpupower.config

# Here should be only the patches up to the upstream canonical Linus tree.

# For a stable release kernel
%if 0%{?stable_base}
Source5000: patch-%{base_major}.%{base_sublevel}.%{stable_base}.xz
%else
# non-released_kernel case
# These are automagically defined by the rcrev value set up
# near the top of this spec file.
%if 0%{?rcrev}
Source5000: patch-%{upstream_major}.%{upstream_sublevel}-rc%{rcrev}.xz
%endif
%endif

Patch1: kernel-tools-c99.patch

Name: kernel-tools
Summary: Assortment of tools for the Linux kernel
License: GPLv2
URL: http://www.kernel.org/
Version: %{rpmversion}
Release: %{pkg_release}
Provides:  cpupowerutils = 1:009-0.6.p1
Obsoletes: cpupowerutils < 1:009-0.6.p1
Provides:  cpufreq-utils = 1:009-0.6.p1
Provides:  cpufrequtils = 1:009-0.6.p1
Obsoletes: cpufreq-utils < 1:009-0.6.p1
Obsoletes: cpufrequtils < 1:009-0.6.p1
Obsoletes: cpuspeed < 1:1.5-16
ExcludeArch: i386 i686
Requires: kernel-tools-libs = %{version}-%{release}
%description -n kernel-tools
This package contains the tools/ directory from the kernel source
and the supporting documentation.


%package -n perf
Summary: Performance monitoring for the Linux kernel
Requires: bzip2
License: GPLv2
%description -n perf
This package contains the perf tool, which enables performance monitoring
of the Linux kernel.

%global pythonperfsum Python bindings for apps which will manipulate perf events
%global pythonperfdesc A Python module that permits applications \
written in the Python programming language to use the interface \
to manipulate perf events.

%package -n python3-perf
Summary: %{pythonperfsum}
%{?python_provide:%python_provide python3-perf}
%description -n python3-perf
%{pythonperfdesc}

%package -n kernel-tools-libs
Summary: Libraries for the kernels-tools
License: GPLv2
%description -n kernel-tools-libs
This package contains the libraries built from the tools/ directory
from the kernel source.

%package -n kernel-tools-libs-devel
Summary: Assortment of tools for the Linux kernel
License: GPLv2
Requires: kernel-tools = %{version}-%{release}
Provides:  cpupowerutils-devel = 1:009-0.6.p1
Obsoletes: cpupowerutils-devel < 1:009-0.6.p1
Requires: kernel-tools-libs = %{version}-%{release}
Provides: kernel-tools-devel
%description -n kernel-tools-libs-devel
This package contains the development files for the tools/ directory from
the kernel source.

%package -n bpftool
Summary: Inspection and simple manipulation of eBPF programs and maps
License: GPLv2
%description -n bpftool
This package contains the bpftool, which allows inspection and simple
manipulation of eBPF programs and maps.

%package -n libperf
Summary: The perf library from kernel source
License: GPLv2
%description -n libperf
This package contains the kernel source perf library.

%package -n libperf-devel
Summary: Developement files for the perf library from kernel source
License: GPLv2
%description -n libperf-devel
This package includes libraries and header files needed for development
of applications which use perf library from kernel source.

%package -n rtla
Summary: RTLA: Real-Time Linux Analysis tools 
License: GPLv2
%description -n rtla
The rtla tool is a meta-tool that includes a set of commands that
aims to analyze the real-time properties of Linux. But, instead of
testing Linux as a black box, rtla leverages kernel tracing
capabilities to provide precise information about the properties
and root causes of unexpected results.

%package -n rv
Summary: RV: Runtime Verification
License: GPLv2
%description -n rv
Runtime Verification (RV) is a lightweight (yet rigorous) method that
complements classical exhaustive verification techniques (such as model
checking and theorem proving) with a more practical approach for
complex systems.
The rv tool is the interface for a collection of monitors that aim
analysing the logical and timing behavior of Linux.


%prep
%setup -q -n kernel-%{kversion}%{?dist} -c

cd linux-%{kversion}

# This is for patching either an -rc or stable
%if 0%{?rcrev}
    xzcat %{SOURCE5000} | patch -p1 -F1 -s
%endif

%if 0%{?stable_base}
    xzcat %{SOURCE5000} | patch -p1 -F1 -s
%endif

%patch 1 -p1

# END OF PATCH APPLICATIONS

%py3_shebang_fix tools/ tools/perf/scripts/python/*.py scripts/clang-tools

###
### build
###
%build
# The kernel tools build with -ggdb3 which seems to interact badly with LTO
# causing various errors with references to discarded sections and symbol
# type errors from the LTO plugin.  Until those issues are addressed
# disable LTO
%define _lto_cflags %{nil}

cd linux-%{kversion}

%ifarch aarch64
%global perf_build_extra_opts CORESIGHT=1
%endif

%global perf_make \
  make %{?make_opts} EXTRA_CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags}" %{?cross_opts} -C tools/perf V=1 NO_PERF_READ_VDSO32=1 NO_PERF_READ_VDSOX32=1 WERROR=0 NO_LIBUNWIND=1 HAVE_CPLUS_DEMANGLE=1 NO_GTK2=1 NO_STRLCPY=1 NO_BIONIC=1 LIBBPF_DYNAMIC=1 LIBTRACEEVENT_DYNAMIC=1 %{?perf_build_extra_opts} prefix=%{_prefix} PYTHON=%{__python3}
# perf
# make sure check-headers.sh is executable
chmod +x tools/perf/check-headers.sh
%{perf_make} DESTDIR=$RPM_BUILD_ROOT all

%global tools_make \
  CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="%{__global_ldflags}" make %{?make_opts}

# cpupower
# make sure version-gen.sh is executable.
chmod +x tools/power/cpupower/utils/version-gen.sh
%{tools_make} %{?_smp_mflags} -C tools/power/cpupower CPUFREQ_BENCH=false
%ifarch %{ix86}
    pushd tools/power/cpupower/debug/i386
    %{tools_make} %{?_smp_mflags} centrino-decode powernow-k8-decode
    popd
%endif
%ifarch x86_64
    pushd tools/power/cpupower/debug/x86_64
    %{tools_make} %{?_smp_mflags} centrino-decode powernow-k8-decode
    popd
%endif
%ifarch %{ix86} x86_64
   pushd tools/power/x86/x86_energy_perf_policy/
   %{tools_make}
   popd
   pushd tools/power/x86/turbostat
   %{tools_make}
   popd
   pushd tools/power/x86/intel-speed-select
   %{tools_make}
   popd
   pushd tools/arch/x86/intel_sdsi
   %{tools_make} CFLAGS="${RPM_OPT_FLAGS}"
   popd
%endif
pushd tools/thermal/tmon/
%{tools_make}
popd
pushd tools/iio/
%{tools_make}
popd
pushd tools/gpio/
%{tools_make}
popd
# build VM tools
pushd tools/mm/
%{tools_make} slabinfo page_owner_sort
popd 
pushd tools/verification/rv/
%{tools_make}
popd
pushd tools/tracing/rtla
%{tools_make}
popd

%global bpftool_make \
  make EXTRA_CFLAGS="${RPM_OPT_FLAGS}" EXTRA_LDFLAGS="%{__global_ldflags}" DESTDIR=$RPM_BUILD_ROOT V=1

pushd tools/bpf/bpftool
%{bpftool_make}
popd
pushd tools/lib/perf
make V=1
popd

# BPF samples
%{make} %{?_smp_mflags} ARCH=$Arch V=1 M=samples/bpf/ VMLINUX_H="${RPM_VMLINUX_H}" || true

# Build the docs
pushd tools/kvm/kvm_stat/
%make_build man
popd
pushd tools/perf/Documentation/
%make_build man
popd

###
### install
###

%install

cd linux-%{kversion}
pwd
# perf tool binary and supporting scripts/binaries
%{perf_make} DESTDIR=$RPM_BUILD_ROOT lib=%{_lib} install-bin
# remove the 'trace' symlink.
rm -f %{buildroot}%{_bindir}/trace

# For both of the below, yes, this should be using a macro but right now
# it's hard coded and we don't actually want it anyway right now.
# Whoever wants examples can fix it up!

# remove examples
rm -rf %{buildroot}/usr/lib/perf/examples
# remove the stray header file that somehow got packaged in examples
rm -rf %{buildroot}/usr/lib/perf/include/bpf/

# python-perf extension
%{perf_make} DESTDIR=%{buildroot} install-python_ext

# perf man pages (note: implicit rpm magic compresses them later)
install -d %{buildroot}/%{_mandir}/man1
install -pm0644 tools/kvm/kvm_stat/kvm_stat.1 %{buildroot}/%{_mandir}/man1/
install -pm0644 tools/perf/Documentation/*.1 %{buildroot}/%{_mandir}/man1/

make -C tools/power/cpupower DESTDIR=%{buildroot} libdir=%{_libdir} mandir=%{_mandir} CPUFREQ_BENCH=false install
rm -f %{buildroot}%{_libdir}/*.{a,la}
%find_lang cpupower
mv cpupower.lang ../
%ifarch %{ix86}
    pushd tools/power/cpupower/debug/i386
    install -m755 centrino-decode %{buildroot}%{_bindir}/centrino-decode
    install -m755 powernow-k8-decode %{buildroot}%{_bindir}/powernow-k8-decode
    popd
%endif
%ifarch x86_64
    pushd tools/power/cpupower/debug/x86_64
    install -m755 centrino-decode %{buildroot}%{_bindir}/centrino-decode
    install -m755 powernow-k8-decode %{buildroot}%{_bindir}/powernow-k8-decode
    popd
%endif
chmod 0755 %{buildroot}%{_libdir}/libcpupower.so*
mkdir -p %{buildroot}%{_unitdir} %{buildroot}%{_sysconfdir}/sysconfig
install -m644 %{SOURCE2000} %{buildroot}%{_unitdir}/cpupower.service
install -m644 %{SOURCE2001} %{buildroot}%{_sysconfdir}/sysconfig/cpupower
%ifarch %{ix86} x86_64
   mkdir -p %{buildroot}%{_mandir}/man8
   pushd tools/power/x86/x86_energy_perf_policy
   %{tools_make} DESTDIR=%{buildroot} install
   popd
   pushd tools/power/x86/turbostat
   %{tools_make} DESTDIR=%{buildroot} install
   popd
   pushd tools/power/x86/intel-speed-select
   %{tools_make} CFLAGS+="-D_GNU_SOURCE -Iinclude -I/usr/include/libnl3" DESTDIR=%{buildroot} install
   popd
   pushd tools/arch/x86/intel_sdsi
   %{tools_make} DESTDIR=%{buildroot} install
   popd
%endif
pushd tools/thermal/tmon
%{tools_make} INSTALL_ROOT=%{buildroot} install
popd
pushd tools/iio
%{tools_make} DESTDIR=%{buildroot} install
popd
pushd tools/gpio
%{tools_make} DESTDIR=%{buildroot} install
popd
# install VM tools
pushd tools/mm/
install -m755 slabinfo %{buildroot}%{_bindir}/slabinfo
install -m755 page_owner_sort %{buildroot}%{_bindir}/page_owner_sort
popd
pushd tools/verification/rv/
%{tools_make} DESTDIR=%{buildroot} install
popd
pushd tools/tracing/rtla/
%{tools_make} DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_bindir}/hwnoise
rm -f %{buildroot}%{_bindir}/osnoise
rm -f %{buildroot}%{_bindir}/timerlat
(cd %{buildroot}

        ln -sf rtla ./%{_bindir}/hwnoise
        ln -sf rtla ./%{_bindir}/osnoise
        ln -sf rtla ./%{_bindir}/timerlat
)
popd
pushd tools/kvm/kvm_stat
%{tools_make} INSTALL_ROOT=%{buildroot} install-tools
popd
pushd tools/bpf/bpftool
%{bpftool_make} prefix=%{_prefix} bash_compdir=%{_sysconfdir}/bash_completion.d/ mandir=%{_mandir} install doc-install
popd
pushd tools/lib/perf
make DESTDIR=%{buildroot} prefix=%{_prefix} libdir=%{_libdir} V=1 install install_headers
popd

# install bpf samples
pushd samples/bpf
install -d %{buildroot}%{_libexecdir}/ksamples/bpf
find -type f -executable -exec install -m755 {} %{buildroot}%{_libexecdir}/ksamples/bpf \;
install -m755 *.sh %{buildroot}%{_libexecdir}/ksamples/bpf
# test_lwt_bpf.sh compiles test_lwt_bpf.c when run; this works only from the
# kernel tree. Just remove it.
rm %{buildroot}%{_libexecdir}/ksamples/bpf/test_lwt_bpf.sh
install -m644 *_kern.o %{buildroot}%{_libexecdir}/ksamples/bpf || true
install -m644 tcp_bpf.readme %{buildroot}%{_libexecdir}/ksamples/bpf
popd


###
### scripts
###

%ldconfig_scriptlets -n kernel-tools-libs

%post -n kernel-tools
%systemd_post cpupower.service

%preun -n kernel-tools
%systemd_preun cpupower.service

%postun
%systemd_postun cpupower.service

%files -n perf
%{_bindir}/perf
%{_libdir}/libperf-jvmti.so
%{_libexecdir}/perf-core
%{_datadir}/perf-core/
%{_mandir}/man[1-8]/perf*
%{_sysconfdir}/bash_completion.d/perf
%doc linux-%{kversion}/tools/perf/Documentation/examples.txt
%license linux-%{kversion}/COPYING
%{_docdir}/perf-tip/tips.txt

%files -n python3-perf
%license linux-%{kversion}/COPYING
%{python3_sitearch}/*

%files -n kernel-tools -f cpupower.lang
%{_bindir}/cpupower
%{_datadir}/bash-completion/completions/cpupower
%ifarch %{ix86} x86_64
%{_bindir}/centrino-decode
%{_bindir}/powernow-k8-decode
%endif
%{_unitdir}/cpupower.service
%{_mandir}/man[1-8]/cpupower*
%config(noreplace) %{_sysconfdir}/sysconfig/cpupower
%ifarch %{ix86} x86_64
%{_bindir}/x86_energy_perf_policy
%{_mandir}/man8/x86_energy_perf_policy*
%{_bindir}/turbostat
%{_mandir}/man8/turbostat*
%{_bindir}/intel-speed-select
%{_sbindir}/intel_sdsi
%endif
%{_bindir}/tmon
%{_bindir}/iio_event_monitor
%{_bindir}/iio_generic_buffer
%{_bindir}/lsiio
%{_bindir}/lsgpio
%{_bindir}/gpio-hammer
%{_bindir}/gpio-event-mon
%{_bindir}/gpio-watch
%{_mandir}/man1/kvm_stat*
%{_bindir}/kvm_stat
%{_bindir}/page_owner_sort
%{_bindir}/slabinfo

%license linux-%{kversion}/COPYING

%files -n kernel-tools-libs
%{_libdir}/libcpupower.so.0
%{_libdir}/libcpupower.so.0.0.1
%license linux-%{kversion}/COPYING

%files -n kernel-tools-libs-devel
%{_libdir}/libcpupower.so
%{_includedir}/cpufreq.h
%{_includedir}/cpuidle.h
%{_includedir}/powercap.h

%files -n bpftool
%{_sbindir}/bpftool
%{_sysconfdir}/bash_completion.d/bpftool
%{_mandir}/man8/bpftool-btf.8.gz
%{_mandir}/man8/bpftool-cgroup.8.gz
%{_mandir}/man8/bpftool-gen.8.gz
%{_mandir}/man8/bpftool-iter.8.gz
%{_mandir}/man8/bpftool-link.8.gz
%{_mandir}/man8/bpftool-map.8.gz
%{_mandir}/man8/bpftool-net.8.gz
%{_mandir}/man8/bpftool-prog.8.gz
%{_mandir}/man8/bpftool-perf.8.gz
%{_mandir}/man8/bpftool-struct_ops.8.gz
%{_mandir}/man8/bpftool-feature.8.gz
%{_mandir}/man8/bpftool.8.gz
%{_libexecdir}/ksamples
%license linux-%{kversion}/COPYING

%files -n libperf
%{_libdir}/libperf.so.0
%{_libdir}/libperf.so.0.0.1
%license linux-%{kversion}/COPYING

%files -n libperf-devel
%{_libdir}/libperf.a
%{_libdir}/libperf.so
%{_libdir}/pkgconfig/libperf.pc
%{_includedir}/internal/*.h
%{_includedir}/perf/bpf_perf.h
%{_includedir}/perf/core.h
%{_includedir}/perf/cpumap.h
%{_includedir}/perf/perf_dlfilter.h
%{_includedir}/perf/event.h
%{_includedir}/perf/evlist.h
%{_includedir}/perf/evsel.h
%{_includedir}/perf/mmap.h
%{_includedir}/perf/threadmap.h
%{_mandir}/man3/libperf.3.gz
%{_mandir}/man7/libperf-counting.7.gz
%{_mandir}/man7/libperf-sampling.7.gz
%{_docdir}/libperf/examples/sampling.c
%{_docdir}/libperf/examples/counting.c
%{_docdir}/libperf/html/libperf.html
%{_docdir}/libperf/html/libperf-counting.html
%{_docdir}/libperf/html/libperf-sampling.html
%license linux-%{kversion}/COPYING

%files -n rtla
%{_bindir}/rtla
%{_bindir}/hwnoise
%{_bindir}/osnoise
%{_bindir}/timerlat
%{_mandir}/man1/rtla-hwnoise.1.gz
%{_mandir}/man1/rtla-osnoise-hist.1.gz
%{_mandir}/man1/rtla-osnoise-top.1.gz
%{_mandir}/man1/rtla-osnoise.1.gz
%{_mandir}/man1/rtla-timerlat-hist.1.gz
%{_mandir}/man1/rtla-timerlat-top.1.gz
%{_mandir}/man1/rtla-timerlat.1.gz
%{_mandir}/man1/rtla.1.gz

%files -n rv
%{_bindir}/rv
%{_mandir}/man1/rv-list.1.gz
%{_mandir}/man1/rv-mon-wip.1.gz
%{_mandir}/man1/rv-mon-wwnr.1.gz
%{_mandir}/man1/rv-mon.1.gz
%{_mandir}/man1/rv.1.gz

%changelog
* Mon Jun 26 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.4.0-1
- Linux v6.4

* Tue Jun 20 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.4.0-0.rc7.git0.1
- Linux v6.4-rc7

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 6.4.0-0.rc6.git0.2
- Rebuilt for Python 3.12

* Mon Jun 12 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.4.0-0.rc6.git0.1
- Linux v6.4-rc6

* Mon Jun 05 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.4.0-0.rc5.git0.1
- Linux v6.4-rc5

* Mon May 22 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.4.0-0.rc3.git0.1
- Linux v6.4-rc3

* Mon May 15 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.4.0-0.rc2.git0.1
- Linux v6.4-rc2

* Mon May 08 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.4.0-0.rc1.git0.1
- Linux v6.4-rc1

* Mon Apr 24 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.3.0-1
- Linux v6.3
- Add rv subpackage

* Tue Apr 18 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.3.0-0.rc7.git0.1
- Linux v6.3-rc7

* Wed Apr 05 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.3.0-0.rc5.git0.2
- Bump for build against new libtracefs

* Mon Apr 03 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.3.0-0.rc5.git0.1
- Linux v6.3-rc5

* Tue Mar 28 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.3.0-0.rc4.git0.1
- Linux v6.3-rc4

* Mon Mar 20 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.3.0-0.rc3.git0.1
- Linux v6.3-rc3

* Mon Mar 13 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.3.0-0.rc2.git0.1
- Linux v6.3-rc2

* Mon Mar 06 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.3.0-0.rc1.git0.1
- Linux v6.3-rc1

* Mon Feb 20 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.2.0-1
- Linux v6.2.0

* Mon Feb 13 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.2.0-0.rc8.git0.1
- Linux v6.2-rc8

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.1.0-1
- Linux v6.1.0

* Mon Dec 05 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.1.0-0.rc8.git0.1
- Linux v6.1-rc8

* Mon Nov 28 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.1.0-0.rc7.git0.1
- Linux v6.1-rc7

* Mon Nov 21 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.1.0-0.rc6.git0.1
- Linux v6.1-rc6

* Mon Nov 14 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.1.0-0.rc5.git0.1
- Linux v6.1-rc5

* Fri Nov 11 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.1.0-0.rc4.git0.2
- Bump for libbpf-1.0 build

* Mon Nov 07 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.1.0-0.rc4.git0.1
- Linux v6.1-rc4

* Wed Nov 02 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.1.0-0.rc3.git0.1
- Linux v6.1-rc3

* Mon Oct 24 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.1.0-0.rc2.git0.1
- Linux v6.1-rc2

* Mon Oct 17 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.0.0-0.rc1.git0.1
- Linux v6.1-rc1

* Mon Oct 03 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.0.0-1
- Linux v6.0

* Mon Sep 26 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.0.0-0.rc7.git0.1
- Linux v6.0-rc7

* Mon Sep 19 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.0.0-0.rc6.git0.1
- Linux v6.0-rc6

* Mon Sep 05 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.0.0-0.rc4.git0.1
- Linux v6.0-rc4

* Mon Aug 29 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.0.0-0.rc3.git0.1
- Linux v6.0-rc3

* Mon Aug 22 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.0.0-0.rc2.git0.1
- Linux v6.0-rc2

* Mon Aug 15 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.0.0-0.rc1.git0.1
- Linux v6.0-rc1

* Mon Aug 01 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.19.0-1
- Linux v5.19.0

* Tue Jul 26 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.19.0-0.rc8.git0.1
- Linux v5.19-rc8

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.19.0-0.rc7.git0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.19.0-0.rc7.git0.1
- Linux v5.19-rc7

* Mon Jul 11 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.19.0-0.rc6.git0.1
- Linux v5.19-rc6

* Mon Jul 04 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.19.0-0.rc5.git0.1
- Linux v5.19-rc5

* Mon Jun 27 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.19.0-0.rc4.git0.1
- Linux v5.19-rc4

* Mon Jun 20 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.19.0-0.rc3.git0.1
- Linux v5.19-rc3

* Tue Jun 14 2022 Justin M. Forbes <jforbes@fedoraproject.org>
- Some spec cleanups
- Build rtla as a subpackage

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 5.19.0-0.rc2.git0.2
- Rebuilt for Python 3.11

* Mon Jun 13 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.19.0-0.rc2.git0.1
- Linux v5.19-rc2

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 5.19.0-0.rc1.git0.2
- Rebuilt for Python 3.11

* Mon Jun 06 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.19.0-0.rc1.git0.1
- Linux v5.19-rc1

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 5.18.0-2
- Perl 5.36 rebuild

* Mon May 23 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.18.0-1
- Linux v5.18.0

* Mon May 16 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.18.0-0.rc7.git0.1
- Linux v5.18-rc7

* Mon May 09 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.18.0-0.rc6.git0.1
- Linux v5.18-rc6

* Mon May 02 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.18.0-0.rc5.git0.1
- Linux v5.18-rc5

* Mon Apr 25 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.18.0-0.rc4.git0.1
- Linux v5.18-rc4

* Mon Apr 18 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.18.0-0.rc3.git0.1
- Linux v5.18-rc3

* Mon Apr 11 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.18.0-0.rc2.git0.1
- Linux v5.18-rc2
- Stop building for i686
- Start building the intel_sdsi utility

* Mon Apr 04 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.18.0-0.rc1.git0.1
- Linux v5.18-rc1

* Mon Mar 21 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.17.0-1
- Linux v5.17.0

* Mon Mar 14 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.17.0-0.rc8.git0.1
- Linux v5.17-rc8

* Mon Mar 07 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.17.0-0.rc7.git0.1
- Linux v5.17-rc7

* Mon Feb 28 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.17.0-0.rc6.git0.1
- Linux v5.17-rc6

* Mon Feb 21 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.17.0-0.rc5.git0.1
- Linux v5.17-rc5
- Temporarily stop libtraceevent dynamic until I can figure out why i686 doesn't build.
- Make coresight aarch64 only.

* Wed Feb 16 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.17.0-0.rc4.git0.2
- Bump for rebuild with libtraceevent update

* Mon Feb 14 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.17.0-0.rc4.git0.1
- Linux v5.17-rc4

* Mon Feb 07 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.17.0-0.rc3.git0.1
- Linux v5.17-rc3

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 5.17.0-0.rc2.git0.2
- Rebuilt for java-17-openjdk as system jdk

* Sun Jan 30 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.17.0-0.rc2.git0.1
- Linux v5.17-rc2

* Mon Jan 24 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.17.0-0.rc1.git0.1
- Linux v5.17-rc1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.16.0-1
- Linux v5.16

* Mon Jan 03 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.16.0-0.rc8.git0.1
- Linux v5.16-rc8

* Mon Dec 27 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.16.0-0.rc7.git0.1
- Linux v5.16-rc7

* Mon Dec 20 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.16.0-0.rc6.git0.1
- Linux v5.16-rc6

* Mon Dec 13 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.16.0-0.rc5.git0.1
- Linux v5.16-rc5

* Mon Dec 06 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.16.0-0.rc4.git0.1
- Linux v5.16-rc4

* Mon Nov 15 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.16.0-0.rc1.git0.1
- Linux v5.16-rc1

* Mon Nov 01 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.15.0-1
- Linux v5.15

* Tue Oct 26 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.15.0-0.rc7.git0.1
- Linux v5.15-rc7

* Mon Oct 18 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.15.0-0.rc6.git0.1
- Linux v5.15-rc6

* Mon Oct 11 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.15.0-0.rc5.git0.1
- Linux v5.15-rc5

* Mon Oct 04 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.15.0-0.rc4.git0.1
- Linux v5.15-rc4

* Mon Oct 04 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.15.0-0.rc3.git0.1
- Linux v5.15-rc3

* Mon Sep 20 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.15.0-0.rc2.git0.1
- Linux v5.15-rc2

* Mon Sep 13 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.15.0-0.rc1.git0.1
- Linux v5.15-rc1

* Mon Aug 30 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.14.0-1
- Linux v5.14.0
