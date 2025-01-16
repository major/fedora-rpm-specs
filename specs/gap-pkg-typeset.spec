%global pkgname typeset
%global giturl  https://github.com/gap-packages/typeset

Name:           gap-pkg-%{pkgname}
Version:        1.2.2
Release:        %autorelease
Summary:        Automatic typesetting framework for common GAP objects

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/typeset/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  dot2tex
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-digraphs-doc
BuildRequires:  graphviz

Requires:       dot2tex
Requires:       gap-core
Requires:       graphviz

Recommends:     gap-pkg-digraphs

%description
This package implements a framework for automatic typesetting of common
GAP objects, for the purpose of embedding them nicely into research
papers.  Currently, an example implementation has been written
specifically for LaTeX.

%package doc
# The content is GPL-2.0-or-later.
# The remaining licenses cover the various fonts embedded in PDFs:
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND GPL-1.0-or-later AND Knuth-CTAN AND AGPL-3.0-only
Summary:        Documentation for the GAP typeset package
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-digraphs-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
mkdir ../pkg
ln -s ../%{pkgname}-%{version} ../pkg/%{pkgname}
gap -l "$PWD/..;" makedoc.g
rm -fr ../pkg

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a demo gap tst *.g  %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
gap -l '%{buildroot}%{gap_libdir};' tst/testall.g

%files
%doc CHANGELOG.md README.md
%license LICENSE
%dir %{gap_libdir}/pkg/%{pkgname}/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/gap/
%{gap_libdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/demo/
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/demo/
%{gap_libdir}/pkg/%{pkgname}/doc/

%changelog
%autochangelog
