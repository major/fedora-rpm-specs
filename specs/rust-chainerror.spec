# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate chainerror

Name:           rust-chainerror
Version:        0.7.1
Release:        %autorelease
Summary:        Make chaining errors easy

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/chainerror
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Make chaining errors easy.}

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

%package     -n %{name}+display-cause-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+display-cause-devel %{_description}

This package contains library source intended for building other packages which
use the "display-cause" feature of the "%{crate}" crate.

%files       -n %{name}+display-cause-devel
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