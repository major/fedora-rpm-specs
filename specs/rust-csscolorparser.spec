# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate csscolorparser

Name:           rust-csscolorparser
Version:        0.6.2
Release:        %autorelease
Summary:        CSS color parser library

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/csscolorparser
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
CSS color parser library.}

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

%package     -n %{name}+cint-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cint-devel %{_description}

This package contains library source intended for building other packages which
use the "cint" feature of the "%{crate}" crate.

%files       -n %{name}+cint-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+lab-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+lab-devel %{_description}

This package contains library source intended for building other packages which
use the "lab" feature of the "%{crate}" crate.

%files       -n %{name}+lab-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+named-colors-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+named-colors-devel %{_description}

This package contains library source intended for building other packages which
use the "named-colors" feature of the "%{crate}" crate.

%files       -n %{name}+named-colors-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+phf-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+phf-devel %{_description}

This package contains library source intended for building other packages which
use the "phf" feature of the "%{crate}" crate.

%files       -n %{name}+phf-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rgb-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rgb-devel %{_description}

This package contains library source intended for building other packages which
use the "rgb" feature of the "%{crate}" crate.

%files       -n %{name}+rgb-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rust-rgb-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rust-rgb-devel %{_description}

This package contains library source intended for building other packages which
use the "rust-rgb" feature of the "%{crate}" crate.

%files       -n %{name}+rust-rgb-devel
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