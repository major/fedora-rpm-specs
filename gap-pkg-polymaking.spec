%global pkgname polymaking

Name:           gap-pkg-%{pkgname}
Version:        0.8.7
Release:        %autorelease
Summary:        GAP interface to polymake

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/polymaking/
VCS:            https://github.com/gap-packages/polymaking
Source0:        %{vcs}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  polymake

Requires:       gap-core
Requires:       polymake

%description
This package provides a very basic GAP interface to polymake.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Polymaking documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version} -p1

# Fix an undefined LaTeX command in the BibTeX file
sed -i 's/URL/url/' doc/polymaking.bib

%build
export LC_ALL=C.UTF-8
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g lib tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8

# Produce less chatter while running the test
polymake --reconfigure - <<< exit;

# Now we can run the actual test.
gap -l "%{buildroot}%{gap_libdir};" tst/testall.g

%files
%doc CHANGES.md README.md
%license LICENSE
%{gap_libdir}/pkg/%{pkgname}/
%exclude %{gap_libdir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/

%changelog
%autochangelog
