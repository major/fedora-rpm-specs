# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate chrono-tz-build

Name:           rust-chrono-tz-build
Version:        0.3.0
Release:        %autorelease
Summary:        Internal build script for chrono-tz

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/chrono-tz-build
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Internal build script for chrono-tz.}

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

%package     -n %{name}+case-insensitive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+case-insensitive-devel %{_description}

This package contains library source intended for building other packages which
use the "case-insensitive" feature of the "%{crate}" crate.

%files       -n %{name}+case-insensitive-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+filter-by-regex-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+filter-by-regex-devel %{_description}

This package contains library source intended for building other packages which
use the "filter-by-regex" feature of the "%{crate}" crate.

%files       -n %{name}+filter-by-regex-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+regex-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+regex-devel %{_description}

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%files       -n %{name}+regex-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+uncased-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+uncased-devel %{_description}

This package contains library source intended for building other packages which
use the "uncased" feature of the "%{crate}" crate.

%files       -n %{name}+uncased-devel
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