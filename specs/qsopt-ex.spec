# Upstream fixed many bugs after the 2.5.10.3 release, but never tagged a new
# release.  Build from git until a new release is made.
%global commit  e5d498fde468e4669a3fbc4736e5d3b878e8c148
%global date    20170729
%global forgeurl https://github.com/jonls/qsopt-ex

# See the Debian version: https://github.com/martinjos/qsopt-ex

Name:           qsopt-ex
Version:        2.5.10.3
Summary:        Exact linear programming solver

%forgemeta

# GPL-3.0-or-later: the project as a whole.  However, many source files contain
# license text for LGPL-2.1-or-later.
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Release:        %autorelease
URL:            https://www.math.uwaterloo.ca/~bico/qsopt/ex/
VCS:            git:%{forgeurl}.git
Source:         %{forgesource}
# Silence a runtime warning about trying to free a NULL pointer
Patch:          %{name}-free-warning.patch
# Silence a message that should only be printed with GMP usage statistics
Patch:          %{name}-silence-mempool-log.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(zlib)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
QSopt_ex is an exact linear programming solver.  This is a fork of the
version originally released by Daniel Espinoza et al.  The goal of the
fork is to update the software, and in particular the build system, to
be more friendly.  In addition, the external dependencies have been
reduced.

%package        libs
Summary:        Exact linear programming solver library

%description    libs
This package contains a library interface to the QSopt_ex exact linear
programming solver.

%package        devel
Summary:        Development files for %{name}-libs
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
This package contains header files and library links for developing
applications that use QSopt_ex.

%prep
%forgeautosetup -p1

%conf
# Update obsolete macros
sed -i '/AC_HEADER_STDC/d;/AC_HEADER_TIME/d;/AC_TYPE_SIGNAL/d' configure.ac
sed -i 's/AC_PROG_LIBTOOL/LT_INIT/' configure.ac
autoupdate -f

# Generate the configure script
autoreconf -fiv .

%build
%configure --disable-debug --disable-static --enable-shared
%make_build
help2man -N --version-string=%{version} --no-discard-stderr esolver/esolver \
  -n 'Exact linear programming solver' > esolver.1

%install
%make_install

# Avoid name collision with the lis-bin package
mv %{buildroot}%{_bindir}/esolver %{buildroot}%{_bindir}/qsopt-ex-esolver

# Install man page under the new name
mkdir -p %{buildroot}%{_mandir}/man1
sed -e 's/esolver/qsopt-ex-&/g;s/ESOLVER/QSOPT-EX-&/g' \
    -e 's/Using QSopt_ex.*/Exact Mixed Integer Linear Solver/' \
    esolver.1 > %{buildroot}%{_mandir}/man1/qsopt-ex-esolver.1

%check
make check

%files
%{_bindir}/qsopt-ex-esolver
%{_mandir}/man1/qsopt-ex-esolver.1*

%files libs
%doc NEWS.md README.md
%license License.txt
%{_libdir}/libqsopt_ex.so.2*

%files devel
%{_includedir}/qsopt_ex/
%{_libdir}/libqsopt_ex.so

%changelog
%autochangelog
