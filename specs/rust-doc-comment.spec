# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate doc-comment

Name:           rust-doc-comment
Version:        0.3.3
Release:        %autorelease
Summary:        Macro to generate doc comments

License:        MIT
URL:            https://crates.io/crates/doc-comment
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Macro to generate doc comments.}

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

%package     -n %{name}+no_core-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+no_core-devel %{_description}

This package contains library source intended for building other packages which
use the "no_core" feature of the "%{crate}" crate.

%files       -n %{name}+no_core-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+old_macros-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+old_macros-devel %{_description}

This package contains library source intended for building other packages which
use the "old_macros" feature of the "%{crate}" crate.

%files       -n %{name}+old_macros-devel
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
