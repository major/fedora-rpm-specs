%global major 91

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
Version:        91.13.0
Release:        1%{?dist}
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
Patch13:        tests-Use-native-TemporaryDirectory.patch

# Build fixes
Patch14:        init_patch.patch
Patch15:        remove-sloppy-m4-detection-from-bundled-autoconf.patch
Patch16:        0001-Python-Build-Use-r-instead-of-rU-file-read-modes.patch

# TODO: Check with mozilla for cause of these fails and re-enable spidermonkey compile time checks if needed
Patch17:        spidermonkey_checks_disable.patch

# s390x/ppc64 fixes
Patch19:        0001-Skip-failing-tests-on-ppc64-and-s390x.patch

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
BuildRequires:  rust
BuildRequires:  perl-devel
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  readline-devel
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
%patch17 -p1

# Fixes for ppc64 and s390x, there is no need to keep it in ifarch here since mozilla tests support ifarch conditions
%patch19 -p1

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
export LINKFLAGS="%{?build_ldflags}"
export PYTHON="%{python3}"

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
* Mon Aug 22 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 91.13.0-1
- mozjs91-91.13.0

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 91.12.0-2
- Rebuilt for ICU 71.1

* Wed Jul 27 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 91.12.0-1
- mozjs91-91.12.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 91.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 91.11.0-2
- Fixup Python 3.11 build

* Mon Jun 27 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 91.11.0-1
- mozjs91-91.11.0

* Tue Jun 14 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 91.10.0-1
- mozjs91-91.10.0

* Sun May 08 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 91.9.0-1
- mozjs91-91.9.0

* Sat Apr 09 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 91.8.0-1
- mozjs91-91.8.0

* Tue Mar 08 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 91.7.0-1
- mozjs91-91.7.0

* Sun Feb 20 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 91.6.0-1
- mozjs91-91.6.0
- switch to system libicu

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 91.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 91.5.0-1
- mozjs91-91.5.0

* Mon Dec 06 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 91.4.0-1
- mozjs91-91.4.0

* Wed Nov 03 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 91.3.0-1
- mozjs91-91.3.0

* Mon Oct 04 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 91.2.0-1
- mozjs91-91.2.0

* Mon Sep 20 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 91.1.0-1
- mozjs91-91.1.0

* Mon Aug 09 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 91.0-1
- Initial mozjs91 package based on mozjs78
