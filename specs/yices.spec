%global giturl  https://github.com/SRI-CSL/yices2

Name:           yices
Version:        2.6.5
Release:        %autorelease
Summary:        SMT solver

# The yices code is GPL-3.0-or-later.  The cudd code is BSD-3-Clause.
License:        GPL-3.0-or-later AND BSD-3-Clause
URL:            http://yices.csl.sri.com/
VCS :           git:%{giturl}.git
Source0:        %{giturl}/archive/Yices-%{version}.tar.gz
# The CUDD web site disappeared in 2018.  The Fedora package was retired in 2019
# when there were no more Fedora users.  Instead of resurrecting the package for
# the sole use of yices, we bundle a snapshot of the last released version.
Source1:        https://github.com/ivmai/cudd/archive/cudd-3.0.0.tar.gz
# Adapt to newer versions of cryptominisat
Patch:          %{name}-cryptominisat.patch
# Get rid of an implicit-int function declaration in a configure check.
Patch:          implicit-int.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cadical-devel
BuildRequires:  cryptominisat-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gperf
BuildRequires:  kissat-devel
BuildRequires:  latexmk
BuildRequires:  libpoly-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  tex(latex)

# See Source1 comment
Provides:       bundled(cudd) = 3.0.0

%description
Yices 2 is an efficient SMT solver that decides the satisfiability of
formulas containing uninterpreted function symbols with equality, linear
real and integer arithmetic, bitvectors, scalar types, and tuples.

Yices 2 can process input written in the SMT-LIB notation (both versions
2.0 and 1.2 are supported).

Alternatively, you can write specifications using the Yices 2
specification language, which includes tuples and scalar types.

Yices 2 can also be used as a library in other software.

%package devel
Summary:        Development files for yices
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}

%description devel
This package contains the header files necessary for developing programs
which use yices.

%package tools
Summary:        Command line tools that use the yices library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
Command line tools that use the yices library.

%package doc
# The content is GPL-3.0-or-later.  Other licenses are due to files copied in
# by Sphinx and due to fonts embedded in PDFs.
# Sphinx file licenses:
# _static/_sphinx_javascript_frameworks_compat.js: BSD-2-Clause
# _static/basic.css: BSD-2-Clause
# _static/classic.css: BSD-2-Clause
# _static/default.css: BSD-2-Clause
# _static/doctools.js: BSD-2-Clause
# _static/documentation_options.js: BSD-2-Clause
# _static/epub.css: BSD-2-Clause
# _static/file.png: BSD-2-Clause
# _static/jquery*.js: MIT
# _static/language_data.js: BSD-2-Clause
# _static/minus.png: BSD-2-Clause
# _static/plus.png: BSD-2-Clause
# _static/searchtools.js: BSD-2-Clause
# _static/sidebar.js: BSD-2-Clause
# _static/underscore*.js: MIT
# genindex.html: BSD-2-Clause
# search.html: BSD-2-Clause
# searchindex.js: BSD-2-Clause
#
# Font licenses:
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# DejaVu: LPPL-1.3a
# LaTeX: LPPL-1.3a
# Nimbus: AGPL-3.0-only
License:        GPL-3.0-or-later AND BSD-2-Clause AND MIT AND OFL-1.1-RFN AND Knuth-CTAN AND LPPL-1.3a AND AGPL-3.0-only
Summary:        Documentation for yices
BuildArch:      noarch

%description doc
This package contains yices documentation.

%prep
%autosetup -n yices2-Yices-%{version} -a 1 -p1

%conf
# Do not try to avoid -fstack-protector
sed -i 's/@NO_STACK_PROTECTOR@//' make.include.in

# Do not override our build flags
sed -i 's/ -O3//;s/ -fomit-frame-pointer//' src/Makefile tests/unit/Makefile

# Use $SOURCE_DATE_EPOCH (or current date)
sed -i "s/^now=.*/now=$(date +%Y-%m-%d ${SOURCE_DATE_EPOCH:+--date=@$SOURCE_DATE_EPOCH})/" \
  utils/make_source_version

# Generate the configure scripts
autoreconf -fi
cd cudd-cudd-3.0.0
autoreconf -fi
cd -

# Fix end of line encodings
sed -i 's/\r//' examples/{jinpeng,problem_with_input}.ys

# Fix permissions
sed -i 's/cp/install -m 0644/' utils/make_source_version

%build
# Build cudd
cd cudd-cudd-3.0.0
%configure CFLAGS='%{build_cflags} -fPIC' CXXFLAGS='%{build_cxxflags} -fPIC'
%make_build
cd -

#bv64_interval_abstraction depends on wrapping for signed overflow
export CFLAGS='%{build_cflags} -fwrapv'
export CXXFLAGS='%{build_cxxflags} -fwrapv'
export CPPFLAGS="-I$PWD/cudd-cudd-3.0.0/cudd -DHAVE_CADICAL -DHAVE_CRYPTOMINISAT -DHAVE_KISSAT"
export LDFLAGS="%{build_ldflags} -L$PWD/cudd-cudd-3.0.0/cudd/.libs"
export LIBS='-lcadical -lcryptominisat5 -lkissat'
%configure --enable-mcsat

guess=$(./config.guess)
if [ "%{_host}" != "$guess" ]; then
  mv configs/make.include.%{_host} configs/make.include.${guess}
fi
%make_build MODE=debug

# Build the manual
make doc

# Build the interface documentation
make -C doc/sphinx html
rm doc/sphinx/build/html/.buildinfo

%install
make install prefix=%{buildroot}%{_prefix} exec_prefix=%{buildroot}%{_prefix} \
     bindir=%{buildroot}%{_bindir} libdir=%{buildroot}%{_libdir} \
     includedir=%{buildroot}%{_includedir}/%{name} MODE=debug
rm -f %{buildroot}%{_libdir}/libyices.a
mkdir -p %{buildroot}%{_mandir}/man1
cp -p doc/*.1 %{buildroot}%{_mandir}/man1

%check
make check MODE=debug

%files
%doc doc/SMT-LIB-LANGUAGE doc/YICES-LANGUAGE
%license copyright.txt LICENSE.txt
%{_libdir}/libyices.so.2*

%files devel
%{_includedir}/%{name}/
%{_libdir}/libyices.so

%files tools
%{_bindir}/yices
%{_bindir}/yices-sat
%{_bindir}/yices-smt
%{_bindir}/yices-smt2
%{_mandir}/man1/yices.1*
%{_mandir}/man1/yices-sat.1*
%{_mandir}/man1/yices-smt.1*
%{_mandir}/man1/yices-smt2.1*

%files doc
%doc doc/manual/manual.pdf doc/sphinx/build/html examples
%license copyright.txt LICENSE.txt

%changelog
%autochangelog
