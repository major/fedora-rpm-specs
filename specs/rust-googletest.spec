# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate googletest

Name:           rust-googletest
Version:        0.11.0
Release:        %autorelease
Summary:        Rich assertion and matcher library inspired by GoogleTest for C++

License:        Apache-2.0
URL:            https://crates.io/crates/googletest
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A rich assertion and matcher library inspired by GoogleTest for C++.}

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
%doc %{crate_instdir}/crate_docs.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+anyhow-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+anyhow-devel %{_description}

This package contains library source intended for building other packages which
use the "anyhow" feature of the "%{crate}" crate.

%files       -n %{name}+anyhow-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+proptest-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+proptest-devel %{_description}

This package contains library source intended for building other packages which
use the "proptest" feature of the "%{crate}" crate.

%files       -n %{name}+proptest-devel
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
