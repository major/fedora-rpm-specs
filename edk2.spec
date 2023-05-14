# https://fedoraproject.org/wiki/Changes/SetBuildFlagsBuildCheck
# breaks cross-building
%undefine _auto_set_build_flags

# actual firmware builds support cross-compiling.  edk2-tools
# in theory should build everywhere without much trouble, but
# in practice the edk2 build system barfs on archs it doesn't know
# (such as ppc), so lets limit things to the known-good ones.
ExclusiveArch: x86_64 aarch64

# edk2-stable202302
%define GITDATE        20230301
%define GITCOMMIT      f80f052277c8
%define TOOLCHAIN      GCC5
%define OPENSSL_VER    1.1.1k

%define DBXDATE        20230509

%if %{defined rhel}
%define build_ovmf 0
%define build_aarch64 0
%ifarch x86_64
  %define build_ovmf 1
%endif
%ifarch aarch64
  %define build_aarch64 1
%endif
%define build_riscv64 0
%else
%define build_ovmf 1
%define build_aarch64 1
%define build_riscv64 1
%endif

%global softfloat_version 20180726-gitb64af41
%define cross %{defined fedora}
%define disable_werror %{defined fedora}


Name:       edk2
Version:    %{GITDATE}git%{GITCOMMIT}
Release:    %autorelease
Summary:    UEFI firmware for 64-bit virtual machines
License:    BSD-2-Clause-Patent and OpenSSL and MIT
URL:        http://www.tianocore.org

# The source tarball is created using following commands:
# COMMIT=bb1bba3d7767
# git archive --format=tar --prefix=edk2-$COMMIT/ $COMMIT \
# | xz -9ev >/tmp/edk2-$COMMIT.tar.xz
Source0: edk2-%{GITCOMMIT}.tar.xz
Source1: ovmf-whitepaper-c770f8c.txt
Source2: openssl-rhel-d00c3c5b8a9d6d3ea3dabfcafdf36afd61ba8bcc.tar.xz
Source3: softfloat-%{softfloat_version}.tar.xz
Source4: edk2-platforms-54306d023e7d.tar.xz
Source5: jansson-2.13.1.tar.bz2

# json description files
Source10: 50-edk2-aarch64-qcow2.json
Source11: 51-edk2-aarch64-raw.json
Source12: 52-edk2-aarch64-verbose-qcow2.json
Source13: 53-edk2-aarch64-verbose-raw.json

Source20: 50-edk2-arm-verbose.json

Source30: 30-edk2-ovmf-ia32-sb-enrolled.json
Source31: 40-edk2-ovmf-ia32-sb.json
Source32: 50-edk2-ovmf-ia32-nosb.json

Source40: 30-edk2-ovmf-4m-qcow2-x64-sb-enrolled.json
Source41: 31-edk2-ovmf-2m-raw-x64-sb-enrolled.json
Source42: 40-edk2-ovmf-4m-qcow2-x64-sb.json
Source43: 41-edk2-ovmf-2m-raw-x64-sb.json
Source44: 50-edk2-ovmf-x64-microvm.json
Source45: 50-edk2-ovmf-4m-qcow2-x64-nosb.json
Source46: 51-edk2-ovmf-2m-raw-x64-nosb.json
Source47: 60-edk2-ovmf-x64-amdsev.json
Source48: 60-edk2-ovmf-x64-inteltdx.json

# https://gitlab.com/kraxel/edk2-build-config
Source80: edk2-build.py
Source81: edk2-build.fedora
Source82: edk2-build.fedora.platforms
Source83: edk2-build.rhel-9

Source90: DBXUpdate-%{DBXDATE}.x64.bin
Source91: DBXUpdate-%{DBXDATE}.ia32.bin

