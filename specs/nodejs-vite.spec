%global npm_name vite

Name:           nodejs-%{npm_name}
Version:        8.3.5
Release:        %autorelease
Summary:        Next Generation NodeJS Frontend Tooling

# vite itself is MIT; its bundled runtime dependencies add ISC (see
# %%{npm_name}-%%{version}-bundled-licenses.txt).
License:        MIT AND ISC AND Apache-2.0 AND BSD-3-Clause AND MPL-2.0
URL:            https://vite.dev/
Source0:        https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Source1:        %{npm_name}-%{version}-nm-prod.tgz
Source2:        %{npm_name}-%{version}-nm-dev.tgz
Source3:        %{npm_name}-%{version}-bundled-licenses.txt

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

# vite 8 replaced the rollup bundler with rolldown (a native napi module that
# carries the per-platform @rolldown/binding-* addons), moved esbuild to a peer
# dependency, and uses lightningcss (native) for CSS. All three are provided by
# system packages built from source rather than the bundled prebuilt binaries.
Requires:       nodejs
Requires:       npm(rolldown)
Requires:       npm(lightningcss)
Requires:       npm(esbuild)
BuildRequires:  nodejs, /usr/bin/node, /usr/bin/npm
BuildRequires:  nodejs-devel
BuildRequires:  npm(rolldown)
BuildRequires:  npm(lightningcss)
BuildRequires:  npm(esbuild)

%description
%{summary}.


%prep
%setup -q -n package
cp %{SOURCE3} .
# Setup bundled runtime (prod) node modules
tar xfz %{SOURCE1}
# Replace bundled native modules with the system packages (built from source).
# rolldown carries the per-platform @rolldown/binding-* prebuilt addons; drop
# them and point at the system rolldown, whose binding is built from source.
rm -rf node_modules_prod/rolldown node_modules_prod/@rolldown/binding-*
ln -sf %{nodejs_sitelib}/rolldown node_modules_prod/
# lightningcss is a native napi module; use the system package.
rm -rf node_modules_prod/lightningcss node_modules_prod/lightningcss-*
ln -sf %{nodejs_sitelib}/lightningcss node_modules_prod/
# esbuild is a peerDependency (not bundled): satisfy it from the system package.
ln -sf %{nodejs_sitelib}/esbuild node_modules_prod/
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_prod/* .
ln -s ../node_modules_prod/.bin . 2>/dev/null || :
popd


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr package.json bin dist misc client.d.ts types \
    %{buildroot}%{nodejs_sitelib}/%{npm_name}
# Copy over bundled nodejs modules
cp -pr node_modules node_modules_prod \
    %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{nodejs_sitelib}/vite/bin
install -p -D -m0755 bin/vite.js %{buildroot}%{nodejs_sitelib}/vite/bin/vite.js
install -p -D -m0755 bin/openChrome.js %{buildroot}%{nodejs_sitelib}/vite/bin/openChrome.js
mkdir -p %{buildroot}%{_bindir}
ln -s %{nodejs_sitelib}/vite/bin/vite.js %{buildroot}%{_bindir}/vite


%check
# vite 8 is ESM-only ("type": "module", exports["."] -> ./dist/node/index.js,
# with no CommonJS entry), so require("./") cannot resolve it.  Import the real
# entry point instead: evaluating its module graph also exercises the system
# rolldown/lightningcss/esbuild that the node_modules_prod symlinks point at, so
# this fails if any of those deps do not resolve.  createServer is a stable
# top-level export.
%{__nodejs} --input-type=module -e 'import { createServer } from "./dist/node/index.js"; if (typeof createServer !== "function") { throw new Error("vite entry did not load"); }'


%files
%doc README.md
%license LICENSE.md %{npm_name}-%{version}-bundled-licenses.txt
%{nodejs_sitelib}/vite
%{_bindir}/vite


%changelog
%autochangelog
