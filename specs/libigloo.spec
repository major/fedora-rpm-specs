Name:       libigloo
Version:    0.9.2
Release:    8%{?dist}
Summary:    C framework from Icecast
# COPYING:                  LGPL-2.0 text
# include/igloo/config.h:   LGPL-2.0-or-later
# include/igloo/cs.h:       LGPL-2.0-or-later
# include/igloo/error.h:    LGPL-2.0-or-later
# include/igloo/feature.h:  LGPL-2.0-or-later
# include/igloo/igloo.h:    LGPL-2.0-or-later
# include/igloo/list.h:     LGPL-2.0-or-later
# include/igloo/prng.h:     LGPL-2.0-or-later
# include/igloo/ro.h:       LGPL-2.0-or-later
# include/igloo/rwlock.h:   LGPL-2.0-or-later
# include/igloo/sp.h:       LGPL-2.0-or-later
# include/igloo/tap.h:      LGPL-2.0-or-later
# include/igloo/time.h:     LGPL-2.0-or-later
# include/igloo/typedef.h:  LGPL-2.0-or-later
# include/igloo/types.h:    LGPL-2.0-or-later
# include/igloo/uuid.h:     LGPL-2.0-or-later
# src/cs.c:         LGPL-2.0-or-later
# src/error.c:      LGPL-2.0-or-later
# src/feature.c:    LGPL-2.0-or-later
# src/igloo.c:      LGPL-2.0-or-later
# src/list.c:       LGPL-2.0-or-later
# src/private.h:    LGPL-2.0-or-later
# src/prng.c:       LGPL-2.0-or-later
# src/ro.c:         LGPL-2.0-or-later
# src/rwlock.c:     LGPL-2.0-or-later
# src/sp.c:         LGPL-2.0-or-later
# src/tap.c:        LGPL-2.0-or-later
# src/time.c:       LGPL-2.0-or-later
# src/uuid.c:       LGPL-2.0-or-later
# tests/cs.c:           LGPL-2.0-or-later
# tests/digest.c:       LGPL-2.0-or-later
# tests/error.c:        LGPL-2.0-or-later
# tests/feature.c:      LGPL-2.0-or-later
# tests/init_igloo_test.c:  LGPL-2.0-or-later
# tests/prng.c:         GPL-2.0-only                !
# tests/ro.c:           LGPL-2.0-or-later
# tests/tap_suite.c:    LGPL-2.0-or-later
# tests/time.c:         LGPL-2.0-or-later
# tests/uuid.c:         LGPL-2.0-or-later
## Used at build, but not in any binary package
# m4/ax_gcc_type_attribute.m4:  FSFAP
## Unbundled
# aclocal.m4:   FSFULLR AND GPL-2.0-or-later WITH Libtool-exception
#               <https://gitlab.com/fedora/legal/fedora-license-data/-/issues/68>
# build-aux/ar-lib:         GPL-2.0-or-later WITH Libtool-exception
# build-aux/compile:        GPL-2.0-or-later WITH Libtool-exception
# build-aux/config.guess:   GPL-3.0-or-later WITH Libtool-exception
# build-aux/config.sub:     GPL-3.0-or-later WITH Libtool-exception
# build-aux/depcomp:        GPL-2.0-or-later WITH Libtool-exception
# build-aux/install-sh:     X11 AND LicenseRef-Fedora-Public-Domain
# build-aux/ltmain.sh:      GPL-2.0-or-later WITH Libtool-exception AND
#                           GPL-3.0-or-later WITH Libtool-exception AND
#                           GPL-3.0-or-later
# build-aux/missing:        GPL-2.0-or-later WITH Libtool-exception
# build-aux/tap-driver.sh:  GPL-2.0-or-later WITH Libtool-exception
# configure:                FSFUL AND GPL-2.0-or-later WITH Libtool-exception
# Makefile.in:      FSFULLR
# m4/ax_check_compile_flag.m4:  GPL-3.0-or-later WITH Autoconf-exception-2.0
# m4/ax_require_defined.m4:     FSFAP
# m4/ax_append_compile_flags.m4:    GPL-3.0-or-later WITH Autoconf-exception-2.0
# m4/ax_append_flag.m4:         GPL-3.0-or-later WITH Autoconf-exception-2.0
# m4/libtool.m4:                FSFULLR AND
#                               GPL-2.0-or-later WITH Libtool-exception
# m4/lt~obsolete.m4:            FSFULLR
# m4/ltoptions.m4:              FSFULLR
# m4/ltsugar.m4:                FSFULLR
# m4/ltversion.m4:              FSFULLR
License:    LGPL-2.0-or-later
URL:        https://icecast.org/
Source0:    https://downloads.xiph.org/releases/igloo/%{name}-%{version}.tar.gz
# Make time test robusts against CPU scheduler whims, proposed to the
# upstream, <https://gitlab.xiph.org/xiph/icecast-libigloo/-/issues/9>.
Patch0:     libigloo-0.9.2-Fix-Make-now-r-now-time-test-tolerant-to-CPU-schedul.patch
BuildRequires:  autoconf >= 2.67
# autoconf-archive for ACX_PTHREAD macro
BuildRequires:  autoconf-archive
BuildRequires:  automake >= 1.14
# binutils for ar command (AM_PROG_AR in configure.ac)
BuildRequires:  binutils
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# pkgconf-pkg-config for pkg-config (PKG_INSTALLDIR)
BuildRequires:  pkgconf-pkg-config
# pkgconf-m4 for PKG_CHECK_MODULES macro
BuildRequires:  pkgconf-m4
BuildRequires:  rhash-devel
BuildRequires:  sed