Patch0001: 0001-BaseTools-do-not-build-BrotliCompress-RH-only.patch
Patch0002: 0002-MdeModulePkg-remove-package-private-Brotli-include-p.patch
Patch0003: 0003-MdeModulePkg-TerminalDxe-set-xterm-resolution-on-mod.patch
Patch0004: 0004-OvmfPkg-take-PcdResizeXterm-from-the-QEMU-command-li.patch
Patch0005: 0005-ArmVirtPkg-take-PcdResizeXterm-from-the-QEMU-command.patch
Patch0006: 0006-OvmfPkg-enable-DEBUG_VERBOSE-RHEL-only.patch
Patch0007: 0007-OvmfPkg-silence-DEBUG_VERBOSE-0x00400000-in-QemuVide.patch
Patch0008: 0008-ArmVirtPkg-silence-DEBUG_VERBOSE-0x00400000-in-QemuR.patch
Patch0009: 0009-OvmfPkg-QemuRamfbDxe-Do-not-report-DXE-failure-on-Aa.patch
Patch0010: 0010-OvmfPkg-silence-EFI_D_VERBOSE-0x00400000-in-NvmExpre.patch
Patch0011: 0011-CryptoPkg-OpensslLib-list-RHEL8-specific-OpenSSL-fil.patch
Patch0012: 0012-OvmfPkg-QemuKernelLoaderFsDxe-suppress-error-on-no-k.patch
Patch0013: 0013-SecurityPkg-Tcg2Dxe-suppress-error-on-no-swtpm-in-si.patch
Patch0014: 0014-SecurityPkg-add-TIS-sanity-check-tpm2.patch
Patch0015: 0015-SecurityPkg-add-TIS-sanity-check-tpm12.patch
Patch0016: 0016-OvmfPkg-Clarify-invariants-for-NestedInterruptTplLib.patch
Patch0017: 0017-OvmfPkg-Relax-assertion-that-interrupts-do-not-occur.patch


# python3-devel and libuuid-devel are required for building tools.
# python3-devel is also needed for varstore template generation and
# verification with "ovmf-vars-generator".
BuildRequires:  python3-devel
BuildRequires:  libuuid-devel
BuildRequires:  /usr/bin/iasl
BuildRequires:  binutils gcc git gcc-c++ make
BuildRequires:  qemu-img

%if %{build_ovmf}
# Only OVMF includes 80x86 assembly files (*.nasm*).
BuildRequires:  nasm

# Only OVMF includes the Secure Boot feature, for which we need to separate out
# the UEFI shell.
BuildRequires:  dosfstools
BuildRequires:  mtools
BuildRequires:  xorriso

# For generating the variable store template with the default certificates
# enrolled.
BuildRequires:  python3-virt-firmware >= 23.5

# endif build_ovmf
%endif

%if %{cross}
BuildRequires:  gcc-aarch64-linux-gnu
BuildRequires:  gcc-arm-linux-gnu
BuildRequires:  gcc-x86_64-linux-gnu
BuildRequires:  gcc-riscv64-linux-gnu
%endif



%package ovmf
Summary:    UEFI firmware for x86_64 virtual machines
BuildArch:  noarch
Provides:   OVMF = %{version}-%{release}
Obsoletes:  OVMF < 20180508-100.gitee3198e672e2.el7

# OVMF includes the Secure Boot and IPv6 features; it has a builtin OpenSSL
# library.
Provides:   bundled(openssl) = %{OPENSSL_VER}
License:    BSD-2-Clause-Patent and OpenSSL

# URL taken from the Maintainers.txt file.
URL:        http://www.tianocore.org/ovmf/

%description ovmf
OVMF (Open Virtual Machine Firmware) is a project to enable UEFI support for
Virtual Machines. This package contains a sample 64-bit UEFI firmware for QEMU
and KVM.


%package aarch64
Summary:    UEFI firmware for aarch64 virtual machines
BuildArch:  noarch
Provides:   AAVMF = %{version}-%{release}
Obsoletes:  AAVMF < 20180508-100.gitee3198e672e2.el7

# need libvirt version with qcow2 support
Conflicts:  libvirt-daemon-driver-qemu < 9.2.0

# No Secure Boot for AAVMF yet, but we include OpenSSL for the IPv6 stack.
Provides:   bundled(openssl) = %{OPENSSL_VER}
License:    BSD-2-Clause-Patent and OpenSSL

