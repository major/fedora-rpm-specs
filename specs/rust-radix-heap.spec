# Generated by rust2rpm 23
%bcond_without check
%global debug_package %{nil}

%global crate radix-heap

Name:           rust-radix-heap
Version:        0.4.2
Release:        %autorelease
Summary:        Fast monotone priority queues

License:        MIT
URL:            https://crates.io/crates/radix-heap
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# - remove criterion dev-dependency as it's only for benchmarking
Patch:          radix-heap-fix-metadata.diff

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Fast monotone priority queues.}

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

%package     -n %{name}+ordered-float-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ordered-float-devel %{_description}

This package contains library source intended for building other packages which
use the "ordered-float" feature of the "%{crate}" crate.

%files       -n %{name}+ordered-float-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
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
