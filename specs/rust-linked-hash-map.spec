# Generated by rust2rpm 24
# * unit tests are excluded from published crates
%bcond_with check
%global debug_package %{nil}

%global crate linked-hash-map

Name:           rust-linked-hash-map
Version:        0.5.6
Release:        %autorelease
Summary:        HashMap wrapper that holds key-value pairs in insertion order

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/linked-hash-map
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
A HashMap wrapper that holds key-value pairs in insertion order.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
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

%package     -n %{name}+heapsize-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+heapsize-devel %{_description}

This package contains library source intended for building other packages which
use the "heapsize" feature of the "%{crate}" crate.

%files       -n %{name}+heapsize-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+heapsize_impl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+heapsize_impl-devel %{_description}

This package contains library source intended for building other packages which
use the "heapsize_impl" feature of the "%{crate}" crate.

%files       -n %{name}+heapsize_impl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%files       -n %{name}+nightly-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde_impl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_impl-devel %{_description}

This package contains library source intended for building other packages which
use the "serde_impl" feature of the "%{crate}" crate.

%files       -n %{name}+serde_impl-devel
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