# URL taken from the Maintainers.txt file.
URL:        https://github.com/tianocore/tianocore.github.io/wiki/ArmVirtPkg

%description aarch64
AAVMF (ARM Architecture Virtual Machine Firmware) is an EFI Development Kit II
platform that enables UEFI support for QEMU/KVM ARM Virtual Machines. This
package contains a 64-bit build.


%package tools
Summary:        EFI Development Kit II Tools
License:        BSD-2-Clause-Patent
URL:            https://github.com/tianocore/tianocore.github.io/wiki/BaseTools
%description tools
This package provides tools that are needed to
build EFI executables and ROMs using the GNU tools.

%package tools-doc
Summary:        Documentation for EFI Development Kit II Tools
BuildArch:      noarch
License:        BSD-2-Clause-Patent
URL:            https://github.com/tianocore/tianocore.github.io/wiki/BaseTools
%description tools-doc
This package documents the tools that are needed to
build EFI executables and ROMs using the GNU tools.

%description
EDK II is a modern, feature-rich, cross-platform firmware development
environment for the UEFI and PI specifications. This package contains sample
64-bit UEFI firmware builds for QEMU and KVM.


%if %{defined fedora}
%package ovmf-ia32
Summary:        Open Virtual Machine Firmware
License:        BSD-2-Clause-Patent and OpenSSL
Provides:       bundled(openssl)
BuildArch:      noarch
%description ovmf-ia32
EFI Development Kit II
Open Virtual Machine Firmware (ia32)

%package ovmf-xen
Summary:        Open Virtual Machine Firmware, Xen build
License:        BSD-2-Clause-Patent and OpenSSL
Provides:       bundled(openssl)
BuildArch:      noarch
%description ovmf-xen
EFI Development Kit II
Open Virtual Machine Firmware (Xen build)

%package ovmf-experimental
Summary:        Open Virtual Machine Firmware, experimental builds
License:        BSD-2-Clause-Patent and OpenSSL
Provides:       bundled(openssl)
BuildArch:      noarch
%description ovmf-experimental
EFI Development Kit II
Open Virtual Machine Firmware (experimental builds)

%package arm
Summary:        ARM Virtual Machine Firmware
BuildArch:      noarch
License:        BSD-2-Clause-Patent and OpenSSL
%description arm
EFI Development Kit II
ARMv7 UEFI Firmware

%package riscv64
Summary:        RISC-V Virtual Machine Firmware
BuildArch:      noarch
License:        BSD-2-Clause-Patent and OpenSSL
%description riscv64
EFI Development Kit II
RISC-V UEFI Firmware

%package ext4
Summary:        Ext4 filesystem driver
License:        BSD-2-Clause-Patent and OpenSSL
BuildArch:      noarch
%description ext4
EFI Development Kit II
Ext4 filesystem driver

%package tools-python
Summary:        EFI Development Kit II Tools
Requires:       python3
BuildArch:      noarch

%description tools-python
This package provides tools that are needed to build EFI executables
and ROMs using the GNU tools.  You do not need to install this package;
you probably want to install edk2-tools only.
# endif fedora
%endif



%prep
# We needs some special git config options that %%autosetup won't give us.
# We init the git dir ourselves, then tell %%autosetup not to blow it away.
%setup -q -n edk2-%{GITCOMMIT}
git init -q
git config core.whitespace cr-at-eol
git config am.keepcr true
# -T is passed to %%setup to not re-extract the archive
# -D is passed to %%setup to not delete the existing archive dir
%autosetup -T -D -n edk2-%{GITCOMMIT} -S git_am

cp -a -- %{SOURCE1} .
tar -C CryptoPkg/Library/OpensslLib -a -f %{SOURCE2} -x
# extract softfloat into place
tar -xf %{SOURCE3} --strip-components=1 --directory ArmPkg/Library/ArmSoftFloatLib/berkeley-softfloat-3/
tar -xf %{SOURCE4} --strip-components=1 "*/Drivers" "*/Features" "*/Platform" "*/Silicon"
tar -xf %{SOURCE5} --strip-components=1 --directory RedfishPkg/Library/JsonLib/jansson

