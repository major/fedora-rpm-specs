# EFI/UEFI binaries are not ELF, but PE32/PE32+/COFF
%global debug_package %{nil}

Name:           sprout
Version:        0.0.26
Release:        1%{?dist}
Summary:        Configurable and programmable UEFI bootloader
SourceLicense:  Apache-2.0
# Apache-2.0
# Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# MPL-2.0
License:        Apache-2.0 and (Apache-2.0 or MIT) and MIT and MPL-2.0
URL:            https://sprout.edera.dev/
Source0:        https://github.com/edera-dev/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  efi-srpm-macros
BuildRequires:  rust-std-static-%{_target_cpu}-unknown-uefi


ExclusiveArch:  %{efi}
# Rust UEFI toolchain has no x86-32 or RISC-V support
ExcludeArch:    %{ix86} %{riscv}

%description
%{summary}.


%dnl -------------------------------------------------------------

%package unsigned-%{efi_arch}
Summary:        Programmable UEFI bootloader written in Rust for %{efi_arch}
Requires:       efi-filesystem
Provides:       %{name}-bootloader-%{efi_arch}
Conflicts:      %{name}-bootloader-%{efi_arch}

BuildArch:      noarch

%description unsigned-%{efi_arch}
%{summary}.

%files unsigned-%{efi_arch}
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}%{efi_arch}.efi

%dnl -------------------------------------------------------------


%prep
%autosetup -C
%cargo_prep


%generate_buildrequires
%cargo_generate_buildrequires


%build
%cargo_build -- --bin sprout --target %{_target_cpu}-unknown-uefi
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
# Install sprout binaries manually...
install -v -m 644 target/%{_target_cpu}-unknown-uefi/rpm/sprout.efi %{buildroot}%{_datadir}/%{name}/%{name}%{efi_arch}.efi


%changelog
* Tue Dec 09 2025 Neal Gompa <ngompa@fedoraproject.org> - 0.0.26-1
- Initial package
