%global pkgname  json

Name:           gap-pkg-%{pkgname}
Version:        2.2.0
Release:        %autorelease
Summary:        JSON reading and writing for GAP

License:        BSD-2-Clause
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/json/
VCS:            https://github.com/gap-packages/json
Source0:        %{vcs}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make

Requires:       gap-core%{?_isa}

# We cannot use the system version of picojson-devel.  The version used by this
# package has had https://github.com/kazuho/picojson/pull/52 merged into it.
# Until upstream merges that and produces a new release, we are stuck with the
# bundled version.
Provides:       bundled(picojson-devel) = 1.1.1

%description
This package defines a mapping between the JSON markup language and GAP.
The built-in datatypes of GAP provide an easy mapping to and from JSON.
This package uses the following mapping between GAP and JSON.

- JSON lists are mapped to GAP lists
- JSON dictionaries are mapped to GAP records
- JSON strings are mapped to GAP strings
- Integers are mapped to GAP integers, non-integer numbers are mapped to
  Floats
- true, false and null are mapped to true, false and fail respectively

Note that this library will not map any other GAP types, such as groups,
permutations, to or from JSON.  If you wish to map between more complex
types, look at the gap-pkg-openmath package, or IO_Pickle in the
gap-pkg-io package.

%package doc
# The content is BSD-2-Clause.  The remaining licenses cover the various fonts
# embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        BSD-2-CLause AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        JSON documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8

# This is NOT an autoconf-generated script.  Do NOT use %%configure.
./configure %{gap_archdir}
%make_build

# Build the documentation
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_archdir}/pkg/%{pkgname}/doc
cp -a *.g bin gap tst %{buildroot}%{gap_archdir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_archdir};" tst/testall.g

%files
%doc HISTORY README
%license LICENSE
%{gap_archdir}/pkg/%{pkgname}/
%exclude %{gap_archdir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_archdir}/pkg/%{pkgname}/doc/
%{gap_archdir}/pkg/%{pkgname}/doc/

%changelog
%autochangelog
