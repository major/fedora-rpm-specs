# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate mimalloc

Name:           rust-mimalloc
Version:        0.1.46
Release:        %autorelease
Summary:        Performance and security oriented drop-in allocator

License:        MIT
URL:            https://crates.io/crates/mimalloc
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Performance and security oriented drop-in allocator.}

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

%package     -n %{name}+debug-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+debug-devel %{_description}

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%files       -n %{name}+debug-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+debug_in_debug-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+debug_in_debug-devel %{_description}

This package contains library source intended for building other packages which
use the "debug_in_debug" feature of the "%{crate}" crate.

%files       -n %{name}+debug_in_debug-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+extended-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+extended-devel %{_description}

This package contains library source intended for building other packages which
use the "extended" feature of the "%{crate}" crate.

%files       -n %{name}+extended-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+local_dynamic_tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+local_dynamic_tls-devel %{_description}

This package contains library source intended for building other packages which
use the "local_dynamic_tls" feature of the "%{crate}" crate.

%files       -n %{name}+local_dynamic_tls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+no_thp-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+no_thp-devel %{_description}

This package contains library source intended for building other packages which
use the "no_thp" feature of the "%{crate}" crate.

%files       -n %{name}+no_thp-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+override-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+override-devel %{_description}

This package contains library source intended for building other packages which
use the "override" feature of the "%{crate}" crate.

%files       -n %{name}+override-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+secure-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+secure-devel %{_description}

This package contains library source intended for building other packages which
use the "secure" feature of the "%{crate}" crate.

%files       -n %{name}+secure-devel
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
