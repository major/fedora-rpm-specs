%global major 78

# LTO - Enable in Release builds, but consider disabling for development as it increases compile time
%global build_with_lto    1

# Require tests to pass?
%global require_tests     1

%if 0%{?build_with_lto}
# LTO is default since F33 and F32 package is backported as is, so no LTO there
%else
%define _lto_cflags %{nil}
%endif

# Require libatomic for ppc
%ifarch ppc
%global system_libatomic 1
%endif

# Big endian platforms
%ifarch ppc ppc64 s390 s390x
%global big_endian 1
%endif

Name:           mozjs%{major}
Version:        78.15.0
Release:        10%{?dist}
Summary:        SpiderMonkey JavaScript library

License:        MPLv2.0 and MPLv1.1 and BSD and GPLv2+ and GPLv3+ and LGPLv2+ and AFL and ASL 2.0
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

# Build fixes
Patch13:        Fixup-compatibility-of-mozbuild-with-Python-3.10.patch
Patch14:        init_patch.patch
# TODO: Check with mozilla for cause of these fails and re-enable spidermonkey compile time checks if needed
Patch15:        spidermonkey_checks_disable.patch
# Python 3.11 compat
Patch16:        0001-Python-Build-Use-r-instead-of-rU-file-read-modes.patch

# armv7 fixes
Patch17:        definitions_for_user_vfp.patch

# s390x/ppc64 fixes, TODO: file bug report upstream?
Patch18:        spidermonkey_style_check_disable_s390x.patch
Patch19:        0001-Skip-failing-tests-on-ppc64-and-s390x.patch

# Fix for https://bugzilla.mozilla.org/show_bug.cgi?id=1644600 ( SharedArrayRawBufferRefs is not exported )
# https://github.com/0ad/0ad/blob/83e81362d850cc6f2b3b598255b873b6d04d5809/libraries/source/spidermonkey/FixSharedArray.diff
Patch30:        FixSharedArray.diff

# Avoid autoconf213 dependency, backported from upstream
# https://bugzilla.mozilla.org/show_bug.cgi?id=1663863
Patch31:        0002-D89554-autoconf1.diff
Patch32:        0003-D94538-autoconf2.diff

BuildRequires:  cargo
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
BuildRequires:  llvm-devel
BuildRequires:  rust
BuildRequires:  perl-devel
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  readline-devel
BuildRequires:  zip

%if 0%{?big_endian}
BuildRequires:  icu
%endif

%if 0%{?system_libatomic}
BuildRequires:  libatomic
%endif

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
%setup -q -n firefox-%{version}/js/src

pushd ../..
%patch01 -p1
%patch02 -p1
%patch03 -p1
%patch09 -p1
%patch10 -p1

%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

%ifarch armv7hl
# Include definitions for user vfp on armv7 as it causes the compilation to fail without them
# https://bugzilla.mozilla.org/show_bug.cgi?id=1526653
%patch17 -p1
%endif

%ifarch s390x
%patch18 -p1
%endif

# Fixes for ppc64 and s390x, there is no need to keep it in ifarch here since mozilla tests support ifarch conditions
%patch19 -p1

# Export SharedArrayRawBufferRefs
%patch30 -p1

# Avoid autoconf213 dependency
%patch31 -p1 -b .autoconf213
%patch32 -p1 -b .autoconf213-2

# Copy out the LICENSE file
cp LICENSE js/src/

# Copy out file containing known test failures with system libicu
cp %{SOURCE1} js/src/
popd

# Remove zlib directory (to be sure using system version)
rm -rf ../../modules/zlib

%build
# Prefer GCC for now
export CC=gcc
export CXX=g++

# Workaround
# error: options `-C embed-bitcode=no` and `-C lto` are incompatible
# error: could not compile `jsrust`.
# https://github.com/japaric/cargo-call-stack/issues/25
export RUSTFLAGS="-C embed-bitcode"

