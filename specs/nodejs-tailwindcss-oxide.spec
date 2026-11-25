# The npm package is scoped (@tailwindcss/oxide); npm_name is the install path
# under %%{nodejs_sitelib}, src_name is the (slash-free) prefix used for the
# generated Source tarballs, and upstream_name is the monorepo repo/dir name.
%global npm_name @tailwindcss/oxide
%global src_name tailwindcss-oxide
%global upstream_name tailwindcss
%undefine _package_note_flags

Name:           nodejs-tailwindcss-oxide
Version:        4.3.3
Release:        %autorelease
Summary:        The Oxide engine for Tailwind CSS (native Node.js addon)

# The @tailwindcss/oxide npm package (napi JS wrapper) and the Rust crates in
# the tailwindcss monorepo are MIT.  The bundled crate dependencies carry
# additional licenses, enumerated in LICENSE.dependencies (generated at build
# time from the vendored crates) and %%{src_name}-%%{version}-bundled-licenses.txt
# (the npm dev dependency, @napi-rs/cli).
License:        MIT AND ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND (Apache-2.0 OR MIT) AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND ISC AND (MIT OR Apache-2.0) AND MIT AND MPL-2.0 AND (Unlicense OR MIT)
URL:            https://tailwindcss.com/
# Upstream ships @tailwindcss/oxide from the tailwindlabs/tailwindcss monorepo;
# the napi crate lives in crates/node and depends on the other crates/* members.
# The stripped tarball is the whole workspace (see tailwindcss-oxide-sources.sh),
# which unpacks to %%{upstream_name}-%%{version}/.
Source0:        %{src_name}-%{version}-stripped.tar.gz
# Dev dependency (@napi-rs/cli, providing the "napi" build CLI).  There are no
# runtime dependencies, so no nm-prod tarball is needed.
Source1:        %{src_name}-%{version}-nm-dev.tgz
Source2:        %{src_name}-%{version}-bundled-licenses.txt
# To create the vendor tarball (see tailwindcss-oxide-sources.sh):
#   tar xf v%%{version}.tar.gz ; pushd %%{upstream_name}-%%{version} ; \
#   cargo vendor && tar Jcvf ../%%{src_name}-%%{version}-vendor.tar.xz vendor/ ; popd
Source3:        %{src_name}-%{version}-vendor.tar.xz

ExclusiveArch:  %{nodejs_arches}
ExcludeArch:    %{ix86}

Requires:       nodejs24
BuildRequires:  nodejs24-npm
BuildRequires:  /usr/bin/npm
BuildRequires:  nodejs24
BuildRequires:  nodejs24-devel
BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  gcc
BuildRequires:  gcc-c++

# https://src.fedoraproject.org/rpms/nodejs-packaging/pull-request/22
# nodejs-packaging bug: does not generate Provides: for scoped modules
# temporarily provide this manually
Provides: npm(@tailwindcss/oxide) = %{version}

%description
Oxide is the high-performance engine at the heart of Tailwind CSS v4, written
in Rust.  This package provides the Node.js bindings (@tailwindcss/oxide), with
the native addon built from source against the vendored Rust crate
dependencies.


%prep
# -a1 unpacks the dev modules (node_modules_dev/), -a3 the vendored crates
# (vendor/).  Both land at the workspace root.
%setup -q -n %{upstream_name}-%{version} -a1 -a3
cp %{SOURCE2} .

# Assemble a node_modules farm from the bundled dev modules so the napi CLI
# (@napi-rs/cli) is on PATH at build time.  There are no prod dependencies.
mkdir -p node_modules
pushd node_modules
ln -sf ../node_modules_dev/* .
mkdir -p .bin
pushd .bin
ln -s ../../node_modules_dev/.bin/* .
popd
popd

# Upstream ships crates/node/.cargo/config.toml with per-target linker overrides
# (e.g. [target.aarch64-unknown-linux-gnu] linker = "aarch64-linux-gnu-gcc")
# intended for cross-compiling the release binaries from x86_64.  napi build
# --platform passes an explicit --target, and cargo applies [target.<triple>]
# config even for a native build, so on aarch64 it would invoke a cross-linker
# that is not installed in the buildroot.  Remove these so the default system
# linker is used; we only ever build natively.
find crates -path '*/.cargo/config.toml' -print -delete

# Configure cargo to build offline from the vendored crates (Source3).  Cargo.toml
# and Cargo.lock are at the workspace root, so prep here.
%cargo_prep -v vendor


%build
# Build entirely offline: the native binding from the vendored Rust crates.  Do
# NOT run "npm install" here; it would reach the network and discard the bundled
# modules.
export CARGO_NET_OFFLINE=true
export npm_config_offline=true
export npm_config_audit=false
export npm_config_fund=false
export PATH="${PWD}/node_modules/.bin:${PATH}"
# The napi module will attempt to use a linker that is not available
# on some architectures.
export CARGO_TARGET_S390X_UNKNOWN_LINUX_GNU_LINKER=gcc
export CARGO_TARGET_POWERPC64LE_UNKNOWN_LINUX_GNU_LINKER=gcc

# Compile the native (napi) addon from the crates/node package.  This mirrors the
# package's "build:platform" script (napi build --platform --release) but skips
# the wasm target and the postbuild move-artifacts step (which only distributes
# the binary into the per-platform npm sub-packages we do not ship).  napi-rs
# also generates index.js and index.d.ts (the loader + type stubs) next to the
# emitted tailwindcss-oxide.<triple>.node.  Run from crates/node so napi reads
# its package.json "napi" config; the workspace and the vendored-source config
# (written by %%cargo_prep at the tree root) are found by cargo's upward search.
pushd crates/node
napi build --platform --release
popd

# Record the licenses of the (vendored) Rust crate dependencies.
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

# Contents of the package's package.json "files": ["index.js","index.d.ts"],
# both generated by napi build in %%build.
cp -p crates/node/index.js crates/node/index.d.ts \
    %{buildroot}%{nodejs_sitelib}/%{npm_name}/

# The native addon built in %%build.  index.js loads it as
# ./tailwindcss-oxide.<triple>.node (its first choice, before any per-platform
# npm package), so shipping it at the package root is sufficient on any arch.
cp -p crates/node/tailwindcss-oxide.*.node %{buildroot}%{nodejs_sitelib}/%{npm_name}/

cp -p crates/node/package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}/

%cargo_vendor_manifest


%check
# Load the *installed* package to catch packaging mistakes (missing native
# addon, wrong file layout).  require() throws if the native binding fails to
# load, and Scanner is re-exported straight from it, so this exercises the
# addon.  Keep this on a single line: backslash line-continuations inside
# node -e '...' are passed literally into the script and break parsing.
%{__nodejs} -e 'const oxide = require("%{buildroot}%{nodejs_sitelib}/%{npm_name}"); if (typeof oxide.Scanner !== "function") throw new Error("@tailwindcss/oxide native binding did not load");'


%files
%doc README.md
%license LICENSE %{src_name}-%{version}-bundled-licenses.txt LICENSE.dependencies cargo-vendor.txt
%{nodejs_sitelib}/%{npm_name}
%dir %{nodejs_sitelib}/@%{upstream_name}


%changelog
%autochangelog
