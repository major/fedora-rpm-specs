# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate dircpy

Name:           rust-dircpy
Version:        0.3.19
Release:        %autorelease
Summary:        Copy directories recursively with flexible options

License:        MIT
URL:            https://crates.io/crates/dircpy
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * drop benchmarks and benchmark-only dependencies
# * drop dependencies for tests that require internet connectivity
Patch:          dircpy-fix-metadata.diff
Patch:          0001-drop-a-test-that-requires-internet-connectivity.patch

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Copy directories recursively with flexible options.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/Changelog.md
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

%package     -n %{name}+jwalk-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+jwalk-devel %{_description}

This package contains library source intended for building other packages which
use the "jwalk" feature of the "%{crate}" crate.

%files       -n %{name}+jwalk-devel
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
%cargo_test
%endif

%changelog
%autochangelog
