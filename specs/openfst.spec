%global release_date "July 2018"

Name:           openfst
Version:        1.8.4
Release:        %autorelease
Summary:        Weighted finite-state transducer library

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://www.openfst.org/
Source0:        http://www.openfst.org/twiki/pub/FST/FstDownload/%{name}-%{version}.tar.gz
Source1:        http://www.openfst.org/twiki/pub/Contrib/OpenFstBashComp/openfstbc

BuildRequires: make
BuildRequires:  chrpath
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  zlib-devel

%description
OpenFst is a library for constructing, combining, optimizing, and
searching weighted finite-state transducers (FSTs).  Weighted
finite-state transducers are automata where each transition has an input
label, an output label, and a weight.  The more familiar finite-state
acceptor is represented as a transducer with each transition's input and
output label equal.  Finite-state acceptors are used to represent sets
of strings (specifically, regular or rational sets); finite-state
transducers are used to represent binary relations between pairs of
strings (specifically, rational transductions).  The weights can be used
to represent the cost of taking a particular transition.

FSTs have key applications in speech recognition and synthesis, machine
translation, optical character recognition, pattern matching, string
processing, machine learning, information extraction and retrieval among
others.  Often a weighted transducer is used to represent a
probabilistic model (e.g., an n-gram model, pronunciation model).  FSTs
can be optimized by determinization and minimization, models can be
applied to hypothesis sets (also represented as automata) or cascaded by
finite-state composition, and the best results can be selected by
shortest-path algorithms.

%package devel
Summary:        Development files for OpenFst
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package includes the necessary files to develop systems with
OpenFst.

%package tools
Summary:        Command-line tools for working with FSTs
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
This package contains command-line tools that give access to OpenFst
functionality.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="$CFLAGS"
%configure --enable-compact-fsts --enable-compress --enable-const-fsts \
  --enable-linear-fsts --enable-lookahead-fsts --enable-ngram-fsts \
  --disable-python --enable-special --enable-bin --enable-grm

# Work around libtool reordering -Wl,--as-needed after all the libraries.
sed -i 's|CC=.g..|& -Wl,--as-needed|' libtool

# Subdirectory dependencies are missing, so we cannot use %%{?_smp_mflags}
make

%install
make install DESTDIR=%{buildroot}

# Get rid of libtool files
find %{buildroot}%{_libdir} -name '*.la' | xargs rm -f

# Remove unnecessary rpaths
for fil in %{buildroot}%{_libdir}/lib*.so.*.*.* %{buildroot}%{_bindir}/*; do
  chrpath -d $fil
done

# Install the bash completion file
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
cp -p %{SOURCE1} %{buildroot}%{_datadir}/bash-completion/completions/fstmap
for fil in arcsort closure compile compose compress concat connect convert \
    determinize difference disambiguate draw encode epsnormalize equal \
    equivalent info intersect invert isomorphic linear loglinearapply \
    minimize print project prune push randgen randmod relabel replace reverse \
    reweight rmepsilon shortestdistance shortestpath symbols synchronize \
    topsort union; do
  ln -s fstmap %{buildroot}%{_datadir}/bash-completion/completions/fst$fil
done

# Generate man pages
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}:%{buildroot}%{_libdir}/fst
mkdir -p %{buildroot}%{_mandir}/man1
for f in %{buildroot}%{_bindir}/*; do
  help2man -N --version-string=%{version} $f \
    -o %{buildroot}%{_mandir}/man1/$(basename $f).1
done
# Fix the date string and remove buildroot paths from the man pages
sed -e '2s/"1" "[[:alpha:]]* [[:digit:]]*"/"1" %{release_date}/' \
    -e 's,/builddir.*%{_bindir}/,,g' \
    -i %{buildroot}%{_mandir}/man1/*.1

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS README
%license COPYING
%dir %{_libdir}/fst
%{_libdir}/fst/*.so
%{_libdir}/*.so.*

%files devel
%{_includedir}/fst/
%{_libdir}/fst/*.so
%{_libdir}/*.so

%files tools
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/bash-completion/completions/*

%changelog
%autochangelog
