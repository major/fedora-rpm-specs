%define debug_package %{nil}

Summary:    Tools for building live CDs
Name:       livecd-tools
Version:    31.0
Release:    19%{?dist}
%if 0%{?fedora}
Epoch:      1
%endif
License:    GPL-2.0-only
URL:        https://github.com/livecd-tools/livecd-tools
# lorax dependency is not available, due to qemu removal
ExcludeArch: %{ix86}

Source0:    %{url}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:     livecd-tools-31.0-py312-distutils-removal.patch
# Allow using local kickstart files:
Patch1:     https://github.com/livecd-tools/livecd-tools/commit/41e15de6de2caef6bfadafcaf3dbb60c0531079c.patch
# Fix mangled output with one word per line:
Patch2:     https://github.com/livecd-tools/livecd-tools/commit/51bd0fefdfd6c06c03990d46b4e7d838cefc9da4.patch

BuildRequires:  make
BuildRequires:  perl-podlators
BuildRequires:  python3-devel

%ifarch %{ix86} x86_64
Requires:   livecd-iso-to-mediums = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
Requires:   python3-imgcreate = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Tools for generating live CDs on Fedora based systems including derived
distributions such as RHEL, CentOS and others.
See http://fedoraproject.org/wiki/FedoraLiveCD for more details.

%package -n python-imgcreate-sysdeps
Summary:    Common system dependencies for python-imgcreate
Requires:   coreutils
Requires:   cryptsetup
Requires:   dosfstools >= 2.11-8
Requires:   dracut
Requires:   dracut-live
Requires:   dumpet
Requires:   e2fsprogs
Requires:   isomd5sum
Requires:   lorax >= 18.3
Requires:   parted
Requires:   policycoreutils
Requires:   rsync
Requires:   selinux-policy-targeted
Requires:   squashfs-tools
Requires:   sssd-client
Requires:   util-linux
Requires:   xorriso >= 1.4.8

%if ! 0%{?rhel}
# hfs+ support for Macs
%ifarch %{ix86} x86_64 ppc ppc64
Requires:   hfsplus-tools
%endif
%endif

# syslinux dependency
%ifarch %{ix86} x86_64
Requires:   syslinux >= 6.02-4
Requires:   syslinux-nonlinux >= 6.02-4
Requires:   syslinux-extlinux
%endif

# For legacy ppc32 systems
%ifarch ppc
Requires:   yaboot
%endif

%description -n python-imgcreate-sysdeps
This package describes the common system dependencies for
python-imgcreate.

%package -n python3-imgcreate
Summary:    Python 3 modules for building system images
%{?python_provide:%python_provide python3-imgcreate}
Requires:   libselinux-python3
Requires:   python-imgcreate-sysdeps%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:   python3-dbus
Requires:   python3-dnf >= 1.1.0
Requires:   python3-kickstart
Requires:   python3-pyparted
Requires:   python3-urlgrabber

%description -n python3-imgcreate
Python 3 modules that can be used for building images for things
like live image or appliances.

%ifarch %{ix86} x86_64
%package -n livecd-iso-to-mediums
Summary:    Tools for installing ISOs to different mediums
Requires:   python-imgcreate-sysdeps%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n livecd-iso-to-mediums
Tools for installing Live CD ISOs to different mediums (e.g. USB sticks, hard
drives, PXE boot, etc.)
%endif

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}

%install
%make_install PYTHON=python3

# Delete docs, we'll grab them later
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%ifnarch %{ix86} x86_64
# livecd-iso-to-mediums doesn't work without syslinux
rm -rfv %{buildroot}%{_bindir}/livecd-iso-to-*
rm -rfv %{buildroot}%{_mandir}/man8/livecd-iso-to-*
%endif

%files
%license COPYING
%doc AUTHORS README HACKING
%doc config/livecd-fedora-minimal.ks
%doc config/livecd-mageia-minimal-*.ks
%{_mandir}/man8/livecd-creator.8*
%{_mandir}/man8/mkbiarch.8*
%{_bindir}/livecd-creator
%{_bindir}/image-creator
%{_bindir}/liveimage-mount
%{_bindir}/editliveos
%{_bindir}/mkbiarch

%files -n python-imgcreate-sysdeps
# No files because empty metapackage

%files -n python3-imgcreate
%license COPYING
%doc API
%{python3_sitelib}/imgcreate

%ifarch %{ix86} x86_64
%files -n livecd-iso-to-mediums
%license COPYING
%{_bindir}/livecd-iso-to-disk
%{_bindir}/livecd-iso-to-pxeboot
%{_mandir}/man8/livecd-iso-to-disk.8*
%endif

%changelog
* Fri Nov 14 2025 Daniel P. Berrangé <berrange@redhat.com> - 1:31.0-19
- Add ExcludeArch for i686 to remove the indirect dep on QEMU

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 1:31.0-18
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 1:31.0-17
- Rebuilt for Python 3.14.0rc2 bytecode

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:31.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jul 04 2025 Simone Caronni <negativo17@gmail.com> - 1:31.0-15
- Add patches.

* Fri Jul 04 2025 Simone Caronni <negativo17@gmail.com> - 1:31.0-14
- Remove obsolete EL7, Python 2 conditionals and Conflicts.
- Switch to a valid Source URL.
- Explicitly list man pages.
- Format SPEC file.
- Trim changelog.

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 1:31.0-13
- Rebuilt for Python 3.14

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:31.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1:31.0-11
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:31.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1:31.0-9
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:31.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:31.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 27 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:31.0-6
- Workaround for python3.12 distutils removal

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:31.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1:31.0-4
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:31.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:31.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Neal Gompa <ngompa@fedoraproject.org> - 1:31.0-1
- Release 31.0 (neal)
- imgcreate/creator.py: fix SELinux unmount order (3526918+cbs228)
- livecd-iso-to-disk: Remove useless test to fix issue #237 (fgrose)
- imgcreate/kickstart.py: correct setfiles relabeling (3526918+cbs228)
- fs.py:  Avoid bind mounting an existing file target. (fgrose)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1:30.0-2
- Rebuilt for Python 3.11

* Tue Apr 26 2022 Neal Gompa <ngompa@fedoraproject.org> - 1:30.0-1
- Release 30.0 (ngompa13)
- imgcreate/fs.py: abort on hard-unmount failure (lersek)
- imgcreate/util: Fix errors import (T-vK) (#2078710)

* Sun Apr 24 2022 Neal Gompa <ngompa@fedoraproject.org> - 1:29.0-1
- Release 29.0 (ngompa13)
- Makefile: Drop creating signed tags (ngompa13)
- Preload the libnss_systemd library (#2007045) (sergey)
- livecd-iso-to-disk, editliveos: Add option to skip macboot.img processing.
  (fgrose)
- Copy 'unicode.pf2' from correct path (zhanggyb)
- editliveos: Refresh vmlinuz & initrd.img files upon kernel updates. (fgrose)
- livecd-iso-to-disk & editliveos: Preserve extra-kernel-args from source.
  (fgrose)
- add livenet dracut module to allow for pxe boot (sobjerke)
- switch from authconfig to authselect (pbrezina)
- live.py: Support either /images or /isolinux directories for efi images.
  (fgrose)
- livecd-iso-to-disk & editliveos: Expand partitioning & filesystem support
  (fgrose)
- make live image the default boot option (sobjerke)
- Modernize detection of checkisomd5 (m.novosyolov)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:28.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Neal Gompa <ngompa@fedoraproject.org> - 1:28.3-4
- Backport fix for finding unicode grub2 font file (rhbz#2037096)
