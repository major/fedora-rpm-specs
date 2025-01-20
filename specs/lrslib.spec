# TODO: Package mplrs, the MPI version.

Name:           lrslib
Version:        7.3
Release:        %autorelease
Summary:        Reverse search for vertex enumeration/convex hull problems

%global upver 0%(sed 's/\\.//' <<< %{version})

License:        GPL-2.0-or-later
URL:            https://cgm.cs.mcgill.ca/~avis/C/lrs.html
Source0:        https://cgm.cs.mcgill.ca/~avis/C/%{name}/archive/%{name}-%{upver}.tar.gz
Source1:        lrslib.module.in
# This patch was sent upstream on 31 May 2011.  It fixes some miscellaneous
# bugs.
Patch:          %{name}-fixes.patch
# This patch was sent upstream on 18 Jan 2025.  It fixes various constructs
# that are not compatible with C23.
Patch:          %{name}-c23.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  environment(modules)
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel

Requires:       environment(modules)

%description
%{name} is a self-contained ANSI C implementation as a callable library
of the reverse search algorithm for vertex enumeration/convex hull
problems and comes with a choice of three arithmetic packages.  Input
file formats are compatible with Komei Fukuda's cdd package (cddlib).
All computations are done exactly in either multiple precision or fixed
integer arithmetic.  Output is not stored in memory, so even problems
with very large output sizes can sometimes be solved.

%package devel
Summary:        Header files and libraries for developing with %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}

%description devel
Header files and libraries for developing with %{name}.

%package utils
Summary:        Sample programs that use %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description utils
Sample programs that use %{name}.

%prep
%autosetup -n %{name}-%{upver}

