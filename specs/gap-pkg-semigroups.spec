%global pkgname semigroups
%global giturl  https://github.com/semigroups/Semigroups

# The standard test suite now regularly consumes on the order of 30GB of
# memory.  This is more than the 32-bit builders can access, and more than even
# some of the 64-bit builders have available (depending on what else is running
# on the same machine).  We skip that test suite.  Brave package maintainers
# with sufficient RAM should build --with-bigtest.
%bcond bigtest 0

Name:           gap-pkg-%{pkgname}
Version:        5.4.0
Release:        %autorelease
Summary:        GAP methods for semigroups

License:        GPL-3.0-or-later
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://semigroups.github.io/Semigroups/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-datastructures
BuildRequires:  gap-pkg-digraphs-doc
BuildRequires:  gap-pkg-ferret
BuildRequires:  gap-pkg-genss
BuildRequires:  gap-pkg-grape
BuildRequires:  gap-pkg-images-doc
BuildRequires:  gap-pkg-io-doc
BuildRequires:  gap-pkg-orb
BuildRequires:  gap-pkg-smallsemi-doc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(libsemigroups)
BuildRequires:  tex(a4wide.sty)

Requires:       gap-pkg-datastructures%{?_isa}
Requires:       gap-pkg-digraphs%{?_isa}
Requires:       gap-pkg-genss
Requires:       gap-pkg-images
Requires:       gap-pkg-io%{?_isa}
Requires:       gap-pkg-orb%{?_isa}

Suggests:       gap-pkg-grape%{?_isa}

%description
This is a GAP package containing methods for semigroups, monoids, and
inverse semigroups, principally of transformations, partial
permutations, bipartitions, subsemigroups of regular Rees 0-matrix
semigroups, free inverse semigroups, free bands, and semigroups of
matrices over finite fields.

Semigroups contains more efficient methods than those available in the
GAP library (and in many cases more efficient than any other software)
for creating semigroups, monoids, and inverse semigroup, calculating
their Green's structure, ideals, size, elements, group of units, small
generating sets, testing membership, finding the inverses of a regular
element, factorizing elements over the generators, and many more.  It is
also possible to test if a semigroup satisfies a particular property,
such as if it is regular, simple, inverse, completely regular, and a
variety of further properties.

There are methods for finding congruences of certain types of
semigroups, the normalizer of a semigroup in a permutation group, the
maximal subsemigroups of a finite semigroup, and smaller degree partial
permutation representations of inverse semigroups.  There are functions
for producing pictures of the Green's structure of a semigroup, and for
drawing bipartitions.

%package doc
# The content is GPL-3.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# RSFS: LicenseRef-Rsfs
# StandardSymL: GPL-1.0-or-later
License:        GPL-3.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only AND LicenseRef-Rsfs
Summary:        Semigraphs documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       GAPDoc-doc
Requires:       gap-pkg-digraphs-doc
Requires:       gap-pkg-images-doc
Requires:       gap-pkg-io-doc
Requires:       gap-pkg-smallsemi-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%conf
# Do not use the bundled libsemigroups
rm -fr libsemigroups

# Do not override our build flags
sed -i 's/ -O3//' GNUmakefile.in

# Do not add an rpath
sed -i '/rpath/s/\(LIBSEMIGROUPS_RPATH=\).*/\1/' configure

# Work around -Wl,--as-needed appearing too late on the command line
sed -i 's/GAP_CXX :=.*/& -Wl,--as-needed/' Makefile.gappkg

%build
export CPPFLAGS='-I%{_includedir}/eigen3'
%configure --with-gaproot=%{gap_archdir} --disable-silent-rules \
  --with-external-libsemigroups --without-march-native

%make_build

# Link to main GAP documentation
ln -s %{gap_libdir}/doc ../../doc
mkdir -p ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
gap -l "$PWD/..;" makedoc.g
rm -fr ../../doc ../pkg

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{pkgname}/doc
cp -a *.g bin data gap tst %{buildroot}%{gap_archdir}/pkg/%{pkgname}
%gap_copy_docs

%check
cd tst
gap -l '%{buildroot}%{gap_archdir};' << EOF
LoadPackage("semigroups");
GAP_EXIT_CODE(Test("testinstall.tst", rec( compareFunction := "uptowhitespace" )));
EOF

%if %{with bigtest}
gap -l '%{buildroot}%{gap_archdir};' teststandard.g
%endif

cd -

%files
%doc CHANGELOG.md README.md VERSIONS
%license GPL LICENSE
%{gap_archdir}/pkg/%{pkgname}/
%exclude %{gap_archdir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_archdir}/pkg/%{pkgname}/doc/
%{gap_archdir}/pkg/%{pkgname}/doc/

%changelog
%autochangelog
