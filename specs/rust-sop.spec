# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate sop

Name:           rust-sop
Version:        0.8.2
Release:        %autorelease
Summary:        Rust Interface for the Stateless OpenPGP Interface

License:        MIT
URL:            https://crates.io/crates/sop
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Rust Interface for the Stateless OpenPGP Interface.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE.txt
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

%package     -n %{name}+anyhow-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+anyhow-devel %{_description}

This package contains library source intended for building other packages which
use the "anyhow" feature of the "%{crate}" crate.

%files       -n %{name}+anyhow-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+chrono-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+chrono-devel %{_description}

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%files       -n %{name}+chrono-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+clap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+clap-devel %{_description}

This package contains library source intended for building other packages which
use the "clap" feature of the "%{crate}" crate.

%files       -n %{name}+clap-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+clap_complete-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+clap_complete-devel %{_description}

This package contains library source intended for building other packages which
use the "clap_complete" feature of the "%{crate}" crate.

%files       -n %{name}+clap_complete-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+clap_mangen-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+clap_mangen-devel %{_description}

This package contains library source intended for building other packages which
use the "clap_mangen" feature of the "%{crate}" crate.

%files       -n %{name}+clap_mangen-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+cli-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cli-devel %{_description}

This package contains library source intended for building other packages which
use the "cli" feature of the "%{crate}" crate.

%files       -n %{name}+cli-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+cliv-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cliv-devel %{_description}

This package contains library source intended for building other packages which
use the "cliv" feature of the "%{crate}" crate.

%files       -n %{name}+cliv-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+libc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libc-devel %{_description}

This package contains library source intended for building other packages which
use the "libc" feature of the "%{crate}" crate.

%files       -n %{name}+libc-devel
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
