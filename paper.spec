# Unbundle gnulib
%bcond_without paper_enables_unbundling_gnulib

Name:           paper
Version:        2.3
Release:        6%{?dist}
Summary:        Query paper size database and retrieve the preferred size
# COPYING:              GPL-3.0 text
# lib/progname.c:       GPL-3.0-or-later (bundled from gnulib)
# lib/progname.h:       GPL-3.0-or-later (bundled from gnulib)
# src/localepaper.c:    FSFAP
# src/paper.in.in:      GPL-3.0-or-later
## Not in any binary package
# aclocal.m4:   FSFULLR
# build-aux/compile:        GPL-2.0-or-later WITH Libtool-exception
#                           <https://gitlab.com/fedora/legal/fedora-license-data/-/issues/68>
# build-aux/config.guess:   GPL-3.0-or-later WITH Libtool-exception
# build-aux/config.sub:     GPL-3.0-or-later WITH Libtool-exception
# build-aux/depcomp:        GPL-2.0-or-later WITH Libtool-exception
# build-aux/install-sh:     MIT
# build-aux/missing:        GPL-2.0-or-later WITH Libtool-exception
# build-aux/relocatable.pl.in:  GPL-3.0-or-later
# configure:    FSFUL
# INSTALL:      FSFAP
# lib/arg-nonnull.h:    GPL-3.0-or-later
# lib/c++defs.h:        GPL-3.0-or-later
# lib/langinfo.in.h:    GPL-3.0-or-later
# lib/locale.in.h:      GPL-3.0-or-later
# lib/Makefile.am:      GPL-3.0-or-later WITH Libtool-exception
# lib/Makefile.in:      GPL-3.0-or-later WITH Libtool-exception AND FSFULLR
# lib/stddef.in.h:      GPL-3.0-or-later
# lib/warn-on-use.h:    GPL-3.0-or-later
# m4/00gnulib.m4:           FSFULLR
# m4/absolute-header.m4:    FSFULLR
# m4/extensions.m4:         FSFULLR
# m4/gnulib-cache.m4:       GPL-3.0-or-later WITH Libtool-exception
# m4/gnulib-common.m4:      FSFULLR
# m4/gnulib-comp.m4:        GPL-3.0-or-later WITH Libtool-exception
# m4/include_next.m4:       FSFULLR
# m4/langinfo_h.m4:         FSFULLR
# m4/locale_h.m4:           FSFULLR
# m4/relocatable-lib.m4:    FSFULLR
# m4/stddef_h.m4:           FSFULLR
# m4/warn-on-use.m4:        FSFULLR
# m4/wchar_t.m4:            FSFULLR
# Makefile.in:      FSFULLR
# man/Makefile.in:  FSFULLR
# src/Makefile.in:  FSFULLR
License:        GPL-3.0-or-later AND FSFAP
URL:            https://github.com/rrthomas/%{name}
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bash
# coreutils for chmod executed from src/Makefile.am
BuildRequires:  coreutils
BuildRequires:  gcc
%if %{with paper_enables_unbundling_gnulib}
BuildRequires:  gnulib-devel
%endif
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(locale)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
# glibc-common for locale tool
BuildRequires:  glibc-common
BuildRequires:  diffutils
Provides:       bundled(gnulib)%(perl -ne 'if($. == 1 and /\A(\d+)-(\d+)-(\d+)/) {print qq{ = $1$2$3}}' %{_defaultdocdir}/gnulib/ChangeLog 2>/dev/null)

%description
This package enables users to indicate their preferred paper size, provides
the paper(1) utility to find the user's preferred default paper size and give
information about known sizes, and specifies system-wide and per-user paper
size catalogs, which can also be used directly (see paperspecs(5)).

%prep
%setup -q
%if %{with paper_enables_unbundling_gnulib}
gnulib-tool --import --no-conditional-dependencies --no-libtool \
    langinfo locale progname relocatable-perl
%endif
autoreconf -fi

%build
%configure --disable-relocatable
%{make_build}

%check
# No upstream tests
echo "Testing localepaper tool"
locale width height > expected
./src/localepaper | tr ' ' "\n" > got
diff -u expected got
echo "Testing paper tool"
perl -c ./src/paper

%install
%{make_install}

%files
%license COPYING
# ChangeLog, NEWS are not helpful
%doc AUTHORS README
%{_bindir}/paper
%config(noreplace) %{_sysconfdir}/paperspecs
%{_libexecdir}/localepaper
%{_mandir}/man1/paper.1*
%{_mandir}/man5/paperspecs.5*

%changelog
* Wed Jan 04 2023 Petr Pisar <ppisar@redhat.com> - 2.3-6
- Correct a typo in a description
- Convert a License tag to the SPDX format

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 15 2020 Petr Pisar <ppisar@redhat.com> - 2.3-1
- 2.3 bump

* Tue Oct 06 2020 Petr Pisar <ppisar@redhat.com> - 2.2-1
- 2.2 version packaged

