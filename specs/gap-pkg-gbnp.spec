%global pkgname gbnp
%global giturl  https://github.com/gap-packages/gbnp

Name:           gap-pkg-%{pkgname}
Version:        1.1.0
Release:        %autorelease
Summary:        Computing Gröbner bases of noncommutative polynomials

License:        LGPL-2.1-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/gbnp/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/GBNP-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  make
BuildRequires:  tex-urlbst

Requires:       gap-core

%description
GBNP provides GAP algorithms for computing Gröbner bases of
non-commutative polynomials with coefficients from a field implemented in
GAP, and some variations, such as a weighted and truncated version and a
tracing facility.

The word algorithm is interpreted loosely: in general one cannot expect
such an algorithm to terminate, as it would imply solvability of the
word problem for finitely presented (semi)groups.

%package doc
# The content is LGPL-2.1-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# LaTeX: LPPL-1.3a
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        LGPL-2.1-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND LPPL-1.3a AND AGPL-3.0-only
Summary:        GBNP documentation and examples
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{version}

%conf
# Help GAP find its files
sed -i 's,\\\\\\\(.*\) ,"%{gap_libdir}\1",;s/eval //' etc/workspace
sed -i 's,\\\\;,%{gap_libdir};,' etc/makedepend etc/workspace
sed -i "s,-r,-l '%{_builddir}/%{pkgname}-%{version}/build;' &,;s/eval //" \
    etc/gapscript

%build
%make_build doc

%install
# We install test files for use by GAP's internal test suite runner.
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g lib tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
cp -a doc/{articles,examples} %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
rm %{buildroot}%{gap_libdir}/pkg/%{pkgname}/lib/{gbnp-uses.sed,OPTIONS,STRUCTURE,TODO}
rm %{buildroot}%{gap_libdir}/pkg/%{pkgname}/tst/{.depend,GNUmakefile,txt2xml.sed}
%gap_copy_docs

%check
gap -l '%{buildroot}%{gap_libdir};' tst/testall.g

%files
%doc Changelog README.md
%license COPYRIGHT doc/LGPL
%dir %{gap_libdir}/pkg/%{pkgname}/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/lib/
%{gap_libdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/

%changelog
%autochangelog
