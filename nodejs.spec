# The following macros control the usage of dependencies bundled from upstream.
#
# When to use what:
# - Regular (presumably non-modular) build: use neither (the default in Fedora)
# - Early bootstrapping build that is not intended to be shipped:
#     use --with=bootstrap; this will bundle deps and add `~bootstrap` release suffix
# - Build with some dependencies not avalaible in necessary versions (i.e. module build):
#     use --with=bundled; will bundle deps, but do not add the suffix
#
# create bootstrapping build with bundled deps and extra release suffix
%bcond_with bootstrap
# bundle dependencies that are not available in Fedora modules
%if %{with bootstrap}
%bcond_without bundled
%else
%bcond_with bundled
%endif

%if 0%{?rhel} && 0%{?rhel} < 9
%bcond_without python3_fixup
%else
%bcond_with python3_fixup
%endif

%if 0%{?rhel} && 0%{?rhel} < 8
%bcond_without bundled_zlib
%else
%bcond_with bundled_zlib
%endif

%bcond npm 1

# LTO is currently broken on Node.js builds
%define _lto_cflags %{nil}

# Heavy-handed approach to avoiding issues with python
# bytecompiling files in the node_modules/ directory
%global __python %{__python3}

# == Master Relase ==
# This is used by both the nodejs package and the npm subpackage that
# has a separate version - the name is special so that rpmdev-bumpspec
# will bump this rather than adding .1 to the end.
%global baserelease %autorelease

