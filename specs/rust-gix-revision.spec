# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate gix-revision

Name:           rust-gix-revision
Version:        0.32.0
Release:        %autorelease
Summary:        Deal with finding names for revisions and parsing specifications

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-revision
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A crate of the gitoxide project dealing with finding names for revisions
and parsing specifications.}

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

%package     -n %{name}+describe-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+describe-devel %{_description}

This package contains library source intended for building other packages which
use the "describe" feature of the "%{crate}" crate.

%files       -n %{name}+describe-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+document-features-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+document-features-devel %{_description}

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%files       -n %{name}+document-features-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+merge_base-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+merge_base-devel %{_description}

This package contains library source intended for building other packages which
use the "merge_base" feature of the "%{crate}" crate.

%files       -n %{name}+merge_base-devel
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
