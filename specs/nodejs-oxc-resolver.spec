# oxc-resolver ships as an unscoped npm package (install path
# %%{nodejs_sitelib}/oxc-resolver).  The published npm package is pure JavaScript
# glue (index.js + a napi loader); the actual work is done by a native napi addon
# (@oxc-resolver/binding-<triple>), which upstream distributes as prebuilt
# per-platform packages.  This package rebuilds that addon from source (from the
# oxc-project/oxc-resolver repo's napi crate) and ships the JS glue from the
# published npm tarball, so nothing prebuilt ships.
%global npm_name oxc-resolver
%undefine _package_note_flags

Name:           nodejs-oxc-resolver
Version:        11.24.2
Release:        %autorelease
Summary:        ESM/CJS module resolution algorithm implemented in Rust

# oxc-resolver's JS glue and the Rust napi crate are MIT.  The native addon links
# the vendored Rust crates, whose licenses are enumerated in LICENSE.dependencies
# (generated at build time) and in oxc-resolver-%%{version}-bundled-licenses.txt
# (the bundled npm build dependency, @napi-rs/cli).
License:        MIT AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR GPL-2.0-only) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-2-Clause AND ISC AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND MIT AND (Unlicense OR MIT) AND Zlib
URL:            https://oxc.rs
# Two upstream inputs:
#  - Source0: the oxc-resolver repo (GitHub tag v%%{version}), the cargo
#    workspace, used to build the native binding from the napi/ crate.  Unpacks to
#    oxc-resolver-%%{version}/.
#  - Source1: the published npm "oxc-resolver" package, providing the JS glue
#    (index.js, the napi loader, browser/webcontainer fallbacks).  This is plain
#    JavaScript (no native code), so we ship the published artifact.  Unpacks to
#    package/.
Source0:        %{npm_name}-%{version}-stripped.tar.gz
Source1:        %{npm_name}-%{version}-npm.tgz
# Build-time JS dependency: @napi-rs/cli, which drives the napi/cargo build.
# oxc-resolver has no runtime JS dependencies, so there is no nm-prod tarball.
Source2:        %{npm_name}-%{version}-nm-dev.tgz
Source3:        %{npm_name}-%{version}-bundled-licenses.txt
# Vendored Rust crate dependencies, so cargo can build offline (see
# oxc-resolver-sources.sh).  Cargo.toml/Cargo.lock live at the workspace root.
Source4:        %{npm_name}-%{version}-vendor.tar.xz

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
oxc-resolver is a fast implementation of the Node.js module resolution algorithm
(including ESM, CommonJS, tsconfig paths and Yarn PnP), written in Rust as part
of the Oxc project.  This package ships the JavaScript API together with the
native napi addon (@oxc-resolver/binding) built from source against the vendored
Rust crate dependencies.


%prep
# -a2 unpacks the build-time JS modules (node_modules_dev/) and -a4 the vendored
# crates (vendor/); both land at the workspace root.
%setup -q -n %{npm_name}-%{version} -a2 -a4

# Unpack the published npm package (JS glue) into npmpkg/.
mkdir -p npmpkg
tar xzf %{SOURCE1} -C npmpkg --strip-components=1

cp %{SOURCE3} .

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

# Configure cargo to build offline from the vendored crates (Source4).  Cargo.toml
# and Cargo.lock are at the workspace root.  The repo's own .cargo/config.toml
# only carries [target.*] linker tweaks (no [env] table), so it does not collide
# with the [env] table %%cargo_prep appends.
%cargo_prep -v vendor


%build
# Build entirely offline.  Do NOT run "npm install"; it would reach the network
# and discard the bundled modules.
export CARGO_NET_OFFLINE=true
export npm_config_offline=true
export npm_config_audit=false
export npm_config_fund=false
export PATH="${PWD}/node_modules/.bin:${PATH}"

# Compile the native napi addon from the napi/ crate.  This mirrors upstream's
# release build script ("napi build --platform --manifest-path napi/Cargo.toml
# --features allocator --release") but via the CLI directly so we do not need the
# vite-plus JS runtime.  Run from the repo root so napi reads the "napi" config
# from package.json (binaryName "resolver", packageName "@oxc-resolver/binding");
# cargo finds the workspace and the vendored-source config (written by
# %%cargo_prep at the tree root) via its upward search.  With --platform and no
# --target, napi builds for the host arch, emitting resolver.<napi-triple>.node.
# The generated JS loader that napi also writes is discarded -- we ship the
# published glue (Source1) instead.
mkdir -p .napi-out
napi build --platform --release --features allocator \
    --manifest-path napi/Cargo.toml \
    --output-dir .napi-out

# Record the licenses of the (vendored) Rust crate dependencies.
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies


%install
# Ship the published JavaScript glue as the oxc-resolver module.
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr npmpkg/index.js npmpkg/index.d.ts npmpkg/browser.js \
    npmpkg/webcontainer-fallback.js npmpkg/package.json \
    %{buildroot}%{nodejs_sitelib}/%{npm_name}/

# Install the native addon next to the JS loader.  index.js loads it as
# ./resolver.<napi-triple>.node (its local-file fallback, before any per-platform
# npm package), so shipping it at the package root is sufficient on any arch.
node_file=$(ls .napi-out/resolver.*.node)
cp -p "${node_file}" %{buildroot}%{nodejs_sitelib}/%{npm_name}/


%check
# Load the *installed* package.  require() throws if the native binding fails to
# load, and ResolverFactory is re-exported straight from it, so this exercises
# the from-source addon.
%{__nodejs} -e 'const r = require("%{buildroot}%{nodejs_sitelib}/%{npm_name}"); if (typeof r.ResolverFactory !== "function") { throw new Error("oxc-resolver native binding did not load"); }'


%files
%doc npmpkg/README.md
%license LICENSE %{npm_name}-%{version}-bundled-licenses.txt LICENSE.dependencies
%{nodejs_sitelib}/%{npm_name}


%changelog
%autochangelog
