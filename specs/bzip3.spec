# We have gnulib and we will unbundle their sources
%if 0%{?rhel} == 10
# bug #2358779
%bcond_with gnulib
%else
%bcond_without gnulib
%endif

# Package bz3most tool
%if 0%{?rhel} && 0%{?rhel} >= 10
%bcond_with most
%else
%bcond_without most
%endif

Name:           bzip3
Version:        1.5.3
Release:        3%{?dist}
Summary:        Tools for compressing and decompressing bzip3 files
# 3rdparty/libsais-LICENSE: Apache-2.0 text
# bz3grep:                  BSD-2-Clause
# include/common.h:         LGPL-3.0-or-later
# include/libsais.h:        Apache-2.0
# include/libbz3.h:         LGPL-3.0-or-later
# include/yarg.h:           (unspecified, defaults to global LGPL-3.0-or-later)
# LICENSE:                  LGPL-3.0 text
# src/libbz3.c:             LGPL-3.0-or-later
# src/main.c:               LGPL-3.0-or-later
## Used at build time but not in any binary package
# build-aux/git-version-gen:    GPL-3.0-or-later
## Unbundled and not in any binary package
# aclocal.m4:               FSFULLR AND GPL-2.0-or-later WITH Autoconf-exception-generic
# build-aux/ax_build_date_epoch.m4: GPL-3.0-or-later WITH Autoconf-exception-macro
# build-aux/ax_pthread.m4:  GPL-3.0-or-later WITH Autoconf-exception-macro
# build-aux/ax_check_compile_flag.m4:   FSFAP
# build-aux/compile:        GPL-2.0-or-later WITH Autoconf-exception-generic
# build-aux/config.guess:   GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# build-aux/config.sub:     GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
# build-aux/depcomp:        GPL-2.0-or-later WITH Autoconf-exception-generic
# build-aux/install-sh:     X11 AND "FSF changes to this file are in the public domain"
# build-aux/libtool.m4:     FSFULLR AND GPL-2.0-or-later WITH Libtool-exception
#                           AND FSFUL
# build-aux/ltmain.sh:      GPL-2.0-or-later WITH Libtool-exception AND
#                           (GPL-2.0-or-later OR MIT)
# build-aux/lt~obsolete.m4  FSFULLR
# build-aux/ltoptions.m4:   FSFULLR
# build-aux/ltsugar.m4:     FSFULLR
# build-aux/missing:        GPL-2.0-or-later WITH Autoconf-exception-generic
# configure:                FSFUL AND GPL-2.0-or-later WITH Libtool-exception
# Makefile.in:              FSFULLR
License:        LGPL-3.0-or-later AND BSD-2-Clause
SourceLicense:  GPL-3.0-or-later AND GPL-3.0-or-later WITH Autoconf-exception-macro AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-2.0-or-later WITH Autoconf-exception-generic AND GPL-2.0-or-later WITH Libtool-exception AND (GPL-2.0-or-later OR MIT) AND LGPL-3.0-or-later AND BSD-2-Clause AND Apache-2.0 AND X11 AND FSFULLR AND FSFUL AND FSFAP
URL:            https://github.com/iczelia/%{name}
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
# Do not use /usr/bin/env in shell bangs, not suitable for upstream,
# <https://github.com/kspalaiologos/bzip3/pull/75>.
Patch0:         bzip3-1.5.0-Do-not-use-usr-bin-env-in-shell-bangs.patch
# Fix pkg-config file, in upstream after 1.5.3,
# <https://github.com/iczelia/bzip3/pull/169>.
Patch1:         bzip3-1.5.3-autoconf-Define-extra_cflags-variable.patch
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  bash
# coreutils for cat, tr in build-aux/git-version-gen
BuildRequires:  coreutils
BuildRequires:  findutils
# awk in configure.ac, configure, Makefile.in
BuildRequires:  gawk
BuildRequires:  gcc
%if %{with gnulib}
# For git-version-gen script executed from autoconf.ac
BuildRequires:  gnulib-devel
%endif
BuildRequires:  libtool
BuildRequires:  make
# PKG_PROG_PKG_CONFIG in configure.ac
BuildRequires:  pkgconf-pkg-config
# sed in build-aux/git-version-gen
BuildRequires:  sed
# Tests:
# md5sum is not helpful
Requires:       %{name}-grep = %{version}-%{release}
Requires:       %{name}-less = %{version}-%{release}
Requires:       %{name}-more = %{version}-%{release}
%if %{with most}
Requires:       %{name}-most = %{version}-%{release}
%endif
Requires:       %{name}-tools%{?_isa} = %{version}-%{release}

