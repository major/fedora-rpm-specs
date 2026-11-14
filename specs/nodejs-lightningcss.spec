%global npm_name lightningcss
%undefine _package_note_flags

Name:           nodejs-%{npm_name}
Version:        1.33.0
Release:        %autorelease
Summary:        An extremely fast CSS parser, transformer, bundler, and minifier

# The npm package (node/ JS wrapper) and the native crate are MPL-2.0.
# The bundled Rust crate dependencies carry additional licenses; they are
# enumerated in %%{npm_name}-%%{version}-bundled-licenses.txt (npm) and
# LICENSE.dependencies (crates, generated at build time).
License:        MPL-2.0 AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND ISC AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (MIT OR Apache-2.0) AND MIT AND MPL-2.0 AND (Unlicense OR MIT)
URL:            https://lightningcss.dev/
Source0:        https://github.com/parcel-bundler/%{npm_name}/archive/refs/tags/v%{version}.tar.gz
Source1:        %{npm_name}-%{version}-nm-prod.tgz
Source2:        %{npm_name}-%{version}-nm-dev.tgz
Source3:        %{npm_name}-%{version}-bundled-licenses.txt
# To create the vendor tarball (see lightningcss-sources.sh):
#   tar xf v%%{version}.tar.gz ; pushd %%{npm_name}-%%{version} ; \
#   cargo vendor && tar Jcvf ../%%{npm_name}-%%{version}-vendor.tar.xz vendor/ ; popd
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

%description
Lightning CSS is a CSS parser, transformer, bundler, and minifier written in
Rust. This package provides the Node.js bindings, with the native addon built
from source against the vendored Rust crate dependencies.


%prep
%setup -q -n %{npm_name}-%{version} -a1 -a2 -a4
cp %{SOURCE3} .
# Assemble a node_modules farm from the bundled prod/dev modules so the napi
# CLI (@napi-rs/cli, a dev dependency) is on PATH at build time.
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_prod/* .
ln -sf ../node_modules_dev/* .
mkdir -p .bin
pushd .bin
ln -s ../../node_modules_dev/.bin/* .
popd
popd

# Configure cargo to build offline from the vendored crates (Source4).
%cargo_prep -v vendor


%build
# Build entirely offline: the native binding from the vendored Rust crates and
# the JS wrapper that ships as-is. Do NOT run "npm install" here; it would reach
# the network and discard the bundled modules.
export CARGO_NET_OFFLINE=true
export npm_config_offline=true
export npm_config_audit=false
export npm_config_fund=false
export PATH="${PWD}/node_modules/.bin:${PATH}"

# Compile the native (napi) addon. This mirrors upstream's scripts/build.js
# ("napi build --platform --cargo-cwd node --release") but is invoked directly
# to skip the macOS-only setup path. It emits ./lightningcss.<triple>.node at
# the package root, which node/index.js loads as ../lightningcss.<triple>.node.
napi build --platform --cargo-cwd node --release

# Record the licenses of the (vendored) Rust crate dependencies.
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

# Runtime dependency from package.json "dependencies".
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}/node_modules/detect-libc
cp -pr node_modules/detect-libc/. \
    %{buildroot}%{nodejs_sitelib}/%{npm_name}/node_modules/detect-libc

# Contents of package.json "files": ["node/*.js","node/*.mjs","node/*.d.ts",
# "node/*.flow"]. The .flow stubs are only produced by the (skipped) build-flow
# step; TypeScript consumers use the .d.ts files, so shipping the .js/.mjs/.d.ts
# is sufficient.
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}/node
cp -pr node/*.js node/*.mjs node/*.d.ts \
    %{buildroot}%{nodejs_sitelib}/%{npm_name}/node/

# The native addon built in %%build (loaded by node/index.js).
cp -pr lightningcss.*.node %{buildroot}%{nodejs_sitelib}/%{npm_name}/

cp -pr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}/


%check
# Load and exercise the *installed* package to catch packaging mistakes
# (missing native addon, missing detect-libc, wrong file layout). Keep this on a
# single line: backslash line-continuations inside node -e '...' are passed
# literally into the script and break parsing.
%{__nodejs} -e 'const css = require("%{buildroot}%{nodejs_sitelib}/%{npm_name}"); const r = css.transform({ filename: "test.css", minify: true, code: Buffer.from("a { color: #ffffff }") }); if (!r.code || !r.code.length) throw new Error("lightningcss transform failed");'


%files
%doc README.md
%license LICENSE %{npm_name}-%{version}-bundled-licenses.txt LICENSE.dependencies
%{nodejs_sitelib}/%{npm_name}


%changelog
%autochangelog
