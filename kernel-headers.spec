# For a stable, released kernel, released_kernel should be 1. For rawhide
# and/or a kernel built from an rc or git snapshot, released_kernel should
# be 0.
%global released_kernel 1

# define buildid .local

# baserelease defines which build revision of this kernel version we're
# building.  We used to call this fedora_build, but the magical name
# baserelease is matched by the rpmdev-bumpspec tool, which you should use.
#
# NOTE: baserelease must be > 0 or bad things will happen if you switch
#       to a released kernel (released version will be < rc version)
#
# For non-released -rc kernels, this will be appended after the rcX and
# gitX tags, so a 3 here would become part of release "0.rcX.gitX.3"
#
%global baserelease 1
%global fedora_build %{baserelease}

# base_sublevel is the kernel version we're starting with and patching
# on top of -- for example, 3.1-rc7-git1 starts with a 3.0 base,
# which yields a base_sublevel of 0.
%define base_sublevel 5

## If this is a released kernel ##
%if 0%{?released_kernel}

# Do we have a -stable update to apply?
%define stable_update 0
# Set rpm version accordingly
%if 0%{?stable_update}
%define stablerev %{stable_update}
%define stable_base %{stable_update}
%endif
%define pkgversion 6.%{base_sublevel}.%{stable_update}

## The not-released-kernel case ##
%else
# The next upstream release sublevel (base_sublevel+1)
%define upstream_sublevel %(echo $((%{base_sublevel} + 1)))
# The rc snapshot level
%global rcrev 0
# The git snapshot level
%define gitrev 0
# Set rpm version accordingly
%define pkgversion 6.%{upstream_sublevel}.0
%endif

# pkg_release is what we'll fill in for the rpm Release: field
%if 0%{?released_kernel}

%define srcversion %{fedora_build}%{?buildid}

%else

# non-released_kernel
%if 0%{?rcrev}
%define rctag .rc%rcrev
%else
%define rctag .rc0
%endif
%if 0%{?gitrev}
%define gittag .git%gitrev
%else
%define gittag .git0
%endif
%define srcversion 0%{?rctag}%{?gittag}.%{fedora_build}%{?buildid}

%endif

%define pkg_release %{?srcversion}%{?dist}

# This package doesn't contain any binary, thus no debuginfo package is needed
%global debug_package %{nil}

Name: kernel-headers
Summary: Header files for the Linux kernel for use by glibc
License: GPLv2
URL: http://www.kernel.org/
Version: %{pkgversion}
Release: %{pkg_release}
# This is a tarball with headers from the kernel, which should be created
# using create_headers_tarball.sh provided in the kernel source package.
# To create the tarball, you should go into a prepared/patched kernel sources
# directory, or git kernel source repository, and do eg.:
# For a RHEL package: (...)/create_headers_tarball.sh -m RHEL_RELEASE
# For a Fedora package: kernel/scripts/create_headers_tarball.sh -r <release number>
Source0: kernel-headers-%{pkgversion}-%{?srcversion}.tar.xz
Obsoletes: glibc-kernheaders < 3.0-46
Provides: glibc-kernheaders = 3.0-46
%if "0%{?variant}"
Obsoletes: kernel-headers < %{version}-%{release}
Provides: kernel-headers = %{version}-%{release}
%endif

%description
Kernel-headers includes the C header files that specify the interface
between the Linux kernel and userspace libraries and programs.  The
header files define structures and constants that are needed for
building most standard programs and are also needed for rebuilding the
glibc package.

%package -n kernel-cross-headers
Summary: Header files for the Linux kernel for use by cross-glibc

%description -n kernel-cross-headers
Kernel-cross-headers includes the C header files that specify the interface
between the Linux kernel and userspace libraries and programs.  The
header files define structures and constants that are needed for
building most standard programs and are also needed for rebuilding the
cross-glibc package.

%prep
%setup -q -c

%build

%install
# List of architectures we support and want to copy their headers
ARCH_LIST="arm arm64 powerpc riscv s390 x86"

ARCH=%_target_cpu
case $ARCH in
	armv7hl)
		ARCH=arm
		;;
	aarch64)
		ARCH=arm64
		;;
	ppc64*)
		ARCH=powerpc
		;;
	riscv64)
		ARCH=riscv
		;;
	s390x)
		ARCH=s390
		;;
	x86_64|i*86)
		ARCH=x86
		;;
