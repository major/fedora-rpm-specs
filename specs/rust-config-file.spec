%bcond check 1
%global debug_package %{nil}

%global crate config-file

Name:           rust-config-file
Version:        0.2.3
Release:        %autorelease
Summary:        Read and parse configuration file automatically

License:        BSD-2-Clause
URL:            https://crates.io/crates/config-file
Source0:        %{crates_source}
Source1:	LICENSE


BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
`config-file` is a simple Rust library
to read and parse configuration files
automatically using Serde.
It supports TOML format
and is designed for ease of use.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license	LICENSE
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

%package     -n %{name}+json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+json-devel %{_description}

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%files       -n %{name}+json-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-xml-rs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-xml-rs-devel %{_description}

This package contains library source intended for building other packages which
use the "serde-xml-rs" feature of the "%{crate}" crate.

%files       -n %{name}+serde-xml-rs-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde_json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_json-devel %{_description}

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%files       -n %{name}+serde_json-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde_yaml-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_yaml-devel %{_description}

This package contains library source intended for building other packages which
use the "serde_yaml" feature of the "%{crate}" crate.

%files       -n %{name}+serde_yaml-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+toml-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+toml-devel %{_description}

This package contains library source intended for building other packages which
use the "toml" feature of the "%{crate}" crate.

%files       -n %{name}+toml-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+toml-crate-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+toml-crate-devel %{_description}

This package contains library source intended for building other packages which
use the "toml-crate" feature of the "%{crate}" crate.

%files       -n %{name}+toml-crate-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+xml-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+xml-devel %{_description}

This package contains library source intended for building other packages which
use the "xml" feature of the "%{crate}" crate.

%files       -n %{name}+xml-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+yaml-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+yaml-devel %{_description}

This package contains library source intended for building other packages which
use the "yaml" feature of the "%{crate}" crate.

%files       -n %{name}+yaml-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
cp %{SOURCE1} LICENSE	#we have to add the LICENSE file manually since upstream doesn't include it


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
* Thu May 29 2025 jados <jados42008@gmail.com> - 0.2.3-1
- Initial package for fedora
