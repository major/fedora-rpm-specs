# rolldown ships as an unscoped npm package (install path %%{nodejs_sitelib}/rolldown).
# The published npm package is pure JavaScript glue (dist/ + bin/); the heavy
# lifting is done by a native napi addon, @rolldown/binding-<triple>, which
# upstream distributes as prebuilt per-platform packages.  This package rebuilds
# that addon from source (from the rolldown monorepo's crates/rolldown_binding)
# and ships the JS glue from the published npm tarball, so nothing prebuilt ships.
%global npm_name rolldown
%undefine _package_note_flags

Name:           nodejs-rolldown
Version:        1.2.15
Release:        %autorelease
Summary:        Fast Rust-based bundler for JavaScript with Rollup-compatible API

# rolldown itself and its JS runtime dependencies (@oxc-project/types,
# @rolldown/pluginutils) are MIT.  The native addon links the vendored Rust
# crates, whose licenses are enumerated in LICENSE.dependencies (generated at
# build time) and in rolldown-%%{version}-bundled-licenses.txt (the bundled npm
# build/runtime dependencies).
License:        MIT AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR GPL-2.0-only) AND (Apache-2.0 OR MIT OR Zlib) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR BSL-1.0) AND Apache-2.0 AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND (CC0-1.0 OR Apache-2.0 OR Apache-2.0 WITH LLVM-exception) AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND CC0-1.0 AND ISC AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND MIT-0 AND MIT AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT) AND Zlib
URL:            https://rolldown.rs/
# Two upstream inputs:
#  - Source0: the rolldown monorepo (GitHub tag v%%{version}), the full cargo
#    workspace, used ONLY to build the native binding from crates/rolldown_binding.
#    Unpacks to rolldown-%%{version}/.
#  - Source1: the published npm "rolldown" package, providing the prebuilt JS
#    glue (dist/, bin/).  Building that JS from source would require the full
#    oxc-node/tsc toolchain; it is plain JavaScript (no native code), so we ship
#    the published artifact, as the vite package does.  Unpacks to package/.
Source0:        %{npm_name}-%{version}-stripped.tar.gz
Source1:        %{npm_name}-%{version}-npm.tgz
# Runtime JS dependencies of rolldown (@oxc-project/types, @rolldown/pluginutils).
Source2:        %{npm_name}-%{version}-nm-prod.tgz
# Build-time JS dependency: @napi-rs/cli, which drives the napi/cargo build.
Source3:        %{npm_name}-%{version}-nm-dev.tgz
Source4:        %{npm_name}-%{version}-bundled-licenses.txt
# Vendored Rust crate dependencies, so cargo can build offline (see
# rolldown-sources.sh).  Cargo.toml/Cargo.lock live at the workspace root.
Source5:        %{npm_name}-%{version}-vendor.tar.xz

ExclusiveArch:  %{nodejs_arches}

Requires:       nodejs24
BuildRequires:  nodejs24-npm
BuildRequires:  /usr/bin/npm
BuildRequires:  nodejs24
BuildRequires:  nodejs24-devel
BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
rolldown is a fast JavaScript/TypeScript bundler written in Rust, powered by
Oxc, and designed as a drop-in replacement for Rollup.  It is the bundler used
by Vite 6+.  This package ships the JavaScript API together with the native
napi addon (@rolldown/binding) built from source against the vendored Rust crate
dependencies.


%prep
# -a3 unpacks the build-time JS modules (node_modules_dev/) and -a5 the vendored
# crates (vendor/); both land at the workspace root.
%setup -q -n %{npm_name}-%{version} -a3 -a5

# Unpack the published npm package (prebuilt JS glue) into npmpkg/.
mkdir -p npmpkg
tar xzf %{SOURCE1} -C npmpkg --strip-components=1

# Unpack rolldown's runtime JS dependencies (-> node_modules_prod/).
tar xzf %{SOURCE2}

cp %{SOURCE4} .

