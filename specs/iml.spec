%bcond autoreconf 1

Name:           iml
Version:        1.0.5
%global so_version 0
Release:        %autorelease
Summary:        Finds solutions to systems of linear equations over integers

# Actual license of source files is BSD-3-Clause, as documented in header
# comments. The source archive includes a license file COPYING that contains
# GPLv2 text, but the only files in the archive with that license belong to the
# Autotools build system. This was clarified by email; see Source1.
#
# On 12/10/21 13:32, Arne Storjohann wrote:
# > Hi Ben,
# >
# > Our intention was to go with a BSD-style license, the one in the source
# > code files.
# > […]
License:        BSD-3-Clause
# The following files with other licenses belong to the build system and do not
# affect the license of the binary RPMs:
#
# FSFUL AND BSD-3-Clause:
# (BSD-3-Clause because it is derived from configure.ac)
#   - configure
# FSFUL AND FSFULLR AND GPL-2.0-or-later WITH Libtool-exception:
#   - config/libtool.m4
# FSFULLR:
#   - aclocal.m4
#   - config/ltoptions.m4
#   - config/ltsugar.m4
#   - config/ltversion.m4,
#   - config/lt~obsolete.m4
# GPL-2.0-or-later:
#   - bootstrap
# GPL-2.0-or-later WITH Autoconf-exception-generic:
#   - compile
#   - depcomp
#   - missing
#   - config/compile,
#   - config/depcomp
#   - config/missing
# GPL-2.0-or-later WITH Libtool-exception:
#   - ltmain.sh
#   - config/ltmain.sh
# GPL-3.0-or-later WITH Autoconf-exception-generic:
#   - config.guess
#   - config.sub
#   - config/config.guess
#   - config/config.sub
# X11:
#   - install-sh
#   - config/install-sh
SourceLicense:  %{shrink:
                %{license} AND
                FSFUL AND
                FSFULLR AND
                GPL-2.0-or-later AND
                GPL-2.0-or-later WITH Autoconf-exception-generic AND
                GPL-2.0-or-later WITH Libtool-exception AND
                GPL-3.0-or-later WITH Autoconf-exception-generic AND
                X11
                }
URL:            https://cs.uwaterloo.ca/~astorjoh/iml.html
Source0:        https://cs.uwaterloo.ca/~astorjoh/iml-%{version}.tar.bz2
Source1:        iml-license-clarification.eml

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  make

%if %{with autoreconf}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif

BuildRequires:  gmp-devel
BuildRequires:  pkgconfig(flexiblas)

%description
IML provides efficient routines to compute exact solutions to dense systems of
linear equations over the integers. The following functionality is provided:
  • Nonsingular rational system solving.
  • Compute the right nullspace of an integer matrix.
  • Certified linear system solving.


%package        devel
Summary:        Development files for iml

Requires:       iml%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}
Requires:       flexiblas-devel%{?_isa}

%description    devel
The iml-devel package contains libraries and header files for developing
applications that use iml.


%prep
%autosetup
cp -p '%{SOURCE1}' .
awk  '/Copyright notice/ {n=1}; n && /\*\// {n=0}; n' src/iml.h |
  sed -r 's/^ \* ?//' > LICENSE
rm -v cblas.h


%conf
%if %{with autoreconf}
autoreconf --force --install --verbose
%endif

%configure \
  --enable-shared \
  --disable-static \
  --with-cblas="$(pkgconf --libs flexiblas)" \
  --with-cblas-include="$(pkgconf --cflags flexiblas | sed -r 's/^-I//')"

# Get rid of undesirable hardcoded rpaths; work around libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool


%build
%make_build


%install
%make_install

# Remove libtool library file
find '%{buildroot}' -type f -name '*.la' -print -delete
# This contains the files “liblink” and “libroutines”, which are actually
# documentation and should be installed in a documentation directory.
rm -vrf '%{buildroot}%{_datadir}/iml'


%check
LD_LIBRARY_PATH="${PWD}/src/.libs" %make_build check


%files
%license LICENSE iml-license-clarification.eml
%doc AUTHORS
%doc README
%{_libdir}/libiml.so.%{so_version}{,.*}


%files devel
%doc doc/liblink
%doc doc/libroutines
%doc examples/
%{_includedir}/iml.h
%{_libdir}/libiml.so


%changelog
%autochangelog
