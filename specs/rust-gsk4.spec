# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate gsk4

Name:           rust-gsk4
Version:        0.9.6
Release:        %autorelease
Summary:        Rust bindings of the GSK 4 library

License:        MIT
URL:            https://crates.io/crates/gsk4
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Rust bindings of the GSK 4 library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/COPYRIGHT
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

%package     -n %{name}+broadway-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+broadway-devel %{_description}

This package contains library source intended for building other packages which
use the "broadway" feature of the "%{crate}" crate.

%files       -n %{name}+broadway-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v4_10-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v4_10-devel %{_description}

This package contains library source intended for building other packages which
use the "v4_10" feature of the "%{crate}" crate.

%files       -n %{name}+v4_10-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v4_14-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v4_14-devel %{_description}

This package contains library source intended for building other packages which
use the "v4_14" feature of the "%{crate}" crate.

%files       -n %{name}+v4_14-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v4_16-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v4_16-devel %{_description}

This package contains library source intended for building other packages which
use the "v4_16" feature of the "%{crate}" crate.

%files       -n %{name}+v4_16-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v4_18-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v4_18-devel %{_description}

This package contains library source intended for building other packages which
use the "v4_18" feature of the "%{crate}" crate.

%files       -n %{name}+v4_18-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v4_2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v4_2-devel %{_description}

This package contains library source intended for building other packages which
use the "v4_2" feature of the "%{crate}" crate.

%files       -n %{name}+v4_2-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v4_4-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v4_4-devel %{_description}

This package contains library source intended for building other packages which
use the "v4_4" feature of the "%{crate}" crate.

%files       -n %{name}+v4_4-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v4_6-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v4_6-devel %{_description}

This package contains library source intended for building other packages which
use the "v4_6" feature of the "%{crate}" crate.

%files       -n %{name}+v4_6-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+vulkan-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+vulkan-devel %{_description}

This package contains library source intended for building other packages which
use the "vulkan" feature of the "%{crate}" crate.

%files       -n %{name}+vulkan-devel
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