# Assemble a node_modules farm from the bundled dev modules so the napi CLI
# (@napi-rs/cli) is on PATH at build time.
mkdir -p node_modules
pushd node_modules
ln -sf ../node_modules_dev/* .
mkdir -p .bin
pushd .bin
ln -s ../../node_modules_dev/.bin/* .
popd
popd

# rolldown ships a workspace-root .cargo/config.toml whose [target.*] entries
# only cover Windows/WASM cross-builds (crt-static, simd128, tokio_unstable) that
# are irrelevant to a native Linux release build, and whose [env] table would
# collide (duplicate key) with the one %%cargo_prep writes.  Remove just this
# workspace-root config: it is the only one cargo reads (the build runs from
# packages/rolldown, whose upward config search reaches only the workspace root),
# and the trivial crates/rolldown_binding/build.rs reads none of its settings.
# Do NOT touch the vendored crates' own .cargo/config.toml files under vendor/ --
# they are part of those crates' cargo-checksummed contents.  %%cargo_prep then
# writes a clean config pointing at the vendored crates.
rm -f .cargo/config.toml

# Configure cargo to build offline from the vendored crates (Source5).  Cargo.toml
# and Cargo.lock are at the workspace root, so prep here.
%cargo_prep -v vendor


%build
# Build entirely offline.  Do NOT run "npm install"; it would reach the network
# and discard the bundled modules.
export CARGO_NET_OFFLINE=true
export npm_config_offline=true
export npm_config_audit=false
export npm_config_fund=false
export PATH="${PWD}/node_modules/.bin:${PATH}"

# Compile the native napi addon from crates/rolldown_binding.  This mirrors
# packages/rolldown/build-binding.ts (which calls "napi build --platform ...")
# but via the CLI so we do not need the oxc-node TS runtime.  Run from
# packages/rolldown so napi reads the "napi" config from its package.json
# (binaryName "rolldown-binding", packageName "@rolldown/binding"); cargo finds
# the workspace and the vendored-source config (written by %%cargo_prep at the
# tree root) via its upward search.  With --platform and no --target, napi builds
# for the host arch, emitting src/rolldown-binding.<napi-triple>.node.
pushd packages/rolldown
napi build --platform --release \
    --manifest-path ../../crates/rolldown_binding/Cargo.toml \
    --package rolldown_binding \
    --output-dir ./src
popd

# Record the licenses of the (vendored) Rust crate dependencies.
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies


%install
# 1. Ship the JavaScript package (published dist/ + bin/) as the rolldown module.
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr npmpkg/dist npmpkg/bin npmpkg/package.json \
    %{buildroot}%{nodejs_sitelib}/%{npm_name}/

# 2. Bundle rolldown's runtime JS dependencies under its OWN node_modules.  This
#    keeps the package self-contained (node resolves them locally) and, crucially,
#    makes the RPM nodejs dependency generator treat them as bundled: it then
#    suppresses the external npm() requires for these deps (which no system
#    package provides) and emits bundled() provides instead.
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}/node_modules
cp -pr node_modules_prod/* %{buildroot}%{nodejs_sitelib}/%{npm_name}/node_modules/

# 3. Install the native addon as a bundled @rolldown/binding-<triple> module, the
#    last entry in rolldown's binding loader fallback chain
#    (require("@rolldown/binding-<triple>")).  Derive the napi triple from the
#    built filename so this is arch-agnostic.
node_file=$(ls packages/rolldown/src/rolldown-binding.*.node)
triple=$(basename "${node_file}" .node)
triple=${triple#rolldown-binding.}
bindir=%{buildroot}%{nodejs_sitelib}/%{npm_name}/node_modules/@rolldown/binding-${triple}
mkdir -p "${bindir}"
cp -p "${node_file}" "${bindir}/"
cat > "${bindir}/package.json" <<EOF
{
  "name": "@rolldown/binding-${triple}",
  "version": "%{version}",
  "main": "rolldown-binding.${triple}.node"
}
EOF

# rolldown CLI.
install -dp %{buildroot}%{_bindir}
ln -s %{nodejs_sitelib}/%{npm_name}/bin/cli.mjs %{buildroot}%{_bindir}/rolldown


%check
# Load the *installed* ESM entry point.  Importing it evaluates rolldown's native
# binding loader, so this fails if the from-source @rolldown/binding-<triple>
# addon cannot be resolved or loaded.  rolldown() is the package's main export.
%{__nodejs} --input-type=module -e 'import { rolldown } from "%{buildroot}%{nodejs_sitelib}/%{npm_name}/dist/index.mjs"; if (typeof rolldown !== "function") { throw new Error("rolldown native binding did not load"); }'


%files
%doc npmpkg/README.md
%license LICENSE %{npm_name}-%{version}-bundled-licenses.txt LICENSE.dependencies
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/rolldown


%changelog
%autochangelog
