%global gap_pkgname unipot
%global giturl      https://github.com/gap-packages/unipot

Name:           gap-pkg-%{gap_pkgname}
Version:        1.6
Release:        %autorelease
Summary:        Unipotent subgroups of Chevalley groups for GAP

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/unipot/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): lib tst
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  tth

Requires:       gap-core

%description
The Unipot package provides GAP with the ability to compute with elements of
unipotent subgroups of Chevalley groups, and also some properties of such
groups.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only AND GPL-1.0-or-later
Summary:        Unipot documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%conf
# Fix paths
sed -i 's,\.\./\.\./\.\./,%{gap_libdir}/,' doc/{make_doc,manual.tex}

%build
ln -s %{gap_libdir}/doc ../../doc
cd doc
./make_doc
cd -
rm ../../doc

%files
%doc CHANGES.md README.md
%license LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/lib/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
