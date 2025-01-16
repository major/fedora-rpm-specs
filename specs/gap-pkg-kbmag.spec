%global pkgname kbmag
%global giturl  https://github.com/gap-packages/kbmag

Name:           gap-pkg-%{pkgname}
Version:        1.5.11
Release:        %autorelease
Summary:        Knuth-Bendix on Monoids and Automatic Groups

License:        GPL-2.0-or-later
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/kbmag/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-nq-doc
BuildRequires:  make

Requires:       gap-core%{?_isa}

%description
KBMAG (pronounced Kay-bee-mag) stands for Knuth-Bendix on Monoids, and
Automatic Groups.  It is a stand-alone package written in C, for use
under UNIX, with an interface to GAP.  There are interfaces for the use
of KBMAG with finitely presented groups, monoids and semigroups defined
within GAP.  The package also contains a collection of routines for
manipulating finite state automata, which can be accessed via the GAP
interface.

The overall objective of KBMAG is to construct a normal form for the
elements of a finitely presented group G in terms of the given
generators together with a word reduction algorithm for calculating the
normal form representation of an element in G, given as a word in the
generators.  If this can be achieved, then it is also possible to
enumerate the words in normal form up to a given length, and to
determine the order of the group, by counting the number of words in
normal form.  In most serious applications, this will be infinite, since
finite groups are (with some exceptions) usually handled better by
Todd-Coxeter related methods.  In fact a finite state automaton W is
calculated that accepts precisely the language of words in the group
generators that are in normal form, and W is used for the enumeration
and counting functions.  It is possible to inspect W directly if
required; for example, it is often possible to use W to determine
whether an element in G has finite or infinite order.

The normal form for an element g in G is defined to be the least word in
the group generators (and their inverses) that represents G, with
respect to a specified ordering on the set of all words in the group
generators.

KBMAG offers two possible means of achieving these objectives.  The
first is to apply the Knuth-Bendix algorithm to the group presentation,
with one of the available orderings on words, and hope that the
algorithm will complete with a finite confluent presentation.  (If the
group is finite, then it is guaranteed to complete eventually but, like
the Todd-Coxeter procedure, it may take a long time, or require more
space than is available.)  The second is to use the automatic group
program.  This also uses the Knuth-Bendix procedure as one component of
the algorithm, but it aims to compute certain finite state automata
rather than to obtain a finite confluent rewriting system, and it
completes successfully on many examples for which such a finite system
does not exist.  In the current implementation, its use is restricted to
the shortlex ordering on words.  That is, words are ordered first by
increasing length, and then words of equal length are ordered
lexicographically, using the specified ordering of the generators.

The GAP4 version of KBMAG also offers extensive facilities for finding
confluent presentations and finding automatic structures relative to a
specified finitely generated subgroup of the group G.  Finally, there is
a collection of functions for manipulating finite state automata that
may be of independent interest.

%package doc
# The content is GPL-2.0-or-later.
# The remaining licenses cover the various fonts embedded in PDFs:
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND GPL-1.0-or-later AND Knuth-CTAN AND AGPL-3.0-only
Summary:        Documentation for the GAP kbmag package
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-nq-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%conf
# Preserve timestamps
sed -i 's/cp /cp -p /' standalone/src/makefile

%build
# This is not an autoconf-generated script.  Do not use %%configure.
./configure --with-gaproot=%{gap_archdir}
%make_build
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{pkgname}/doc
cp -a bin gap tst *.g  %{buildroot}%{gap_archdir}/pkg/%{pkgname}
%gap_copy_docs

%check
make test
gap -l '%{buildroot}%{gap_archdir};' tst/testall.g

%files
%doc CHANGES README.md
%license LICENSE
%dir %{gap_archdir}/pkg/%{pkgname}/
%{gap_archdir}/pkg/%{pkgname}/*.g
%{gap_archdir}/pkg/%{pkgname}/bin/
%{gap_archdir}/pkg/%{pkgname}/gap/
%{gap_archdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_archdir}/pkg/%{pkgname}/doc/
%{gap_archdir}/pkg/%{pkgname}/doc/

%changelog
%autochangelog
