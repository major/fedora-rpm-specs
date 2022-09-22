%global debug_package %{nil}

Summary:   Firmware update EFI binaries
Name:      fwupd-efi
Version:   1.3
Release:   2%{?dist}
License:   LGPLv2+
URL:       https://github.com/fwupd/fwupd-efi
Source0:   http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz

# these are the only architectures supporting UEFI UpdateCapsule
ExclusiveArch: x86_64 aarch64

BuildRequires: gcc
BuildRequires: meson
BuildRequires: gnu-efi-devel
BuildRequires: pesign

%description
fwupd is a project to allow updating device firmware, and this package provides
the EFI binary that is used for updating using UpdateCapsule.

%prep
%autosetup -p1

%build

%meson \
    -Defi_sbat_distro_id="fedora" \
    -Defi_sbat_distro_summary="The Fedora Project" \
    -Defi_sbat_distro_pkgname="%{name}" \
    -Defi_sbat_distro_version="%{version}-%{release}" \
    -Defi_sbat_distro_url="https://src.fedoraproject.org/rpms/%{name}"

%meson_build

%install
%meson_install

# not required yet
rm $RPM_BUILD_ROOT%{_libdir}/pkgconfig/fwupd-efi.pc

# sign fwupd.efi loader
%ifarch x86_64
%global efiarch x64
%endif
%ifarch aarch64
%global efiarch aa64
%endif
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

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr 14 2022 Richard Hughes <richard@hughsie.com> 1.3-1
- New package version
- Fix a regression when applying updates on an HP M60
- Fix the ARM system crt0 name
- Show the version when starting fwupd-efi

* Sun Jan 23 2022 Richard Hughes <richard@hughsie.com> 1.2-1
- New package version
- Sleep longer when no updates to process or event of error

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 19 2021 Richard Hughes <richard@hughsie.com> 1.1-1
- New package version
- Pass the found genpeimg to generate_binary

* Mon May 17 2021 Richard Hughes <richard@hughsie.com> 1.0-2
- Rebuilt to use the HSM signers.

* Mon Apr 26 2021 Richard Hughes <richard@hughsie.com> 1.0-1
- Initial package version, split from the main fwupd package
