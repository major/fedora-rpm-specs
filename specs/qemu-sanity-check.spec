%global debug_package %{nil}

# Architectures where the tests should pass.
#
# 2020-09: Fails on power64 because qemu TCG does not support all the
#   features required to boot Fedora.
# 2025-07: Fails on aarch64 because of lack of support for zstd + zboot
#   https://bugzilla.redhat.com/show_bug.cgi?id=2385692
%global test_arches %{s390x} x86_64

Name:           qemu-sanity-check
Version:        1.1.6
Release:        20%{?dist}
Summary:        Simple qemu and Linux kernel sanity checker
License:        GPL-2.0-or-later

ExclusiveArch:  %{kernel_arches}

%if 0%{?rhel} >= 9
# No KVM on POWER in RHEL 9
ExcludeArch:    %{power64}
%endif

URL:            http://people.redhat.com/~rjones/qemu-sanity-check
Source0:        http://people.redhat.com/~rjones/qemu-sanity-check/files/%{name}-%{version}.tar.gz
Source1:        http://people.redhat.com/~rjones/qemu-sanity-check/files/%{name}-%{version}.tar.gz.sig
# Keyring used to verify tarball signature.
Source2:        libguestfs.keyring

# Patches (all upstream).
Patch:          0001-tests-run-qemu-sanity-check-Add-v-flag-for-verbose-m.patch
Patch:          0002-Add-cpu-option.patch
Patch:          0003-Set-RAM-to-something-larger-than-qemu-default.patch
Patch:          0004-Set-console-on-ARM-and-s390.patch
Patch:          0005-Ignore-user-added-local-files-such-as-.-localconfigu.patch
Patch:          0006-Move-the-tests-into-a-subdirectory.patch
Patch:          0007-Move-the-source-files-into-a-subdirectory.patch
Patch:          0008-Attempt-RB_POWER_OFF-before-reboot.patch
Patch:          0009-Make-sure-that-qemu-sanity-check-v-displays-kernel-o.patch
Patch:          0010-Error-out-if-any-kernel-panic-is-seen.patch
Patch:          0011-src-Add-more-information-about-kernel-and-qemu-searc.patch
Patch:          0012-docs-Use-F-around-file-references-in-the-manual.patch
Patch:          0013-src-Look-for-kernels-in-lib-modules-vmlinuz.patch
Patch:          0014-Choose-cpu-max-by-default.patch

# To verify the tarball signature.
BuildRequires:  gnupg2

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake

# For building manual pages.
BuildRequires:  /usr/bin/perldoc

# For building the initramfs.
BuildRequires:  cpio
BuildRequires:  glibc-static

# For testing.
%if !0%{?rhel}
BuildRequires:  qemu
%else
BuildRequires:  qemu-kvm
%endif
BuildRequires:  kernel

# For complicated reasons, this is required so that
# /bin/kernel-install puts the kernel directly into /boot, instead of
# into a /boot/<machine-id> subdirectory (in Fedora >= 23).  Read the
# kernel-install script to understand why.
BuildRequires:  grubby

%if !0%{?rhel}
%ifarch %{ix86} x86_64
Requires:       qemu-system-x86
%global qemu    %{_bindir}/qemu-system-x86_64
%endif
%ifarch armv7hl
Requires:       qemu-system-arm
%global qemu    %{_bindir}/qemu-system-arm
%endif
%ifarch aarch64
Requires:       qemu-system-aarch64
%global qemu    %{_bindir}/qemu-system-aarch64
%endif
%ifarch %{power64}
Requires:       qemu-system-ppc
%global qemu    %{_bindir}/qemu-system-ppc64
%endif
%ifarch %{s390x}
Requires:       qemu-system-s390x
%global qemu    %{_bindir}/qemu-system-s390x
%endif
%else
# RHEL, any arch
Requires:       qemu-kvm
%global qemu    %{_libexecdir}/qemu-kvm
%endif

Requires:       kernel

# Require the -nodeps subpackage.
Requires:       %{name}-nodeps = %{version}-%{release}


%description
Qemu-sanity-check is a short shell script that test-boots a Linux
kernel under qemu, making sure it boots up to userspace.  The idea is
to test the Linux kernel and/or qemu to make sure they are working.

