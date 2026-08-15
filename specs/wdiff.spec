%bcond rebuild_mans 1
# As of 1.2.3, cannot autoreconf due to:
# configure:14538: error: undefined or overquoted macro: gl_PTHREADLIB
# configure:14651: error: undefined or overquoted macro: gl_WEAK_SYMBOLS
# configure:15859: error: undefined or overquoted macro: gl_TYPE_WINT_T_PREREQ
%bcond autoreconf 0

Name:           wdiff
Version:        1.2.3
Release:        %autorelease
Summary:        Compare files on a word per word basis

# Entire source is GPL-3.0-or-later, except:
#
# Latex2e:
#   wdiff.texi and the documentation built from it, including info, HTML, and
#     PDF documentation, to include doc/wdiff.info in the source tree.
# LGPL-2.0-or-later:
#     lib/_Noreturn.h
#     lib/arg-nonnull.h
#     lib/c++defs.h
#     lib/warn-on-use.h
# LGPL-2.1-or-later:
#   the entire contents of lib/, except:
#     - those listed as LGPL-2.0-or-later, above
#     - lib/Makefile.{am,in}, which are build-system files and are documented
#       above SourceLicense, and
#     - the following, which are GPL-3.0-or-later:
#       lib/xalloc-die.c lib/xalloc.h lib/xmalloc.c
#   lib/*/*.*
License:        %{shrink:
    GPL-3.0-or-later AND
    LGPL-2.0-or-later AND
    LGPL-2.1-or-later AND
    Latex2e
    }
# Additionally, build-system files do not contribute to the licenses of the
# binary RPMs, and some of these are under other licenses:
#
# FSFAP:
#   AUTHORS
#   config.h.in (inasmuch as it is derived from configure.ac, which is
#     explicitly so licensed)
#   configure.ac
#   INSTALL
#   Makefile.am
#   README
#   THANKS
#   TODO
#   doc/Makefile.am
#   man/Makefile.am
#   po/POTFILES.in
#   src/Makefile.am
# FSFAP AND FSFULLRWD: (Each is documented as FSFULLRWD, but derived from a
#     corresponding Makefile.am that is FSFAP.)
#   Makefile.in
#   doc/Makefile.in
#   man/Makefile.in
#   src/Makefile.in
# FSFAP-no-warranty-disclaimer:
#   configure
#   build-aux/config.rpath
# FSFUL:
#   tests/testsuite
# FSFULLR AND FSFULLRWD:
#   aclocal.m4
# FSFULLRWD AND GPL-3.0-or-later WITH Autoconf-exception-generic:
#   lib/Makefile.in
# FSFULLRWD:
#   m4/*, except:
#     - m4/gnulib-cache.m4
#     - m4/gnulib-comp.m4
#     - m4/init-package-version.m4
# GPL-2.0-or-later:
#   build-aux/gnupload
# GPL-2.0-or-later WITH Autoconf-exception-generic:
#   build-aux/compile
#   build-aux/depcomp
#   build-aux/mdate-sh
#   build-aux/missing
#   m4/init-package-version.m4
# GPL-3.0-or-later WITH Autoconf-exception-generic:
#   lib/Makefile.am
#   m4/gnulib-cache.m4
#   m4/gnulib-comp.m4
# GPL-3.0-or-later WITH Autoconf-exception-generic-3.0:
#   build-aux/config.guess
#   build-aux/config.sub
# GPL-3.0-or-later WITH Texinfo-exception:
#   build-aux/texinfo.tex
# X11 AND LicenseRef-Fedora-Public-Domain:
#   build-aux/install (“FSF changes to this file are in the public domain.”)
SourceLicense:  %{shrink:
    %{license} AND
    FSFAP AND
    FSFAP-no-warranty-disclaimer AND
    FSFUL AND
    FSFULLR AND
    FSFULLRWD AND
    GPL-2.0-or-later AND
    GPL-2.0-or-later WITH Autoconf-exception-generic AND
    GPL-3.0-or-later WITH Autoconf-exception-generic AND
    GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND
    GPL-3.0-or-later WITH Texinfo-exception AND
    LicenseRef-Fedora-Public-Domain AND
    X11
    }
URL:            https://www.gnu.org/software/wdiff
Source0:        https://ftp.gnu.org/gnu/wdiff/wdiff-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/wdiff/wdiff-%{version}.tar.gz.sig
# Fetched 2026-08-13:
Source2:        https://ftp.gnu.org/gnu/gnu-keyring.gpg

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  make
%if %{with autoreconf}
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool  
%endif

BuildRequires:  gettext-devel
BuildRequires:  ncurses-devel

BuildRequires:  help2man
BuildRequires:  texinfo  
BuildRequires:  texinfo-tex
BuildRequires:  tex(latex)

BuildRequires:  gpgverify

# https://fedorahosted.org/fpc/ticket/174
# Unclear which version of gnulib is currently bundled.
Provides: bundled(gnulib)

%description
The GNU wdiff program is a front end to diff for comparing files on a word per
word basis. A word is anything between whitespace. This is useful for comparing
two texts in which a few words have been changed and for which paragraphs have
been refilled. It works by creating two temporary files, one word per line, and
then executes diff on these files. It collects the diff output and uses it to
produce a nicer display of word differences between the original files.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%conf
%if %{with autoreconf}
autoreconf --force --install --verbose
%endif
%configure --enable-experimental="mdiff wdiff2 unify" 


%build
%make_build all

%if %{with rebuild_mans}
rm --verbose man/mdiff.1 man/wdiff.1 man/wdiff2.1 man/unify.1
%make_build --directory=man mdiff.1 wdiff.1 wdiff2.1 unify.1
%endif

# Make sure we rebuild the info page too.
rm --verbose doc/wdiff.info
%make_build --directory=doc info html pdf


%install
%make_install
find '%{buildroot}' -type f -name '*gnulib.mo' -print -delete
rm '%{buildroot}%{_infodir}/dir'
install --directory '%{buildroot}%{_pkgdocdir}'
install --preserve-timestamp --mode=0644 --target='%{buildroot}%{_pkgdocdir}' \
    ABOUT-NLS AUTHORS BACKLOG ChangeLog NEWS README THANKS TODO
cp --recursive --preserve doc/wdiff.html '%{buildroot}%{_pkgdocdir}/html'

%find_lang wdiff


%check
%make_build check


%files -f wdiff.lang
%license COPYING

%{_bindir}/mdiff
%{_bindir}/wdiff
%{_bindir}/wdiff2
%{_bindir}/unify

%{_mandir}/man1/mdiff.1*
%{_mandir}/man1/wdiff.1*
%{_mandir}/man1/wdiff2.1*
%{_mandir}/man1/unify.1*

%{_infodir}/wdiff.info.*

%{_pkgdocdir}/


%changelog
%autochangelog
