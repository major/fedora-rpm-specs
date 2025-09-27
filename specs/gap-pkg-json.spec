%global gap_pkgname json
%global giturl      https://github.com/gap-packages/json

Name:           gap-pkg-%{gap_pkgname}
Version:        2.2.3
Release:        %autorelease
Summary:        JSON reading and writing for GAP

License:        BSD-2-Clause
URL:            https://gap-packages.github.io/json/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(install): bin gap tst
BuildOption(check): tst/testall.g

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
This package defines a mapping between the JSON markup language and GAP.  The
built-in datatypes of GAP provide an easy mapping to and from JSON.  This
package uses the following mapping between GAP and JSON.

- JSON lists are mapped to GAP lists
- JSON dictionaries are mapped to GAP records
- JSON strings are mapped to GAP strings
- Integers are mapped to GAP integers, non-integer numbers are mapped to
  Floats
- true, false and null are mapped to true, false and fail respectively

Note that this library will not map any other GAP types, such as groups,
permutations, to or from JSON.  If you wish to map between more complex types,
look at the gap-pkg-openmath package, or IO_Pickle in the gap-pkg-io package.

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
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%build -p
# This is NOT an autoconf-generated script.  Do NOT use %%configure.
./configure %{gap_archdir}
%make_build

%files
%doc README
%license LICENSE
%dir %{gap_archdir}/pkg/%{gap_upname}/
%{gap_archdir}/pkg/%{gap_upname}/*.g
%{gap_archdir}/pkg/%{gap_upname}/bin/
%{gap_archdir}/pkg/%{gap_upname}/gap/
%{gap_archdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_archdir}/pkg/%{gap_upname}/doc/
%{gap_archdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
