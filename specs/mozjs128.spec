%global major 128

# LTO - Enable in Release builds, but consider disabling for development as it increases compile time
%global build_with_lto    1

# https://bugzilla.redhat.com/show_bug.cgi?id=2304756
%global toolchain clang

# Require tests to pass?
%global require_tests     1

%if !%{build_with_lto}
# LTO is the default
%define _lto_cflags %{nil}
%endif

%ifarch %{ix86}
# OOM with LTO on i686
%global _lto_cflags %{nil}
%endif

# Big endian platforms
%ifarch ppc ppc64 s390 s390x
%global big_endian 1
%endif

Name:           mozjs%{major}
Version:        128.11.0
Release:        %autorelease
Summary:        SpiderMonkey JavaScript library

License:        MPL-2.0 AND Apache-2.0 AND BSD-3-Clause AND BSD-2-Clause AND MIT AND GPL-3.0-or-later
URL:            https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey
Source0:        https://ftp.mozilla.org/pub/firefox/releases/%{version}esr/source/firefox-%{version}esr.source.tar.xz

# Known failures with system libicu
Source1:        known_failures.txt

# Patches from mozjs68, rebased for mozjs78:
Patch01:        fix-soname.patch
Patch02:        copy-headers.patch
Patch03:        tests-increase-timeout.patch
Patch09:        icu_sources_data.py-Decouple-from-Mozilla-build-system.patch
Patch10:        icu_sources_data-Write-command-output-to-our-stderr.patch

# Build fixes - https://hg.mozilla.org/mozilla-central/rev/ca36a6c4f8a4a0ddaa033fdbe20836d87bbfb873
Patch12:        emitter.patch
Patch13:        tests-Use-native-TemporaryDirectory.patch

# Build fixes
Patch14:        init_patch.patch
Patch15:        remove-sloppy-m4-detection-from-bundled-autoconf.patch

# tentative patch for RUSTFLAGS parsing issue, taken from firefox package:
# https://bugzilla.redhat.com/show_bug.cgi?id=2184743
# https://bugzilla.mozilla.org/show_bug.cgi?id=1474486
Patch16:        firefox-112.0-commasplit.patch

# Python 3.13 fixup
Patch17:        six-is-always-PY3-don-t-ask-for-it.patch

# TODO: Check with mozilla for cause of these fails and re-enable spidermonkey compile time checks if needed
Patch20:        spidermonkey_checks_disable.patch

BuildRequires:  cargo
%if "%{toolchain}" == "clang"
BuildRequires:  clang
%endif
BuildRequires:  clang-devel
%if "%{toolchain}" == "gcc"
BuildRequires:  gcc
BuildRequires:  gcc-c++
%endif
BuildRequires:  m4
BuildRequires:  make
%if !0%{?rhel}
BuildRequires:  nasm
%endif
BuildRequires:  libicu-devel
BuildRequires:  llvm
BuildRequires:  rust
BuildRequires:  rustfmt
BuildRequires:  cbindgen
BuildRequires:  perl-devel
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3.13-devel
BuildRequires:  readline-devel
BuildRequires:  wget
BuildRequires:  zip

%description
SpiderMonkey is the code-name for Mozilla Firefox's C++ implementation of
JavaScript. It is intended to be embedded in other applications
that provide host environments for JavaScript.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n firefox-%{version} -p1

# Copy out the LICENSE file
cp LICENSE js/src/

# Copy out file containing known test failures with system libicu
cp %{SOURCE1} js/src/

# Remove zlib directory (to be sure using system version)
rm -rf modules/zlib

# Remove unneeded bundled stuff
rm -rf js/src/devtools/automation/variants/
rm -rf js/src/octane/
rm -rf js/src/ctypes/libffi/

# Fixups executable permmissions
chmod -x third_party/rust/bumpalo/src/lib.rs

# icu >= 76 link fix
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11
sed -i 's/icu-i18n/icu-uc &/' js/moz.configure
%endif

