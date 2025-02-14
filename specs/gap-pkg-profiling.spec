%global pkgname profiling
%global giturl  https://github.com/gap-packages/profiling

Name:           gap-pkg-%{pkgname}
Version:        2.6.0
Release:        %autorelease
Summary:        Line by line profiling and code coverage for GAP

# The project as a whole is MIT.
# rapidjson, which is a header-only package, is also MIT.
# src/md5.{cc,h} is Public Domain.
License:        MIT AND LicenseRef-Fedora-Public-Domain
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/profiling/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
# Adapt to rapidjson 1.1.0
Patch:          %{name}-rapidjson.patch
# Fix FTBFS with GCC 15
Patch:          %{name}-gcc15.patch

BuildRequires:  elinks
BuildRequires:  flamegraph
BuildRequires:  flamegraph-stackcollapse
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-io
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(RapidJSON)
BuildRequires:  which
BuildRequires:  xdg-utils

Requires:       flamegraph
Requires:       flamegraph-stackcollapse
Requires:       gap-pkg-io%{?_isa}
Requires:       which
Requires:       xdg-utils

# See https://fedoraproject.org/wiki/Bundled_Libraries_Virtual_Provides
Provides:       bundled(md5-plumb)

%description
This package provides line-by-line profiling of GAP, allowing both
discovering which lines of code take the most time, and which lines of
code are even executed.

The main function provided by this package is
OutputAnnotatedCodeCoverageFiles, which takes a previously generated
profile (using ProfileLineByLine or CoverageLineByLine, both provided by
the GAP library), and outputs human-readable HTML files.

There is also OutputFlameGraph, which outputs a graphical diagram
showing which functions took the most time during execution.

%package doc
# The content is MIT.  The remaining licenses cover the various fonts embedded
# in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        MIT AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Profiling documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{version}

%conf
fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Do not use the bundled rapidjson
rm -fr src/rapidjson
sed -i.orig 's,"\(rapidjson/.*h\)",<\1>,' src/json_parse_rapidjson.h
fixtimestamp src/json_parse_rapidjson.h

# Do not use the bundled FlameGraph
rm -fr FlameGraph
sed -i.orig '/Flame/s,DirectoriesPackageLibrary([^)]*),Directory("%{_bindir}"),' gap/profiling.gi
fixtimestamp gap/profiling.gi

%build
# This is not an autoconf-generated configure script; do not use %%configure
./configure %{gap_archdir}
%make_build V=1

# Build the documentation
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{pkgname}/doc
cp -a *.g bin data gap tst %{buildroot}%{gap_archdir}/pkg/%{pkgname}
%gap_copy_docs

%check
export BROWSER=elinks
gap -l '%{buildroot}%{gap_archdir};' tst/testall.g

%files
%doc AUTHORS HISTORY.md README.md
%license COPYRIGHT
%dir %{gap_archdir}/pkg/%{pkgname}/
%{gap_archdir}/pkg/%{pkgname}/*.g
%{gap_archdir}/pkg/%{pkgname}/bin/
%{gap_archdir}/pkg/%{pkgname}/data/
%{gap_archdir}/pkg/%{pkgname}/gap/
%{gap_archdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_archdir}/pkg/%{pkgname}/doc/
%{gap_archdir}/pkg/%{pkgname}/doc/

%changelog
%autochangelog