Most users should install the %{name} package.

If you are testing qemu or the kernel in those packages and you want
to avoid a circular dependency on qemu or kernel, you should use
'BuildRequires: %{name}-nodeps' instead.


%package nodeps
Summary:         Simple qemu and Linux kernel sanity checker (no dependencies)
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:         GPL-2.0-or-later


%description nodeps
This is the no-depedencies version of %{name}.  It is exactly the same
as %{name} except that this package does not depend on qemu or kernel.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
autoreconf -fi


%build
# NB: canonical_arch is a variable in the final script, so it
# has to be escaped here.
%configure \
%if 0%{?qemu:1}
    --with-qemu-list="%{qemu}" \
%else
    --with-qemu-list="qemu-system-\$canonical_arch" \
%endif
|| {
    cat config.log
    exit 1
}
make %{?_smp_mflags}


%check
%ifarch %{test_arches}
make check || {
    cat tests/run-qemu-sanity-check.log ||:
    cat tests/test-suite.log ||:
    exit 1
}
%endif


%install
make DESTDIR=$RPM_BUILD_ROOT install


%files
%doc COPYING


%files nodeps
%doc COPYING README
%{_bindir}/qemu-sanity-check
%{_libdir}/qemu-sanity-check
%{_mandir}/man1/qemu-sanity-check.1*


%changelog
* Thu Jul 31 2025 Richard W.M. Jones <rjones@redhat.com> - 1.1.6-20
- Disable tests on arm (RHBZ#2385561)

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 09 2025 Richard W.M. Jones <rjones@redhat.com> - 1.1.6-17
- Use -cpu max by default

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.6-16
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Richard W.M. Jones <rjones@redhat.com> - 1.1.6-14
- Look for kernels in /lib/modules/*/vmlinuz
- Display the correct test-suite.log if %%check fails
- Enhance debugging in tests/run-qemu-sanity-check

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 01 2023 Richard W.M. Jones <rjones@redhat.com> - 1.1.6-11
- Rebase with all latest upstream patches

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 18 2023 Richard W.M. Jones <rjones@redhat.com> - 1.1.6-9
- Add package to EPEL 9, keep it synched with Fedora Rawhide.
- Use qemu-kvm package on EPEL.
- Remove comment about armv7, no longer applicable on Fedora.

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Richard W.M. Jones <rjones@redhat.com> - 1.1.6-5
- Rebuild for fixed qemu metapackage.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 25 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.6-2
- Add some upstream patches to fix aarch64 tests.
- Enable tests on aarch64.

* Thu Sep 10 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.6-1
- New upstream version 1.1.6.
- Remove all patches.
- Run the tests on some more arches.
- Require qemu-system-<arch>.
- Enable hardened build.
- Enable signed tarball.

* Wed Aug 19 2020 Merlin Mathesius <mmathesi@redhat.com> - 1.1.5-16
- Use ExclusiveArch: %%{kernel_arches}

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1.5-13
- Disable on i686 because no kernel package.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Richard W.M. Jones <rjones@redhat.com> - 1.1.5-11
- Add upstream patch to remove deprecated -nodefconfig option.
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Richard W.M. Jones <rjones@redhat.com> - 1.1.5-4
- +BR grubby.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 02 2014 Richard W.M. Jones <rjones@redhat.com> - 1.1.5-1
- New upstream version 1.1.5.
- Adds --accel option to select qemu acceleration mode.
- Remove upstream patch.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 28 2013 Richard W.M. Jones <rjones@redhat.com> - 1.1.4-2
- New upstream version 1.1.4.
- Remove 3 x patches which are now upstream.
- This version can handle debug kernels (RHBZ#1002189).

* Thu Aug 22 2013 Richard W.M. Jones <rjones@redhat.com> - 1.1.3-4
- +BR autoconf, automake.
- Run autoreconf after patching.

* Thu Aug 22 2013 Richard W.M. Jones <rjones@redhat.com> - 1.1.3-2
- Fedora kernels don't respond properly to panic=1 parameter (appears
  to be related to having debug enabled).  Add some upstream and one
  non-upstream patches to work around this.

* Thu Aug 22 2013 Richard W.M. Jones <rjones@redhat.com> - 1.1.3-1
- Initial release (RHBZ#999108).
