Name:           txnupd-rootfs
Version:        1.0
Release:        1%{?dist}
Summary:        Read-only root file system support for transactional updates

License:        GPL-2.0-or-later
URL:            https://codeberg.org/KalpaDesktop/txnupd-rootfs
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  bash
BuildRequires:  btrfs-progs
BuildRequires:  cmake
BuildRequires:  coreutils
BuildRequires:  python3
BuildRequires:  rsync
BuildRequires:  scdoc
BuildRequires:  systemd
BuildRequires:  util-linux

Requires:       python3
Requires:       btrfs-progs
Requires:       coreutils
Requires:       rsync
Requires:       systemd
Requires:       util-linux
# /etc subvolumes are managed by the snapper plugin of tukit, which pulls in
# tukit and snapper
Requires:       tukit-snapper-plugin
Recommends:     libdnf5-plugin-txnupd
# grub2-editenv, to set up the GRUB environment block on btrfs
Recommends:     grub2-tools-minimal

%description
Support files for running Fedora with a read-only root file system and
transactional updates (tukit, libdnf5-plugin-txnupd) on btrfs.

This package contains

 - txnupd-rootfs-setup, which prepares the btrfs root file system of a NEW
   installation: it turns /etc into a nested subvolume and adjusts fstab.

Installing this package does not change the system. The root file system is
only converted when an installer or an image build runs txnupd-rootfs-setup
against a target that is not the running system; converting an installed,
running system is deliberately not supported.


%package -n dracut-volatile-overlay
Summary:        Dracut module to mount tmpfs overlays on /etc and /var
# Taken from the openSUSE read-only-root-fs package, whose files carry no
# per-file notice and whose COPYING is the plain GPL, version 2: "or later" is
# not granted there, so it is not claimed here either.
License:        GPL-2.0-only
Requires:       dracut

%description -n dracut-volatile-overlay
A dracut module that mounts an overlay file system on /etc and on /var, with
the upper layer in a tmpfs, so that a system with a read-only root file system
boots with writable, non-persistent /etc and /var. To have more persistent
locations, such as /root or /home, add further fstab entries.

The module is never included in an initramfs by default. Request it
explicitly, for example with

  add_dracutmodules+=" volatile-overlay "

in a file in /etc/dracut.conf.d/.


%prep
%autosetup -C

%conf
%cmake

%build
%cmake_build

%install
%cmake_install


%check
bash tests/test-fstab.sh
# creates real subvolumes, so it is skipped when the build directory is not on
# btrfs (as in mock)
WORKDIR=%{_builddir} bash tests/test-setup.sh


%files
%license COPYING
%{_sbindir}/txnupd-rootfs-setup
%{_mandir}/man8/txnupd-rootfs-setup.8*


%files -n dracut-volatile-overlay
%license COPYING
%{_prefix}/lib/dracut/modules.d/99volatile-overlay/


%changelog
* Thu Nov 05 2026 Shawn W Dunn <sfalken@kalpadesktop.org> - 1.0-1
- Initial Packaging

