# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate write16

Name:           rust-write16
Version:        1.0.0
Release:        %autorelease
Summary:        UTF-16 analog of the Write trait

License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/write16
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A UTF-16 analog of the Write trait.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/COPYRIGHT
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

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+arrayvec-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+arrayvec-devel %{_description}

This package contains library source intended for building other packages which
use the "arrayvec" feature of the "%{crate}" crate.

%files       -n %{name}+arrayvec-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+smallvec-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+smallvec-devel %{_description}

This package contains library source intended for building other packages which
use the "smallvec" feature of the "%{crate}" crate.

%files       -n %{name}+smallvec-devel
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
