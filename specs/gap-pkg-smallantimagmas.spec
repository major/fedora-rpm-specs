%global pkgname smallantimagmas
%global giturl  https://github.com/gap-packages/smallantimagmas

Name:           gap-pkg-%{pkgname}
Version:        0.4.1
Release:        %autorelease
Summary:        Library of antiassociative magmas of small order

License:        GPL-3.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/smallantimagmas/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{pkgname}-%{version}.tar.gz
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc

Requires:       gap-core

%description
This package contains a library of antiassociative magmas of small order for
GAP.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        smallantimagmas documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}
rm tst/.gitignore

%build
mkdir ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
gap -l "$PWD/..;" makedoc.g
rm -fr ../pkg

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g *.ipynb data lib tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
gap -l '%{buildroot}%{gap_libdir};' tst/testall.g

%files
%doc README.md
%license LICENSE.txt
%dir %{gap_libdir}/pkg/%{pkgname}/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/*.ipynb
%{gap_libdir}/pkg/%{pkgname}/data/
%{gap_libdir}/pkg/%{pkgname}/lib/
%{gap_libdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/

%changelog
%autochangelog