%description
This is a collection of functions used in Icecast project. Namely: deprecation
warnings, string conversion functions, digests, HMAC, PRNG, UUID, error codes,
logging, lists, locking, objects with reference counting, Test Any Protocol,
clock. The cryptographical features are implemented with RHash library.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
Libraries and header files for developing applications that use %{name}.

%package tests
Summary:    Tests for %{name}
License:    LGPL-2.0-or-later AND GPL-2.0-only
BuildArch:  noarch
Requires:   %{name}-devel = %{version}-%{release}
Requires:   autoconf >= 2.67
Requires:   automake >= 1.14
Requires:   coreutils
Requires:   gawk
Requires:   gcc
Requires:   make
Requires:   pkgconf-m4

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1
# Remove bundled files
rm -r aclocal.m4 build-aux
find m4 -type f \! -name ax_gcc_type_attribute.m4 -delete
# Remove pregenerated files
rm configure Makefile.in

%build
autoreconf -vfi
%configure \
    --with-boot-id=/proc/sys/kernel/random/boot_id \
    --enable-largefile \
    --with-machine-id=/etc/machine-id \
    --without-sanitizer \
    --enable-shared \
    --disable-static \
    --with-urandom=/dev/urandom
%{make_build}

%check
make check %{?_smp_mflags}

%install
%{make_install}
find %{buildroot} -name '*.la' -delete

# Install the tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a tests %{buildroot}%{_libexecdir}/%{name}
sed -n -e '/^# Tests/,/^# Public header files/p' < Makefile.am \
    > %{buildroot}%{_libexecdir}/%{name}/Makefile.am
cat > %{buildroot}%{_libexecdir}/%{name}/configure.ac << 'EOF'
AC_INIT([test], [0])
AC_PREREQ([2.67])
AC_CONFIG_AUX_DIR([build-aux])
AM_INIT_AUTOMAKE([1.14 foreign subdir-objects])
AC_PROG_CC
PKG_CHECK_MODULES([LIBIGLOO], [igloo], [
  CFLAGS="${CFLAGS} ${LIBIGLOO_CFLAGS}"
  LIBS="${LIBS} ${LIBIGLOO_LIBS}"
])
AC_REQUIRE_AUX_FILE([tap-driver.sh])
AC_CONFIG_HEADERS([config.h])
AC_CONFIG_FILES([
  Makefile
])
AC_OUTPUT
EOF
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# autoconf writes into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/{configure.ac,Makefile.am,tests} "$DIR"
pushd "$DIR"
autoreconf -vfi
./configure
make -j "$(getconf _NPROCESSORS_ONLN)" check
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%files
%license COPYING
%doc NEWS README
%{_libdir}/%{name}.so.0
%{_libdir}/%{name}.so.0.*

%files devel
%{_includedir}/igloo
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/igloo.pc

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 23 2024 Orion Poplawski <orion@nwra.com> - 0.9.2-6
- Rebuild for rhash 1.4.4 soname bump

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 17 2023 Petr Pisar <ppisar@redhat.com> - 0.9.2-3
- Make time test robusts against CPU scheduler whims (upstream bug #9)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 31 2023 Petr Pisar <ppisar@redhat.com> - 0.9.2-1
- 0.9.2 packaged

