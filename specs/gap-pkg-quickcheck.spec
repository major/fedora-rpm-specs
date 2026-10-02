%global gap_pkgname quickcheck
%global giturl      https://github.com/gap-packages/quickcheck

Name:           gap-pkg-%{gap_pkgname}
Version:        1.1.0
Release:        %autorelease
Summary:        Randomized property-based testing for GAP

License:        MPL-2.0
URL:            https://gap-packages.github.io/quickcheck/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): examples gap tst
BuildOption(check): tst/testall.g

BuildRequires:  gap(autodoc) >= 2026.03.17
BuildRequires:  gap(digraphs) >= 1.0.0
BuildRequires:  gap(polycyclic) >= 1.1
BuildRequires:  gap-devel >= 4.13

Requires:       gap(polycyclic) >= 1.1
Requires:       gap-core >= 4.13

Provides:       gap(QuickCheck) = %{version}-%{release}
Provides:       gap(quickcheck) = %{version}-%{release}

%description
This package provides a library for randomized, property-based testing in GAP,
inspired by the QuickCheck framework found in languages like Haskell.

It allows you to write tests as general properties that should hold true for
your code, and the QuickCheck package will then generate a large number of
random test cases to try and find a counterexample.

Features:
- Property-Based Testing: Define properties and let the framework generate
  test data automatically.
- Automatic Sizing: The package automatically tries a range of different sizes
  for the generated objects, starting with small and simple cases to find the
  minimal counterexamples first.
- Variety of Types: It supports random generation for a range of common GAP
  types.

%package doc
# The content is MPL-2.0.  The remaining licenses cover the various fonts
# embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        MPL-2.0 AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        QuickCheck documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%files
%doc README.md
%license LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_libdir}/pkg/%{gap_upname}/examples/
%{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/examples/

%changelog
%autochangelog