%if 0%{?build_with_lto}
# https://github.com/ptomato/mozjs/commit/36bb7982b41e0ef9a65f7174252ab996cd6777bd
export CARGO_PROFILE_RELEASE_LTO=true
%endif

export CFLAGS="%{optflags}"
export CXXFLAGS="$CFLAGS"
export LINKFLAGS="%{?__global_ldflags}"
export PYTHON="%{__python3}"

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

%if 0%{?big_endian}
echo "Generate big endian version of config/external/icu/data/icud67l.dat"
pushd ../..
  icupkg -tb config/external/icu/data/icudt67l.dat config/external/icu/data/icudt67b.dat
  rm -f config/external/icu/data/icudt*l.dat
popd
%endif

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
PYTHONPATH=tests/lib %{__python3} tests/jstests.py -d -s -t 2400 --exclude-file=known_failures.txt --no-progress --wpt=disabled ../../js/src/dist/bin/js%{major}
%else
PYTHONPATH=tests/lib %{__python3} tests/jstests.py -d -s -t 2400 --exclude-file=known_failures.txt --no-progress --wpt=disabled ../../js/src/dist/bin/js%{major} || :
%endif

# Run basic JIT tests
%if 0%{?require_tests}
PYTHONPATH=tests/lib %{__python3} jit-test/jit_test.py -s -t 2400 --no-progress ../../js/src/dist/bin/js%{major} basic
%else
PYTHONPATH=tests/lib %{__python3} jit-test/jit_test.py -s -t 2400 --no-progress ../../js/src/dist/bin/js%{major} basic || :
%endif

%ldconfig_scriptlets

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
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 78.15.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 78.15.0-9
- Rebuild for ICU 72

* Fri Dec 02 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.15.0-8
- Add few more test exceptions

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.15.0-7
- Rebuilt for ICU 71.1

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.15.0-6
- Switch to system-icu everywhere

* Sun Jul 24 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.15.0-5
- Fixup Python 3.11 build

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 78.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 20 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.15.0-3
- Switch to system-icu on armv7hl to fix FTBFS

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 78.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.15.0-1
- Update to 78.15.0

* Mon Sep 27 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.14.0-1
- Update to 78.14.0

* Mon Aug 09 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.13.0-1
- Update to 78.13.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 78.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.12.0-2
- Fixup compatibility of mozbuild with Python 3.10

* Tue Jul 13 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.12.0-1
- Update to 78.12.0

* Wed Jun 02 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.11.0-1
- Update to 78.11.0

* Tue Apr 20 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.10.0-1
- Update to 78.10.0

* Mon Apr 12 2021 Jan Horak <jhorak@redhat.com> - 78.9.0-3
- Removed autoconf213 dependency

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 78.9.0-2
- Rebuilt for removed libstdc++ symbol (#1937698)

* Thu Mar 25 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.9.0-1
- Update to 78.9.0
- Rebase patches
- Replace armv7_disable_WASM_EMULATE_ARM_UNALIGNED_FP_ACCESS with patch from Debian to include vfp defs

* Tue Feb 23 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.8.0-2
- Don't BR nasm on RHEL

* Tue Feb 23 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.8.0-1
- Update to 78.8.0
- Add fix for MOZBZ#1644600

* Tue Jan 26 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.7.0-1
- Update to 78.7.0

* Tue Dec 15 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.6.0-1
- Update to 78.6.0

* Tue Nov 17 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.5.0-1
- Update to 78.5.0
- Build with: --enable-optimize, --disable-debug

* Mon Oct 19 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.4.0-1
- Update to 78.4.0

* Tue Sep 22 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.3.0-1
- Update to 78.3.0

* Mon Aug 24 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.2.0-1
- Update to 78.2.0

* Mon Aug 17 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.1.0-2
- Add BR: python3-setuptools
- Backport fix for https://bugzilla.mozilla.org/show_bug.cgi?id=1654696
- Set CARGO_PROFILE_RELEASE_LTO=true

* Tue Jul 28 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 78.1.0-1
- Initial mozjs78 package based on mozjs68
