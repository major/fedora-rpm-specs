%global giturl  https://github.com/algebraic-solving/msolve

Name:           msolve
Version:        0.7.3
Release:        %autorelease
Summary:        Polynomial System Solving through Algebraic Methods

# GPL-2.0-or-later: The project as a whole
# LGPL-2.1-or-later:
# - src/crt/longlong.h
# - src/crt/ulong_extras.h
# - src/fglm/berlekamp_massey.c
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://msolve.lip6.fr/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz
# Detect AVX2 support at runtime instead of compile time
Patch:          %{name}-avx2.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  flint-devel
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(mpfr)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%global _desc %{expand:
msolve is an open source C library implementing computer algebra
algorithms for solving polynomial systems (with rational coefficients or
coefficients in a prime field).

Currently, with msolve, you can basically solve multivariate polynomial
systems.  This encompasses:
- the computation of Groebner bases
- real root isolation of the solutions to polynomial systems
- the computation of the dimension and the degree of the solution set
  and many other things you can do using msolve.}

%description %_desc

This package contains a command line tool to access the msolve
functionality.

%package        libs
Summary:        Library for Polynomial System Solving through Algebraic Methods

%description    libs %_desc

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}

%description    devel
Header files and library links for developing applications that use
msolve.

%prep
%autosetup -p1

%conf
# Fix the pkgconfig file
sed -i 's/ -lflint -lmpfr -lgmp/\nLibs.private:&/' msolve.pc.in

# Generate the configure script
./autogen.sh

%build
%configure --enable-openmp --disable-static

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/*.la

# Install the header files, swizzling #include directives along the way
mkdir -p %{buildroot}%{_includedir}/msolve
cd src/msolve
for h in *.h; do
  sed -e '/#include/s,"\.\./\(neogb/[[:alnum:]_-]*\.h\)",<\1>,' \
      -e '/#include/s,"\([[:alnum:]_-]*\.h\)",<msolve/\1>,' $h > \
    %{buildroot}%{_includedir}/msolve/$h
  touch -r $h %{buildroot}%{_includedir}/msolve/$h
done
cd -

mkdir -p %{buildroot}%{_includedir}/neogb
cd src/neogb
for h in *.h; do
  sed '/#include/s,"\([[:alnum:]_-]*\.h\)",<neogb/\1>,' $h > \
    %{buildroot}%{_includedir}/neogb/$h
  touch -r $h %{buildroot}%{_includedir}/neogb/$h
done
cd -

# Create a man page
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_mandir}/man1
help2man -N -v %{version} %{buildroot}%{_bindir}/msolve \
  -n 'Polynomial System Solving through Algebraic Methods' \
  > %{buildroot}%{_mandir}/man1/msolve.1

%check
make check

%files
%{_bindir}/msolve
%{_mandir}/man1/msolve.1*

%files libs
%doc AUTHORS README.md
%license COPYING
%{_libdir}/libmsolve.so.0*
%{_libdir}/libneogb.so.0*

%files devel
%{_includedir}/msolve/
%{_includedir}/neogb/
%{_libdir}/libmsolve.so
%{_libdir}/libneogb.so
%{_libdir}/pkgconfig/msolve.pc

%changelog
%autochangelog