# Done by %setup, but we do not use it for the auxiliary tarballs
chmod -Rf a+rX,u+w,g-w,o-w .

cp -a -- \
   %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} \
   %{SOURCE20} \
   %{SOURCE30} %{SOURCE31} %{SOURCE32} \
   %{SOURCE40} %{SOURCE41} %{SOURCE42} %{SOURCE43} %{SOURCE44} \
   %{SOURCE45} %{SOURCE46} %{SOURCE47} %{SOURCE48} \
   %{SOURCE80} %{SOURCE81} %{SOURCE82} %{SOURCE83} \
   %{SOURCE90} %{SOURCE91} \
   .

%build

build_iso() {
  dir="$1"
  UEFI_SHELL_BINARY=${dir}/Shell.efi
  ENROLLER_BINARY=${dir}/EnrollDefaultKeys.efi
  UEFI_SHELL_IMAGE=uefi_shell.img
  ISO_IMAGE=${dir}/UefiShell.iso

  UEFI_SHELL_BINARY_BNAME=$(basename -- "$UEFI_SHELL_BINARY")
  UEFI_SHELL_SIZE=$(stat --format=%s -- "$UEFI_SHELL_BINARY")
  ENROLLER_SIZE=$(stat --format=%s -- "$ENROLLER_BINARY")

  # add 1MB then 10% for metadata
  UEFI_SHELL_IMAGE_KB=$((
    (UEFI_SHELL_SIZE + ENROLLER_SIZE + 1 * 1024 * 1024) * 11 / 10 / 1024
  ))

  # create non-partitioned FAT image
  rm -f -- "$UEFI_SHELL_IMAGE"
  mkdosfs -C "$UEFI_SHELL_IMAGE" -n UEFI_SHELL -- "$UEFI_SHELL_IMAGE_KB"

  # copy the shell binary into the FAT image
  export MTOOLS_SKIP_CHECK=1
  mmd   -i "$UEFI_SHELL_IMAGE"                       ::efi
  mmd   -i "$UEFI_SHELL_IMAGE"                       ::efi/boot
  mcopy -i "$UEFI_SHELL_IMAGE"  "$UEFI_SHELL_BINARY" ::efi/boot/bootx64.efi
  mcopy -i "$UEFI_SHELL_IMAGE"  "$ENROLLER_BINARY"   ::
  mdir  -i "$UEFI_SHELL_IMAGE"  -/                   ::

  # build ISO with FAT image file as El Torito EFI boot image
  mkisofs -input-charset ASCII -J -rational-rock \
    -e "$UEFI_SHELL_IMAGE" -no-emul-boot \
    -o "$ISO_IMAGE" "$UEFI_SHELL_IMAGE"
}

export EXTRA_OPTFLAGS="%{optflags}"
export EXTRA_LDFLAGS="%{__global_ldflags}"
export RELEASE_DATE="$(echo %{GITDATE} | sed -e 's|\(....\)\(..\)\(..\)|\2/\3/\1|')"

touch OvmfPkg/AmdSev/Grub/grub.efi   # dummy

%if %{build_ovmf}
%if %{defined rhel}

./edk2-build.py --config edk2-build.rhel-9 --silent --release-date "$RELEASE_DATE" -m ovmf
virt-fw-vars --input   RHEL-9/ovmf/OVMF_VARS.fd \
             --output  RHEL-9/ovmf/OVMF_VARS.secboot.fd \
             --set-dbx DBXUpdate-%{DBXDATE}.x64.bin \
             --enroll-redhat --secure-boot
build_iso RHEL-9/ovmf

%else

./edk2-build.py --config edk2-build.fedora --silent --release-date "$RELEASE_DATE" -m ovmf
./edk2-build.py --config edk2-build.fedora.platforms --silent -m x64
virt-fw-vars --input   Fedora/ovmf/OVMF_VARS.fd \
             --output  Fedora/ovmf/OVMF_VARS.secboot.fd \
             --set-dbx DBXUpdate-%{DBXDATE}.x64.bin \
             --enroll-redhat --secure-boot
