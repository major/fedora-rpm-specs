# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate libheif-sys
%global crate_version 4.1.0+1.19.8

Name:           rust-libheif-sys
Version:        4.1.0
Release:        %autorelease
Summary:        Libheif bindings

License:        MIT
URL:            https://crates.io/crates/libheif-sys
Source:         %{crates_source %{crate} %{crate_version}}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          libheif-sys-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  pkgconfig(libheif) >= 1.16

%global _description %{expand:
Libheif bindings.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libheif) >= 1.16

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/README.md
%doc %{crate_instdir}/dev.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+latest-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+latest-devel %{_description}

This package contains library source intended for building other packages which
use the "latest" feature of the "%{crate}" crate.

%files       -n %{name}+latest-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+use-bindgen-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+use-bindgen-devel %{_description}

This package contains library source intended for building other packages which
use the "use-bindgen" feature of the "%{crate}" crate.

%files       -n %{name}+use-bindgen-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v1_17-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v1_17-devel %{_description}

This package contains library source intended for building other packages which
use the "v1_17" feature of the "%{crate}" crate.

%files       -n %{name}+v1_17-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v1_18-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v1_18-devel %{_description}

This package contains library source intended for building other packages which
use the "v1_18" feature of the "%{crate}" crate.

%files       -n %{name}+v1_18-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v1_19-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v1_19-devel %{_description}

This package contains library source intended for building other packages which
use the "v1_19" feature of the "%{crate}" crate.

%files       -n %{name}+v1_19-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{crate_version} -p1
%cargo_prep
# drop vendored copy of libbeif
rm -rf vendor/

%generate_buildrequires
%cargo_generate_buildrequires -f v1_17

%build
%cargo_build -f v1_17

%install
%cargo_install -f v1_17

%if %{with check}
%check
# * skip a test that expects a an exact libheif version
%cargo_test -f v1_17 -- -- --skip create_heic_context
%endif

%changelog
%autochangelog
