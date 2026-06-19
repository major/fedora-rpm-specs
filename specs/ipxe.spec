# ROMS we want for QEMU with format PCIID:QEMUNAME
%global qemuroms \\\
  8086100e:e1000 \\\
  10ec8139:rtl8139 \\\
  1af41000:virtio \\\
  808610d3:e1000e

%if 0%{?fedora}
# Fedora specific roms
%global qemuroms %{qemuroms} \\\
  10222000:pcnet \\\
  10ec8029:ne2k_pci \\\
  80861209:eepro100 \\\
  15ad07b0:vmxnet3
%endif

# We only build the ROMs if on an EFI build host. The resulting
# binary RPM will be noarch, so other archs will still be able
# to use the binary ROMs.
%global buildarches x86_64 aarch64

# debugging firmwares does not go the same way as a normal program.
# moreover, all architectures providing debuginfo for a single noarch
# package is currently clashing in koji, so don't bother.
%global debug_package %{nil}

%global forgeurl https://github.com/ipxe/ipxe/
%global commit 13a83f4ab30bd75831261e6b197903244f1ad753
%global date 20260614
%global version0 2.0.0
%forgemeta

Name:    ipxe
Summary: A network boot loader
Epoch:   1
Version: %forgeversion
Release: %autorelease

License: BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-only AND (GPL-2.0-only OR MPL-1.1) AND GPL-2.0-or-later AND GPL-2.0-or-later WITH UBDL-exception AND ISC AND MIT
URL:     http://ipxe.org/

Source:  %forgesource

# Enable IPv6 for qemu's config
# Sent upstream: http://lists.ipxe.org/pipermail/ipxe-devel/2015-November/004494.html
Patch0001: 0001-build-customize-configuration.patch
Patch0002: 0002-Use-spec-compliant-timeouts.patch

%ifarch %{buildarches}
BuildRequires: perl-interpreter
BuildRequires: perl-Getopt-Long
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
BuildRequires: perl-FindBin
BuildRequires: perl-lib
%endif
%ifarch x86_64
BuildRequires: syslinux
%endif
BuildRequires: mtools
BuildRequires: xorriso
BuildRequires: edk2-tools
BuildRequires: xz-devel
BuildRequires: gcc
BuildRequires: binutils-devel
BuildRequires: make

Obsoletes: gpxe <= 1.0.1
%endif

%ifarch x86_64
%package bootimgs-x86
Summary: X86 Network boot loader images
BuildArch: noarch
Provides: %{name}-bootimgs = %{version}-%{release}
Obsoletes: %{name}-bootimgs < 20200823-9.git4bd064de
Obsoletes: gpxe-bootimgs <= 1.0.1

%package roms-qemu
Summary: Network boot loader roms supported by QEMU, .rom format
BuildArch: noarch
Obsoletes: gpxe-roms-qemu <= 1.0.1

%description bootimgs-x86
iPXE is an open source network bootloader.

This package contains iPXE x86 boot images for UEFI (snponly.efi) and
BIOS (undionly.kpxe).

%description roms-qemu
iPXE is an open source network bootloader. It provides a direct
replacement for proprietary PXE ROMs, with many extra features such as
DNS, HTTP, iSCSI, etc.

This package contains the iPXE ROMs for devices emulated by QEMU, in
.rom format.
%endif

%ifarch aarch64
%package bootimgs-aarch64
Summary: ARM Network boot loader images
BuildArch: noarch

%description bootimgs-aarch64
iPXE is an open source network bootloader.

This package contains iPXE aarch64 boot images for UEFI (snponly.efi).
%endif

%description
iPXE is an open source network bootloader. It provides a direct
replacement for proprietary PXE ROMs, with many extra features such as
DNS, HTTP, iSCSI, etc.

%prep
%forgeautosetup -p1

%build
cd src