virt-fw-vars --input   Fedora/ovmf-4m/OVMF_VARS.fd \
             --output  Fedora/ovmf-4m/OVMF_VARS.secboot.fd \
             --set-dbx DBXUpdate-%{DBXDATE}.x64.bin \
             --enroll-redhat --secure-boot
virt-fw-vars --input   Fedora/ovmf-ia32/OVMF_VARS.fd \
             --output  Fedora/ovmf-ia32/OVMF_VARS.secboot.fd \
             --set-dbx DBXUpdate-%{DBXDATE}.ia32.bin \
             --enroll-redhat --secure-boot
build_iso Fedora/ovmf
build_iso Fedora/ovmf-ia32

for raw in */ovmf-4m/*.fd; do
    qcow2="${raw%.fd}.qcow2"
    qemu-img convert -f raw -O qcow2 -o cluster_size=4096 -S 4096 "$raw" "$qcow2"
    rm -f "$raw"
done

# experimental stateless builds
virt-fw-vars --input   Fedora/experimental/OVMF.stateless.fd \
             --output  Fedora/experimental/OVMF.stateless.secboot.fd \
             --set-dbx DBXUpdate-%{DBXDATE}.x64.bin \
             --enroll-redhat --secure-boot

for image in \
	Fedora/ovmf/OVMF_CODE.secboot.fd \
	Fedora/ovmf-4m/OVMF_CODE.secboot.qcow2 \
	Fedora/experimental/OVMF.stateless.secboot.fd \
; do
	pcr="${image%.fd}.pcr"
	python3 /usr/share/doc/python3-virt-firmware/experimental/measure.py \
		--image "$image" \
		--version "%{name}-%{version}-%{release}" \
                --no-shim \
		> "$pcr"
done

%endif
%endif

%if %{build_aarch64}
%if %{defined rhel}
./edk2-build.py --config edk2-build.rhel-9 --silent --release-date "$RELEASE_DATE" -m armvirt
%else
./edk2-build.py --config edk2-build.fedora --silent --release-date "$RELEASE_DATE" -m armvirt
./edk2-build.py --config edk2-build.fedora.platforms --silent -m aa64
%endif
for raw in */aarch64/*.raw; do
    qcow2="${raw%.raw}.qcow2"
    qemu-img convert -f raw -O qcow2 -o cluster_size=4096 -S 4096 "$raw" "$qcow2"
done
%endif

%if %{build_riscv64}
./edk2-build.py --config edk2-build.fedora --silent --release-date "$RELEASE_DATE" -m riscv
./edk2-build.py --config edk2-build.fedora.platforms --silent -m riscv
%endif

%install

cp -a OvmfPkg/License.txt License.OvmfPkg.txt
cp -a CryptoPkg/Library/OpensslLib/openssl/LICENSE LICENSE.openssl
mkdir -p %{buildroot}%{_datadir}/qemu/firmware

# install the tools
mkdir -p %{buildroot}%{_bindir} \
         %{buildroot}%{_datadir}/%{name}/Conf \
         %{buildroot}%{_datadir}/%{name}/Scripts
install BaseTools/Source/C/bin/* \
        %{buildroot}%{_bindir}
install BaseTools/BinWrappers/PosixLike/LzmaF86Compress \
        %{buildroot}%{_bindir}
install BaseTools/BuildEnv \
        %{buildroot}%{_datadir}/%{name}
install BaseTools/Conf/*.template \
        %{buildroot}%{_datadir}/%{name}/Conf
install BaseTools/Scripts/GccBase.lds \
        %{buildroot}%{_datadir}/%{name}/Scripts

# install firmware images
mkdir -p %{buildroot}%{_datadir}/%{name}
%if %{defined rhel}
cp -av RHEL-9/* %{buildroot}%{_datadir}/%{name}
%else
cp -av Fedora/* %{buildroot}%{_datadir}/%{name}
%endif


%if %{build_ovmf}

# compat symlinks
mkdir -p %{buildroot}%{_datadir}/OVMF
ln -s ../%{name}/ovmf/OVMF_CODE.fd         %{buildroot}%{_datadir}/OVMF/
ln -s ../%{name}/ovmf/OVMF_CODE.secboot.fd %{buildroot}%{_datadir}/OVMF/
ln -s ../%{name}/ovmf/OVMF_VARS.fd         %{buildroot}%{_datadir}/OVMF/
ln -s ../%{name}/ovmf/OVMF_VARS.secboot.fd %{buildroot}%{_datadir}/OVMF/
ln -s ../%{name}/ovmf/UefiShell.iso        %{buildroot}%{_datadir}/OVMF/
ln -s OVMF_CODE.fd %{buildroot}%{_datadir}/%{name}/ovmf/OVMF_CODE.cc.fd

# json description files
mkdir -p %{buildroot}%{_datadir}/qemu/firmware
install -m 0644 \
        30-edk2-ovmf-4m-qcow2-x64-sb-enrolled.json \
        31-edk2-ovmf-2m-raw-x64-sb-enrolled.json \
        40-edk2-ovmf-4m-qcow2-x64-sb.json \
        41-edk2-ovmf-2m-raw-x64-sb.json \
        50-edk2-ovmf-4m-qcow2-x64-nosb.json \
        51-edk2-ovmf-2m-raw-x64-nosb.json \
        60-edk2-ovmf-x64-amdsev.json \
        60-edk2-ovmf-x64-inteltdx.json \
        %{buildroot}%{_datadir}/qemu/firmware
%if %{defined fedora}
install -m 0644 \
        50-edk2-ovmf-x64-microvm.json \
        30-edk2-ovmf-ia32-sb-enrolled.json \
        40-edk2-ovmf-ia32-sb.json \
        50-edk2-ovmf-ia32-nosb.json \
        %{buildroot}%{_datadir}/qemu/firmware
%endif

# endif build_ovmf
%endif

%if %{build_aarch64}

# compat symlinks
mkdir -p %{buildroot}%{_datadir}/AAVMF
ln -s ../%{name}/aarch64/QEMU_EFI-pflash.raw \
  %{buildroot}%{_datadir}/AAVMF/AAVMF_CODE.verbose.fd
ln -s ../%{name}/aarch64/QEMU_EFI-silent-pflash.raw \
  %{buildroot}%{_datadir}/AAVMF/AAVMF_CODE.fd
ln -s ../%{name}/aarch64/vars-template-pflash.raw \
  %{buildroot}%{_datadir}/AAVMF/AAVMF_VARS.fd
%if %{defined fedora}
ln -s ../%{name}/arm/QEMU_EFI-pflash.raw \
   %{buildroot}%{_datadir}/AAVMF/AAVMF32_CODE.fd
%endif

# json description files
install -m 0644 \
        50-edk2-aarch64-qcow2.json \
        51-edk2-aarch64-raw.json \
        52-edk2-aarch64-verbose-qcow2.json \
        53-edk2-aarch64-verbose-raw.json \
        %{buildroot}%{_datadir}/qemu/firmware
%if %{defined fedora}
install -m 0644 \
        50-edk2-arm-verbose.json \
        %{buildroot}%{_datadir}/qemu/firmware
%endif

# endif build_aarch64
%endif

%if %{defined fedora}

# edk2-tools-python install
cp -R BaseTools/Source/Python %{buildroot}%{_datadir}/%{name}/Python
for i in build BPDG Ecc GenDepex GenFds GenPatchPcdTable PatchPcdValue TargetTool Trim UPT; do
echo '#!/bin/sh
export PYTHONPATH=%{_datadir}/%{name}/Python
exec python3 '%{_datadir}/%{name}/Python/$i/$i.py' "$@"' > %{buildroot}%{_bindir}/$i
  chmod +x %{buildroot}%{_bindir}/$i
done

%if 0%{?py_byte_compile:1}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python_Appendix/#manual-bytecompilation
%py_byte_compile %{python3} %{buildroot}%{_datadir}/edk2/Python
%endif

%endif

%check
for file in %{buildroot}%{_datadir}/%{name}/*/*VARS.secboot.fd; do
    test -f "$file" || continue
    virt-fw-vars --input $file --print | grep "SecureBootEnable.*ON" || exit 1
