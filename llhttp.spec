# This package is rather exotic. The compiled library is a typical shared
# library with a C API. However, it has only a tiny bit of C source code. Most
# of the library is written in TypeScript, which is transpiled to C, via LLVM
# IR, using llparse (https://github.com/nodejs/llparse)—all of which happens
# within the NodeJS ecosystem.
#
# The package therefore “builds like” a NodeJS package, and to the extent they
# are relevant we apply the NodeJS packaging guidelines. However, the result of
# the build “installs like” a traditional C library package and has no NodeJS
# dependencies, including bundled ones.
#
# Furthermore, the package is registered with npm as “llhttp”, but current
# releases are not published there, so we use the GitHub archive as the
# canonical source and use a custom bundler script based on
# nodejs-packaging-bundler to fetch NodeJS build dependencies.
#
# Overall, we cherry-pick from the standard and NodeJS packaging guidelines as
# each seems to best apply, understanding that this package does not fit well
# into any of the usual patterns or templates.
#
# Note that there is now a “release” tarball, e.g.
# https://github.com/nodejs/llhttp/archive/refs/tags/release/v%%{version}tar.gz,
# that allows this package to be built without the NodeJS/TypeScript machinery.
# However, the release archive lacks the original TypeScript source code for
# the generated C code, which we would need to include in the source RPM as an
# additional source even if we do not do the re-generation ourselves.

Name:           llhttp
Version:        9.0.1
%global so_version 9.0
Release:        %autorelease
Summary:        Port of http_parser to llparse

# License of llhttp is (SPDX) MIT; nothing from the NodeJS dependency bundle is
# installed, so its contents do not contribute to the license of the binary
# RPMs, and we do not need a file llhttp-%%{version}-bundled-licenses.txt.
License:        MIT
URL:            https://github.com/nodejs/llhttp
Source0:        %{url}/archive/v%{version}/llhttp-%{version}.tar.gz

# Based closely on nodejs-packaging-bundler, except:
#
# - The GitHub source tarball specified in this spec file is used since the
#   current version is not typically published on npm
# - No production dependency bundle is generated, since none is needed—and
#   therefore, no bundled licenses text file is generated either
Source1:        llhttp-packaging-bundler
# Created with llhttp-packaging-bundler (Source1):
Source2:        llhttp-%{version}-nm-dev.tgz

# While nothing in the dev bundle is installed, we still choose to audit for
# null licenses at build time and to keep manually-approved exceptions in a
# file.
Source3:        check-null-licenses
Source4:        audited-null-licenses.toml

# The compiled RPM does not depend on NodeJS at all, but we cannot *build* it
# on architectures without NodeJS.
ExclusiveArch:  %{nodejs_arches}

# For generating the C source “release” from TypeScript:
BuildRequires:  nodejs-devel
BuildRequires:  make

# For compiling the C library
BuildRequires:  cmake
BuildRequires:  gcc

# For tests
BuildRequires:  gcc-c++

# For check-null-licenses
BuildRequires:  python3-devel

%description
This project is a port of http_parser to TypeScript. llparse is used to
generate the output C source file, which could be compiled and linked with the
embedder's program (like Node.js).


%package devel
Summary:        Development files for llhttp

Requires:       llhttp%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
The llhttp-devel package contains libraries and header files for
developing applications that use llhttp.


%prep
%autosetup

# Remove build flags specifying ISA extensions not in the architectural
# baseline from the test fixture setup.
sed -r -i 's@([[:blank:]]*)(.*-m(sse4))@\1// \2@' test/fixtures/index.ts

# We build the library that we install via release/CMakeLists.txt, but the
# tests are built via Makefile targets. Don’t apply non-default optimization or
# debug flags to the test executables.
sed -r -i 's@ -[Og].\b@@g' Makefile

# Set up bundled (dev) node modules required to generate the C sources from the
# TypeScript sources.
tar -xzf '%{SOURCE2}'
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_dev/* .
ln -s ../node_modules_dev/.bin .
popd

# We run ts-node out of node_modules/.bin rather than using npx (which we will
# not have available).
sed -r -i 's@\bnpx[[:blank:]](ts-node)\b@node_modules/.bin/\1@' Makefile


%build
# Generate the C source “release” from TypeScript using the “node_modules_dev”
# bundle.
%make_build release RELEASE='%{version}'

# To help prove that nothing from the bundled NodeJS dev dependencies is
# included in the binary packages, remove the “node_modules” symlinks.
rm -rvf node_modules

cd release
%cmake
%cmake_build


%install
cd release
%cmake_install


%check
# Symlink the NodeJS bundle again so that we can test with Mocha
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_dev/* .
ln -s ../node_modules_dev/.bin .
popd

# Verify that no bundled dev dependency has a null license field, unless we
# already audited it by hand. This reduces the chance of accidentally including
# code with license problems in the source RPM.
%{python3} '%{SOURCE3}' --exceptions '%{SOURCE4}' --with dev node_modules_dev

# http-loose-request.c:7205:20: error: invalid conversion from 'void*' to
#     'const unsigned char*' [-fpermissive]
#  7205 |     start = state->_span_pos0;
#       |             ~~~~~~~^~~~~~~~~~
#       |                    |
#       |                    void*
export CXXFLAGS="${CXXFLAGS-} -fpermissive"
export CFLAGS="${CFLAGS-} -fpermissive"
export CLANG=gcc
# See scripts.mocha in package.json:
NODE_ENV=test ./node_modules/.bin/mocha \
    -r ts-node/register/type-check \
    test/*-test.ts


%files
%license release/LICENSE-MIT
%{_libdir}/libllhttp.so.%{so_version}{,.*}


%files devel
%doc release/README.md
%{_includedir}/llhttp.h
%{_libdir}/libllhttp.so
%{_libdir}/pkgconfig/libllhttp.pc
%{_libdir}/cmake/llhttp/


%changelog
%autochangelog
