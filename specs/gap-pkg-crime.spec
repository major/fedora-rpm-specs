%global gap_pkgname crime
%global giturl      https://github.com/gap-packages/crime

Name:           gap-pkg-%{gap_pkgname}
Version:        1.6
Release:        %autorelease
Summary:        Group cohomology and Massey products

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/crime/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): gap tst

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  perl-generators

Requires:       gap-core

%description
This GAP package computes cohomology rings for finite p-groups using Jon
Carlson's method, both as GAP objects, and also in terms of generators and
relators.  It also computes induced homomorphisms on cohomology and Massey
products in the cohomology ring.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Group cohomology documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%check
# Do not run the batch.g test.  It never terminates.  The instructions indicate
# it has to be interrupted manually.
gap -l '%{buildroot}%{gap_libdir};' << EOF
LoadPackage("crime");
GAP_EXIT_CODE(Test("tst/test.tst", rec(compareFunction := "uptowhitespace")));
EOF

%files
%doc CHANGES.md README.md
%license COPYING
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