done

%global common_files \
  %%license License.txt License.OvmfPkg.txt License-History.txt LICENSE.openssl \
  %%dir %%{_datadir}/%%{name}/ \
  %%dir %%{_datadir}/qemu \
  %%dir %%{_datadir}/qemu/firmware

%if %{build_ovmf}
%files ovmf
%common_files
%doc OvmfPkg/README
%doc ovmf-whitepaper-c770f8c.txt
%dir %{_datadir}/OVMF/
%{_datadir}/OVMF/OVMF_CODE.fd
%{_datadir}/OVMF/OVMF_CODE.secboot.fd
%{_datadir}/OVMF/OVMF_VARS.fd
%{_datadir}/OVMF/OVMF_VARS.secboot.fd
%{_datadir}/OVMF/UefiShell.iso
%dir %{_datadir}/%{name}/ovmf/
%{_datadir}/%{name}/ovmf/OVMF_CODE.fd
%{_datadir}/%{name}/ovmf/OVMF_CODE.cc.fd
%{_datadir}/%{name}/ovmf/OVMF_CODE.secboot.fd
%{_datadir}/%{name}/ovmf/OVMF_VARS.fd
%{_datadir}/%{name}/ovmf/OVMF_VARS.secboot.fd
%{_datadir}/%{name}/ovmf/OVMF.amdsev.fd
%{_datadir}/%{name}/ovmf/OVMF.inteltdx.fd
%{_datadir}/%{name}/ovmf/UefiShell.iso
%{_datadir}/%{name}/ovmf/Shell.efi
%{_datadir}/%{name}/ovmf/EnrollDefaultKeys.efi
%{_datadir}/qemu/firmware/30-edk2-ovmf-4m-qcow2-x64-sb-enrolled.json
%{_datadir}/qemu/firmware/31-edk2-ovmf-2m-raw-x64-sb-enrolled.json
%{_datadir}/qemu/firmware/40-edk2-ovmf-4m-qcow2-x64-sb.json
%{_datadir}/qemu/firmware/41-edk2-ovmf-2m-raw-x64-sb.json
%{_datadir}/qemu/firmware/50-edk2-ovmf-4m-qcow2-x64-nosb.json
%{_datadir}/qemu/firmware/51-edk2-ovmf-2m-raw-x64-nosb.json
%{_datadir}/qemu/firmware/60-edk2-ovmf-x64-amdsev.json
%{_datadir}/qemu/firmware/60-edk2-ovmf-x64-inteltdx.json
%if %{defined fedora}
%{_datadir}/%{name}/ovmf/MICROVM.fd
%{_datadir}/qemu/firmware/50-edk2-ovmf-x64-microvm.json
%dir %{_datadir}/%{name}/ovmf-4m/
%{_datadir}/%{name}/ovmf-4m/OVMF_CODE.qcow2
%{_datadir}/%{name}/ovmf-4m/OVMF_CODE.secboot.qcow2
%{_datadir}/%{name}/ovmf-4m/OVMF_VARS.qcow2
%{_datadir}/%{name}/ovmf-4m/OVMF_VARS.secboot.qcow2
%{_datadir}/%{name}/ovmf/*.pcr
%{_datadir}/%{name}/ovmf-4m/*.pcr
%endif
# endif build_ovmf
%endif

%if %{build_aarch64}
%files aarch64
%common_files
%dir %{_datadir}/AAVMF/
%{_datadir}/AAVMF/AAVMF_CODE.verbose.fd
%{_datadir}/AAVMF/AAVMF_CODE.fd
%{_datadir}/AAVMF/AAVMF_VARS.fd
%dir %{_datadir}/%{name}/aarch64/
%{_datadir}/%{name}/aarch64/QEMU_EFI-pflash.*
%{_datadir}/%{name}/aarch64/QEMU_EFI-silent-pflash.*
%{_datadir}/%{name}/aarch64/vars-template-pflash.*
%{_datadir}/%{name}/aarch64/QEMU_EFI.fd
%{_datadir}/%{name}/aarch64/QEMU_EFI.silent.fd
%{_datadir}/%{name}/aarch64/QEMU_VARS.fd
%if %{defined fedora}
%{_datadir}/%{name}/aarch64/BL32_AP_MM.fd
%{_datadir}/%{name}/aarch64/QEMU_EFI.kernel.fd
%endif
%{_datadir}/qemu/firmware/50-edk2-aarch64-qcow2.json
%{_datadir}/qemu/firmware/51-edk2-aarch64-raw.json
%{_datadir}/qemu/firmware/52-edk2-aarch64-verbose-qcow2.json
%{_datadir}/qemu/firmware/53-edk2-aarch64-verbose-raw.json
# endif build_aarch64
%endif

%files tools
%license License.txt
%license License-History.txt
%{_bindir}/DevicePath
%{_bindir}/EfiRom
%{_bindir}/GenCrc32
%{_bindir}/GenFfs
%{_bindir}/GenFv
%{_bindir}/GenFw
%{_bindir}/GenSec
%{_bindir}/LzmaCompress
%{_bindir}/LzmaF86Compress
%{_bindir}/TianoCompress
%{_bindir}/VfrCompile
%{_bindir}/VolInfo
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/BuildEnv
%{_datadir}/%{name}/Conf
%{_datadir}/%{name}/Scripts

%files tools-doc
%doc BaseTools/UserManuals/*.rtf


%if %{defined fedora}
%if %{build_ovmf}
%files ovmf-ia32
%common_files
%dir %{_datadir}/%{name}/ovmf-ia32
%{_datadir}/%{name}/ovmf-ia32/EnrollDefaultKeys.efi
%{_datadir}/%{name}/ovmf-ia32/OVMF_CODE.fd
%{_datadir}/%{name}/ovmf-ia32/OVMF_CODE.secboot.fd
%{_datadir}/%{name}/ovmf-ia32/OVMF_VARS.fd
%{_datadir}/%{name}/ovmf-ia32/OVMF_VARS.secboot.fd
%{_datadir}/%{name}/ovmf-ia32/Shell.efi
%{_datadir}/%{name}/ovmf-ia32/UefiShell.iso
%{_datadir}/qemu/firmware/30-edk2-ovmf-ia32-sb-enrolled.json
%{_datadir}/qemu/firmware/40-edk2-ovmf-ia32-sb.json
%{_datadir}/qemu/firmware/50-edk2-ovmf-ia32-nosb.json

%files ovmf-experimental
%common_files
%dir %{_datadir}/%{name}/experimental
%{_datadir}/%{name}/experimental/*.fd
%{_datadir}/%{name}/experimental/*.raw
%{_datadir}/%{name}/experimental/*.pcr

%files ovmf-xen
%common_files
%dir %{_datadir}/%{name}/xen
%{_datadir}/%{name}/xen/*.fd
%endif

%files arm
%common_files
%dir %{_datadir}/AAVMF/
%{_datadir}/AAVMF/AAVMF32_CODE.fd
%dir %{_datadir}/%{name}/arm
%{_datadir}/%{name}/arm/QEMU_EFI-pflash.raw
%{_datadir}/%{name}/arm/QEMU_EFI.fd
%{_datadir}/%{name}/arm/QEMU_VARS.fd
%{_datadir}/%{name}/arm/vars-template-pflash.raw
%{_datadir}/qemu/firmware/50-edk2-arm-verbose.json

%files riscv64
%common_files
%{_datadir}/%{name}/riscv/*.fd
%{_datadir}/%{name}/riscv/*.raw

%files ext4
%common_files
%dir %{_datadir}/%{name}/drivers
%{_datadir}/%{name}/drivers/ext4*.efi


%files tools-python
%{_bindir}/build
%{_bindir}/BPDG
%{_bindir}/Ecc
%{_bindir}/GenDepex
%{_bindir}/GenFds
%{_bindir}/GenPatchPcdTable
%{_bindir}/PatchPcdValue
%{_bindir}/TargetTool
%{_bindir}/Trim
%{_bindir}/UPT
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/Python

# endif fedora
%endif


%changelog
%autochangelog
