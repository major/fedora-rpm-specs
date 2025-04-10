# Generated by rust2rpm 26
# * tests can only be run in-tree
%bcond_with check
%global debug_package %{nil}

%global crate futures-util

Name:           rust-futures-util
Version:        0.3.31
Release:        %autorelease
Summary:        Common utilities and extension traits for the futures-rs library

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/futures-util
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * drop unused compat support for futures 0.1
# * drop unused compat support for tokio 0.1
Patch:          futures-util-fix-metadata.diff
# * revert upstream change that broke compilation with Rust < 1.81:
#   https://github.com/rust-lang/futures-rs/issues/2892
Patch10:        0001-revert-removal-of-unstable-io_slice_advance-feature-.patch

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Common utilities and extension traits for the futures-rs library.}

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

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async-await-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-await-devel %{_description}

This package contains library source intended for building other packages which
use the "async-await" feature of the "%{crate}" crate.

%files       -n %{name}+async-await-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async-await-macro-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-await-macro-devel %{_description}

This package contains library source intended for building other packages which
use the "async-await-macro" feature of the "%{crate}" crate.

%files       -n %{name}+async-await-macro-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+bilock-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bilock-devel %{_description}

This package contains library source intended for building other packages which
use the "bilock" feature of the "%{crate}" crate.

%files       -n %{name}+bilock-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+cfg-target-has-atomic-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cfg-target-has-atomic-devel %{_description}

This package contains library source intended for building other packages which
use the "cfg-target-has-atomic" feature of the "%{crate}" crate.

%files       -n %{name}+cfg-target-has-atomic-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+channel-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+channel-devel %{_description}

This package contains library source intended for building other packages which
use the "channel" feature of the "%{crate}" crate.

%files       -n %{name}+channel-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures-channel-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-channel-devel %{_description}

This package contains library source intended for building other packages which
use the "futures-channel" feature of the "%{crate}" crate.

%files       -n %{name}+futures-channel-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures-io-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-io-devel %{_description}

This package contains library source intended for building other packages which
use the "futures-io" feature of the "%{crate}" crate.

%files       -n %{name}+futures-io-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures-macro-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-macro-devel %{_description}

This package contains library source intended for building other packages which
use the "futures-macro" feature of the "%{crate}" crate.

%files       -n %{name}+futures-macro-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures-sink-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-sink-devel %{_description}

This package contains library source intended for building other packages which
use the "futures-sink" feature of the "%{crate}" crate.

%files       -n %{name}+futures-sink-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+io-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+io-devel %{_description}

This package contains library source intended for building other packages which
use the "io" feature of the "%{crate}" crate.

%files       -n %{name}+io-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+memchr-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+memchr-devel %{_description}

This package contains library source intended for building other packages which
use the "memchr" feature of the "%{crate}" crate.

%files       -n %{name}+memchr-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+portable-atomic-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+portable-atomic-devel %{_description}

This package contains library source intended for building other packages which
use the "portable-atomic" feature of the "%{crate}" crate.

%files       -n %{name}+portable-atomic-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+sink-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sink-devel %{_description}

This package contains library source intended for building other packages which
use the "sink" feature of the "%{crate}" crate.

%files       -n %{name}+sink-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+slab-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+slab-devel %{_description}

This package contains library source intended for building other packages which
use the "slab" feature of the "%{crate}" crate.

%files       -n %{name}+slab-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-devel %{_description}

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%files       -n %{name}+unstable-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+write-all-vectored-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+write-all-vectored-devel %{_description}

This package contains library source intended for building other packages which
use the "write-all-vectored" feature of the "%{crate}" crate.

%files       -n %{name}+write-all-vectored-devel
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
