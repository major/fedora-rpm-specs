%global     npm_name undici

%global     llhttp_version_major    8
%global     llhttp_version_minor    1
%global     llhttp_version_patch    0

Name:       nodejs-%{npm_name}
Summary:    An HTTP/1.1 client, written from scratch for Node.js
Version:    5.27.2
Release:    %autorelease

License:    MIT
URL:        https://undici.nodejs.org
# See Source4 on how these archives were generated
Source0:    %{npm_name}-%{version}-stripped.tar.gz
Source1:    %{npm_name}-%{version}-nm-prod.tgz
Source2:    %{npm_name}-%{version}-nm-dev.tgz
Source3:    %{npm_name}-%{version}-bundled-licenses.txt
Source4:    %{npm_name}-sources.sh

# Upstream proposal: https://github.com/nodejs/undici/pull/2403
Patch:      0001-feat-allow-customization-of-build-environment.patch

# Binary artifacts in this package are aimed at the wasm32-wasi "architecture".
%global     _binaries_in_noarch_packages_terminate_build 0
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires: clang lld wasi-libc-devel
BuildRequires: nodejs-devel npm
# for autosetup -S git_am
BuildRequires: git-core

# This package bundles it's own copy of llhttp
Provides:   bundled(llhttp) = %{llhttp_version_major}.%{llhttp_version_minor}.%{llhttp_version_patch}

%description
An HTTP/1.1 client, written from scratch for Node.js.

%prep
%autosetup -n %{npm_name}-%{version} -S git_am
cp -p %{S:3} .

# Check for bundled llhttp version
if ! grep -q 'LLHTTP_VERSION_MAJOR %{llhttp_version_major}' deps/llhttp/include/llhttp.h \
|| ! grep -q 'LLHTTP_VERSION_MINOR %{llhttp_version_minor}' deps/llhttp/include/llhttp.h \
|| ! grep -q 'LLHTTP_VERSION_PATCH %{llhttp_version_patch}' deps/llhttp/include/llhttp.h
then
    echo 'llhttp version mismatch' >&2; exit 2
fi

# Link node_modules
mkdir -p node_modules/.bin/
tar -xzf %{S:1}
ln -srt node_modules/       node_modules_prod/*
ln -srt node_modules/.bin/  node_modules_prod/.bin

%build
export WASM_CC=clang
export WASM_CFLAGS='--target=wasm32-wasi --sysroot=/usr/wasm32-wasi'
export WASM_LDFLAGS='-nodefaultlibs'
export WASM_LDLIBS='-lc'

# `npm run build` uses docker; invoke the build script directly
%{__nodejs} build/wasm.js
npm --offline pack

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
tar -C   %{buildroot}%{nodejs_sitelib}/%{npm_name} -xzf %{npm_name}-%{version}.tgz --strip-components=1
cp -prt  %{buildroot}%{nodejs_sitelib}/%{npm_name} node_modules_prod node_modules

%check
%{__nodejs} -e 'require("./")'

tar -xzf %{S:2}
ln -fsrt node_modules/      node_modules_dev/*
ln -fsrt node_modules/.bin/ node_modules_dev/.bin/*
# Depends on the environment/OpenSSL version, etc. Informational only.
npm --offline run test || :

%files
%doc README.md
%license LICENSE %{npm_name}-%{version}-bundled-licenses.txt
%dir %{nodejs_sitelib}
%{nodejs_sitelib}/%{npm_name}

%changelog
%autochangelog
