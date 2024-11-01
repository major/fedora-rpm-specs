# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate rkyv

Name:           rust-rkyv0.7
Version:        0.7.45
Release:        %autorelease
Summary:        Zero-copy deserialization framework for Rust

License:        MIT
URL:            https://crates.io/crates/rkyv
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * bump hashbrown dependency from 0.12 to 0.14
# * drop unused support for various third-party crates
Patch:          rkyv-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Zero-copy deserialization framework for Rust.}

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
%doc %{crate_instdir}/crates-io.md
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

%package     -n %{name}+arbitrary_enum_discriminant-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+arbitrary_enum_discriminant-devel %{_description}

This package contains library source intended for building other packages which
use the "arbitrary_enum_discriminant" feature of the "%{crate}" crate.

%files       -n %{name}+arbitrary_enum_discriminant-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+archive_be-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+archive_be-devel %{_description}

This package contains library source intended for building other packages which
use the "archive_be" feature of the "%{crate}" crate.

%files       -n %{name}+archive_be-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+archive_le-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+archive_le-devel %{_description}

This package contains library source intended for building other packages which
use the "archive_le" feature of the "%{crate}" crate.

%files       -n %{name}+archive_le-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+arrayvec-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+arrayvec-devel %{_description}

This package contains library source intended for building other packages which
use the "arrayvec" feature of the "%{crate}" crate.

%files       -n %{name}+arrayvec-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+bytecheck-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bytecheck-devel %{_description}

This package contains library source intended for building other packages which
use the "bytecheck" feature of the "%{crate}" crate.

%files       -n %{name}+bytecheck-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+copy-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+copy-devel %{_description}

This package contains library source intended for building other packages which
use the "copy" feature of the "%{crate}" crate.

%files       -n %{name}+copy-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+copy_unsafe-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+copy_unsafe-devel %{_description}

This package contains library source intended for building other packages which
use the "copy_unsafe" feature of the "%{crate}" crate.

%files       -n %{name}+copy_unsafe-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+hashbrown-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+hashbrown-devel %{_description}

This package contains library source intended for building other packages which
use the "hashbrown" feature of the "%{crate}" crate.

%files       -n %{name}+hashbrown-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rend-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rend-devel %{_description}

This package contains library source intended for building other packages which
use the "rend" feature of the "%{crate}" crate.

%files       -n %{name}+rend-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+size_16-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+size_16-devel %{_description}

This package contains library source intended for building other packages which
use the "size_16" feature of the "%{crate}" crate.

%files       -n %{name}+size_16-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+size_32-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+size_32-devel %{_description}

This package contains library source intended for building other packages which
use the "size_32" feature of the "%{crate}" crate.

%files       -n %{name}+size_32-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+size_64-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+size_64-devel %{_description}

This package contains library source intended for building other packages which
use the "size_64" feature of the "%{crate}" crate.

%files       -n %{name}+size_64-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+strict-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+strict-devel %{_description}

This package contains library source intended for building other packages which
use the "strict" feature of the "%{crate}" crate.

%files       -n %{name}+strict-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+validation-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+validation-devel %{_description}

This package contains library source intended for building other packages which
use the "validation" feature of the "%{crate}" crate.

%files       -n %{name}+validation-devel
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
