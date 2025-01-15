%global giturl  https://github.com/cddlib/cddlib

Name:           cddlib
Epoch:          1
Version:        0.94m
Release:        %autorelease
Summary:        A library for generating all vertices in convex polyhedrons
License:        GPL-2.0-or-later
URL:            https://people.inf.ethz.ch/fukudak/cdd_home/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/%{version}/%{name}-%{version}.tar.gz
# Fix a segfault in blockelimination
Patch:          %{giturl}/commit/f83bdbc.patch

BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  tex(latex)

%description
The C-library cddlib is a C implementation of the Double Description 
Method of Motzkin et al. for generating all vertices (i.e. extreme points)
and extreme rays of a general convex polyhedron in R^d given by a system 
of linear inequalities:

   P = { x=(x1, ..., xd)^T :  b - A∙x ≥ 0 }

where A is a given m×d real matrix, b is a given m-vector
and 0 is the m-vector of all zeros.

The program can be used for the reverse operation (i.e. convex hull
computation). This means that one can move back and forth between 
an inequality representation and a generator (i.e. vertex and ray) 
representation of a polyhedron with cdd. Also, cdd can solve a linear
programming problem, i.e. a problem of maximizing and minimizing 
a linear function over P.


%package devel
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN
Summary:        Headers for cddlib
Requires:       gmp-devel%{?_isa}
Requires:       %{name}%{?_isa} = 1:%{version}-%{release}

%description devel
Include files for cddlib.


%package static
Summary:        Static libraries for cddlib

%description static
Static libraries for cddlib.


%package tools
Summary:        Sample binaries that use cddlib
Requires:       %{name}%{?_isa} = 1:%{version}-%{release}

%description tools
Sample binaries that use cddlib.


%prep
%autosetup -p1


%conf
# Fix the FSF's address
for f in $(find . -type f -exec grep -Fl '675 Mass' {} +); do
  sed -i.orig \
    's/675 Mass Ave, Cambridge, MA 02139/51 Franklin Street, Suite 500, Boston, MA  02110-1335/' \
    $f
  touch -r $f.orig $f
  rm -f $f.orig
done

# Force rebuilding of the documentation
rm -f doc/cddlibman.pdf


%build
%configure

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

# Need one more invocation of pdflatex to get cross references correct
pushd doc
pdflatex cddlibman
popd


%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

# Do not prematurely install documentation
rm -fr %{buildroot}%{_pkgdocdir}


%files
%doc AUTHORS ChangeLog
%license COPYING
%{_libdir}/libcdd.so.0*
%{_libdir}/libcddgmp.so.0*


%files devel
%doc doc/cddlibman.pdf examples*
%{_includedir}/cddlib
%{_libdir}/libcdd.so
%{_libdir}/libcddgmp.so
%{_libdir}/pkgconfig/%{name}.pc


%files static
%{_libdir}/libcdd.a
%{_libdir}/libcddgmp.a


%files tools
%{_bindir}/adjacency
%{_bindir}/adjacency_gmp
%{_bindir}/allfaces
%{_bindir}/allfaces_gmp
%{_bindir}/cddexec
%{_bindir}/cddexec_gmp
%{_bindir}/fourier
%{_bindir}/fourier_gmp
%{_bindir}/lcdd
%{_bindir}/lcdd_gmp
%{_bindir}/projection
%{_bindir}/projection_gmp
%{_bindir}/redcheck
%{_bindir}/redcheck_gmp
%{_bindir}/scdd
%{_bindir}/scdd_gmp
%{_bindir}/testcdd1
%{_bindir}/testcdd1_gmp
%{_bindir}/testcdd2
%{_bindir}/testcdd2_gmp
%{_bindir}/testlp1
%{_bindir}/testlp1_gmp
%{_bindir}/testlp2
%{_bindir}/testlp2_gmp
%{_bindir}/testlp3
%{_bindir}/testlp3_gmp
%{_bindir}/testshoot
%{_bindir}/testshoot_gmp

%changelog
%autochangelog
