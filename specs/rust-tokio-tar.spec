# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate tokio-tar

Name:           rust-tokio-tar
Version:        0.3.1
Release:        %autorelease
Summary:        Rust implementation of an async TAR file reader and writer

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/tokio-tar
Source:         %{crates_source}
# # * GitHub sources corresponding to the published crate; we extract only the
# #   tests/archives/ subdirectory for running tests.
Source10:       https://github.com/vorot93/tokio-tar/archive/v%{version}/tokio-tar-%{version}.tar.gz
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          tokio-tar-fix-metadata-auto.diff
# # * Use portable-atomic to support PowerPC
# # * https://github.com/vorot93/tokio-tar/pull/23
# # * Rebased on released crate (with normalized Cargo.toml)
Patch10:       tokio-tar-0.3.1-ppc64le.patch

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A Rust implementation of an async TAR file reader and writer. This
library does not currently handle compression, but it is abstract over
all I/O readers and writers. Additionally, great lengths are taken to
ensure that the entire contents are never required to be entirely
resident in memory all at once.}

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

%package     -n %{name}+xattr-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+xattr-devel %{_description}

This package contains library source intended for building other packages which
use the "xattr" feature of the "%{crate}" crate.

%files       -n %{name}+xattr-devel
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
# Extract test tarballs (only) from the GitHub archive
tar -xzvf '%{SOURCE10}' --strip-components=1 'tokio-tar-%{version}/tests/archives/'
%ifnarch %{ix86} aarch64
# * There are various flaky failures due to apparent race conditions; see
#   discussion in https://github.com/astral-sh/uv/issues/3423. For now, the best
#   we can do is to skip the most-frequently-failing test unconditionally.
%cargo_test -- -- --exact --skip insert_local_file_different_name
%elifarch %{ix86}
# Additionally, builder::Builder<W>::append_dir_all fails with “memory
# allocation of 1677721600 bytes failed” on i686.
# * https://github.com/astral-sh/uv/issues/3423#issuecomment-2120970932
%cargo_test -- -- --skip insert_local_file_different_name --skip 'builder::Builder<W>::append_dir_all'
%elifarch aarch64
# Flaky test failures are so widespread on this architecture that we need
# to skip a lot more individual tests to avoid excessive build failures.
%cargo_test -- -- --exact --skip insert_local_file_different_name --skip large_filename --skip path_separators --skip writing_and_extracting_directories --skip writing_files
%endif
%endif

%changelog
%autochangelog
