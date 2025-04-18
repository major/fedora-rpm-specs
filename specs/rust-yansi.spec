# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate yansi

Name:           rust-yansi
Version:        1.0.1
Release:        %autorelease
Summary:        Dead simple ANSI terminal color painting library

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/yansi
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A dead simple ANSI terminal color painting library.}

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

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+detect-env-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+detect-env-devel %{_description}

This package contains library source intended for building other packages which
use the "detect-env" feature of the "%{crate}" crate.

%files       -n %{name}+detect-env-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+detect-tty-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+detect-tty-devel %{_description}

This package contains library source intended for building other packages which
use the "detect-tty" feature of the "%{crate}" crate.

%files       -n %{name}+detect-tty-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+hyperlink-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+hyperlink-devel %{_description}

This package contains library source intended for building other packages which
use the "hyperlink" feature of the "%{crate}" crate.

%files       -n %{name}+hyperlink-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+is-terminal-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+is-terminal-devel %{_description}

This package contains library source intended for building other packages which
use the "is-terminal" feature of the "%{crate}" crate.

%files       -n %{name}+is-terminal-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
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
