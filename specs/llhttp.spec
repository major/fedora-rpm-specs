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
Version:        9.2.1
%global so_version 9.2
Release:        %autorelease
Summary:        Port of http_parser to llparse

# License of llhttp is (SPDX) MIT; nothing from the NodeJS dependency bundle is
# installed, so its contents do not contribute to the license of the binary
# RPMs, and we do not need a file llhttp-%%{version}-bundled-licenses.txt.
License:        MIT
# See Source3, llhttp-%%{version}-bundled-source-licenses.txt.
#
# There is a lot in the dev-dependency bundle, so this audit is likely
# imperfect.
#
# "Apache-2.0"
# "BSD-2-Clause"
# "BSD-3-Clause"
# "CC0-1.0"
#   - node_modules_dev/binary-search/:
#
#     The CC0-1.0 license is *not allowed* in Fedora for code, but
#     binary_search falls under the following blanket exception:
#
#       Existing uses of CC0-1.0 on code files in Fedora packages prior to
#       2022-08-01, and subsequent upstream versions of those files in those
#       packages, continue to be allowed. We encourage Fedora package
#       maintainers to ask upstreams to relicense such files.
#
#     https://gitlab.com/fedora/legal/fedora-license-data/-/issues/91#note_1151947383
#
#     Furthermore, its README says,
#
#       To the extent possible by law, The Dark Sky Company, LLC has [waived
#       all copyright and related or neighboring rights][cc0] to this library.
#
#       [cc0]: http://creativecommons.org/publicdomain/zero/1.0/
#
#     which should arguably be considered a public-domain dedication.
# "ISC"
# "MIT"
# "(MIT OR CC0-1.0)"
#    Since this applies to code, and CC0-1.0 is not-allowed for code in Fedora,
#    we treat this as simply "MIT".
# "Python-2.0"
#    This is for npm argparse. See:
#      argparse has Python 2.0 license issue
#      https://gitlab.com/fedora/legal/fedora-license-data/-/issues/470
#    Based on that, we assume the true license should be PSF-2.0 instead.
SourceLicense:  %{shrink:
                Apache-2.0 AND
                BSD-2-Clause AND
                BSD-3-Clause AND
                CC0-1.0 AND
                ISC AND
                MIT AND
                PSF-2.0
                }
URL:            https://github.com/nodejs/llhttp
Source0:        %{url}/archive/v%{version}/llhttp-%{version}.tar.gz

# Based closely on nodejs-packaging-bundler, except:
#
# - The GitHub source tarball specified in this spec file is used since the
#   current version is not typically published on npm
Source1:        llhttp-packaging-bundler
# Created with llhttp-packaging-bundler (Source1):
Source2:        llhttp-%{version}-nm-dev.tar.zst
# No production dependency bundle is inlcluded, since none is needed—and
# therefore, no bundled licenses text file is included either. However, we do
# track the licenses in the dev-depenencies bundle:
Source3:        llhttp-%{version}-bundled-source-licenses.txt

# While nothing in the dev bundle is installed, we still choose to audit for
# null licenses at build time and to keep manually-approved exceptions in a
# file.
Source4:        check-null-licenses
Source5:        audited-null-licenses.toml

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
%ifnarch %{ix86}
%if !0%{?rhel}
# For additional license auditing:
BuildRequires:  askalono-cli
BuildRequires:  licensecheck
%endif
%endif

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
tar --zstd --extract --file='%{SOURCE2}'
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
%{python3} '%{SOURCE4}' --exceptions '%{SOURCE5}' --with dev node_modules_dev

%ifnarch %{ix86}
%if !0%{?rhel}
# Ensure we have checked all of the licenses in the dev dependency bundle for
# allowability.
pattern="${pattern-}${pattern+|}UNKNOWN|(Apache|Python) License 2\\.0"
pattern="${pattern-}${pattern+|}(MIT|ISC|BSD [023]-Clause) License"
pattern="${pattern-}${pattern+|}BSD 2-Clause with views sentence"
pattern="${pattern-}${pattern+|}MIT License and/or X11 License"
pattern="${pattern-}${pattern+|}GNU General Public License"
# The CC0-1.0 license is *not allowed* in Fedora for code, but the
# binary-search dev dependency falls under the following blanket exception:
#
#   Existing uses of CC0-1.0 on code files in Fedora packages prior to
#   2022-08-01, and subsequent upstream versions of those files in those
#   packages, continue to be allowed. We encourage Fedora package maintainers
#   to ask upstreams to relicense such files.
#
# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/91#note_1151947383
#
# This can be verified by checking out commit
# f460573ec4dc41968e600a96aaaf03a167b236bf (2021-12-16) from dist-git for this
# package, obtaining the source llhttp-6.0.6-nm-dev.tgz, and observing that
# llhttp-6.0.6/node_modules_dev/binary-search/package.json shows the CC0-1.0
# license.
pattern="${pattern-}${pattern+|}binary-search/package.json: (\*No copyright\* )?Creative Commons CC0 1\.0"
# The license BSD-3-Clause-Clear appears in sprintf-js/bower.json. This license
# is on the not-allowed list, but it is not real: sprintf-js/package.json and
# sprintf-js/LICENSE have the correct (and allowed) BSD-3-Clause license, and
# upstream confirmed in “Licensing Question”
# https://github.com/alexei/sprintf.js/issues/211 that the appearance of
# BSD-3-Clause-Clear in this file was a mere typo.
pattern="${pattern-}${pattern+|}sprintf-js/bower.json: (\*No copyright\* )?BSD 3-Clause Clear License"

if licensecheck -r node_modules_dev |
    grep -vE "(${pattern})( \\[generated file\\])?\$" ||
  ! askalono crawl node_modules_dev | awk '
      $1 == "License:" { license = $0; next }
      $1 == "Score:" {
        if ( \
          license ~ /: (MIT|ISC) \(/ || \
          license ~ /: (0BSD|BSD-2-Clause(-Views)?|BSD-3-Clause) \(/ || \
          license ~ /: (Apache-2\.0|Python-2\.0\.1) \(/ \
        ) {
          next # license is OK
        }
        # license needs auditing
        problem = 1
        print file; print license; print $0
        next
      }
      { file = $0 }
      END { exit problem }'

then
  cat 1>&2 <<'EOF'
=================================================================
Possible new license(s) found in dev dependency bundle!

While these do not contribute to License, they must appear in:
https://docs.fedoraproject.org/en-US/legal/allowed-licenses/

Please audit them and modify the patterns representing expected
licenses in the spec file!
=================================================================
EOF
  exit 1
fi
%endif
%endif

# http-loose-request.c:7205:20: error: invalid conversion from 'void*' to
#     'const unsigned char*' [-fpermissive]
#  7205 |     start = state->_span_pos0;
#       |             ~~~~~~~^~~~~~~~~~
#       |                    |
#       |                    void*
export CXXFLAGS="${CXXFLAGS-} -fpermissive"
export CFLAGS="${CFLAGS-} -fpermissive"
export CLANG=gcc
# See scripts.test in package.json:
NODE_ENV=test node -r ts-node/register/type-check ./test/md-test.ts


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