%{?!_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

# == Node.js Version ==
# Note: Fedora should only ship LTS versions of Node.js (currently expected
# to be major versions with even numbers). The odd-numbered versions are new
# feature releases that are only supported for nine months, which is shorter
# than a Fedora release lifecycle.
%global nodejs_epoch 1
%global nodejs_major 18
%global nodejs_minor 11
%global nodejs_patch 0
%global nodejs_abi %{nodejs_major}.%{nodejs_minor}
# nodejs_soversion - from NODE_MODULE_VERSION in src/node_version.h
%global nodejs_soversion 108
%global nodejs_version %{nodejs_major}.%{nodejs_minor}.%{nodejs_patch}
%global nodejs_release %{baserelease}

%global nodejs_datadir %{_datarootdir}/nodejs

# == Bundled Dependency Versions ==
# v8 - from deps/v8/include/v8-version.h
# Epoch is set to ensure clean upgrades from the old v8 package
%global v8_epoch 2
%global v8_major 10
%global v8_minor 2
%global v8_build 154
%global v8_patch 15
%global v8_version %{v8_major}.%{v8_minor}.%{v8_build}.%{v8_patch}
%global v8_release %{nodejs_epoch}.%{nodejs_major}.%{nodejs_minor}.%{nodejs_patch}.%{nodejs_release}

# zlib - from deps/zlib/zlib.h
%global zlib_version 1.2.11

# c-ares - from deps/cares/include/ares_version.h
# https://github.com/nodejs/node/pull/9332
%global c_ares_version 1.18.1

# llhttp - from deps/llhttp/include/llhttp.h
%global llhttp_version 6.0.10

# libuv - from deps/uv/include/uv/version.h
%global libuv_version 1.43.0

# nghttp2 - from deps/nghttp2/lib/includes/nghttp2/nghttp2ver.h
%global nghttp2_version 1.47.0

# ICU - from tools/icu/current_ver.dep
%global icu_major 71
%global icu_minor 1
%global icu_version %{icu_major}.%{icu_minor}

%global icudatadir %{nodejs_datadir}/icudata
%{!?little_endian: %global little_endian %(%{__python3} -c "import sys;print (0 if sys.byteorder=='big' else 1)")}
# " this line just fixes syntax highlighting for vim that is confused by the above and continues literal


# OpenSSL minimum version
%global openssl11_minimum 1:1.1.1
%global openssl30_minimum 1:3.0.2

# punycode - from lib/punycode.js
# Note: this was merged into the mainline since 0.6.x
# Note: this will be unmerged in an upcoming major release
%global punycode_version 2.1.0

# npm - from deps/npm/package.json
%global npm_epoch 1
%global npm_version 8.19.2

# In order to avoid needing to keep incrementing the release version for the
# main package forever, we will just construct one for npm that is guaranteed
# to increment safely. Changing this can only be done during an update when the
# base npm version number is increasing.
%global npm_release %{nodejs_epoch}.%{nodejs_major}.%{nodejs_minor}.%{nodejs_patch}.%{nodejs_release}

# uvwasi - from deps/uvwasi/include/uvwasi.h
%global uvwasi_version 0.0.13

# histogram_c - assumed from timestamps
%global histogram_version 0.9.7

Name: nodejs
Epoch: %{nodejs_epoch}
Version: %{nodejs_version}
Release: %{nodejs_release}
Summary: JavaScript runtime
License: MIT and ASL 2.0 and ISC and BSD
Group: Development/Languages
URL: http://nodejs.org/

ExclusiveArch: %{nodejs_arches}

# nodejs bundles openssl, but we use the system version in Fedora
# because openssl contains prohibited code, we remove openssl completely from
# the tarball, using the script in Source100
Source0: node-v%{nodejs_version}-stripped.tar.gz
Source1: npmrc
Source2: btest402.js
# The binary data that icu-small can use to get icu-full capability
Source3: https://github.com/unicode-org/icu/releases/download/release-%{icu_major}-%{icu_minor}/icu4c-%{icu_major}_%{icu_minor}-data-bin-b.zip
Source4: https://github.com/unicode-org/icu/releases/download/release-%{icu_major}-%{icu_minor}/icu4c-%{icu_major}_%{icu_minor}-data-bin-l.zip
Source100: nodejs-sources.sh

# Disable running gyp on bundled deps we don't use
Patch1: 0001-Disable-running-gyp-on-shared-deps.patch

BuildRequires: make
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python%{python3_pkgversion}-jinja2
%if !%{with python3_fixup}
BuildRequires: python-unversioned-command
%endif
%if %{with bundled_zlib}
Provides: bundled(zlib) = %{zlib_version}
%else
BuildRequires: zlib-devel
%endif
BuildRequires: brotli-devel
%if 0%{?rhel} && 0%{?rhel} < 8
BuildRequires: devtoolset-11-gcc
BuildRequires: devtoolset-11-gcc-c++
%else
BuildRequires: gcc >= 8.3.0
BuildRequires: gcc-c++ >= 8.3.0
%endif

BuildRequires: jq

%if %{with npm}
# needed to generate bundled provides for npm dependencies
# https://src.fedoraproject.org/rpms/nodejs/pull-request/2
# https://pagure.io/nodejs-packaging/pull-request/10
BuildRequires: nodejs-packaging
%endif

BuildRequires: chrpath
BuildRequires: libatomic
BuildRequires: ninja-build
BuildRequires: systemtap-sdt-devel
BuildRequires: unzip

%if %{with bundled}
Provides:      bundled(libuv) = %{libuv_version}
%else
BuildRequires: libuv-devel >= 1:%{libuv_version}
Requires:      libuv >= 1:%{libuv_version}
%endif

# Node.js frequently bumps this faster than Fedora can follow,
# so we will bundle it.
Provides: bundled(nghttp2) = %{nghttp2_version}

# Temporarily bundle llhttp because the upstream doesn't
# provide releases for it.
Provides: bundled(llhttp) = %{llhttp_version}


%if 0%{?rhel} && 0%{?rhel} < 8
BuildRequires: openssl11-devel >= %{openssl11_minimum}
Requires: openssl11 >= %{openssl11_minimum}
%global ssl_configure --shared-openssl --shared-openssl-includes=%{_includedir}/openssl11 --shared-openssl-libpath=%{_libdir}/openssl11
%else

%if 0%{?fedora} >= 36
BuildRequires: openssl >= %{openssl30_minimum}
BuildRequires: openssl-devel >= %{openssl30_minimum}
%global openssl_fips_configure --openssl-is-fips
%else
Requires: openssl >= %{openssl11_minimum}
BuildRequires: openssl-devel >= %{openssl11_minimum}
%global openssl_fips_configure %{nil}
%endif

%global ssl_configure --shared-openssl %{openssl_fips_configure}
%endif

# we need the system certificate store
Requires: ca-certificates

Requires: nodejs-libs%{?_isa} = %{nodejs_epoch}:%{version}-%{release}

# Pull in the full-icu data by default
%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends: nodejs-full-i18n%{?_isa} = %{nodejs_epoch}:%{version}-%{release}
%endif

# we need ABI virtual provides where SONAMEs aren't enough/not present so deps
# break when binary compatibility is broken
Provides: nodejs(abi) = %{nodejs_abi}
Provides: nodejs(abi%{nodejs_major}) = %{nodejs_abi}

# this corresponds to the "engine" requirement in package.json
Provides: nodejs(engine) = %{nodejs_version}

# Node.js currently has a conflict with the 'node' package in Fedora
# The ham-radio group has agreed to rename their binary for us, but
# in the meantime, we're setting an explicit Conflicts: here
Conflicts: node <= 0.3.2-12

# The punycode module was absorbed into the standard library in v0.6.
# It still exists as a seperate package for the benefit of users of older
# versions.  Since we've never shipped anything older than v0.10 in Fedora,
# we don't need the seperate nodejs-punycode package, so we Provide it here so
# dependent packages don't need to override the dependency generator.
# See also: RHBZ#11511811
# UPDATE: punycode will be deprecated and so we should unbundle it in Node v8
# and use upstream module instead
# https://github.com/nodejs/node/commit/29e49fc286080215031a81effbd59eac092fff2f
Provides: nodejs-punycode = %{punycode_version}
Provides: npm(punycode) = %{punycode_version}

# Node.js has forked c-ares from upstream in an incompatible way, so we need
# to carry the bundled version internally.
# See https://github.com/nodejs/node/commit/766d063e0578c0f7758c3a965c971763f43fec85
Provides: bundled(c-ares) = %{c_ares_version}

# Node.js is closely tied to the version of v8 that is used with it. It makes
# sense to use the bundled version because upstream consistently breaks ABI
# even in point releases. Node.js upstream has now removed the ability to build
# against a shared system version entirely.
# See https://github.com/nodejs/node/commit/d726a177ed59c37cf5306983ed00ecd858cfbbef
Provides: bundled(v8) = %{v8_version}

# Node.js is bound to a specific version of ICU which may not match the OS
# We cannot pin the OS to this version of ICU because every update includes
# an ABI-break, so we'll use the bundled copy.
Provides: bundled(icu) = %{icu_version}

# Upstream added new dependencies, but so far they are not available in Fedora
# or there's no option to built it as a shared dependency, so we bundle them
Provides: bundled(uvwasi) = %{uvwasi_version}
Provides: bundled(histogram) = %{histogram_version}

%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends: npm >= %{npm_epoch}:%{npm_version}-%{npm_release}
%endif
Conflicts: npm < %{npm_epoch}:%{npm_version}-%{npm_release}


%description
Node.js is a platform built on Chrome's JavaScript runtime
for easily building fast, scalable network applications.
Node.js uses an event-driven, non-blocking I/O model that
makes it lightweight and efficient, perfect for data-intensive
real-time applications that run across distributed devices.


%package devel
Summary: JavaScript runtime - development headers
Group: Development/Languages
Requires: %{name}%{?_isa} = %{epoch}:%{nodejs_version}-%{nodejs_release}
Requires: %{name}-libs%{?_isa} = %{epoch}:%{nodejs_version}-%{nodejs_release}
Requires: openssl-devel%{?_isa}
%if !%{with bundled_zlib}
Requires: zlib-devel%{?_isa}
%endif
Requires: brotli-devel%{?_isa}
Requires: nodejs-packaging

%if %{without bundled}
Requires: libuv-devel%{?_isa}
%endif

%description devel
Development headers for the Node.js JavaScript runtime.


%package libs
Summary: Node.js and v8 libraries

# Compatibility for obsolete v8 package
%if 0%{?__isa_bits} == 64
Provides: libv8.so.%{v8_major}()(64bit) = %{v8_epoch}:%{v8_version}
Provides: libv8_libbase.so.%{v8_major}()(64bit) = %{v8_epoch}:%{v8_version}
Provides: libv8_libplatform.so.%{v8_major}()(64bit) = %{v8_epoch}:%{v8_version}
%else
# 32-bits
Provides: libv8.so.%{v8_major} = %{v8_epoch}:%{v8_version}
Provides: libv8_libbase.so.%{v8_major} = %{v8_epoch}:%{v8_version}
Provides: libv8_libplatform.so.%{v8_major} = %{v8_epoch}:%{v8_version}
%endif

Provides: v8 = %{v8_epoch}:%{v8_version}-%{nodejs_release}
Provides: v8%{?_isa} = %{v8_epoch}:%{v8_version}-%{nodejs_release}
Obsoletes: v8 < 1:6.7.17-10

%description libs
Libraries to support Node.js and provide stable v8 interfaces.


%package full-i18n
Summary: Non-English locale data for Node.js
Requires: %{name}%{?_isa} = %{nodejs_epoch}:%{nodejs_version}-%{nodejs_release}

%description full-i18n
Optional data files to provide full-icu support for Node.js. Remove this
package to save space if non-English locales are not needed.


%package -n v8-devel
Summary: v8 - development headers
Epoch: %{v8_epoch}
Version: %{v8_version}
Release: %{v8_release}
Requires: %{name}-devel%{?_isa} = %{nodejs_epoch}:%{nodejs_version}-%{nodejs_release}
Requires: %{name}-libs%{?_isa} = %{nodejs_epoch}:%{nodejs_version}-%{nodejs_release}
Conflicts: v8-314-devel

%description -n v8-devel
Development headers for the v8 runtime.

%if %{with npm}
%package -n npm
Summary: Node.js Package Manager
Epoch: %{npm_epoch}
Version: %{npm_version}
Release: %{npm_release}

# We used to ship npm separately, but it is so tightly integrated with Node.js
# (and expected to be present on all Node.js systems) that we ship it bundled
# now.
Obsoletes: npm < 0:3.5.4-6
Requires: nodejs = %{nodejs_epoch}:%{nodejs_version}-%{nodejs_release}
%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends: nodejs-docs = %{nodejs_epoch}:%{nodejs_version}-%{nodejs_release}
%endif

# Do not add epoch to the virtual NPM provides or it will break
# the automatic dependency-generation script.
Provides: npm(npm) = %{npm_version}

%description -n npm
npm is a package manager for node.js. You can use it to install and publish
your node programs. It manages dependencies and does other cool stuff.
%endif


%package docs
Summary: Node.js API documentation
Group: Documentation
BuildArch: noarch

# We don't require that the main package be installed to
# use the docs, but if it is installed, make sure the
# version always matches
Conflicts: %{name} > %{nodejs_epoch}:%{nodejs_version}-%{nodejs_release}
Conflicts: %{name} < %{nodejs_epoch}:%{nodejs_version}-%{nodejs_release}

%description docs
The API documentation for the Node.js JavaScript runtime.


%prep
%autosetup -p1 -n node-v%{nodejs_version}

# remove bundled dependencies that we aren't building
%if !%{with bundled_zlib}
rm -rf deps/zlib
%endif

rm -rf deps/brotli
rm -rf deps/v8/third_party/jinja2
rm -rf tools/inspector_protocol/jinja2

# Replace any instances of unversioned python' with python3
%if %{with python3_fixup}
pathfix.py -i %{__python3} -pn $(find -type f ! -name "*.js")
find . -type f -exec sed -i "s~/usr\/bin\/env python~/usr/bin/python3~" {} \;
find . -type f -exec sed -i "s~/usr\/bin\/python\W~/usr/bin/python3~" {} \;
sed -i "s~usr\/bin\/python2~usr\/bin\/python3~" ./deps/v8/tools/gen-inlining-tests.py
sed -i "s~usr\/bin\/python.*$~usr\/bin\/python3~" ./deps/v8/tools/mb/mb_unittest.py
find . -type f -exec sed -i "s~python -c~python3 -c~" {} \;
%endif


%build

# Activate DevToolset 11 on EPEL 7
%if 0%{?rhel} && 0%{?rhel} < 8
. /opt/rh/devtoolset-11/enable
%endif

# When compiled on armv7hl this package generates an out of range
# reference to the literal pool.  This is most likely a GCC issue.
%ifarch armv7hl
%define _lto_cflags %{nil}
%endif

# Decrease debuginfo verbosity to reduce memory consumption during final
# library linking
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')

export CC='%{__cc}'
export CXX='%{__cxx}'
%if %{with python3_fixup}
export NODE_GYP_FORCE_PYTHON=%{__python3}
%endif

# build with debugging symbols and add defines from libuv (#892601)
# Node's v8 breaks with GCC 6 because of incorrect usage of methods on
# NULL objects. We need to pass -fno-delete-null-pointer-checks
# 2022-07-14: There's a bug in either torque or gcc that causes a
# segmentation fault on ppc64le and s390x if compiled with -O2. Things
# run fine on -O1 and -O3, so we'll just go with -O3 (like upstream)
# while this gets sorted out.
extra_cflags=(
    -D_LARGEFILE_SOURCE
    -D_FILE_OFFSET_BITS=64
    -DZLIB_CONST
    -fno-delete-null-pointer-checks
    -O3
)
export CFLAGS="%{optflags} ${extra_cflags[*]}" CXXFLAGS="%{optflags} ${extra_cflags[*]}"
export LDFLAGS="%{build_ldflags}"

%{__python3} configure.py \
           --ninja \
           --enable-lto \
           --prefix=%{_prefix} \
           --shared \
           --libdir=%{_lib} \
           %{ssl_configure} \
           %{!?with_bundled_zlib:--shared-zlib} \
           --shared-brotli \
           %{!?with_bundled:--shared-libuv} \
           %{?with_bundled:--without-dtrace}%{!?with_bundled:--with-dtrace} \
           --with-intl=small-icu \
           --with-icu-default-data-dir=%{icudatadir} \
           --without-corepack \
           %{!?with_npm:--without-npm} \
           --openssl-use-def-ca-store

%ninja_build -C out/Release


%install
rm -rf %{buildroot}

# The ninja build does not put the shared library in the expected location, so
# we will move it.
mv out/Release/lib/libnode.so.%{nodejs_soversion} out/Release/
./tools/install.py install %{buildroot} %{_prefix}

# Set the binary permissions properly
chmod 0755 %{buildroot}/%{_bindir}/node
chrpath --delete %{buildroot}%{_bindir}/node

# Install library symlink
ln -s libnode.so.%{nodejs_soversion} %{buildroot}%{_libdir}/libnode.so

# Install v8 compatibility symlinks
for header in %{buildroot}%{_includedir}/node/libplatform %{buildroot}%{_includedir}/node/v8*.h; do
    header=$(basename ${header})
    ln -s ./node/${header} %{buildroot}%{_includedir}/${header}
done
ln -s ./node/cppgc %{buildroot}%{_includedir}/cppgc
for soname in libv8 libv8_libbase libv8_libplatform; do
    ln -s libnode.so.%{nodejs_soversion} %{buildroot}%{_libdir}/${soname}.so
    ln -s libnode.so.%{nodejs_soversion} %{buildroot}%{_libdir}/${soname}.so.%{v8_major}
done

# own the sitelib directory
mkdir -p %{buildroot}%{_prefix}/lib/node_modules

# install documentation
mkdir -p %{buildroot}%{_pkgdocdir}/html
cp -pr doc/* %{buildroot}%{_pkgdocdir}/html
rm -f %{buildroot}%{_pkgdocdir}/html/nodejs.1

# node-gyp needs common.gypi too
mkdir -p %{buildroot}%{_datadir}/node
cp -p common.gypi %{buildroot}%{_datadir}/node

# The config.gypi file is platform-dependent, so rename it to not conflict
mv %{buildroot}%{_includedir}/node/config.gypi \
   %{buildroot}%{_includedir}/node/config-%{_arch}.gypi

# Install the GDB init tool into the documentation directory
mv %{buildroot}/%{_datadir}/doc/node/gdbinit %{buildroot}/%{_pkgdocdir}/gdbinit


%if %{with npm}
# install NPM docs to mandir
mkdir -p %{buildroot}%{_mandir} \
         %{buildroot}%{_pkgdocdir}/npm

cp -pr deps/npm/man/* %{buildroot}%{_mandir}/
rm -rf %{buildroot}%{_prefix}/lib/node_modules/npm/man
ln -srf %{buildroot}%{_mandir} %{buildroot}%{_prefix}/lib/node_modules/npm/man


# Install Gatsby HTML documentation to %%{_pkgdocdir}
cp -pr deps/npm/docs %{buildroot}%{_pkgdocdir}/npm/
rm -rf %{buildroot}%{_prefix}/lib/node_modules/npm/docs

ln -srf %{buildroot}%{_pkgdocdir}/npm %{buildroot}%{_prefix}/lib/node_modules/npm/docs
%endif

# Node tries to install some python files into a documentation directory
# (and not the proper one). Remove them for now until we figure out what to
# do with them.
rm -f %{buildroot}/%{_defaultdocdir}/node/lldb_commands.py \
      %{buildroot}/%{_defaultdocdir}/node/lldbinit


%if %{with npm}
# Some NPM bundled deps are executable but should not be. This causes
# unnecessary automatic dependencies to be added. Make them not executable.
# Skip the npm bin directory or the npm binary will not work.
find %{buildroot}%{_prefix}/lib/node_modules/npm \
    -not -path "%{buildroot}%{_prefix}/lib/node_modules/npm/bin/*" \
    -executable -type f \
    -exec chmod -x {} \;

# The above command is a little overzealous. Add a few permissions back.
chmod 0755 %{buildroot}%{_prefix}/lib/node_modules/npm/node_modules/@npmcli/run-script/lib/node-gyp-bin/node-gyp
chmod 0755 %{buildroot}%{_prefix}/lib/node_modules/npm/node_modules/node-gyp/bin/node-gyp.js

# Drop the NPM default configuration in place
mkdir -p %{buildroot}%{_sysconfdir}
cp %{SOURCE1} %{buildroot}%{_sysconfdir}/npmrc

# NPM upstream expects it to be in /usr/etc/npmrc, so we'll put a symlink here
# This is done in the interests of keeping /usr read-only.
mkdir -p %{buildroot}%{_prefix}/etc
ln -rsf %{buildroot}%{_sysconfdir}/npmrc %{buildroot}%{_prefix}/etc/npmrc
%endif

# Install the full-icu data files
mkdir -p %{buildroot}%{icudatadir}
%if 0%{?little_endian}
unzip -d %{buildroot}%{icudatadir} %{SOURCE4} icudt%{icu_major}l.dat
%else
unzip -d %{buildroot}%{icudatadir} %{SOURCE3} icudt%{icu_major}b.dat
%endif


%check
# Fail the build if the versions don't match
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{buildroot}/%{_bindir}/node -e "require('assert').equal(process.versions.node, '%{nodejs_version}')"
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{buildroot}/%{_bindir}/node -e "require('assert').equal(process.versions.v8.replace(/-node\.\d+$/, ''), '%{v8_version}')"
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{buildroot}/%{_bindir}/node -e "require('assert').equal(process.versions.ares.replace(/-DEV$/, ''), '%{c_ares_version}')"

# Ensure we have punycode and that the version matches
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{buildroot}/%{_bindir}/node -e "require(\"assert\").equal(require(\"punycode\").version, '%{punycode_version}')"

%if %{with npm}
# Ensure we have npm and that the version matches
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{buildroot}%{_bindir}/node %{buildroot}%{_bindir}/npm version --json |jq -e '.npm == "%{npm_version}"'
%endif

# Make sure i18n support is working
NODE_PATH=%{buildroot}%{_prefix}/lib/node_modules:%{buildroot}%{_prefix}/lib/node_modules/npm/node_modules LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{buildroot}/%{_bindir}/node --icu-data-dir=%{buildroot}%{icudatadir} %{SOURCE2}


%if 0%{?rhel} && 0%{?rhel} < 8
%pretrans -n npm -p <lua>
-- Remove all of the symlinks from the bundled npm node_modules directory
base_path = "%{_prefix}/lib/node_modules/npm/node_modules/"
d_st = posix.stat(base_path)
if d_st then
  for f in posix.files(base_path) do
    path = base_path..f
    st = posix.stat(path)
    if st and st.type == "link" then
      os.remove(path)
    end
  end
end
%endif

%files
%{_bindir}/node
%dir %{_prefix}/lib/node_modules
%dir %{_datadir}/node
%dir %{_datadir}/systemtap
%dir %{_datadir}/systemtap/tapset
%{_datadir}/systemtap/tapset/node.stp

%if %{without bundled}
%dir %{_usr}/lib/dtrace
%{_usr}/lib/dtrace/node.d
%endif

%doc AUTHORS CHANGELOG.md onboarding.md GOVERNANCE.md README.md
%doc %{_mandir}/man1/node.1*


%files devel
%{_includedir}/node
%{_libdir}/libnode.so
%{_datadir}/node/common.gypi
%{_pkgdocdir}/gdbinit


%files full-i18n
%dir %{icudatadir}
%{icudatadir}/icudt%{icu_major}*.dat


%files libs
%license LICENSE
%{_libdir}/libnode.so.%{nodejs_soversion}
%{_libdir}/libv8.so.%{v8_major}
%{_libdir}/libv8_libbase.so.%{v8_major}
%{_libdir}/libv8_libplatform.so.%{v8_major}
%dir %{nodejs_datadir}/


%files -n v8-devel
%{_includedir}/libplatform
%{_includedir}/v8*.h
%{_includedir}/cppgc
%{_libdir}/libv8.so
%{_libdir}/libv8_libbase.so
%{_libdir}/libv8_libplatform.so


%if %{with npm}
%files -n npm
%{_bindir}/npm
%{_bindir}/npx
%{_prefix}/lib/node_modules/npm
%config(noreplace) %{_sysconfdir}/npmrc
%{_prefix}/etc/npmrc
%ghost %{_sysconfdir}/npmignore
%doc %{_mandir}/man*/
%exclude %doc %{_mandir}/man1/node.1*
%endif

%files docs
%doc doc
%dir %{_pkgdocdir}
%{_pkgdocdir}/html

%if %{with npm}
%{_pkgdocdir}/npm/docs
%endif


%changelog
%autochangelog
