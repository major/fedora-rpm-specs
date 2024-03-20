%global debug_package %{nil}

Summary:   Firmware update EFI binaries
Name:      fwupd-efi
Version:   1.5
Release:   %autorelease
License:   LGPL-2.1-or-later
URL:       https://github.com/fwupd/fwupd-efi
Source0:   http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz

# discussed in https://github.com/fwupd/fwupd-efi/pull/53
Patch01: 0001-Revert-lds-add-init_array-fini_array-sections.patch

# these are the only architectures supporting UEFI UpdateCapsule
ExclusiveArch: x86_64 aarch64

BuildRequires: gcc
BuildRequires: meson
BuildRequires: gnu-efi-devel
BuildRequires: pesign
BuildRequires: python3-pefile

%description
fwupd is a project to allow updating device firmware, and this package provides
the EFI binary that is used for updating using UpdateCapsule.

%prep
%autosetup -p1
# gnu-efi linker scripts (lds) are missing SBAT, included scripts are used
# instead but the build system expects the name to match
%ifarch x86_64
%global efiarch x64
%endif
%ifarch aarch64
%global efiarch aa64
%endif
ln -s elf_%{_arch}_efi.lds efi/lds/efi.lds
%ifarch aarch64
ln -s crt0-efi-%{_arch}.S efi/crt0/crt0-efi-%{efiarch}.S
%endif

%build

%meson \
    -Defi-libdir=%{_prefix}/lib \
    -Defi_sbat_distro_id="fedora" \
    -Defi_sbat_distro_summary="The Fedora Project" \
    -Defi_sbat_distro_pkgname="%{name}" \
    -Defi_sbat_distro_version="%{version}-%{release}" \
    -Defi_sbat_distro_url="https://src.fedoraproject.org/rpms/%{name}"

%meson_build

%install
%meson_install

# sign fwupd.efi loader
%global fwup_efi_fn $RPM_BUILD_ROOT%{_libexecdir}/fwupd/efi/fwupd%{efiarch}.efi
%pesign -s -i %{fwup_efi_fn} -o %{fwup_efi_fn}.tmp
%define __pesign_client_cert fwupd-signer
%pesign -s -i %{fwup_efi_fn}.tmp -o %{fwup_efi_fn}.signed
rm -vf %{fwup_efi_fn}.tmp

%files
%doc README.md AUTHORS
%license COPYING
%{_libexecdir}/fwupd/efi/*.efi
%{_libexecdir}/fwupd/efi/*.efi.signed
%{_libdir}/pkgconfig/fwupd-efi.pc

%changelog
%autochangelog
