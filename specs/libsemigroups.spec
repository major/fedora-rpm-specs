# NOTE: The documentation is no longer built because Fedora does not have
# hugo-book or doxygen-awesome-css.

# TODO: Unbundle backward-cpp, catch2, magic_enum, and rx-ranges.

%global giturl  https://github.com/libsemigroups/libsemigroups

Name:           libsemigroups
Version:        3.5.3
Release:        %autorelease
Summary:        C++ library for semigroups and monoids

# libsemigroups itself is GPL-3.0-or-later.
# TextFlow is BSL-1.0.
# magic_enum and rx-ranges are MIT.
# All other licenses are due to use of eigen3.
License:        GPL-3.0-or-later AND BSL-1.0 AND MIT AND MPL-2.0 AND BSD-3-Clause AND Apache-2.0
URL:            https://libsemigroups.readthedocs.io/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl(open)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(fmt)

# HPCombi cannot yet be used on x86_64.  See below.
%ifarch %{arm64}
BuildRequires:  pkgconfig(hpcombi)
%endif

# This can be removed when F48 reaches EOL
Obsoletes:      %{name}-doc < 3.0.0
Provides:       %{name}-doc = %{version}-%{release}

%description
Libsemigroups is a C++ library for semigroups and monoids; it is partly based
on "Algorithms for computing finite semigroups", "Expository Slides", and
Semigroupe 2.01 by Jean-Eric Pin.

The libsemigroups library is used in the Semigroups package for GAP.

Some of the features of Semigroupe 2.01 are not yet implemented in
libsemigroups; this is a work in progress.  Missing features include those
for:

- Green's relations, or classes
- finding a zero
- minimal ideal, principal left/right ideals, or indeed any ideals
- inverses
- local submonoids
- the kernel
- variety tests.
These will be included in a future version.

Libsemigroups performs roughly the same as Semigroupe 2.01 when there is a
known upper bound on the size of the semigroup being enumerated, and this is
used to initialize the data structures for the semigroup; see
libsemigroups::Semigroup::reserve for more details.  Note that in Semigroupe
2.01 it is always necessary to provide such an upper bound, but in
libsemigroups it is not.

Libsemigroups also has some advantages over Semigroupe 2.01:
- there is a (hopefully) convenient C++ API, which makes it relatively easy to
  create and manipulate semigroups and monoids
- there are some multithreaded methods for semigroups and their congruences
- you do not have to know/guess the size of a semigroup or monoid before you
  begin
- libsemigroups supports more types of elements than Semigroupe 2.01
- it is relatively straightforward to add support for further types of
  elements and semigroups
- it is possible to enumerate a certain number of elements of a semigroup or
  monoid (say if you are looking for an element with a particular property),
  to stop, and then to start the enumeration again at a later point
- you can instantiate as many semigroups and monoids as you can fit in memory
- it is possible to add more generators after a semigroup or monoid has been
  constructed, without losing or having to recompute any information that was
  previously known
- libsemigroups contains rudimentary implementations of the Todd-Coxeter and
  Knuth-Bendix algorithms for finitely presented semigroups, which can also be
  used to compute congruences of a (not necessarily finitely presented)
  semigroup or monoid.

%package devel
Summary:        Headers files for developing with %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for developing applications that use %{name}.

%prep
%autosetup -p1

# Do not override Fedora build flags
sed -i 's/ -O3//' Makefile.am

# Fix the version number
echo %{version} > .VERSION

%conf
# Generate the configure script
autoreconf -fi .

# Hpcombi is an x86-specific library that uses SSE and AVX instructions.
# It is available in Fedora, but we cannot assume the availability of AVX.
# We will use it when microarchitecture support is nailed down.
%configure \
    --disable-silent-rules \
    --disable-static \
%ifarch %{arm64}
    --enable-hpcombi \
%else
    --disable-hpcombi \
%endif
    --enable-eigen \
    --with-external-eigen \
    --enable-fmt \
    --with-external-fmt

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%build
%make_build

%install
%make_install

# Do not bundle the eigen3 headers
rm -fr %{buildroot}%{_includedir}/libsemigroups/Eigen

# Do not bundle the fmt headers
rm -fr %{buildroot}%{_includedir}/libsemigroups/fmt

%check
LD_LIBRARY_PATH=$PWD/.libs make check

%files
%doc README.md
%license LICENSE
%{_libdir}/%{name}.so.3{,.*}

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
