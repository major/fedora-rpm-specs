%global     npm_name undici

# Note: clang runs wasm-opt automatically if found in $PATH,
# which can cause confusing errors ("bulk memory is disabled").
# Workaround by disabling the wasm-opt on releases when this manifests.
# Can be fixed by --no-wasm-opt flag, once that lands in released clang:
# https://github.com/llvm/llvm-project/pull/95208
# Adjust as needed.
%bcond      wasm_opt %[0%{?fedora} > 39]

%global     llhttp_version_major    9
%global     llhttp_version_minor    2
%global     llhttp_version_patch    0

Name:       nodejs-%{npm_name}
Summary:    An HTTP/1.1 client, written from scratch for Node.js
Version:    7.2.0
Release:    %autorelease

License:    MIT
URL:        https://undici.nodejs.org
# See Source4 on how these archives were generated
Source0:    %{npm_name}-%{version}-stripped.tar.gz
Source1:    %{npm_name}-%{version}-nm-prod.tgz
Source2:    %{npm_name}-%{version}-nm-dev.tgz
Source3:    %{npm_name}-%{version}-bundled-licenses.txt
Source4:    %{npm_name}-sources.sh


# Binary artifacts in this package are aimed at the wasm32-wasi "architecture".
%global     _binaries_in_noarch_packages_terminate_build 0
BuildArch:  noarch
# would be %%{nodejs_arches} noarch, but lld is not yet supported on s390x
ExclusiveArch: %{ix86} x86_64 aarch64 ppc64le riscv64 noarch

BuildRequires: clang lld wasi-libc-devel
BuildRequires: nodejs-devel npm
%if %{with wasm_opt}
BuildRequires: binaryen
%endif
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
%if %{with wasm_opt}
export WASM_OPT=/usr/bin/wasm-opt
%endif

# `npm run build` uses docker; invoke the build script directly
env EXTERNAL_PATH='%{nodejs_sitelib}/%{npm_name}' %{__nodejs} build/wasm.js
npm --offline pack

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
tar -C   %{buildroot}%{nodejs_sitelib}/%{npm_name} -xzf %{npm_name}-%{version}.tgz --strip-components=1
cp -prt  %{buildroot}%{nodejs_sitelib}/%{npm_name} node_modules_prod node_modules

# Built (WASM) files are no longer packaged with npm pack
install -p -Dt %{buildroot}%{nodejs_sitelib}/%{npm_name}/lib/llhttp/ lib/llhttp/*.wasm lib/llhttp/*.js
install -p -Dt %{buildroot}%{nodejs_sitelib}/%{npm_name}/            loader.js

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
