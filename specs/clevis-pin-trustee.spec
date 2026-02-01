# SPDX-FileCopyrightText: Sergio Arroutbi <sarroutb@redhat.com>
#
# SPDX-License-Identifier: MIT

# Fedora: Use system Rust libraries as josekit 0.7.4+ is available
%global bundled_rust_deps 0

Name:           clevis-pin-trustee
Version:        0.0.1
Release:        %autorelease
Summary:        Clevis PIN for Trustee attestation

# (Apache-2.0 OR MIT) AND BSD-3-Clause
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# MIT OR Zlib OR Apache-2.0
# Unicode-3.0
# Unlicense OR MIT
License:        BSD-3-Clause AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND MIT AND (MIT OR Zlib OR Apache-2.0) AND Unicode-3.0 AND (Unlicense OR MIT)
URL:            https://github.com/latchset/clevis-pin-trustee
Source0:        https://github.com/latchset/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo-rpm-macros
BuildRequires:  openssl-devel
# rust-tempfile required for test execution
BuildRequires:  rust-tempfile+default-devel

# Runtime dependencies
Requires:       clevis
Requires:       jose

%description
clevis-pin-trustee is a Clevis PIN that implements encryption and decryption
operations using remote attestation via a Trustee server. It enables automated
unlocking of LUKS-encrypted volumes in confidential computing environments by
fetching encryption keys from Trustee servers after successful attestation.

%prep
%autosetup
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
# Build using cargo macros
%cargo_build

# Generate license information for statically-linked dependencies
%cargo_license_summary
# Generate license file for bundled dependencies
%{cargo_license} > LICENSE.dependencies

%install
# Install main binary
install -D -m 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# Install Clevis wrapper scripts
install -D -m 0755 clevis-encrypt-trustee %{buildroot}%{_bindir}/clevis-encrypt-trustee
install -D -m 0755 clevis-decrypt-trustee %{buildroot}%{_bindir}/clevis-decrypt-trustee

%check
# Run tests using cargo macro
%cargo_test

%files
%license LICENSES/MIT.txt
%license LICENSE.dependencies
%doc README.md
%{_bindir}/%{name}
%{_bindir}/clevis-encrypt-trustee
%{_bindir}/clevis-decrypt-trustee

%changelog
%autochangelog
