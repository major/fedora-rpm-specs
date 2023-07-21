# EFI/UEFI binaries are not ELF, but PE32/PE32+/COFF
%global debug_package %{nil}

# Vendor name for the EFI System Partition directory
%global efi_vendor %{name}

# Git commit mentioned at https://github.com/pbatard/efifs
%global grub2_version    2.11-0
%global grub2_commit     d9b4638c50b16d4722e66d334e2c1a674b4a45cc

# Preferrably the latest stable version shipped in Fedora
%global edk2_stable_date 202205
%global edk2_stable_str  edk2-stable%{edk2_stable_date}

Summary:        Free software EFI/UEFI standalone file system drivers
Name:           efifs
Version:        1.9
Release:        3%{?dist}
License:        GPLv3+
URL:            https://efi.akeo.ie/
Source0:        https://github.com/pbatard/efifs/archive/v%{version}/%{name}-%{version}.tar.gz
# Fedora's grub2 RPM packages don't provide neither a -devel subpackage nor any
# patched GRUB2 sources such as grub-core/{kern/{err,list,misc},fs/{fshelp,<fs>}.c
Source1:        https://git.savannah.gnu.org/cgit/grub.git/snapshot/grub-%{grub2_commit}.tar.gz
# Fedora's edk2 RPM packages might be nice, but unusable for EfiFs depending on
# EDK II build artifacts and files such as MdePkg/MdePkg.dec, ShellPkg/ShellPkg.dec
Source2:        https://github.com/tianocore/edk2/archive/%{edk2_stable_str}.tar.gz
# Small helper script to enable EfiFs drivers using efibootmgr
Source3:        efifs-enable.sh
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libuuid-devel
BuildRequires:  python3
%ifarch x86_64 %{ix86}
BuildRequires:  nasm
%endif
BuildRequires:  efi-srpm-macros
ExclusiveArch:  %{efi}
Requires:       efi-filesystem
Provides:       bundled(grub2-efi-modules) = %{grub2_version}.git%(c=%{grub2_commit}; echo ${c:0:7})
Provides:       bundled(edk2-tools) = %{edk2_stable_date}01stable

%description
Free software EFI/UEFI standalone file system drivers, based on the GRUB 2.0
read-only drivers: AFFS (Amiga Fast FileSystem), BFS (BeOS FileSystem), btrfs,
exFAT, ext2/ext3/ext4, F2FS (experimental), HFS and HFS+ (Mac OS, including
the compression support), ISO9660, JFS (Journaled FileSystem), nilfs2, NTFS
(including compression support), ReiserFS, SFS (Amiga Smart FileSystem), UDF,
UFS/FFS, UFS2/FFS2, XFS, ZFS and more.

%prep
%setup -q -T -c %{name}-%{version} -a 0 -a 2
cp -p %{SOURCE3} .

pushd %{name}-%{version}
# Extract GRUB2 into place (Git submodule)
tar -xf %{SOURCE1} --strip-components=1 --directory grub

# Apply EfiFs upstream patch to GRUB2
cd grub && patch -Np1 -i ../0001-GRUB-fixes.patch
popd

pushd edk2-%{edk2_stable_str}

# Do not build BrotliCompress (because it's unused)
sed -e '/BrotliCompress/d' -i BaseTools/Source/C/GNUmakefile

# Symlink EfiFs into EDK II build-time working directory
ln -s ../%{name}-%{version} EfiFsPkg
popd

%build
pushd edk2-%{edk2_stable_str}
export PYTHON_COMMAND=%{__python3}
%make_build -C BaseTools EXTRA_OPTFLAGS="$RPM_OPT_FLAGS" EXTRA_LDFLAGS="$RPM_LD_FLAGS"
source ./edksetup.sh --reconfig

# EDK II violates UEFI 2.8 specification by not using AA64
%ifarch aarch64
%global efi_arch_upper AARCH64
%endif

# Fedora's armv7hl expects hardware floating-point ABI
%ifarch %{arm}
sed -e 's/-mfloat-abi=soft/-mfloat-abi=hard/' -i Conf/tools_def.txt
%endif

./EfiFsPkg/set_grub_cpu.sh %{efi_arch_upper}
build -a %{efi_arch_upper} -b RELEASE -t GCC5 -p EfiFsPkg/EfiFsPkg.dsc

%install
install -d -m 0700 $RPM_BUILD_ROOT%{efi_esp_dir}/
install -p -m 0700 edk2-%{edk2_stable_str}/Build/EfiFs/RELEASE_GCC5/%{efi_arch_upper}/*.efi $RPM_BUILD_ROOT%{efi_esp_dir}/

%files
%license %{name}-%{version}/LICENSE %{name}-%{version}/grub/COPYING
%doc %{name}-%{version}/ChangeLog.txt %{name}-%{version}/README.md efifs-enable.sh
%{efi_esp_dir}/

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 06 2022 Robert Scheck <robert@fedoraproject.org> 1.9-1
- Upgrade to 1.9 (#2124389)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr 18 2022 Robert Scheck <robert@fedoraproject.org> 1.8-3
- Update bundled edk2 to 202202 and add GCC 12 fixes (#2045335)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 21 2021 Robert Scheck <robert@fedoraproject.org> 1.8-1
- Upgrade to 1.8 (#1996231)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Nov 29 2020 Robert Scheck <robert@fedoraproject.org> 1.7-2
- Changes to match the Fedora Packaging Guidelines (#1902498)

* Wed Nov 25 2020 Robert Scheck <robert@fedoraproject.org> 1.7-1
- Upgrade to 1.7

* Fri May 01 2020 Robert Scheck <robert@fedoraproject.org> 1.5-1
- Upgrade to 1.5
- Initial spec file for Fedora and Red Hat Enterprise Linux