%build
# Use bundled autoconf
export M4=m4
export AWK=awk
export AC_MACRODIR=./build/autoconf/
export PYTHON3="/usr/bin/python3.13"

pushd js/src/
%configure \
  --with-system-icu \
  --with-system-zlib \
  --disable-tests \
  --disable-strip \
  --with-intl-api \
  --enable-readline \
  --enable-shared-js \
  --enable-optimize \
  --disable-debug \
  --enable-pie \
  --disable-jemalloc

%make_build

%install
pushd js/src/
%make_install

# Fix permissions
chmod -x %{buildroot}%{_libdir}/pkgconfig/*.pc

# Avoid multilib conflicts
case `uname -i` in
  i386 | ppc | s390 | sparc )
    wordsize="32"
    ;;
  x86_64 | ppc64 | s390x | sparc64 )
    wordsize="64"
    ;;
  *)
    wordsize=""
    ;;
esac

if test -n "$wordsize"
then
  mv %{buildroot}%{_includedir}/mozjs-%{major}/js-config.h \
     %{buildroot}%{_includedir}/mozjs-%{major}/js-config-$wordsize.h

  cat >%{buildroot}%{_includedir}/mozjs-%{major}/js-config.h <<EOF
#ifndef JS_CONFIG_H_MULTILIB
#define JS_CONFIG_H_MULTILIB

#include <bits/wordsize.h>

#if __WORDSIZE == 32
# include "js-config-32.h"
#elif __WORDSIZE == 64
# include "js-config-64.h"
#else
# error "unexpected value for __WORDSIZE macro"
#endif

#endif
EOF

fi

# Remove unneeded files
rm %{buildroot}%{_bindir}/js%{major}-config
rm %{buildroot}%{_libdir}/libjs_static.ajs

# Rename library and create symlinks, following fix-soname.patch
mv %{buildroot}%{_libdir}/libmozjs-%{major}.so \
   %{buildroot}%{_libdir}/libmozjs-%{major}.so.0.0.0
ln -s libmozjs-%{major}.so.0.0.0 %{buildroot}%{_libdir}/libmozjs-%{major}.so.0
ln -s libmozjs-%{major}.so.0 %{buildroot}%{_libdir}/libmozjs-%{major}.so

# Executable bit
chmod -x %{buildroot}%{_includedir}/mozjs-%{major}/js/ProfilingCategoryList.h
chmod -x %{buildroot}%{_includedir}/mozjs-%{major}/js-config.h

%check
# Use bundled py3 modules since we're using non-default Python (3.13)
export PYTHONPATH="${PYTHONPATH}:../../third_party/python/"

pushd js/src/
# Run SpiderMonkey tests
%if 0%{?require_tests}
/usr/bin/python3.13 tests/jstests.py -d -s -t 2400 --exclude-file=known_failures.txt --no-progress --wpt=disabled ../../js/src/dist/bin/js%{major}
%else
/usr/bin/python3.13 tests/jstests.py -d -s -t 2400 --exclude-file=known_failures.txt --no-progress --wpt=disabled ../../js/src/dist/bin/js%{major} || :
%endif

# Run basic JIT tests
%if 0%{?require_tests}

# large-arraybuffers/basic.js fails on s390x
%ifarch s390 s390x
/usr/bin/python3.13 jit-test/jit_test.py -s -t 2400 --no-progress -x large-arraybuffers/basic.js ../../js/src/dist/bin/js%{major} basic
%else
/usr/bin/python3.13 jit-test/jit_test.py -s -t 2400 --no-progress ../../js/src/dist/bin/js%{major} basic
%endif

%else
/usr/bin/python3.13 jit-test/jit_test.py -s -t 2400 --no-progress ../../js/src/dist/bin/js%{major} basic || :
%endif

%files
%doc js/src/README.html
%license js/src/LICENSE
%{_libdir}/libmozjs-%{major}.so.0*

%files devel
%{_bindir}/js%{major}
%{_libdir}/libmozjs-%{major}.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/mozjs-%{major}/

%changelog
%autochangelog