# Remove extraneous executable bits
find . -type f -perm /0111 -exec chmod a-x {} +
chmod a+x scripts/*

%build
# The Makefile is too primitive to use.  For one thing, it only builds
# binaries, not libraries.  We do our own thing here.
# Recent changes to the Makefile make it less primitive, but it still does not
# work well for building on a mixture of 32-bit and 64-bit architectures.

# Upstream wants to use 1.0.0 as the soname version number for now.
%global sover 1
%global ver 1.0.0

ARITH=$(ls -1d lrsarith-*)
CFLAGS="%{build_cflags} -fopenmp -DPLRS -DMA -I . -I $ARITH"
GMPCFLAGS="$CFLAGS -DGMP"
INTCFLAGS="$CFLAGS -DSAFE -DLRSLONG"

# Build the individual objects
gcc $GMPCFLAGS -fPIC -c -o $ARITH/lrsgmp.o $ARITH/lrsgmp.c
gcc $INTCFLAGS -fPIC -c -o $ARITH/lrslong1.o $ARITH/lrslong.c
gcc $GMPCFLAGS -fPIC -c -o lrslibgmp.o lrslib.c
gcc $INTCFLAGS -fPIC -c -o lrslib1.o lrslib.c
gcc $GMPCFLAGS -fPIC -c -o lrsdriver.o lrsdriver.c
gcc $GMPCFLAGS -fPIC -c -o lrsnashlib.o lrsnashlib.c
%if 0%{?__isa_bits} == 64
gcc $INTCFLAGS -DB128 -fPIC -c -o $ARITH/lrslong2.o $ARITH/lrslong.c
gcc $INTCFLAGS -DB128 -fPIC -c -o lrslib2.o lrslib.c
%endif

# Build the library
gcc $CFLAGS %{build_ldflags} -fPIC -shared -Wl,-soname,liblrs.so.%{sover} \
  -o liblrs.so.%{ver} \
%if 0%{?__isa_bits} == 64
  $ARITH/lrslong2.o lrslib2.o \
%endif
  $ARITH/lrsgmp.o $ARITH/lrslong1.o lrslibgmp.o lrslib1.o \
  lrsdriver.o lrsnashlib.o -lgmp
ln -s liblrs.so.%{ver} liblrs.so.%{sover}
ln -s liblrs.so.%{sover} liblrs.so

# Build the binaries
LDFLAGS='%{build_ldflags} -L . -llrs -lgmp'
%if 0%{?__isa_bits} == 64
gcc $INTCFLAGS -DB128 lrs.c -o lrs $LDFLAGS
gcc $INTCFLAGS -DB128 lrsnash.c -o lrsnash2 $LDFLAGS
%else
gcc $INTCFLAGS lrs.c -o lrs $LDFLAGS
%endif
gcc $GMPCFLAGS lrs.c -o lrsgmp $LDFLAGS
gcc $GMPCFLAGS lrsnash.c -o lrsnash $LDFLAGS
gcc $INTCFLAGS lrsnash.c -o lrsnash1 $LDFLAGS
gcc $GMPCFLAGS 2nash.c -o 2nash $LDFLAGS
gcc $GMPCFLAGS buffer.c -o buffer $LDFLAGS
gcc $GMPCFLAGS hvref.c -o hvref $LDFLAGS
gcc $GMPCFLAGS inedel.c -o inedel $LDFLAGS
gcc $GMPCFLAGS polyv.c -o polyv $LDFLAGS
gcc $GMPCFLAGS setupnash.c -o setupnash $LDFLAGS
gcc $GMPCFLAGS setupnash2.c -o setupnash2 $LDFLAGS
gcc $GMPCFLAGS -DLRSMP -Dcopy=copy_dict_1 -Dlrs_mp_init=lrs_mp_init_1 \
  -Dpmp=pmp_1 -Drattodouble=rattodouble_1 -Dreadrat=readrat_1 rat2float.c \
  -o rat2float $LDFLAGS
gcc $GMPCFLAGS float2rat.c -o float2rat $LDFLAGS
gcc $GMPCFLAGS $ARITH/fixed.c -o fixed $LDFLAGS

%install
ARITH=$(ls -1d lrsarith-*)

# Install the library
mkdir -p %{buildroot}%{_libdir}
cp -a liblrs*.so* %{buildroot}%{_libdir}
chmod 0755 %{buildroot}%{_libdir}/lib*.so.%{ver}

# Install the environment-modules file
mkdir -p %{buildroot}%{_modulesdir}
sed 's,@LIBDIR@,'%{_libdir}/%{name}',g;' < %{SOURCE1} \
  > %{buildroot}%{_modulesdir}/%{name}-%{_arch}

# Install the binaries
mkdir -p %{buildroot}%{_libdir}/%{name}/bin
install -p -m 0755 lrs lrsgmp lrsnash lrsnash? 2nash buffer hvref inedel polyv \
  setupnash setupnash2 rat2float float2rat fixed \
  %{buildroot}%{_libdir}/%{name}/bin
ln -s lrs %{buildroot}%{_libdir}/%{name}/bin/fel
ln -s lrs %{buildroot}%{_libdir}/%{name}/bin/minrep
ln -s lrs %{buildroot}%{_libdir}/%{name}/bin/redund

# Install the header files, but fix up the include directives.
mkdir -p %{buildroot}%{_includedir}/%{name}
sed -r 's|"(lrs.*\.h)"|<lrslib/\1>|' lrslib.h > \
    %{buildroot}%{_includedir}/%{name}/lrslib.h
touch -r lrslib.h %{buildroot}%{_includedir}/%{name}/lrslib.h

sed -r 's|"(lrs.*\.h)"|<lrslib/\1>|' $ARITH/lrsarith.h > \
    %{buildroot}%{_includedir}/%{name}/lrsarith.h
touch -r $ARITH/lrsarith.h %{buildroot}%{_includedir}/%{name}/lrsarith.h

sed -e 's|"gmp.h"|<gmp.h>|' $ARITH/lrsgmp.h > \
    %{buildroot}%{_includedir}/%{name}/lrsgmp.h
touch -r $ARITH/lrsgmp.h %{buildroot}%{_includedir}/%{name}/lrsgmp.h

sed -e 's|"lrsrestart.h"|<lrslib/lrsrestart.h>|' lrsdriver.h > \
    %{buildroot}%{_includedir}/%{name}/lrsdriver.h
touch -r lrsdriver.h %{buildroot}%{_includedir}/%{name}/lrsdriver.h

cp -p $ARITH/lrslong.h $ARITH/lrsmp.h lrsnashlib.h lrsrestart.h \
  %{buildroot}%{_includedir}/%{name}

# Install the man pages
mkdir -p %{buildroot}%{_mandir}
cp -a man/man1 %{buildroot}%{_mandir}
cp -a man/man5 %{buildroot}%{_mandir}
cp -p lrsarith-*/man/man5/lrsarith.5 %{buildroot}%{_mandir}/man5

%files
%doc README
%license COPYING
%{_libdir}/liblrs.so.1
%{_libdir}/liblrs.so.1.*

%files devel
%doc chdemo.c lpdemo.c lpdemo1.c lpdemo2.c nashdemo.c vedemo.c
%{_includedir}/%{name}
%{_libdir}/liblrs.so
%{_mandir}/man5/*.5*

%files utils
%{_libdir}/%{name}/
%{_mandir}/man1/*.1*
%{_modulesdir}/%{name}-%{_arch}

%changelog
%autochangelog
