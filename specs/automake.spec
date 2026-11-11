%global api_version 1.20

# redhat-rpm-config sets CFLAGS, CXXFLAGS and LDFLAGS, but not
# OBJCFLAGS. This means that Obj-C tests will be compiled without hardening
# flags, and then fail when linked with the hardened linker flags.
# We therefore need to disable build flags to be able to test automake itself.
# Since the automake executables are all interpreted languages, they aren't
# compiled and so the build flags only affect the tests anyway.
%undefine _auto_set_build_flags

# do not mangle shebang in files which are part of bootstraped project
%global __brp_mangle_shebangs_exclude_from /usr/share/automake-%{api_version}

# run "make check" by default
%bcond_without check
# Run optional test
%bcond_without automake_enables_optional_test

Summary:    A GNU tool for automatically creating Makefiles
Name:       automake
# Any bump here requires libtool rebuild, rhbz#1813010
Version:    %{api_version}
Release:    %autorelease

# To help future rebase, the following licenses were seen in the following files/folders:
# usr/bin/* - GPL-2.0-or-later
# usr/share/aclocal-1.16/* - FSFULLR
# usr/share/automake-1.16:
#   Automake/Getopt.pm - GPL-3.0-or-later
#   Automake/* - GPL-2.0-or-later
#   am/* - GPL-2.0-or-later
#   INSTALL - FSFAP
#   install-sh - X11 AND LicenseRef-Fedora-Public-Domain (added by autoconf)
#   mkinstalldirs - LicenseRef-Fedora-Public-Domain
#   config.{guess,sub} - GPL-3.0-or-later WITH Autoconf-exception-generic-3.0
#   texinfo.tex - GPL-3.0-or-later WITH Texinfo-exception
#   * - GPL-2.0-or-later WITH Autoconf-exception-generic
# usr/share/doc/automake:
#   {NEWS,README} - GPL-2.0-or-later
#   amhello-1.0.tar:
#     src/Makefile.in - FSFULLRWD
#     src/* - FSFUL
#     {Makefile.in,aclocal.m4} - FSFULLRWD
#     {Makefile.am,configure,configure.ac} - FSFUL
#     {compile,depcomp,missing} - GPL-2.0-or-later WITH Autoconf-exception-generic
#     install-sh - X11 AND LicenseRef-Fedora-Public-Domain (added by autoconf)
# usr/share/info:
#  * - GFDL-1.3-or-later
# usr/share/man/man1/*: generated from usr/bin/{aclocal,automake} using help2man
License:    GPL-2.0-or-later AND GPL-2.0-or-later WITH Autoconf-exception-generic AND GPL-3.0-or-later AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GPL-3.0-or-later WITH Texinfo-exception AND GFDL-1.3-or-later AND FSFAP AND FSFUL AND FSFULLR AND FSFULLRWD AND X11 AND LicenseRef-Fedora-Public-Domain

Source:     ftp://ftp.gnu.org/gnu/automake/automake-%{version}.tar.xz

# ~> downstream
# The patch is only made necessary due to fedora specific changes
# which lead to .package_note-automake-1.16.5-3.fc36.x86_64.ld
# being inserted in build logs, breaking the original grep instruction
Patch: fort2.patch

URL:        http://www.gnu.org/software/automake/
Requires:   autoconf >= 2.65

# requirements not detected automatically (#919810)
Requires:   perl(Thread::Queue)
Requires:   perl(threads)

BuildRequires:  autoconf >= 2.65
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Thread::Queue)
BuildRequires:  perl(threads)

BuildArch:  noarch

# for better tests coverage:
%if %{with check}
%if %{with automake_enables_optional_test}
BuildRequires: automake
BuildRequires: bison
BuildRequires: cscope
BuildRequires: dejagnu
BuildRequires: emacs
BuildRequires: expect
BuildRequires: flex
BuildRequires: gcc-gfortran
BuildRequires: gettext-devel
BuildRequires: libtool
BuildRequires: sharutils
BuildREquires: texlive-dvips
BuildRequires: texinfo-tex
BuildRequires: vala
%if !0%{?rhel:1}
BuildRequires: gcc-objc
BuildRequires: gcc-objc++
BuildRequires: imake
BuildRequires: lzip
BuildRequires: ncompress
%endif
%endif
%endif

# remove bogus Automake perl dependencies and provides
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Automake::
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Automake::

%description
Automake is a tool for automatically generating `Makefile.in'
files compliant with the GNU Coding Standards.

You should install Automake if you are developing software and would
like to use its ability to automatically generate GNU standard
Makefiles.


%prep
%autosetup -p1
%if %{with check} && %{with automake_enables_optional_test}
autoreconf -iv
%endif


%build
# redhat-rpm-config package, which provides this configure macro, will overwrite
# the config.sub and config.guess files intentionally. The automake maintainer
# needs to check that those files are provided up to date.
%configure
%make_build
cp m4/acdir/README README.aclocal
cp contrib/multilib/README README.multilib


%install
%make_install


%check
# %%global TESTS_FLAGS t/preproc-errmsg t/preproc-basics
%if %{with check}
make -k %{?_smp_mflags} check %{?TESTS_FLAGS: TESTS="%{TESTS_FLAGS}"} \
    || ( cat ./test-suite.log && false )
%endif


%files
%license COPYING*
%doc AUTHORS README THANKS NEWS README.aclocal README.multilib
%doc %{_pkgdocdir}/amhello-1.0.tar.gz
%exclude %{_infodir}/dir
%exclude %{_datadir}/aclocal
%{_bindir}/*
%{_infodir}/*.info*
%{_datadir}/automake-%{api_version}
%{_datadir}/aclocal-%{api_version}
%{_mandir}/man1/*


%changelog
%autochangelog