esac

cd arch-$ARCH/include
mkdir -p $RPM_BUILD_ROOT%{_includedir}
cp -a asm-generic $RPM_BUILD_ROOT%{_includedir}

# Copy all the architectures we care about to their respective asm directories
for arch in $ARCH_LIST; do
	mkdir -p $RPM_BUILD_ROOT%{_prefix}/${arch}-linux-gnu/include
	cp -a asm-generic $RPM_BUILD_ROOT%{_prefix}/${arch}-linux-gnu/include/
done

# Remove what we copied already
rm -rf asm-generic

# Copy the rest of the headers over
cp -a * $RPM_BUILD_ROOT%{_includedir}/
for arch in $ARCH_LIST; do
cp -a * $RPM_BUILD_ROOT%{_prefix}/${arch}-linux-gnu/include/
done

%files
%defattr(-,root,root)
%{_includedir}/*

%files -n kernel-cross-headers
%defattr(-,root,root)
%{_prefix}/*-linux-gnu/*

%changelog
* Mon Aug 28 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.5.0-1
- Linux v6.5

* Mon Aug 14 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.5.0-0.rc6.git0.1
- Linux v6.5-rc6.git0

* Mon Jul 17 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.5.0-0.rc2.git0.1
- Linux v6.5-rc2.git0

* Mon Jun 26 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.4.0-1
- Linux v6.4

* Tue Jun 20 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.4.0-0.rc7.git0.1
- Linux v6.4-rc7.git0

* Mon Jun 12 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.4.0-0.rc6.git0.1
- Linux v6.4-rc6.git0

* Mon Jun 05 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.4.0-0.rc5.git0.1
- Linux v6.4-rc5.git0

* Mon May 22 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.4.0-0.rc3.git0.1
- Linux v6.4-rc3.git0

* Mon May 15 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.4.0-0.rc2.git0.1
- Linux v6.4-rc2.git0

* Mon May 08 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.4.0-0.rc1.git0.1
- Linux v6.4-rc1.git0

* Mon Apr 24 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.2.0-1
- Linux v6.3

* Mon Apr 17 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.3.0-0.rc7.git0.1
- Linux v6.3-rc7.git0

* Mon Apr 10 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.3.0-0.rc6.git0.1
- Linux v6.3-rc6.git0

* Mon Apr 03 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.3.0-0.rc5.git0.1
- Linux v6.3-rc5.git0

* Tue Mar 28 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.3.0-0.rc4.git0.1
- Linux v6.3-rc4.git0

* Mon Mar 20 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.3.0-0.rc3.git0.1
- Linux v6.3-rc3.git0

* Mon Mar 13 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.3.0-0.rc2.git0.1
- Linux v6.3-rc2.git0

* Mon Mar 06 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.3.0-0.rc1.git0.1
- Linux v6.3-rc1.git0

* Mon Feb 20 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.2.0-1
- Linux v6.2

* Mon Feb 13 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.2.0-0.rc8.git0.1
- Linux v6.2-rc8.git0

* Mon Jan 30 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.2.0-0.rc6.git0.1
- Linux v6.2-rc6.git0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.0-0.rc4.git0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.2.0-0.rc4.git0.1
- Linux v6.2-rc4.git0

* Mon Jan 02 2023 Justin M. Forbes <jforbes@fedoraproject.org> - 6.2.0-0.rc2.git0.1
- Linux v6.2-rc2.git0

* Mon Dec 12 2022 Justin M. Forbes <jforbes@fedoraproject.org> 6.1.0-1
- Linux v6.1.0

* Mon Dec 05 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.1.0-0.rc8.git0.1
- Linux v6.1-rc8.git0

* Mon Nov 28 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.1.0-0.rc7.git0.1
- Linux v6.1-rc7.git0

* Mon Nov 21 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.1.0-0.rc6.git0.1
- Linux v6.1-rc6.git0

* Mon Nov 14 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.1.0-0.rc5.git0.1
- Linux v6.1-rc5.git0

* Mon Nov 07 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.1.0-0.rc4.git0.1
- Linux v6.1-rc4.git0

* Mon Oct 24 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.1.0-0.rc2.git0.1
- Linux v6.1-rc2.git0

* Mon Oct 17 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.1.0-0.rc1.git0.1
- Linux v6.1-rc1.git0

* Mon Oct 03 2022 Justin M. Forbes <jforbes@fedoraproject.org>- 6.0.0-1
- Linux v6.0

* Mon Sep 26 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.0.0-0.rc7.git0.1
- Linux v6.0-rc7.git0

* Mon Sep 19 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.0.0-0.rc6.git0.1
- Linux v6.0-rc6.git0

* Mon Sep 05 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.0.0-0.rc4.git0.1
- Linux v6.0-rc4.git0

* Mon Aug 29 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.0.0-0.rc3.git0.1
- Linux v6.0-rc3.git0

* Mon Aug 22 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.0.0-0.rc2.git0.1
- Linux v6.0-rc2.git0

* Mon Aug 15 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 6.0.0-0.rc1.git0.1
- Linux v6.0-rc1.git0

* Mon Aug 01 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.18.0-1
- Linux v5.19

* Tue Jul 26 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.19.0-0.rc8.git0.1
- Linux v5.19-rc8.git0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.19.0-0.rc7.git0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.19.0-0.rc7.git0.1
- Linux v5.19-rc7.git0

* Mon Jul 11 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.19.0-0.rc6.git0.1
- Linux v5.19-rc6.git0

* Mon Jul 04 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.19.0-0.rc5.git0.1
- Linux v5.19-rc5.git0

* Mon Jun 27 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.19.0-0.rc4.git0.1
- Linux v5.19-rc4.git0

* Mon Jun 20 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.19.0-0.rc3.git0.1
- Linux v5.19-rc3.git0

* Mon Jun 13 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.19.0-0.rc2.git0.1
- Linux v5.19-rc2.git0

* Mon Jun 06 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.19.0-0.rc1.git0.1
- Linux v5.19-rc1.git0

* Mon May 23 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.18.0-1
- Linux v5.18.0

* Mon May 16 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.18.0-0.rc7.git0.1
- Linux v5.18-rc7.git0

* Mon May 09 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.18.0-0.rc6.git0.1
- Linux v5.18-rc6.git0

* Mon May 02 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.18.0-0.rc5.git0.1
- Linux v5.18-rc5.git0

* Mon Apr 25 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.18.0-0.rc4.git0.1
- Linux v5.18-rc4.git0

* Mon Apr 18 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.18.0-0.rc3.git0.1
- Linux v5.18-rc3.git0

* Mon Apr 11 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.18.0-0.rc2.git0.1
- Linux v5.18-rc2.git0

* Mon Apr 04 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.18-rc1.git0.1
- Linux v5.18-rc1.git0

* Mon Mar 21 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.17.0-1
- Linux v5.17.0

* Mon Mar 14 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.17.0-0.rc8.git0.1
- Linux v5.17-rc8.git0

* Mon Mar 07 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.17.0-0.rc7.git0.1
- Linux v5.17-rc7.git0

* Mon Feb 28 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.17.0-0.rc6.git0.1
- Linux v5.17-rc6.git0

* Mon Feb 21 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.17.0-0.rc5.git0.1
- Linux v5.17-rc5.git0

* Mon Feb 14 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.17.0-0.rc4.git0.1
- Linux v5.17-rc4.git0

* Mon Feb 07 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.17.0-0.rc3.git0.1
- Linux v5.17-rc3.git0

* Sun Jan 30 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.17.0-0.rc2.git0.1
- Linux v5.17-rc2.git0

* Mon Jan 24 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.17.0-0.rc1.git0.1
- Linux v5.17-rc1.git0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.16.0-1
- Linux v5.16

* Mon Jan 03 2022 Justin M. Forbes <jforbes@fedoraproject.org> - 5.16.0-0.rc8.git0.1
- Linux v5.16-rc8.git0

* Mon Dec 27 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.16.0-0.rc7.git0.1
- Linux v5.16-rc7.git0

* Mon Dec 20 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.16.0-0.rc6.git0.1
- Linux v5.16-rc6.git0

* Mon Dec 13 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.16.0-0.rc5.git0.1
- Linux v5.16-rc5.git0

* Mon Dec 06 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.16.0-0.rc4.git0.1
- Linux v5.16-rc4.git0

* Mon Nov 15 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.16.0-0.rc1.git0.1
- Linux v5.16-rc1.git0

* Mon Nov 01 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.15.0-1
- Linux v5.15.0

* Tue Oct 26 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.15.0-0.rc7.git0.1
- Linux v5.15-rc7.git0

* Mon Oct 18 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.15.0-0.rc6.git0.1
- Linux v5.15-rc6.git0

* Mon Oct 11 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.15.0-0.rc5.git0.1
- Linux v5.15-rc5.git0

* Mon Oct 04 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.15.0-0.rc4.git0.1
- Linux v5.15-rc4.git0

* Mon Sep 20 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.15.0-0.rc2.git0.1
- Linux v5.15-rc2.git0

* Mon Sep 13 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.15.0-0.rc1.git0.1
- Linux v5.15-rc1.git0

* Mon Aug 30 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.14.0-1
- Linux v5.14.0

* Mon Aug 23 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.14.0-0.rc7.git0.1
- Linux v5.14-rc7.git0

* Mon Aug 16 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.14.0-0.rc6.git0.1
- Linux v5.14-rc6.git0

* Mon Aug 09 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.14.0-0.rc5.git0.1
- Linux v5.14-rc5.git0

* Mon Aug 02 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.14.0-0.rc4.git0.1
- Linux v5.14-rc4.git0

* Mon Jul 26 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.14.0-0.rc3.git0.1
- Linux v5.14-rc3.git0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.0-0.rc2.git0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 20 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.14.0-0.rc2.git0.1
- Linux v5.14-rc2.git0

* Mon Jul 12 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.14.0-0.rc1.git0.1
- Linux v5.14-rc1.git0

* Mon Jun 28 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.13.0-1
- Linux v5.13

* Mon Jun 21 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.13.0-0.rc7.git0.1
- Linux v5.13-rc7.git0

* Tue Jun 15 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.13.0-0.rc6.git0.1
- Linux v5.13-rc6.git0

* Mon Jun 07 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.13.0-0.rc5.git0.1
- Linux v5.13-rc5.git0

* Tue Jun 01 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.13.0-0.rc4.git0.1
- Linux v5.13-rc4.git0

* Mon May 24 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.13.0-0.rc3.git0.1
- Linux v5.13-rc3.git0

* Mon May 17 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.13.0-0.rc2.git0.1
- Linux v5.13-rc2.git0

* Mon May 10 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.13.0-0.rc1.git0.1
- Linux v5.13-rc1.git0

* Mon Apr 26 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.12.0-1
- Linux v5.12.0

* Mon Apr 19 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.12.0-0.rc8.git0.1
- Linux v5.12-rc8.git0

* Mon Apr 12 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.12.0-0.rc7.git0.1
- Linux v5.12-rc7.git0

* Mon Apr 05 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.12.0-0.rc6.git0.1
- Linux v5.12-rc6.git0

* Mon Mar 29 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.12.0-0.rc5.git0.1
- Linux v5.12-rc5.git0

* Mon Mar 22 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.12.0-0.rc4.git0.1
- Linux v5.12-rc4.git0

* Mon Mar 15 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.12.0-0.rc3.git0.1
- Linux v5.12-rc3.git0

* Sat Mar 06 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.12.0-0.rc2.git0.1
- Linux v5.12-rc2.git0

* Mon Mar 01 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.12.0-0.rc1.git0.1
- Linux v5.12-rc1.git0

* Mon Feb 15 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.11.0-1
- Linux v5.11.0

* Mon Feb 08 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.11.0-0.rc7.git0.1
- Linux v5.11-rc7.git0

* Mon Feb 01 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.11.0-0.rc6.git0.1
- Linux v5.11-rc6.git0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.0-0.rc5.git0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 08:52:15 CST 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.11.0-0.rc5.git0.1
- Linux v5.11-rc5.git0

* Mon Jan 18 00:43:05 CST 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.11.0-0.rc4.git0.1
- Linux v5.11-rc4.git0

* Mon Jan  4 14:50:39 CST 2021 Justin M. Forbes <jforbes@fedoraproject.org> - 5.11.0-0.rc2.git0.1
- Linux v5.11-rc2.git0

* Mon Dec 14 09:36:14 CST 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.10.0-1
- Linux v5.10

* Mon Dec  7 10:31:32 CST 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.10.0-0.rc7.git0.1
- Linux v5.10-rc7.git0

* Mon Nov 30 10:31:13 CST 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.10.0-0.rc6.git0.1
- Linux v5.10-rc6.git0

* Mon Nov 23 11:34:18 CST 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.10.0-0.rc5.git0.1
- Linux v5.10-rc5.git0

* Mon Nov 16 10:54:27 CST 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.10.0-0.rc4.git0.1
- Linux v5.10-rc4.git0

* Mon Nov  9 10:52:05 CST 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.10.0-0.rc3.git0.1
- Linux v5.10-rc3.git0

* Tue Nov  3 12:14:54 CST 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.10.0-0.rc2.git0.1
- Linux v5.10-rc2.git0

* Mon Oct 26 09:38:56 CDT 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.10.0-0.rc1.git0.1
- Linux v5.10-rc1.git0

* Mon Oct 12 10:09:39 CDT 2020 Justin M. Forbes <jforbes@fedoraproject.org>  - 5.9.0-1
- Linux v5.9.0

* Mon Oct  5 14:54:56 CDT 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.9.0-0.rc8.git0.1
- Linux v5.9-rc8.git0

* Mon Sep 28 13:47:22 CDT 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.9.0-0.rc7.git0.1
- Linux v5.9-rc7.git0

* Mon Sep 21 10:06:55 CDT 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.9.0-0.rc6.git0.1
- Linux v5.9-rc6.git0

* Tue Sep 15 08:45:34 CDT 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.9.0-0.rc5.git0.1
- Linux v5.9-rc5.git0

* Mon Aug 31 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.9.0-0.rc3.git0.1
- Linux v5.9-rc3.git0

* Tue Aug 25 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.9.0-0.rc2.git0.1
- Linux v5.9-rc2.git0

* Mon Aug 17 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.8.0-1
- Linux v5.9-rc1.git0

* Mon Aug 03 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.8.0-1
- Linux v5.8.0

* Mon Jul 27 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.8.0-0.rc7.git0.1
- Linux v5.8-rc7.git0

* Mon Jul 13 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.8.0-0.rc5.git0.1
- Linux v5.8-rc5.git0

* Mon Jul 06 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.8.0-0.rc4.git0.1
- Linux v5.8-rc4.git0

* Mon Jun 29 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.8.0-0.rc3.git0.1
- Linux v5.8-rc3.git0

* Mon Jun 15 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.8.0-0.rc1.git0.1
- Linux v5.8-rc1.git0

* Mon Jun 01 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.7.0-1
- Linux v5.7.0

* Tue May 26 2020 Justin M. Forbes <jforbes@fedoraproject.org>
- Add riscv

* Mon May 25 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.7.0-0.rc7.git0.1
- Linux v5.7-rc7.git0

* Mon May 11 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.7.0-0.rc5.git0.1
- Linux v5.7-rc5.git0

* Wed May 06 2020  Justin M. Forbes <jforbes@fedoraproject.org> - 5.7.0-rc4
- Linux v5.7-rc4

* Sun Apr 26 2020  Justin M. Forbes <jforbes@fedoraproject.org> - 5.7.0-rc3
- Linux v5.7-rc3

* Mon Apr 13 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.6.0-1
- Linux v5.7-rc1.git0

* Mon Mar 30 2020 Jeremy Cline <jcline@redhat.com> - 5.7.0-0.rc7.git0.1
- Linux v5.6.0

* Mon Mar 23 2020 Jeremy Cline <jcline@redhat.com> - 5.6.0-0.rc7.git0.1
- Linux v5.6-rc7.git0

* Tue Mar 17 2020 Jeremy Cline <jcline@redhat.com> - 5.6.0-0.rc6.git0.1
- Linux v5.6-rc6.git0

* Mon Mar 09 2020 Jeremy Cline <jcline@redhat.com> - 5.6.0-0.rc5.git0.1
- Linux v5.6-rc5.git0

* Mon Mar 02 2020 Jeremy Cline <jcline@redhat.com> - 5.6.0-0.rc4.git0.1
- Linux v5.6-rc4.git0

* Mon Feb 24 2020 Jeremy Cline <jcline@redhat.com> - 5.6.0-0.rc3.git0.1
- Linux v5.6-rc3.git0

* Wed Feb 19 2020 Jeremy Cline <jcline@redhat.com> - 5.6.0-0.rc2.git2.1
- Linux v5.6-rc2.git2

* Mon Feb 17 2020 Jeremy Cline <jcline@redhat.com> - 5.6.0-0.rc2.git0.1
- Linux v5.6-rc2.git0

* Tue Feb 11 2020 Jeremy Cline <jcline@redhat.com> - 5.6.0-0.rc1.git0.1
- Linux v5.6-rc1.git0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.5.0-1
- Linux v5.5.0

* Mon Jan 20 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.5.0-0.rc7.git0.1
- Linux v5.5-rc7.git0

* Mon Jan 13 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.5.0-0.rc6.git0.1
- Linux v5.5-rc6.git0

* Mon Jan 06 2020 Justin M. Forbes <jforbes@fedoraproject.org> - 5.5.0-0.rc5.git0.1
- Linux v5.5-rc5.git0

* Mon Dec 30 2019 Peter Robinson <pbrobinson@gmail.com> - 5.5.0-0.rc4.git0.1
- Linux v5.5-rc4.git0

* Mon Dec 23 2019 Justin M. Forbes <jforbes@fedoraproject.org> - 5.5.0-0.rc3.git0.1
- Linux v5.5-rc3.git0

* Mon Dec 16 2019 Justin M. Forbes <jforbes@fedoraproject.org> - 5.5.0-0.rc2.git0.1
- Linux v5.5-rc2.git0

* Tue Dec 10 2019 Justin M. Forbes <jforbes@fedoraproject.org> - 5.4.0-1
- Linux v5.5-rc1.git0

* Wed Dec 04 2019 Jeremy Cline <jcline@redhat.com> - 5.4.0-1
- Linux v5.4.0

* Mon Nov 04 2019 Jeremy Cline <jcline@redhat.com> - 5.4.0-0.rc6.git0.1
- Linux v5.4-rc6.git0

* Mon Oct 28 2019 Jeremy Cline <jcline@redhat.com> - 5.4.0-0.rc5.git0.1
- Linux v5.4-rc5.git0

* Thu Oct 03 2019 Jeremy Cline <jcline@redhat.com> - 5.4.0-0.rc1.git0.1
- Linux v5.4-rc1

* Mon Sep 16 2019 Laura Abbott <labbott@redhat.com> - 5.3.0-1
- Linux v5.3.0

* Tue Sep 10 2019 Laura Abbott <labbott@redhat.com> - 5.3.0-0.rc8.git0.1
- Linux v5.3-rc8.git0

* Tue Sep 03 2019 Laura Abbott <labbott@redhat.com> - 5.3.0-0.rc7.git0.1
- Linux v5.3-rc7.git0

* Mon Aug 26 2019 Laura Abbott <labbott@redhat.com> - 5.3.0-0.rc6.git0.1
- Linux v5.3-rc6.git0

* Mon Aug 19 2019 Laura Abbott <labbott@redhat.com> - 5.3.0-0.rc5.git0.1
- Linux v5.3-rc5.git0

* Tue Aug 13 2019 Laura Abbott <labbott@redhat.com> - 5.3.0-0.rc4.git0.1
- Linux v5.3-rc4.git0

* Mon Aug 05 2019 Laura Abbott <labbott@redhat.com> - 5.3.0-0.rc3.git0.1
- Linux v5.3-rc3.git0

* Mon Jul 29 2019 Laura Abbott <labbott@redhat.com> - 5.3.0-0.rc2.git0.1
- Linux v5.3-rc2.git0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-0.rc1.git0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Laura Abbott <labbott@redhat.com> - 5.3.0-0.rc1.git0.1
- Linux v5.3-rc1.git0

* Thu Jul 18 2019 Laura Abbott <labbott@redhat.com> - 5.3.0-0.rc0.git7.1
- Linux v5.3-rc0.git7

* Tue Jul 16 2019 Laura Abbott <labbott@redhat.com> - 5.3.0-rc0.git5.1
- Linux v5.3-rc0.git5

* Mon Jul 08 2019 Justin M. Forbes <jforbes@fedoraproject.org> - 5.2.0-1
- Linux v5.2.0

* Mon Jul 01 2019 Justin M. Forbes <jforbes@fedoraproject.org> - 5.2.0-0.rc7.git0.1
- Linux v5.2-rc7.git0

* Mon Jun 24 2019 Justin M. Forbes <jforbes@fedoraproject.org> - 5.2.0-0.rc6.git0.1
- Linux v5.2-rc6.git0

* Mon Jun 17 2019 Justin M. Forbes <jforbes@fedoraproject.org> - 5.2.0-0.rc5.git0.1
- Linux v5.2-rc5.git0

* Mon Jun 10 2019 Justin M. Forbes <jforbes@fedoraproject.org> - 5.2.0-0.rc4.git0.1
- Linux v5.2-rc4.git0

* Mon Jun 03 2019 Justin M. Forbes <jforbes@fedoraproject.org> - 5.2.0-0.rc3.git0.1
- Linux v5.2-rc3.git0

* Mon May 27 2019 Justin M. Forbes <jforbes@fedoraproject.org> - 5.2.0-0.rc2.git0.1
- Linux v5.2-rc2.git0

* Mon May 20 2019 Justin M. Forbes <jforbes@fedoraproject.org> - 5.2.0-rc1.git0.1
- Linux v5.2-rc1.git0

* Mon May 06 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-1
- Linux v5.1.0

* Fri May 03 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc7.git4.1
- Linux v5.1-rc7.git4

* Thu May 02 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc7.git3.1
- Linux v5.1-rc7.git3

* Wed May 01 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc7.git2.1
- Linux v5.1-rc7.git2

* Tue Apr 30 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc7.git1.1
- Linux v5.1-rc7.git1

* Mon Apr 29 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc7.git0.1
- Linux v5.1-rc7.git0

* Fri Apr 26 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc6.git4.1
- Linux v5.1-rc6.git4

* Thu Apr 25 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc6.git3.1
- Linux v5.1-rc6.git3

* Wed Apr 24 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc6.git2.1
- Linux v5.1-rc6.git2

* Tue Apr 23 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc6.git1.1
- Linux v5.1-rc6.git1

* Mon Apr 22 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc6.git0.1
- Linux v5.1-rc6.git0

* Wed Apr 17 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc5.git2.1
- Linux v5.1-rc5.git2

* Tue Apr 16 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc5.git1.1
- Linux v5.1-rc5.git1

* Mon Apr 15 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc5.git0.1
- Linux v5.1-rc5.git0

* Fri Apr 12 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc4.git4.1
- Linux v5.1-rc4.git4

* Thu Apr 11 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc4.git3.1
- Linux v5.1-rc4.git3

* Wed Apr 10 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc4.git2.1
- Linux v5.1-rc4.git2

* Tue Apr 09 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc4.git1.1
- Linux v5.1-rc4.git1

* Mon Apr 08 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc4.git0.1
- Linux v5.1-rc4.git0

* Fri Apr 05 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc3.git3.1
- Linux v5.1-rc3.git3

* Wed Apr 03 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc3.git2.1
- Linux v5.1-rc3.git2

* Tue Apr 02 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc3.git1.1
- Linux v5.1-rc3.git1

* Mon Apr 01 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc3.git0.1
- Linux v5.1-rc3.git0

* Fri Mar 29 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc2.git4.1
- Linux v5.1-rc2.git4

* Thu Mar 28 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc2.git3.1
- Linux v5.1-rc2.git3

* Wed Mar 27 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc2.git2.1
- Linux v5.1-rc2.git2

* Tue Mar 26 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc2.git1.1
- Linux v5.1-rc2.git1

* Mon Mar 25 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc2.git0.1
- Linux v5.1-rc2.git0

* Fri Mar 22 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc1.git2.1
- Linux v5.1-rc1.git2

* Wed Mar 20 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc1.git1.1
- Linux v5.1-rc1.git1

* Mon Mar 18 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc1.git0.1
- Linux v5.1-rc1.git0

* Fri Mar 15 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc0.git9.1
- Linux v5.1-rc0.git9

* Thu Mar 14 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc0.git8.1
- Linux v5.1-rc0.git8

* Wed Mar 13 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc0.git7.1
- Linux v5.1-rc0.git7

* Tue Mar 12 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc0.git6.1
- Linux v5.1-rc0.git6

* Mon Mar 11 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc0.git5.1
- Linux v5.1-rc0.git5

* Fri Mar 08 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc0.git4.1
- Linux v5.1-rc0.git4

* Thu Mar 07 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc0.git3.1
- Linux v5.1-rc0.git3

* Wed Mar 06 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc0.git2.1
- Linux v5.1-rc0.git2

* Tue Mar 05 2019 Jeremy Cline <jcline@redhat.com> - 5.1.0-0.rc0.git1.1
- Linux v5.1-rc0.git1

* Mon Mar 04 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-1
- Linux v5.0.0

* Mon Feb 25 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc8.git0.1
- Linux v5.0-rc8.git0

* Fri Feb 22 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc7.git3.1
- Linux v5.0-rc7.git3

* Wed Feb 20 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc7.git2.1
- Linux v5.0-rc7.git2

* Tue Feb 19 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc7.git1.1
- Linux v5.0-rc7.git1

* Mon Feb 18 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc7.git0.1
- Linux v5.0-rc7.git0

* Wed Feb 13 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc6.git1.1
- Linux v5.0-rc6.git1

* Mon Feb 11 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc6.git0.1
- Linux v5.0-rc6.git0

* Mon Feb 04 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc5.git0.1
- Linux v5.0-rc5.git0

* Fri Feb 01 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc4.git3.1
- Linux v5.0-rc4.git3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-0.rc4.git2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc4.git2.1
- Linux v5.0-rc4.git2

* Tue Jan 29 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc4.git1.1
- Linux v5.0-rc4.git1

* Mon Jan 28 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc4.git0.1
- Linux v5.0-rc4.git0

* Mon Jan 21 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc3.git0.1
- Linux v5.0-rc3.git0

* Fri Jan 18 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc2.git4.1
- Linux v5.0-rc2.git4

* Thu Jan 17 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc2.git3.1
- Linux v5.0-rc2.git3

* Wed Jan 16 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc2.git2.1
- Linux v5.0-rc2.git2

* Tue Jan 15 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc2.git1.1
- Linux v5.0-rc2.git1

* Mon Jan 14 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc2.git0.1
- Linux v5.0-rc2.git0

* Thu Jan 10 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc1.git3.1
- Linux v5.0-rc1.git3

* Wed Jan 09 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc1.git2.1
- Linux v5.0-rc1.git2

* Tue Jan 08 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc1.git1.1
- Linux v5.0-rc1.git1

* Mon Jan 07 2019 Laura Abbott <labbott@redhat.com> - 5.0.0-0.rc1.git0.1
- Linux v5.0-rc1.git0

* Fri Jan 04 2019 Laura Abbott <labbott@redhat.com> - 4.21.0-0.rc0.git7.1
- Linux v4.21-rc0.git7

* Thu Jan 03 2019 Laura Abbott <labbott@redhat.com> - 4.21.0-0.rc0.git6.1
- Linux v4.21-rc0.git6

* Wed Jan 02 2019 Laura Abbott <labbott@redhat.com> - 4.21.0-0.rc0.git5.1
- Linux v4.21-rc0.git5

* Mon Dec 31 2018 Laura Abbott <labbott@redhat.com> - 4.21.0-0.rc0.git4.1
- Linux v4.21-rc0.git4

* Sun Dec 30 2018 Laura Abbott <labbott@redhat.com> - 4.21.0-0.rc0.git3.1
- Linux v4.21-rc0.git3

* Fri Dec 28 2018 Laura Abbott <labbott@redhat.com> - 4.21.0-0.rc0.git2.1
- Linux v4.21-rc0.git2
