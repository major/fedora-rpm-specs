# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate minijinja

Name:           rust-minijinja
Version:        2.11.0
Release:        %autorelease
Summary:        Powerful template engine for Rust with minimal dependencies

License:        Apache-2.0
URL:            https://crates.io/crates/minijinja
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * drop unused "source" feature with missing dependencies: memo-map ^0.3.1
Patch:          minijinja-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A powerful template engine for Rust with minimal dependencies.}

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

%package     -n %{name}+adjacent_loop_items-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+adjacent_loop_items-devel %{_description}

This package contains library source intended for building other packages which
use the "adjacent_loop_items" feature of the "%{crate}" crate.

%files       -n %{name}+adjacent_loop_items-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+builtins-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+builtins-devel %{_description}

This package contains library source intended for building other packages which
use the "builtins" feature of the "%{crate}" crate.

%files       -n %{name}+builtins-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+custom_syntax-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+custom_syntax-devel %{_description}

This package contains library source intended for building other packages which
use the "custom_syntax" feature of the "%{crate}" crate.

%files       -n %{name}+custom_syntax-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+debug-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+debug-devel %{_description}

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%files       -n %{name}+debug-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+deserialization-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+deserialization-devel %{_description}

This package contains library source intended for building other packages which
use the "deserialization" feature of the "%{crate}" crate.

%files       -n %{name}+deserialization-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+fuel-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fuel-devel %{_description}

This package contains library source intended for building other packages which
use the "fuel" feature of the "%{crate}" crate.

%files       -n %{name}+fuel-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+indexmap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+indexmap-devel %{_description}

This package contains library source intended for building other packages which
use the "indexmap" feature of the "%{crate}" crate.

%files       -n %{name}+indexmap-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+internal_debug-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+internal_debug-devel %{_description}

This package contains library source intended for building other packages which
use the "internal_debug" feature of the "%{crate}" crate.

%files       -n %{name}+internal_debug-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+internal_safe_search-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+internal_safe_search-devel %{_description}

This package contains library source intended for building other packages which
use the "internal_safe_search" feature of the "%{crate}" crate.

%files       -n %{name}+internal_safe_search-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+json-devel %{_description}

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%files       -n %{name}+json-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+key_interning-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+key_interning-devel %{_description}

This package contains library source intended for building other packages which
use the "key_interning" feature of the "%{crate}" crate.

%files       -n %{name}+key_interning-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+loop_controls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+loop_controls-devel %{_description}

This package contains library source intended for building other packages which
use the "loop_controls" feature of the "%{crate}" crate.

%files       -n %{name}+loop_controls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+macros-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+macros-devel %{_description}

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%files       -n %{name}+macros-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+multi_template-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+multi_template-devel %{_description}

This package contains library source intended for building other packages which
use the "multi_template" feature of the "%{crate}" crate.

%files       -n %{name}+multi_template-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+percent-encoding-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+percent-encoding-devel %{_description}

This package contains library source intended for building other packages which
use the "percent-encoding" feature of the "%{crate}" crate.

%files       -n %{name}+percent-encoding-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+preserve_order-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+preserve_order-devel %{_description}

This package contains library source intended for building other packages which
use the "preserve_order" feature of the "%{crate}" crate.

%files       -n %{name}+preserve_order-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde_json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_json-devel %{_description}

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%files       -n %{name}+serde_json-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+speedups-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+speedups-devel %{_description}

This package contains library source intended for building other packages which
use the "speedups" feature of the "%{crate}" crate.

%files       -n %{name}+speedups-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+stacker-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+stacker-devel %{_description}

This package contains library source intended for building other packages which
use the "stacker" feature of the "%{crate}" crate.

%files       -n %{name}+stacker-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std_collections-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std_collections-devel %{_description}

This package contains library source intended for building other packages which
use the "std_collections" feature of the "%{crate}" crate.

%files       -n %{name}+std_collections-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicase-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicase-devel %{_description}

This package contains library source intended for building other packages which
use the "unicase" feature of the "%{crate}" crate.

%files       -n %{name}+unicase-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-devel %{_description}

This package contains library source intended for building other packages which
use the "unicode" feature of the "%{crate}" crate.

%files       -n %{name}+unicode-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicode-ident-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicode-ident-devel %{_description}

This package contains library source intended for building other packages which
use the "unicode-ident" feature of the "%{crate}" crate.

%files       -n %{name}+unicode-ident-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unstable_machinery-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable_machinery-devel %{_description}

This package contains library source intended for building other packages which
use the "unstable_machinery" feature of the "%{crate}" crate.

%files       -n %{name}+unstable_machinery-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unstable_machinery_serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable_machinery_serde-devel %{_description}

This package contains library source intended for building other packages which
use the "unstable_machinery_serde" feature of the "%{crate}" crate.

%files       -n %{name}+unstable_machinery_serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+urlencode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+urlencode-devel %{_description}

This package contains library source intended for building other packages which
use the "urlencode" feature of the "%{crate}" crate.

%files       -n %{name}+urlencode-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v_htmlescape-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v_htmlescape-devel %{_description}

This package contains library source intended for building other packages which
use the "v_htmlescape" feature of the "%{crate}" crate.

%files       -n %{name}+v_htmlescape-devel
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
