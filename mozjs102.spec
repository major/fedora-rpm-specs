%global major 102

# LTO - Enable in Release builds, but consider disabling for development as it increases compile time
%global build_with_lto    1

# Require tests to pass?
%global require_tests     1

%if 0%{?build_with_lto}
# LTO is the default
%else
%define _lto_cflags %{nil}
%endif

# Big endian platforms
%ifarch ppc ppc64 s390 s390x
%global big_endian 1
%endif

Name:           mozjs%{major}
Version:        102.7.0
Release:        1%{?dist}
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
Patch16:        0001-Python-Build-Use-r-instead-of-rU-file-read-modes.patch

# TODO: Check with mozilla for cause of these fails and re-enable spidermonkey compile time checks if needed
Patch20:        spidermonkey_checks_disable.patch

# s390x/ppc64 fixes
Patch21:        0001-Skip-failing-tests-on-ppc64-and-s390x.patch

BuildRequires:  cargo
BuildRequires:  ccache
BuildRequires:  clang-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  m4
BuildRequires:  make
%if !0%{?rhel}
BuildRequires:  nasm
%endif
BuildRequires:  libicu-devel
BuildRequires:  llvm
BuildRequires:  rust
BuildRequires:  rustfmt
BuildRequires:  perl-devel
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
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
%autosetup -n firefox-%{version}/js/src -N

pushd ../..
%autopatch -p1

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

popd

%build
%if 0%{?build_with_lto}
# https://github.com/ptomato/mozjs/commit/36bb7982b41e0ef9a65f7174252ab996cd6777bd
export CARGO_PROFILE_RELEASE_LTO=true
%endif

# Use bundled autoconf
export M4=m4
export AWK=awk
export AC_MACRODIR=/builddir/build/BUILD/firefox-%{version}/build/autoconf/

sh ../../build/autoconf/autoconf.sh --localdir=/builddir/build/BUILD/firefox-%{version}/js/src configure.in > configure
chmod +x configure

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

%check
# Run SpiderMonkey tests
%if 0%{?require_tests}
%{python3} tests/jstests.py -d -s -t 2400 --exclude-file=known_failures.txt --no-progress --wpt=disabled ../../js/src/dist/bin/js%{major}
%else
%{python3} tests/jstests.py -d -s -t 2400 --exclude-file=known_failures.txt --no-progress --wpt=disabled ../../js/src/dist/bin/js%{major} || :
%endif

# Run basic JIT tests
%if 0%{?require_tests}

# large-arraybuffers/basic.js fails on s390x
%ifarch s390 s390x
%{python3} jit-test/jit_test.py -s -t 2400 --no-progress -x large-arraybuffers/basic.js ../../js/src/dist/bin/js%{major} basic
%else
%{python3} jit-test/jit_test.py -s -t 2400 --no-progress ../../js/src/dist/bin/js%{major} basic
%endif

%else
%{python3} jit-test/jit_test.py -s -t 2400 --no-progress ../../js/src/dist/bin/js%{major} basic || :
%endif

%files
%doc README.html
%license LICENSE
%{_libdir}/libmozjs-%{major}.so.0*

%files devel
%{_bindir}/js%{major}
%{_libdir}/libmozjs-%{major}.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/mozjs-%{major}/

%changelog
* Mon Jan 16 2023 Frantisek Zatloukal <fzatlouk@redhat.com> - 102.7.0-1
- mozjs102-102.7.0 (fixes RHBZ#2161250)

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 102.6.0-2
- Rebuild for ICU 72

* Mon Dec 12 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 102.6.0-1
- mozjs102-102.6.0 (fixes RHBZ#2152654)

* Tue Nov 15 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 102.5.0-1
- mozjs102-102.5.0

* Mon Oct 17 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 102.4.0-1
- mozjs102-102.4.0 (fixes RHBZ#2135298)

* Wed Sep 21 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 102.3.0-1
- mozjs102-102.3.0 (fixes RHBZ#2127989)

* Mon Aug 22 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 102.2.0-1
- mozjs102-102.2.0

* Wed Jul 27 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 102.1.0-1
- Initial mozjs102 package based on mozjs91
