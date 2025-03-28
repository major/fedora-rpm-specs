# Generated by rust2rpm 22
%bcond_without check
%global debug_package %{nil}

%global crate compress-tools

Name:           rust-compress-tools
Version:        0.12.4
Release:        %autorelease
Summary:        Utility functions for compressed and archive files handling

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/compress-tools
Source:         %{crates_source}
# Automatically generated patch to strip foreign dependencies
Patch:          compress-tools-fix-metadata-auto.diff
# * backported upstream patch to port from encoding to encoding_rs:
#   https://github.com/OSSystems/compress-tools-rs/commit/5e7bbdd
Patch:          0001-backport-tests-port-from-unmaintained-crate-encoding.patch

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Utility functions for compressed and archive files handling.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libarchive) >= 3.5.1

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/CHANGES.md
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

%package     -n %{name}+async-trait-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-trait-devel %{_description}

This package contains library source intended for building other packages which
use the "async-trait" feature of the "%{crate}" crate.

%files       -n %{name}+async-trait-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async_support-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async_support-devel %{_description}

This package contains library source intended for building other packages which
use the "async_support" feature of the "%{crate}" crate.

%files       -n %{name}+async_support-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+blocking-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+blocking-devel %{_description}

This package contains library source intended for building other packages which
use the "blocking" feature of the "%{crate}" crate.

%files       -n %{name}+blocking-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures-channel-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-channel-devel %{_description}

This package contains library source intended for building other packages which
use the "futures-channel" feature of the "%{crate}" crate.

%files       -n %{name}+futures-channel-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures-core-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-core-devel %{_description}

This package contains library source intended for building other packages which
use the "futures-core" feature of the "%{crate}" crate.

%files       -n %{name}+futures-core-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures-executor-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-executor-devel %{_description}

This package contains library source intended for building other packages which
use the "futures-executor" feature of the "%{crate}" crate.

%files       -n %{name}+futures-executor-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures-io-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-io-devel %{_description}

This package contains library source intended for building other packages which
use the "futures-io" feature of the "%{crate}" crate.

%files       -n %{name}+futures-io-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures-util-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-util-devel %{_description}

This package contains library source intended for building other packages which
use the "futures-util" feature of the "%{crate}" crate.

%files       -n %{name}+futures-util-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures_support-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures_support-devel %{_description}

This package contains library source intended for building other packages which
use the "futures_support" feature of the "%{crate}" crate.

%files       -n %{name}+futures_support-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tokio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-devel %{_description}

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%files       -n %{name}+tokio-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tokio-util-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-util-devel %{_description}

This package contains library source intended for building other packages which
use the "tokio-util" feature of the "%{crate}" crate.

%files       -n %{name}+tokio-util-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tokio_support-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio_support-devel %{_description}

This package contains library source intended for building other packages which
use the "tokio_support" feature of the "%{crate}" crate.

%files       -n %{name}+tokio_support-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'pkgconfig(libarchive) >= 3.5.1'

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
# some tests require the environment to have a UTF-8 locale
export LANG=C.UTF-8
%cargo_test
%endif

%changelog
%autochangelog
