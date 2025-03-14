# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate bindgen

Name:           rust-bindgen0.63
Version:        0.63.0
Release:        %autorelease
Summary:        Automatically generates Rust FFI bindings to C and C++ libraries

License:        BSD-3-Clause
URL:            https://crates.io/crates/bindgen
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Automatically generates Rust FFI bindings to C and C++ libraries.}

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

%package     -n %{name}+log-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+log-devel %{_description}

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%files       -n %{name}+log-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+logging-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+logging-devel %{_description}

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

%files       -n %{name}+logging-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+runtime-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+runtime-devel %{_description}

This package contains library source intended for building other packages which
use the "runtime" feature of the "%{crate}" crate.

%files       -n %{name}+runtime-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+static-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+static-devel %{_description}

This package contains library source intended for building other packages which
use the "static" feature of the "%{crate}" crate.

%files       -n %{name}+static-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+testing_only_docs-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+testing_only_docs-devel %{_description}

This package contains library source intended for building other packages which
use the "testing_only_docs" feature of the "%{crate}" crate.

%files       -n %{name}+testing_only_docs-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+testing_only_extra_assertions-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+testing_only_extra_assertions-devel %{_description}

This package contains library source intended for building other packages which
use the "testing_only_extra_assertions" feature of the "%{crate}" crate.

%files       -n %{name}+testing_only_extra_assertions-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+testing_only_libclang_5-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+testing_only_libclang_5-devel %{_description}

This package contains library source intended for building other packages which
use the "testing_only_libclang_5" feature of the "%{crate}" crate.

%files       -n %{name}+testing_only_libclang_5-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+testing_only_libclang_9-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+testing_only_libclang_9-devel %{_description}

This package contains library source intended for building other packages which
use the "testing_only_libclang_9" feature of the "%{crate}" crate.

%files       -n %{name}+testing_only_libclang_9-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+which-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+which-devel %{_description}

This package contains library source intended for building other packages which
use the "which" feature of the "%{crate}" crate.

%files       -n %{name}+which-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+which-rustfmt-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+which-rustfmt-devel %{_description}

This package contains library source intended for building other packages which
use the "which-rustfmt" feature of the "%{crate}" crate.

%files       -n %{name}+which-rustfmt-devel
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
