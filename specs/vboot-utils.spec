%define gitshort 9b08a3c4

Name:		vboot-utils
Version:	20230127
Release:	6.git%{gitshort}%{?dist}
Summary:	Verified Boot Utility from Chromium OS
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://chromium.googlesource.com/chromiumos/platform/vboot_reference

ExclusiveArch:	%{arm} aarch64 %{ix86} x86_64

# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  git clone https://git.chromium.org/git/chromiumos/platform/vboot_reference.git
#  cd vboot_reference/
#  git archive --format=tar --prefix=vboot-utils-9b08a3c4/ 9b08a3c4 | xz > vboot-utils-9b08a3c4.tar.xz
Source0:	%{name}-%{gitshort}.tar.xz

# Fix VB2_DEBUG function usage
Patch0:	vboot-utils-9b08a3c4.patch
# Fix linking error with USE_FLASHROM=0
Patch1: flashrom-ensure-flashrom-symbols-are-not-loaded-if-U.patch

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	glibc-static
BuildRequires:	openssl-devel
BuildRequires:	trousers-devel
BuildRequires:	libyaml-devel
BuildRequires:	xz-devel
BuildRequires:	libuuid-devel

%description
Verified boot is a collection of utilities helpful for chromebook computer.
Pack and sign the kernel, manage gpt partitions.


%prep
%autosetup -p1 -n %{name}-%{gitshort}

%build

%ifarch %{arm} aarch64
%global ARCH arm
%endif

%ifarch x86_64
%global ARCH x86_64
%endif

%ifarch i686
%global ARCH i386
%endif


make V=1 ARCH=%{ARCH} COMMON_FLAGS="$RPM_OPT_FLAGS" USE_FLASHROM=0


%install
make install V=1 DESTDIR=%{buildroot} ARCH=%{ARCH} COMMON_FLAGS="$RPM_OPT_FLAGS" USE_FLASHROM=0
mkdir -p %{buildroot}%{_datadir}/vboot/
cp -rf tests/devkeys %{buildroot}%{_datadir}/vboot/

# Remove unneeded build artifacts
rm -rf %{buildroot}/usr/lib/pkgconfig/
rm -rf %{buildroot}/usr/default/
rm -rf %{buildroot}/etc/default/
rm -rf %{buildroot}/usr/share/vboot/bin/
rm -f %{buildroot}/usr/bin/chromeos-tpm-recovery
rm -f %{buildroot}/usr/bin/crossystem
rm -f %{buildroot}/usr/bin/dev_debug_vboot
rm -f %{buildroot}/usr/bin/dumpRSAPublicKey
rm -f %{buildroot}/usr/bin/dump_fmap
rm -f %{buildroot}/usr/bin/dump_kernel_config
rm -f %{buildroot}/usr/bin/enable_dev_usb_boot
rm -f %{buildroot}/usr/bin/gbb_utility
rm -f %{buildroot}/usr/bin/tpm-nvsize
rm -f %{buildroot}/usr/bin/tpmc
rm -f %{buildroot}/usr/bin/vbutil_firmware
rm -f %{buildroot}/usr/bin/vbutil_key
rm -f %{buildroot}/usr/bin/vbutil_keyblock
rm -f %{buildroot}/usr/lib/libvboot_host.a

%files
%license LICENSE
%doc README
%{_bindir}/futility
%{_bindir}/vbutil_kernel
%{_bindir}/cgpt
%{_datadir}/vboot/devkeys/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20230127-6.git9b08a3c4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 20230127-5.git9b08a3c4
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230127-4.git9b08a3c4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230127-3.git9b08a3c4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20230127-2.git9b08a3c4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 27 2023 Javier Martinez Canillas <javierm@redhat.com> - 20230127-1.git9b08a3c4
- Update to upstream snapshot 9b08a3c4
- Drop `BuildRequires: flashrom-devel` since all tools depending on it are removed.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20220621-3.git61971455
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20220621-2.git61971455
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Dorinda Bassey <dbassey@redhat.com> - 20220621-1.git61971455
- Fix VB2_DEBUG function usage
- New Upstream snapshot 61971455
- Clean up spec file

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20190823-9.git595108c0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 20190823-8.git595108c0
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20190823-7.git595108c0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20190823-6.git595108c0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20190823-5.git595108c0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 01 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 20190823-4.git595108c0
- Drop tests to drop python2 dep

* Thu Feb 27 2020 Than Ngo <than@redhat.com> - 20190823-3.git595108c
- Fix FTBFS

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20190823-2.git595108c0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 26 2019 Peter Robinson <pbrobinson@fedoraproject.org> 20190823.1.git595108c0
- Rebase to upstream 595108c0 snapshot

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180531-4.git2cc35b0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180531-3.git2cc35b0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20180531-2.git2cc35b0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun  3 2018 Peter Robinson <pbrobinson@fedoraproject.org> 20180531-1.2cc35b0
- New upstream snapshot

* Sun Mar 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 20170302-5.gita1c5f7c
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 20170302-4.gita1c5f7c
- Escape macros in %%changelog

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170302-3.gita1c5f7c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170302-2.gita1c5f7c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun  4 2017 Peter Robinson <pbrobinson@fedoraproject.org> 20170302-1.gita1c5f7c
- Move to newer upstream snapshot needed for some devices
- Spec cleanups

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20130222gite6cf2c2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20130222gite6cf2c2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130222gite6cf2c2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 20130222gite6cf2c2-7
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130222gite6cf2c2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130222gite6cf2c2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130222gite6cf2c2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 04 2013 Jon Disnard <jdisnard@gmail.com> 20130222gite6cf2c2-3
- Clean up spec file
- Honor rpmbuild CFLAGS
- Fix strncat arguments in cgpt/cgpt_add.c

* Sat Feb 23 2013 Jon Disnard <jdisnard@gmail.com> 20130222gite6cf2c2-2
- Put back wcohen's fixes for i686 builds.
- Put back the patch to fix bmpblk_utility.cc printf formating %%ld -> %%zu
- Put back BR for gcc-c++ & libstdc++

* Fri Feb 22 2013 Jon Disnard <jdisnard@gmail.com> 20130222gite6cf2c2-1
- Pull upstream git
- Adjust ifarch conditionals to follow upstream changes in Makefile.
- Use XZ instead of BZIP2 for source archive, smaller SRPM size.
- Upstream fixed bug, so removing CC printf formating patch.
- Refactor patch that disabled static building for new Makefile.
- Enable test scripts again, but ignore failures (for mock builds).
- Remove BuildRequires for gcc-c++ & libstdc++, removed upstream.

* Tue Feb  5 2013 William Cohen <wcohen@redhat.c>  20130129git68f54d4-4
- Correct logic for setting 32-bit/64-bit x86.

* Tue Feb  5 2013 William Cohen <wcohen@redhat.c>  20130129git68f54d4-3
- Disable smp build because of problem with make dependencies

* Mon Feb  4 2013 William Cohen <wcohen@redhat.c>  20130129git68f54d4-2
- spec file clean up.

* Sat Jan  5 2013 Jon Disnard <jdisnard@gmail.com> 20130129git68f54d4-1
- Inception
- Patch0 prevents static building.
- Patch1 fixes minor printf formating bug in c++ code.
- tests disabled as they do not work in mock chroot.
