# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate libbpf-sys
%global crate_version 1.5.0+v1.5.0

Name:           rust-libbpf-sys
Version:        1.5.0
Release:        %autorelease
Summary:        Rust bindings to libbpf from the Linux kernel

License:        BSD-2-Clause
URL:            https://crates.io/crates/libbpf-sys
Source:         %{crates_source %{crate} %{crate_version}}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          libbpf-sys-fix-metadata-auto.diff
# Manually created patch for downstream crate metadata changes
# * relax bindgen version requirement from ^0.70.1 to allow version 0.69
Patch:          libbpf-sys-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  elfutils-libelf-devel
BuildRequires:  kernel-headers
BuildRequires:  zlib-devel

%global _description %{expand:
Rust bindings to libbpf from the Linux kernel.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       elfutils-libelf-devel
Requires:       kernel-headers
Requires:       zlib-devel

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%license %{crate_instdir}/libbpf/LICENSE
%license %{crate_instdir}/libbpf/LICENSE.BSD-2-Clause
%license %{crate_instdir}/libbpf/LICENSE.LGPL-2.1
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

%package     -n %{name}+bindgen-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bindgen-devel %{_description}

This package contains library source intended for building other packages which
use the "bindgen" feature of the "%{crate}" crate.

%files       -n %{name}+bindgen-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+bindgen-source-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bindgen-source-devel %{_description}

This package contains library source intended for building other packages which
use the "bindgen-source" feature of the "%{crate}" crate.

%files       -n %{name}+bindgen-source-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+novendor-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+novendor-devel %{_description}

This package contains library source intended for building other packages which
use the "novendor" feature of the "%{crate}" crate.

%files       -n %{name}+novendor-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+static-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+static-devel %{_description}

This package contains library source intended for building other packages which
use the "static" feature of the "%{crate}" crate.

%files       -n %{name}+static-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+static-libbpf-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+static-libbpf-devel %{_description}

This package contains library source intended for building other packages which
use the "static-libbpf" feature of the "%{crate}" crate.

%files       -n %{name}+static-libbpf-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+static-libelf-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+static-libelf-devel %{_description}

This package contains library source intended for building other packages which
use the "static-libelf" feature of the "%{crate}" crate.

%files       -n %{name}+static-libelf-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+static-zlib-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+static-zlib-devel %{_description}

This package contains library source intended for building other packages which
use the "static-zlib" feature of the "%{crate}" crate.

%files       -n %{name}+static-zlib-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+vendored-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+vendored-devel %{_description}

This package contains library source intended for building other packages which
use the "vendored" feature of the "%{crate}" crate.

%files       -n %{name}+vendored-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+vendored-libbpf-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+vendored-libbpf-devel %{_description}

This package contains library source intended for building other packages which
use the "vendored-libbpf" feature of the "%{crate}" crate.

%files       -n %{name}+vendored-libbpf-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+vendored-libelf-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+vendored-libelf-devel %{_description}

This package contains library source intended for building other packages which
use the "vendored-libelf" feature of the "%{crate}" crate.

%files       -n %{name}+vendored-libelf-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+vendored-zlib-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+vendored-zlib-devel %{_description}

This package contains library source intended for building other packages which
use the "vendored-zlib" feature of the "%{crate}" crate.

%files       -n %{name}+vendored-zlib-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{crate_version} -p1
rm -rf elfutils zlib
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
