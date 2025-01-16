Name:           nauty
Version:        2.8.9
Release:        %autorelease
Summary:        Graph canonical labeling and automorphism group computation

%global nautytarver %(tr . _ <<< %{version})

# The projects as a whole is Apache-2.0.
# The bundled cliquer code in nautycliquer.c is GPL-2.0-or-later, but we patch
# it out.
# Other licenses are due to embedded fonts in the PDF manual.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
License:        Apache-2.0 AND Knuth-CTAN AND GPL-1.0-or-later
URL:            https://pallini.di.uniroma1.it/
Source:         https://pallini.di.uniroma1.it/%{name}%{nautytarver}.tar.gz

# Debian patch to fix the gt_numorbits declaration
Patch:          %{name}-fix-gt_numorbits.patch
# Use zlib-ng instead of invoking zcat through a pipe
Patch:          %{name}-zlib-dimacs2g.patch
# Debian patch to improve usage and help information
Patch:          %{name}-help2man.patch
# Link binaries with shared libraries instead of static libraries
Patch:          %{name}-shared.patch
# Detect availability of the popcnt instruction at runtime
Patch:          %{name}-popcnt.patch
# Unbundle cliquer
Patch:          %{name}-unbundle-cliquer.patch
# Fix incorrect printf format strings
Patch:          %{name}-format.patch
# Fix uninitialized variable warnings
Patch:          %{name}-uninitialized.patch
# Fix a function that can fall off the end
Patch:          %{name}-fall-off.patch

BuildRequires:  cliquer-devel
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(zlib-ng)

# Some version of planarity is bundled.  I do not know which version it is,
# but the interface is completely different from the one provided by Fedora's
# planarity package.
Provides:       bundled(planarity)

# The shortg program invokes sort.
Requires:       coreutils
Requires:       lib%{name}%{?_isa} = %{version}-%{release}

%description
Nauty and Traces are programs for computing automorphism groups of
graphs and digraphs.  (At present, Traces does not accept digraphs.)
They can also produce a canonical label.  They are written in a portable
subset of C, and run on a considerable number of different systems.

There is a small suite of programs called gtools included in the
package.  For example, geng can generate non-isomorphic graphs very
quickly.  There are also generators for bipartite graphs, digraphs, and
multigraphs, and programs for manipulating files of graphs in a compact
format.

%package     -n libnauty
License:        Apache-2.0
Summary:        Library for graph automorphism

%description -n libnauty
Nauty (No AUTomorphisms, Yes?) is a set of procedures for computing
automorphism groups of graphs and digraphs.  This package contains a
library of nauty procedures.

%package     -n libnauty-devel
License:        Apache-2.0
Summary:        Development files for libnauty
Requires:       lib%{name}%{?_isa} = %{version}-%{release}

%description -n libnauty-devel
This package contains files needed to develop programs that use libnauty.

%prep
%autosetup -p1 -n %{name}%{nautytarver}

%conf
# Remove the pregenerated makefile
rm -f makefile

# Avoid obsolescence warnings
sed -i 's/egrep/grep -E/' configure.ac

# Regenerate the configure script due to the patches
aclocal
autoreconf -fi

# Fix the pkgconfig file
sed -i 's,/usr/local,%{_prefix},' nauty.pc
if [ '%{_lib}' != 'lib' ]; then
    sed -i 's,/lib,/lib64,' nauty.pc
fi

%build
export CFLAGS='%{build_cflags} -fwrapv -I%{_includedir}/cliquer'
export LIBS='-lz-ng'
%configure \
    --enable-ansi \
    --enable-generic \
%ifarch %{ix86} x86_64
    --disable-popcnt \
    --enable-runtime-popcnt \
%endif
    --enable-tls

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

# FIXME: parallel building was broken in version 2.8.9
make

%install
%make_install

# We do not want the libtool archives or static archives
rm %{buildroot}%{_libdir}/*.{a,la}

# Generate the man pages
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_mandir}/man1
for f in %{buildroot}%{_bindir}/*; do
  help2man -N -o %{buildroot}%{_mandir}/man1/$(basename $f).1 \
    --version-string=%{version} $f
done

# Link identical executables
rm %{buildroot}%{_bindir}/pickg
ln -s countg %{buildroot}%{_bindir}/pickg

# Move the headers
mkdir -p %{buildroot}%{_includedir}/nauty
mv %{buildroot}%{_includedir}/*.h %{buildroot}%{_includedir}/nauty

%check
chmod a+x runalltests
LD_LIBRARY_PATH=$PWD/.libs PATH=$PWD:$PATH make check

%files
%doc README nug28.pdf
%{_bindir}/*g
%{_bindir}/*gL
%{_bindir}/dreadnaut
%{_bindir}/dretodot
%{_bindir}/hamheuristic
%{_bindir}/watercluster2
%{_mandir}/man1/*g.1*
%{_mandir}/man1/*gL.1*
%{_mandir}/man1/dreadnaut.1*
%{_mandir}/man1/dretodot.1*
%{_mandir}/man1/hamheuristic.1*
%{_mandir}/man1/watercluster2.1*

%files -n libnauty
%doc changes24-28.txt formats.txt
%license COPYRIGHT LICENSE-2.0.txt
%{_libdir}/libnauty-2.8.9.so
%{_libdir}/libnautyS-2.8.9.so
%{_libdir}/libnautyW-2.8.9.so
%{_libdir}/libnautyL-2.8.9.so
%{_libdir}/libnauty1-2.8.9.so
%{_libdir}/libnautyS1-2.8.9.so
%{_libdir}/libnautyW1-2.8.9.so
%{_libdir}/libnautyL1-2.8.9.so
%if 0%{?__isa_bits} == 64
%{_libdir}/libnautyQ-2.8.9.so
%{_libdir}/libnautyQ1-2.8.9.so
%endif

%files -n libnauty-devel
%doc schreier.txt
%{_includedir}/nauty/
%{_libdir}/pkgconfig/lib%{name}*.pc
%{_libdir}/libnauty.so
%{_libdir}/libnautyS.so
%{_libdir}/libnautyW.so
%{_libdir}/libnautyL.so
%{_libdir}/libnauty1.so
%{_libdir}/libnautyS1.so
%{_libdir}/libnautyW1.so
%{_libdir}/libnautyL1.so
%if 0%{?__isa_bits} == 64
%{_libdir}/libnautyQ.so
%{_libdir}/libnautyQ1.so
%endif

%changelog
%autochangelog
