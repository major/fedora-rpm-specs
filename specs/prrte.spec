Name:           prrte
Version:        3.0.14
Release:        %autorelease
Summary:        PMIx Reference RunTime Environment (PRRTE)
# src/mca/prtereachable/netlink/reachable_netlink_utils_common.c is BSD-2-Clause
# -devel related licenses:
# src/docs/show-help-files/_build/text/_static/jquery.js is MIT
# docs/_build/html/_static/js/html5shiv.min.js is MIT OR GPL-2.0-or-later
# docs/_build/html/_static/css/fonts/* are (OFL-1.1 OR MIT)
License:        BSD-3-Clause-Open-MPI AND BSD-2-Clause
URL:            https://github.com/openpmix/%{name}
Source0:        https://github.com/openpmix/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.bz2
# Fix loss of hardening flags (including CET). Submitted as:
# https://github.com/openpmix/prrte/pull/2776
# Obsoleted by upstream removal of flex-based parser
# in 11 commits f9ee7c5d57b8..cfc373e95c83 on master,
# which were then backported to the "v5.0" branch, but not older branches.
Patch0:         prrte-fix-cflags-before-picky.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  hwloc-devel
BuildRequires:  libevent-devel
BuildRequires:  pmix-devel >= 4.2.2
# For pmixcc - https://bugzilla.redhat.com/show_bug.cgi?id=2078048
BuildRequires:  pmix-tools
BuildRequires:  perl-interpreter
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

# openmpi, pmix no longer support 32-bit platforms
ExcludeArch:    %{ix86}

%description
PRRTE is the PMIx Reference Run Time Environment.

The project is formally referred to in documentation by "PRRTE", and
the GitHub repository is "openpmix/%{name}".

However, we have found that most users do not like typing the two
consecutive "r"s in the name. Hence, all of the internal API symbols,
environment variables, MCA frameworks, and CLI executables all use the
abbreviated "prte" (one "r", not two) for convenience.


%package        libs
Summary:        Libraries for %{name}

%description    libs
Runtime libraries for %{name}.


%package        devel
Summary:        Development files for %{name}
License:        BSD-3-Clause-Open-MPI AND BSD-2-Clause AND MIT AND (MIT OR GPL-2.0-or-later) AND (OFL-1.1 OR MIT)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# For pmixcc, the target of the pcc symlink
Requires:       pmix-tools%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}-%{version}

# touch lexer sources to recompile them
find src -name \*.l -print -exec touch --no-create {} \;

# Remove “BSD with advertising” licensed qsort implementation, which was only
# needed to work around ancient Solaris bugs. The typedef keeps the translation
# unit from being empty.
echo '' > src/util/qsort.h
echo 'typedef int x;' > src/util/qsort.c

# Patch0 touches configure.ac-derived files; regenerate the build system.
./autogen.pl


%build
# Install into openmpi dir to avoid conflict with putty
# https://bugzilla.redhat.com/show_bug.cgi?id=2247407
%configure \
    --sysconfdir=%{_sysconfdir}/prte \
    --bindir=%{_libdir}/openmpi/bin \
    --mandir=%{_libdir}/openmpi/share/man \
    --disable-static \
    --disable-silent-rules \
    --enable-shared \
    --with-sge \
    --with-pmix=%{_prefix}

%make_build


%install
%make_install

# remove libtool archives
find %{buildroot} -name '*.la' -delete

# remove Sphinx's own incremental-build cache markers, not useful in the
# installed docs
rm %{buildroot}%{_docdir}/%{name}/html/.buildinfo*


%check
%make_build check


%files
%doc README.md
%{_libdir}/openmpi/bin/prte
%{_libdir}/openmpi/bin/prte_info
%{_libdir}/openmpi/bin/prted
%{_libdir}/openmpi/bin/prterun
%{_libdir}/openmpi/bin/prun
%{_libdir}/openmpi/bin/pterm
%{_libdir}/openmpi/share/man/man1/*.1*
%{_libdir}/openmpi/share/man/man5/*.5*

%files libs
%license LICENSE
%dir %{_sysconfdir}/prte
%config(noreplace) %{_sysconfdir}/prte/*
%{_datadir}/prte/
%{_libdir}/lib%{name}.so.3*

%files devel
%{_libdir}/openmpi/bin/pcc
%{_docdir}/prrte/
%{_includedir}/prte*.h
%{_includedir}/prte/
%{_libdir}/lib%{name}.so


%changelog
%autochangelog
