# Generated by rust2rpm 23
%bcond_without check
%global debug_package %{nil}

%global crate vcsgraph

Name:           rust-vcsgraph
Version:        0.2.0
Release:        %autorelease
Summary:        Library to perform various computation of a version control graph

# https://foss.heptapod.net/mercurial/vcsgraph/-/issues/16
License:        GPL-2.0-or-later
URL:            https://crates.io/crates/vcsgraph
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * prevent development-only binaries from being built and installed
Patch:          vcsgraph-fix-metadata.diff

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Library to perform various computation of a version control graph.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
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

%package     -n %{name}+cli-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cli-devel %{_description}

This package contains library source intended for building other packages which
use the "cli" feature of the "%{crate}" crate.

%files       -n %{name}+cli-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+structopt-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+structopt-devel %{_description}

This package contains library source intended for building other packages which
use the "structopt" feature of the "%{crate}" crate.

%files       -n %{name}+structopt-devel
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
