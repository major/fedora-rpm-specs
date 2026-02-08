%bcond check 1

# RHEL lacks individual packaged Rust crates, so we must bundle them (Source2).
# Fedora has these crates packaged, so we can use system dependencies.
%if 0%{?rhel}
%bcond_without bundle_rust_deps
%else
%bcond_with bundle_rust_deps
%endif

Name:           trustee
Version:        0.15.0
Release:        %autorelease
Summary:        Tools and components for attesting confidential guests and providing secrets

### BEGIN LICENSE SUMMARY ###
# (Apache-2.0 OR MIT) AND BSD-3-Clause
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 AND ISC AND (MIT OR Apache-2.0)
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# BSD-3-Clause
# ISC
# MIT
# MIT AND Apache-2.0 AND BSD-3-Clause
# MIT OR Apache-2.0
# MIT OR Zlib OR Apache-2.0
# MPL-2.0
# Unicode-3.0
# Unlicense OR MIT
# Zlib
###  END LICENSE SUMMARY  ###

License:        %{shrink: Apache-2.0 AND
                         (Apache-2.0 OR BSL-1.0) AND
                          BSD-2-Clause AND
                          BSD-3-Clause AND
                          ISC AND
                          MIT AND
                          MPL-2.0 AND
                          Unicode-DFS-2016 AND
                          Unicode-3.0 AND
                          Zlib}
URL:            https://github.com/confidential-containers/trustee
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        https://github.com/confidential-containers/guest-components/archive/refs/tags/v%{version}/guest-components-%{version}.tar.gz
# Generated via create_vendor_source.sh script
Source2:		trustee-%{version}-vendor.tar.zstd

# Restrict workspace members for the kbs component only
Patch: 0001-restrict-workspace-members-to-kbs-only.patch
# Remove built-in attestation-service for lightweight broker(only kbs) mode
Patch: 0002-kbs-remove-built-in-attestation-service-for-lightwei.patch
# Drop concat-kdf dependency in favor of internal implementation similarly to guest-components does
Patch: 0003-kbs-replace-concat-kdf-dependency-with-internal-impl.patch
# replace jwt-simple with jsonwebtoken in Admin API to reduce dependencies
Patch: 0004-Refactor-kbs-replace-jwt-simple-with-jsonwebtoken-in.patch
# adjust project dependencies to align with Fedora upstreams
Patch: 0005-Refactor-deps-align-crate-versions-with-Fedora-upstr.patch
# replace derivative with educe for debug derivation
# https://github.com/confidential-containers/trustee/pull/1086
Patch: 0006-replace-derivative-with-educe-for-debug-derivation.patch
# replace git dependencies with path/registry deps for offline builds
Patch: 0007-replace-git-dependencies-with-path-registry-deps-for.patch
# do not import RVPS in config tests
Patch: 0008-guard-RVPS-import-in-config-tests.patch

%if %{with bundle_rust_deps}
BuildRequires:  rust-toolset
BuildRequires:  pkgconfig
%else
BuildRequires:  cargo-rpm-macros
%endif
BuildRequires:  git-core

%description
Tools and components for attesting confidential guests and providing secrets to 
them. Collectively, these components are known as Trustee. Trustee typically
operates on behalf of the guest owner and interacts remotely with guest
components, providing the necessary services for Attestation and Secret
Delivery.

#===============================================================================

%package kbs
Summary:        Key Broker Service for Confidential Computing
Requires:       openssl

%description kbs
The Key Broker Service (KBS) is a key management component for Confidential
Computing scenarios. It provides secure key distribution for confidential
containers and virtual machines. KBS supports multiple backend storage
systems and attestation services.

#===============================================================================

%prep
%autosetup -n trustee-%{version} -a1 -S git

%if %{with bundle_rust_deps}
tar xf %{SOURCE2}
# The vendor tarball may contain files with the executable bit set.
# If these files start with an inner attribute like `#![no_std]`,
# rpmbuild's dependency generator interprets the `#!` as a shebang
# and fails because the path is invalid. Removing the executable bit
# prevents this check.
find vendor -type f -exec chmod -x {} +
%cargo_prep -v vendor
%else
%cargo_prep
%generate_buildrequires
%cargo_generate_buildrequires
%endif

# Force openssl-sys to use system OpenSSL instead of building from source.
# 1. Check if OPENSSL_NO_VENDOR is already defined (skips if true).
# 2. Check if [env] section exists. If not, append it.
# 3. Insert the variable definition after the [env] header.
if ! grep -q "OPENSSL_NO_VENDOR" .cargo/config.toml; then
  grep -q "^\[env\]" .cargo/config.toml || printf "\n[env]\n" >> .cargo/config.toml
  sed -i '/^\[env\]/a OPENSSL_NO_VENDOR = "1"' .cargo/config.toml
fi

%build
%cargo_build

%if %{with bundle_rust_deps}
%cargo_vendor_manifest
%endif

%cargo_license_summary
%{cargo_license} > LICENSE.dependencies

%install
# Install KBS
install -D -m 755 target/rpm/kbs %{buildroot}%{_bindir}/kbs

%if %{with check}
%check
%cargo_test
%endif

%files kbs
%license LICENSE
%license LICENSE.dependencies
%if %{with bundle_rust_deps}
%license cargo-vendor.txt
%endif
%doc README.md
%{_bindir}/kbs

%changelog
%autochangelog