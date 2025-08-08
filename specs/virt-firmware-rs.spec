%bcond efi_apps 0
%bcond check    1

%if 0%{?fedora}

%ifarch aarch64
%bcond efi_apps 1
%define efiarch aa64
BuildRequires:  rust-std-static-aarch64-unknown-uefi
%endif

%ifarch x86_64
%bcond efi_apps 1
%define efiarch x64
BuildRequires:  rust-std-static-x86_64-unknown-uefi
%endif

%endif

Name:           virt-firmware-rs
Version:        25.8
Release:        %autorelease
Summary:        Tools for EFI and virtual machine firmware

SourceLicense:  MIT
License:        %{shrink:
        Apache-2.0
        Apache-2.0 OR BSL-1.0
        Apache-2.0 OR MIT
        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
        BSD-2-Clause OR Apache-2.0 OR MIT
        MIT
        MIT OR Apache-2.0
        MPL-2.0
        Unlicense OR MIT
}

URL:            https://gitlab.com/kraxel/virt-firmware-rs
Source:         https://gitlab.com/kraxel/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  pkgconfig(libudev)

%description
A collection of tools to deal with efi and virtual machine
firmware.  This package has linux tools.

%if %{with efi_apps}

%package -n %{name}-%{efiarch}
BuildArch:      noarch
Summary:        %{summary}

%description -n %{name}-%{efiarch}
A collection of tools to deal with efi and virtual machine
firmware.  This package has EFI applications for %{efiarch}.

%endif # build_efi_apps

%prep
%autosetup -n %{name}-v%{version} -p1
%cargo_prep
# drop unused packages from workspace to reduce dependencies.
sed -i Cargo.toml -e '/varstore/d'
%if %{without efi_apps}
sed -i Cargo.toml -e '/efi-apps/d'
%endif

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build -- --package virtfw-efi-tools --features udev
%cargo_build -- --package virtfw-efi-tools
%cargo_build -- --package virtfw-igvm-tools
%if %{with efi_apps}
%cargo_build -- --package virtfw-efi-apps --target $(uname -m)-unknown-uefi
%endif
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
# efi-tools + igvm-tools
install -d %{buildroot}%{_bindir}
install -v -m 755 target/rpm/generate-boot-csv %{buildroot}%{_bindir}
install -v -m 755 target/rpm/list-sb-vars %{buildroot}%{_bindir}
install -v -m 755 target/rpm/mini-bootcfg %{buildroot}%{_bindir}
install -v -m 755 target/rpm/uefi-boot-menu %{buildroot}%{_bindir}/uefi-boot-menu-rs
install -v -m 755 target/rpm/igvm-inspect %{buildroot}%{_bindir}
install -v -m 755 target/rpm/igvm-wrap %{buildroot}%{_bindir}
%if %{with efi_apps}
# efi-apps
install -d %{buildroot}%{_datadir}/%{name}/%{efiarch}
install -v -m 644 target/*-unknown-uefi/rpm/*.efi %{buildroot}%{_datadir}/%{name}/%{efiarch}
%endif
# rename readme files
for dir in efi-apps efi-tools igvm-tools; do
    cp -v ${dir}/README.md README.${dir}.md
done

%check
%ifarch s390x
echo "skip tests on bigendian"
%else
%cargo_test -- --package virtfw-libefi
%cargo_test -- --package virtfw-efi-tools --features udev
%cargo_test -- --package virtfw-igvm-tools
%endif

%files
%license LICENSE LICENSE.dependencies
%doc README.md
%doc README.efi-tools.md
%doc README.igvm-tools.md
%{_bindir}/generate-boot-csv
%{_bindir}/list-sb-vars
%{_bindir}/mini-bootcfg
%{_bindir}/uefi-boot-menu-rs
%{_bindir}/igvm-inspect
%{_bindir}/igvm-wrap

%if %{with efi_apps}
%files -n %{name}-%{efiarch}
%license LICENSE LICENSE.dependencies
%doc README.efi-apps.md
%dir %{_datadir}/%{name}/%{efiarch}
%{_datadir}/%{name}/%{efiarch}/*.efi
%endif

%changelog
%autochangelog
