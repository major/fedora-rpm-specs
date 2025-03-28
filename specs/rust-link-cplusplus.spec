# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate link-cplusplus

Name:           rust-link-cplusplus
Version:        1.0.10
Release:        %autorelease
Summary:        Link libstdc++ or libc++ automatically or manually

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/link-cplusplus
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Link libstdc++ or libc++ automatically or manually.}

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

%package     -n %{name}+libc++-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libc++-devel %{_description}

This package contains library source intended for building other packages which
use the "libc++" feature of the "%{crate}" crate.

%files       -n %{name}+libc++-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+libcxx-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libcxx-devel %{_description}

This package contains library source intended for building other packages which
use the "libcxx" feature of the "%{crate}" crate.

%files       -n %{name}+libcxx-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+libstdc++-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libstdc++-devel %{_description}

This package contains library source intended for building other packages which
use the "libstdc++" feature of the "%{crate}" crate.

%files       -n %{name}+libstdc++-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+libstdcxx-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libstdcxx-devel %{_description}

This package contains library source intended for building other packages which
use the "libstdcxx" feature of the "%{crate}" crate.

%files       -n %{name}+libstdcxx-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+nothing-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nothing-devel %{_description}

This package contains library source intended for building other packages which
use the "nothing" feature of the "%{crate}" crate.

%files       -n %{name}+nothing-devel
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