%description
These are tools for compressing, decompressing, printing, and searching bzip3
files. bzip3 features higher compression ratios and better performance than
bzip2 thanks to an order-0 context mixing entropy coder, a fast
Burrows-Wheeler transform code making use of suffix arrays and a run-length
encoding with Lempel-Ziv prediction pass based on LZ77-style string matching
and PPM-style context modeling.

If you only need bzip3 tool, consider installing %{name}-tools package
instead.

%package libs
Summary:        Shared libraries for bzip3 compression and decompression
License:        LGPL-3.0-or-later AND Apache-2.0 
# Forked, fixed, and pruned libasais <https://github.com/IlyaGrebnov/libsais>
# because of rejected fix <https://github.com/IlyaGrebnov/libsais/issues/10>.
Provides:       bundled(libsais) = 2.7.0

%description libs
This is a library for compressing and decompressing bzip3 compression format.
bzip3 features higher compression ratios and better performance than bzip2
thanks to an order-0 context mixing entropy coder, a fast Burrows-Wheeler
transform code making use of suffix arrays and a run-length encoding with
Lempel-Ziv prediction pass based on LZ77-style string matching and PPM-style
context modeling.

%package devel
Summary:        Files for developing with bzip3 library
License:        LGPL-3.0-or-later
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Header files, a pkg-config module and link objects for building applications
which use a bzip3 library.

%package grep
Summary:        Print lines matching a pattern in bzip3-compressed files
License:        LGPL-3.0-or-later
BuildArch:      noarch
Requires:       %{name}-tools = %{version}-%{release}
Requires:       grep

%description grep
This package contains a bz3most tool. It displays bzip3-compressed files with
the "most" pager.

%package less
Summary:        View bzip3-compressed files with less pager
License:        LGPL-3.0-or-later
BuildArch:      noarch
Requires:       %{name}-tools = %{version}-%{release}
Requires:       less

%description less
This package contains a bz3less tool. It displays bzip3-compressed files with
the "less" pager.

%package more
Summary:        View bzip3-compressed files with more pager
License:        LGPL-3.0-or-later
BuildArch:      noarch
Requires:       %{name}-tools = %{version}-%{release}
# For "more" program
Requires:       util-linux-core

%description more
This package contains a bz3more tool. It displays bzip3-compressed files with
the "more" pager.

%if %{with most}
%package most
Summary:        View bzip3-compressed files with most pager
License:        LGPL-3.0-or-later
BuildArch:      noarch
Requires:       %{name}-tools = %{version}-%{release}
Requires:       most

%description most
This package contains a bz3most tool. It displays bzip3-compressed files with
the "most" pager.
%endif

%package tools
Summary:        Tools for compressing and decompressing bzip3 archives
License:        LGPL-3.0-or-later
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Recommends:     (%{name}-grep if grep)
Recommends:     (%{name}-less if less)
Recommends:     (%{name}-more if util-linux-core)
%if %{with most}
Recommends:     (%{name}-most if most)
%endif

%description tools
This package contains bunzip3, bz3cat, and bzip3 tools.

%prep
%autosetup -p1
# Remove generated autoconf files
rm aclocal.m4 configure Makefile.in
# Remove generated manual pages
for F in *.1.in; do
    rm "${F%%.in}"
done
# Unbundle autoconf macros and scripts, except those not yet packaged in
# autoconf-archive
find build-aux -type f \! \( \
%if %{without gnulib}
    -name git-version-gen -o \
%endif
    -name ax_progvar.m4 -o \
    -name ax_subst_man_date.m4 -o \
    -name ax_subst_transformed_package_name.m4 \
    \) -delete
%if %{with gnulib}
# Execute git-version-gen from a system location
ln -s %{_datadir}/gnulib/build-aux/git-version-gen build-aux/git-version-gen
%endif

%build
autoreconf -vfi
%configure \
    --disable-arch-native \
    --with-pic \
    --with-pthread \
    --enable-shared \
    --disable-static \
    --disable-static-exe
