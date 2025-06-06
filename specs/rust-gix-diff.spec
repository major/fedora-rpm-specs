# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate gix-diff

Name:           rust-gix-diff
Version:        0.50.0
Release:        %autorelease
Summary:        Calculate differences between various git objects

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-diff
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Calculate differences between various git objects.}

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
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+blob-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+blob-devel %{_description}

This package contains library source intended for building other packages which
use the "blob" feature of the "%{crate}" crate.

%files       -n %{name}+blob-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+document-features-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+document-features-devel %{_description}

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%files       -n %{name}+document-features-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+index-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+index-devel %{_description}

This package contains library source intended for building other packages which
use the "index" feature of the "%{crate}" crate.

%files       -n %{name}+index-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
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
