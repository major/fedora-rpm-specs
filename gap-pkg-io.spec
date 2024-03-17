%global pkgname io

Name:           gap-pkg-%{pkgname}
Version:        4.8.2
Release:        %autorelease
Summary:        Unix I/O functionality for GAP

License:        GPL-3.0-or-later
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/io/
VCS:            https://github.com/gap-packages/io
Source0:        %{vcs}/releases/download/v%{version}/%{pkgname}-%{version}.tar.bz2

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig

Requires:       gap-core%{?_isa}

%description
This GAP package provides a link to the standard UNIX I/O functionality
that is available through the C library.  This part basically consists
of functions on the GAP level that allow functions in the C library to
be called.

Built on top of this is a layer for buffered input/output which is
implemented completely in the GAP language.  It is intended to be used
by programs for which it is not necessary to have full direct access to
the operating system.

On this level, quite a few convenience functions are implemented for
interprocess communication like starting up pipelines of processes to
filter data through them and to start up processes and then communicate
with them.  There is also support for creating network connections over
TCP/IP and UDP.

Building on this, the package contains an implementation of the client
side of the HTTP protocol making it possible among other things to
access web pages from within GAP.

Another part of the package is a framework for object serialization.
That is, GAP objects can be converted into a platform-independent byte
sequence which can be stored to a file or sent over the network.  The
code takes complete care of arbitrarily self-referential data structures
like lists containing themselves as an entry.  The resulting byte
strings can be read back into GAP and the original objects are rebuilt
with exactly the same self-references.  This works for most of the
standard builtin types of GAP like numbers, permutations, polynomials,
lists, and records and can be extended to nearly arbitrary GAP objects.

%package doc
# The content is GPL-3.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-3.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
BuildArch:      noarch
Summary:        Unix I/O for GAP documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8
%configure --with-gaproot=%{gap_archdir}
%make_build GAP="%{_bindir}/gap --bare"
make doc GAP="%{_bindir}/gap --bare"

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{pkgname}/doc
cp -a *.g bin example gap tst %{buildroot}%{gap_archdir}/pkg/%{pkgname}
%gap_copy_docs

%check
# Cannot run the HTTP test, as there is no network access on koji builders
runtest() {
  gap -l "%{buildroot}%{gap_archdir};" --bare -c 'LoadPackage("io");' $1 < /dev/null 2>&1 | tee log
  ! grep -Fq 'gap> Error' log
  rm -f log
}

export LC_ALL=C.UTF-8
pushd tst
echo Testing platform
runtest platform.g
echo Testing pickle
runtest pickle.g
echo Testing buffered
runtest buffered.g
echo Testing compression
runtest compression.g
popd

%files
%doc CHANGES README.md TODO
%license GPL LICENSE
%{gap_archdir}/pkg/%{pkgname}/
%exclude %{gap_archdir}/pkg/%{pkgname}/doc/
%exclude %{gap_archdir}/pkg/%{pkgname}/example/

%files doc
%docdir %{gap_archdir}/pkg/%{pkgname}/doc/
%docdir %{gap_archdir}/pkg/%{pkgname}/example/
%{gap_archdir}/pkg/%{pkgname}/doc/
%{gap_archdir}/pkg/%{pkgname}/example/

%changelog
%autochangelog
