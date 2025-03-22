Name:           flint
Version:        3.2.1
Release:        %autorelease
Summary:        Fast Library for Number Theory

# LGPL-3.0-or-later: the project as a whole
# LGPL-2.1-or-later: src/longlong.h, src/fmpz/is_perfect_power.c,
#   src/generic_files/clz_tab.c, src/mpn_extras/get_d.c
# GPL-2.0-or-later: src/dirichlet/char_index.c, src/dirichlet/index_char.c
# LGPL-3.0-or-later OR GPL-2.0-or-later: src/mpn_extras/asm-defs.m4,
#   src/mpn_extras/broadwell/x86_64-defs.m4
# BSD-2-Clause: src/bernoulli/mod_p_harvey.c
License:        LGPL-3.0-or-later AND LGPL-2.1-or-later AND GPL-2.0-or-later AND (LGPL-3.0-or-later OR GPL-2.0-or-later) AND BSD-2-Clause
URL:            https://flintlib.org/
VCS:            git:https://github.com/flintlib/flint.git
Source:         https://flintlib.org/download/%{name}-%{version}.tar.gz

BuildRequires:  flexiblas-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  ntl-devel
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  tex(latex)

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# This can be removed when F43 reaches EOL
Obsoletes:      antic < 3.0.0
Obsoletes:      arb < 3.0.0
Obsoletes:      arb-doc < 3.0.0
Obsoletes:      flint-static < 3.0.0
Provides:       antic = %{version}-%{release}
Provides:       arb = %{version}-%{release}
Provides:       arb-doc = %{version}-%{release}
Provides:       flint-static = %{version}-%{release}

%description
FLINT is a C library for doing number theory, written by William Hart
and David Harvey.


%package        devel
Summary:        Development files for FLINT
Requires:       %{name}%{?_isa} = %{version}-%{release}

# This can be removed when F43 reaches EOL
Obsoletes:      antic-devel < 3.0.0
Provides:       antic-devel = %{version}-%{release}
Obsoletes:      arb-devel < 3.0.0
Provides:       arb-devel = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%conf
fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# sanitize header files
ln -sf $PWD flint
# sanitize references to external headers
for fil in $(find src -name \*.c -o -name \*.h -o -name \*.in); do
  sed -ri.orig 's/"((cblas|gc|gmp|math|mpfr|string)\.h)"/<\1>/' $fil
  fixtimestamp $fil
done
# sanitize references to project headers
for fil in $(find src -name \*.c -o -name \*.h); do
  sed -ri.orig 's@"(\.\./)?([^"]+\.h])"@<flint/\2>@' $fil
  fixtimestamp $fil
done
# "

# Use the classic sphinx theme
sed -i "s/'default'/'classic'/" doc/source/conf.py

# Look for flexiblas
sed -i 's/openblas/flexiblas/' configure


%build
# FLINT builds and passes all tests without this using GCC <= 14
# Tests fail with incorrect answers using GCC >= 15.0
CFLAGS='%{build_cflags} -fno-strict-aliasing'
CXXFLAGS='%{build_cxxflags} -fno-strict-aliasing'
%configure \
  --disable-arch \
  --disable-static \
  --with-blas-include=%{_includedir}/flexiblas \
  --with-ntl-include=%{_includedir}/NTL
%make_build

# Build the documentation
make -C doc html


%install
%make_install


%check
export FLEXIBLAS=netlib
make check


%files
%doc AUTHORS
%doc README.md
%license COPYING COPYING.LESSER
%{_libdir}/libflint.so.20*


%files devel
%doc doc/build/html
%{_includedir}/flint/
%{_libdir}/libflint.so
%{_libdir}/pkgconfig/flint.pc


%changelog
%autochangelog