%{make_build}

%check
make check roundtrip %{?_smp_mflags}

%install
%{make_install}
find %{buildroot} -name '*.la' -delete
# Deduplicate identical files
if cmp %{buildroot}%{_mandir}/man1/{bz3cat,bunzip3}.1; then
    rm %{buildroot}%{_mandir}/man1/bunzip3.1
    ln -s bz3cat.1 %{buildroot}%{_mandir}/man1/bunzip3.1
fi

%files
# An umbrella metapackage.

%files libs
%license 3rdparty/libsais-LICENSE LICENSE
%doc NEWS README.md
%{_libdir}/libbzip3.so.1{,.*}

%files devel
%{_includedir}/libbz3.h
%{_libdir}/libbzip3.so
%{_libdir}/pkgconfig/bzip3.pc

%files grep
%{_bindir}/bz3grep
%{_mandir}/man1/bz3grep.1*

%files less
%{_bindir}/bz3less
%{_mandir}/man1/bz3less.1*

%files more
%{_bindir}/bz3more
%{_mandir}/man1/bz3more.1*

%if %{with most}
%files most
%{_bindir}/bz3most
%{_mandir}/man1/bz3most.1*
%else
%exclude %{_bindir}/bz3most
%exclude %{_mandir}/man1/bz3most.1*
%endif

%files tools
%define programs \{bunzip3,bz3cat,bzip3\}
%{_bindir}/%{programs}
%{_mandir}/man1/%{programs}.1*

%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Mon Aug 18 2025 Petr Pisar <ppisar@redhat.com> - 1.5.3-1
- 1.5.3 bump

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Apr 30 2025 Petr Pisar <ppisar@redhat.com> - 1.5.2-1
- 1.5.2 bump
- Fix handling failed memory allocations in the bzip3 tool

* Thu Apr 10 2025 Petr Pisar <ppisar@redhat.com> - 1.5.1-4
- Move bunzip3, bz3cat, and bzip3 to bzip3-tools package
- Move bz3grep to bzip3-grep package
- Move bz3less to bzip3-less package
- Move bz3more to bzip3-more package
- Move bz3most to bzip3-most package

* Mon Mar 24 2025 Petr Pisar <ppisar@redhat.com> - 1.5.1-3
- Fix bz3cat processing a standard input (bug #2354263)

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 16 2024 Petr Pisar <ppisar@redhat.com> - 1.5.1-1
- 1.5.1 bump

* Mon Dec 16 2024 Petr Pisar <ppisar@redhat.com> - 1.5.0-1
- 1.5.0 bump

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 09 2024 Petr Pisar <ppisar@redhat.com> - 1.4.0-1
- 1.4.0 bump

* Mon Aug 07 2023 Petr Pisar <ppisar@redhat.com> - 1.3.2-1
- 1.3.2 bump

* Tue Jul 25 2023 Petr Pisar <ppisar@redhat.com> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 22 2023 Petr Pisar <ppisar@redhat.com> - 1.3.1-1
- 1.3.1 bump

* Wed Apr 05 2023 Petr Pisar <ppisar@redhat.com> - 1.3.0-1
- 1.3.0 bump (CVE-2023-29415, CVE-2023-29416, CVE-2023-29417, CVE-2023-29418,
  CVE-2023-29419, CVE-2023-29420, CVE-2023-29421)

* Mon Mar 27 2023 Petr Pisar <ppisar@redhat.com> - 1.2.3-1
- 1.2.3 bump

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Petr Pisar <ppisar@redhat.com> - 1.2.2-1
- 1.2.2 bump

* Fri Nov 11 2022 Petr Pisar <ppisar@redhat.com> - 1.2.1-1
- 1.2.1 bump

* Wed Nov 02 2022 Petr Pisar <ppisar@redhat.com> - 1.2.0-3
- Do not own pkg-config directory

* Wed Nov 02 2022 Petr Pisar <ppisar@redhat.com> - 1.2.0-2
- Less globs and and more verbose output in a spec file

* Tue Nov 01 2022 Petr Pisar <ppisar@redhat.com> - 1.2.0-1
- 1.2.0 bump

* Wed Oct 26 2022 Petr Pisar <ppisar@redhat.com> - 1.1.8-1
- 1.1.8 packaged

