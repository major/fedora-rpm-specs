# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate uguid

Name:           rust-uguid
Version:        2.2.1
Release:        %autorelease
Summary:        GUID (Globally Unique Identifier) no_std library

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/uguid
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
GUID (Globally Unique Identifier) no_std library.}

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
%doc %{crate_instdir}/CHANGELOG.md
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

%package     -n %{name}+bytemuck-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bytemuck-devel %{_description}

This package contains library source intended for building other packages which
use the "bytemuck" feature of the "%{crate}" crate.

%files       -n %{name}+bytemuck-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -f bytemuck,serde

%build
%cargo_build -f bytemuck,serde

%install
%cargo_install -f bytemuck,serde

%if %{with check}
%check
# * skip tests that fail due to slightly different error messages in Rust 1.87+
%cargo_test -f bytemuck,serde -- -- --exact --skip test_compilation_errors
%endif

%changelog
%autochangelog
