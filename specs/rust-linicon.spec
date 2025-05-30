# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate linicon

Name:           rust-linicon
Version:        2.3.0
Release:        %autorelease
Summary:        Look up icons and icon theme info on Linux

License:        MPL-2.0
URL:            https://crates.io/crates/linicon
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * Drop unneeded criterion dependency
Patch:          linicon-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Look up icons and icon theme info on Linux.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
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

%package     -n %{name}+expand-paths-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+expand-paths-devel %{_description}

This package contains library source intended for building other packages which
use the "expand-paths" feature of the "%{crate}" crate.

%files       -n %{name}+expand-paths-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+linicon-theme-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+linicon-theme-devel %{_description}

This package contains library source intended for building other packages which
use the "linicon-theme" feature of the "%{crate}" crate.

%files       -n %{name}+linicon-theme-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+shellexpand-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+shellexpand-devel %{_description}

This package contains library source intended for building other packages which
use the "shellexpand" feature of the "%{crate}" crate.

%files       -n %{name}+shellexpand-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+system-theme-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+system-theme-devel %{_description}

This package contains library source intended for building other packages which
use the "system-theme" feature of the "%{crate}" crate.

%files       -n %{name}+system-theme-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
# * Skip broken tests
%{cargo_test -- -- --exact %{shrink:
    --skip tests::do_lookup
    --skip tests::do_lookup_no_scale
    --skip tests::do_lookup_no_size
    --skip tests::do_lookup_no_size_scale
    --skip tests::get_themes
    --skip tests::move_iter
    --skip tests::move_threads
}}
%endif

%changelog
%autochangelog
