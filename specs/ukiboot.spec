Name:		ukiboot
Version:	0.2.1
Release:	2%{?dist}
Summary:	A UEFI bootloader implementing UEFI based A/B boot
License:	LGPL-2.1-or-later
URL:		https://gitlab.com/CentOS/automotive/src/ukiboot
Source:		%{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:	efi-srpm-macros
BuildRequires:	gnu-efi-devel
BuildRequires:	python3
BuildRequires:	systemd
BuildRequires:	systemd-ukify
BuildRequires:	systemd-boot
Requires:	efi-filesystem

ExclusiveArch:	%{efi}

%description
A UEFI bootloader implementing UEFI based A/B boot similar to
android boot.

%prep
%autosetup -p1

%build
%meson -D esp-dir=EFI/%{efi_vendor}
%meson_build

%install
%meson_install

# Install the efi binaries into %{efi_esp_dir}
# We need these files to be owned by the rpm for bootupd to find the owning package.
mkdir -p %{buildroot}%{efi_esp_dir}/ukiboot_a.efi.extra.d
mkdir -p %{buildroot}%{efi_esp_dir}/ukiboot_b.efi.extra.d
install %{buildroot}%{_libexecdir}/ukiboot/efi/ukiboot*.efi %{buildroot}%{efi_esp_dir}/
install %{buildroot}%{_libexecdir}/ukiboot/efi/slot_a.addon.efi %{buildroot}%{efi_esp_dir}/ukiboot_a.efi.extra.d
install %{buildroot}%{_libexecdir}/ukiboot/efi/slot_b.addon.efi %{buildroot}%{efi_esp_dir}/ukiboot_b.efi.extra.d

%post
%systemd_post ukiboot-set-success.service

%preun
%systemd_preun ukiboot-set-success.service

%postun
%systemd_postun ukiboot-set-success.service

%files
%license COPYING.LIB
%doc README.md
%{efi_esp_dir}/ukiboot*
%{_libexecdir}/ukiboot
%{_bindir}/ukibootctl
%{_unitdir}/ukiboot-set-success.service

%changelog
* Tue Jan 20 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Oct 02 2025 Javier Martinez Canillas <javierm@redhat.com> - 0.2.1-1
- Update to 0.2.1

* Tue Sep 30 2025 Alexander Larsson  <alexl@redhat.com> - 0.2.0-1
- Fix support for signed pe binaries

* Fri Sep 26 2025 Alexander Larsson  <alexl@redhat.com> - 0.1.9-1
- Update to 0.1.9

* Fri Aug 29 2025 Alexander Larsson  <alexl@redhat.com> - 0.1.8-1
- Update to 0.1.8

* Mon Aug 18 2025 Alexander Larsson  <alexl@redhat.com> - 0.1.7-1
- Update to 0.1.7
- Install in vendored esp dir

* Thu Aug 07 2025 Alexander Larsson  <alexl@redhat.com> - 0.1.6-3
- Install the EFI binaries into /boot/EFI in the actual package

* Mon Aug 04 2025 Alexander Larsson  <alexl@redhat.com> - 0.1.6-2
- Make the gnu-efi-ukiboot workaround conditional to rhel9.

* Mon Aug 04 2025 Alexander Larsson  <alexl@redhat.com> - 0.1.6-1
- Update to 0.1.6

* Tue Jul 01 2025 Alexander Larsson  <alexl@redhat.com> - 0.1.5-1
- Update to 0.1.5

* Fri May 16 2025 Alexander Larsson  <alexl@redhat.com> - 0.1.4-1
- Update to 0.1.4

* Wed May 07 2025 Alexander Larsson  <alexl@redhat.com> - 0.1.3-1
- Update to 0.1.3

* Wed May 07 2025 Alexander Larsson  <alexl@redhat.com> - 0.1.2-1
- Update to 0.1.2

* Wed Apr 30 2025 Alexander Larsson  <alexl@redhat.com> - 0.1.1-1
- Update to 0.1.1

* Wed Feb 26 2025 Alexander Larsson <alexl@redhat.com>
- Initial version
