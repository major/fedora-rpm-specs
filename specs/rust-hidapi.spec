# Generated by rust2rpm 22
%bcond_without check
%global debug_package %{nil}

%global crate hidapi

Name:           rust-hidapi
Version:        1.4.1
Release:        %autorelease
Summary:        Rust-y wrapper around hidapi

License:        MIT
URL:            https://crates.io/crates/hidapi
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * remove features for Illumos OS support
# * remove features for statically linking with hidapi
Patch:          hidapi-fix-metadata.diff
Patch:          0001-add-missing-linker-flags-for-linking-with-libusb-1.0.patch

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Rust-y wrapper around hidapi.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE.txt
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+linux-shared-hidraw-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(hidapi-hidraw)

%description -n %{name}+linux-shared-hidraw-devel %{_description}

This package contains library source intended for building other packages which
use the "linux-shared-hidraw" feature of the "%{crate}" crate.

%files       -n %{name}+linux-shared-hidraw-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+linux-shared-libusb-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(hidapi-libusb)

%description -n %{name}+linux-shared-libusb-devel %{_description}

This package contains library source intended for building other packages which
use the "linux-shared-libusb" feature of the "%{crate}" crate.

%files       -n %{name}+linux-shared-libusb-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
# remove bundled hidapi sources
rm -rf etc/
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'pkgconfig(hidapi-hidraw)'
echo 'pkgconfig(hidapi-libusb)'
echo 'pkgconfig(libusb-1.0)'

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
