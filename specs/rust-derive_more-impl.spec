# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate derive_more-impl

Name:           rust-derive_more-impl
Version:        1.0.0
Release:        %autorelease
Summary:        Internal implementation of derive_more crate

License:        MIT
URL:            https://crates.io/crates/derive_more-impl
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Internal implementation of `derive_more` crate.}

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

%package     -n %{name}+add-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+add-devel %{_description}

This package contains library source intended for building other packages which
use the "add" feature of the "%{crate}" crate.

%files       -n %{name}+add-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+add_assign-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+add_assign-devel %{_description}

This package contains library source intended for building other packages which
use the "add_assign" feature of the "%{crate}" crate.

%files       -n %{name}+add_assign-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+as_ref-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+as_ref-devel %{_description}

This package contains library source intended for building other packages which
use the "as_ref" feature of the "%{crate}" crate.

%files       -n %{name}+as_ref-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+constructor-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+constructor-devel %{_description}

This package contains library source intended for building other packages which
use the "constructor" feature of the "%{crate}" crate.

%files       -n %{name}+constructor-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+debug-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+debug-devel %{_description}

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%files       -n %{name}+debug-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+deref-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+deref-devel %{_description}

This package contains library source intended for building other packages which
use the "deref" feature of the "%{crate}" crate.

%files       -n %{name}+deref-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+deref_mut-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+deref_mut-devel %{_description}

This package contains library source intended for building other packages which
use the "deref_mut" feature of the "%{crate}" crate.

%files       -n %{name}+deref_mut-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+display-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+display-devel %{_description}

This package contains library source intended for building other packages which
use the "display" feature of the "%{crate}" crate.

%files       -n %{name}+display-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+error-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+error-devel %{_description}

This package contains library source intended for building other packages which
use the "error" feature of the "%{crate}" crate.

%files       -n %{name}+error-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+from-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+from-devel %{_description}

This package contains library source intended for building other packages which
use the "from" feature of the "%{crate}" crate.

%files       -n %{name}+from-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+from_str-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+from_str-devel %{_description}

This package contains library source intended for building other packages which
use the "from_str" feature of the "%{crate}" crate.

%files       -n %{name}+from_str-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+full-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+full-devel %{_description}

This package contains library source intended for building other packages which
use the "full" feature of the "%{crate}" crate.

%files       -n %{name}+full-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+index-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+index-devel %{_description}

This package contains library source intended for building other packages which
use the "index" feature of the "%{crate}" crate.

%files       -n %{name}+index-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+index_mut-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+index_mut-devel %{_description}

This package contains library source intended for building other packages which
use the "index_mut" feature of the "%{crate}" crate.

%files       -n %{name}+index_mut-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+into-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+into-devel %{_description}

This package contains library source intended for building other packages which
use the "into" feature of the "%{crate}" crate.

%files       -n %{name}+into-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+into_iterator-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+into_iterator-devel %{_description}

This package contains library source intended for building other packages which
use the "into_iterator" feature of the "%{crate}" crate.

%files       -n %{name}+into_iterator-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+is_variant-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+is_variant-devel %{_description}

This package contains library source intended for building other packages which
use the "is_variant" feature of the "%{crate}" crate.

%files       -n %{name}+is_variant-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+mul-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+mul-devel %{_description}

This package contains library source intended for building other packages which
use the "mul" feature of the "%{crate}" crate.

%files       -n %{name}+mul-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+mul_assign-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+mul_assign-devel %{_description}

This package contains library source intended for building other packages which
use the "mul_assign" feature of the "%{crate}" crate.

%files       -n %{name}+mul_assign-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+not-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+not-devel %{_description}

This package contains library source intended for building other packages which
use the "not" feature of the "%{crate}" crate.

%files       -n %{name}+not-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+sum-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sum-devel %{_description}

This package contains library source intended for building other packages which
use the "sum" feature of the "%{crate}" crate.

%files       -n %{name}+sum-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+testing-helpers-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+testing-helpers-devel %{_description}

This package contains library source intended for building other packages which
use the "testing-helpers" feature of the "%{crate}" crate.

%files       -n %{name}+testing-helpers-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+try_from-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+try_from-devel %{_description}

This package contains library source intended for building other packages which
use the "try_from" feature of the "%{crate}" crate.

%files       -n %{name}+try_from-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+try_into-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+try_into-devel %{_description}

This package contains library source intended for building other packages which
use the "try_into" feature of the "%{crate}" crate.

%files       -n %{name}+try_into-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+try_unwrap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+try_unwrap-devel %{_description}

This package contains library source intended for building other packages which
use the "try_unwrap" feature of the "%{crate}" crate.

%files       -n %{name}+try_unwrap-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unwrap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unwrap-devel %{_description}

This package contains library source intended for building other packages which
use the "unwrap" feature of the "%{crate}" crate.

%files       -n %{name}+unwrap-devel
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