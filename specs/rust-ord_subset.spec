# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate ord_subset

Name:           rust-ord_subset
Version:        3.1.1
Release:        %autorelease
Summary:        Tools for working with the Ord subset of certain PartialOrd types, like floats

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ord_subset
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Tools for working with the Ord subset of certain PartialOrd types, like
floats.}

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

%package     -n %{name}+ops-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ops-devel %{_description}

This package contains library source intended for building other packages which
use the "ops" feature of the "%{crate}" crate.

%files       -n %{name}+ops-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unchecked_ops-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unchecked_ops-devel %{_description}

This package contains library source intended for building other packages which
use the "unchecked_ops" feature of the "%{crate}" crate.

%files       -n %{name}+unchecked_ops-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-devel %{_description}

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%files       -n %{name}+unstable-devel
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