make_ipxe() {
    make %{?_smp_mflags} \
        NO_WERROR=1 V=1 \
        GITVERSION=%{commit} \
        "$@"
}

%ifarch x86_64

make_ipxe bin-x86_64-efi/snponly.efi

make_ipxe ISOLINUX_BIN=/usr/share/syslinux/isolinux.bin \
    bin/undionly.kpxe

# build roms with efi support for qemu
mkdir bin-combined
for romstr in %{qemuroms}; do
  rom=$(echo "$romstr" | cut -d ":" -f 1)

  make_ipxe CONFIG=qemu bin/${rom}.rom
  make_ipxe CONFIG=qemu bin-x86_64-efi/${rom}.efidrv
  vid="0x${rom%%????}"
  did="0x${rom#????}"
  EfiRom -f "$vid" -i "$did" --pci23 \
         -ec bin-x86_64-efi/${rom}.efidrv \
         -o  bin-combined/${rom}.eficrom
  util/catrom.pl \
      bin/${rom}.rom \
      bin-combined/${rom}.eficrom \
      > bin-combined/${rom}.rom
  EfiRom -d  bin-combined/${rom}.rom
  # truncate to at least 256KiB
  truncate -s \>256K bin-combined/${rom}.rom
  # verify rom fits in 256KiB
  test $(stat -c '%s' bin-combined/${rom}.rom) -le $((256 * 1024))
done

%endif

%ifarch aarch64
make_ipxe bin-arm64-efi/snponly.efi
%endif

%install
%ifarch x86_64
mkdir -p %{buildroot}/%{_datadir}/%{name}/
mkdir -p %{buildroot}/%{_datadir}/%{name}.efi/

pushd src/bin/
cp -a undionly.kpxe %{buildroot}/%{_datadir}/%{name}/
popd

cp -a src/bin-x86_64-efi/snponly.efi %{buildroot}/%{_datadir}/%{name}/ipxe-snponly-x86_64.efi

mkdir -p %{buildroot}%{_datadir}/%{name}/qemu/

for romstr in %{qemuroms}; do
  # the roms supported by qemu will be packaged separatedly
  # remove from the main rom list and add them to qemu.list
  rom=$(echo "$romstr" | cut -d ":" -f 1)
  qemuname=$(echo "$romstr" | cut -d ":" -f 2)
  echo %{_datadir}/%{name}/${rom}.rom >> qemu.rom.list

  cp src/bin/${rom}.rom %{buildroot}/%{_datadir}/%{name}/
  cp src/bin-combined/${rom}.rom %{buildroot}/%{_datadir}/%{name}.efi/
  echo %{_datadir}/%{name}.efi/${rom}.rom >> qemu.rom.list

  # Set up symlinks with expected qemu firmware names
  ln -s ../../ipxe/${rom}.rom %{buildroot}%{_datadir}/%{name}/qemu/pxe-${qemuname}.rom
  ln -s ../../ipxe.efi/${rom}.rom %{buildroot}%{_datadir}/%{name}/qemu/efi-${qemuname}.rom
done

# endif x86_64
%endif

%ifarch aarch64
mkdir -p %{buildroot}/%{_datadir}/%{name}/arm64-efi
cp -a src/bin-arm64-efi/snponly.efi %{buildroot}/%{_datadir}/%{name}/arm64-efi/snponly.efi
%endif

%ifarch x86_64
%files bootimgs-x86
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/undionly.kpxe
%{_datadir}/%{name}/ipxe-snponly-x86_64.efi
%doc COPYING COPYING.GPLv2 COPYING.UBDL

%files roms-qemu -f qemu.rom.list
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}.efi
%{_datadir}/%{name}/qemu
%doc COPYING COPYING.GPLv2 COPYING.UBDL
%endif

%ifarch aarch64
%files bootimgs-aarch64
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/arm64-efi
%{_datadir}/%{name}/arm64-efi/snponly.efi
%endif

%changelog
%autochangelog
