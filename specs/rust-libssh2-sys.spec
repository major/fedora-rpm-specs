# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate libssh2-sys

Name:           rust-libssh2-sys
Version:        0.3.0
Release:        %autorelease
Summary:        Native bindings to the libssh2 library

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/libssh2-sys
Source0:        %{crates_source}
# https://github.com/alexcrichton/ssh2-rs/issues/289
Source1:        https://github.com/alexcrichton/ssh2-rs/raw/libssh2-sys-0.3.0/LICENSE-APACHE
Source2:        https://github.com/alexcrichton/ssh2-rs/raw/libssh2-sys-0.3.0/LICENSE-MIT
# Automatically generated patch to strip foreign dependencies
Patch:          libssh2-sys-fix-metadata-auto.diff
# Manually created patch for downstream crate metadata changes
# * drop windows-specific dependencies and features
# * drop dependency and feature for unused zlib-ng support
# * drop feature for vendored OpenSSL sources
Patch:          libssh2-sys-fix-metadata.diff
# * unconditionally link against system libssh2 with pkg-config
Patch:          0001-build.rs-always-use-pkg-config.patch

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Native bindings to the libssh2 library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libssh2)

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
# remove bundled copy of libssh2 sources
rm -rv libssh2/
%cargo_prep
cp -pav %{SOURCE1} %{SOURCE2} .

%generate_buildrequires
%cargo_generate_buildrequires
echo 'pkgconfig(libssh2)'

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