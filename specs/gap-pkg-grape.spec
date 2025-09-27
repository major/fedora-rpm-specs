%global gap_pkgname grape
%global giturl      https://github.com/gap-packages/grape

Name:           gap-pkg-%{gap_pkgname}
Version:        4.9.3
Release:        %autorelease
Summary:        GRaph Algorithms using PErmutation groups

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/grape/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz
# Fedora-only patch: unbundle nauty
Patch:          %{name}-nauty.patch

BuildArch:      noarch
BuildSystem:    gap
BuildOption(install): grh htm lib tst
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  nauty
BuildRequires:  tth

Requires:       gap-core
Requires:       nauty

%description
GRAPE is a package for computing with graphs and groups, and is primarily
designed for constructing and analyzing graphs related to groups, finite
geometries, and designs.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only AND GPL-1.0-or-later
Summary:        GRAPE documentation and examples
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -p1 -n %{gap_upname}-%{version}

%conf
# There is no ext manual anymore
sed -i '/UseReferences.*ext/d' doc/manual.tex

# Remove nauty sources so we use the system version
rm -fr nauty2_8_6

%build
# Link to main GAP documentation
ln -s %{gap_libdir}/etc ../../etc
ln -s %{gap_libdir}/doc ../../doc
pushd doc
./make_doc
popd
rm -f ../../{doc,etc}

%files
%doc CHANGES.md README.md
%license gpl.txt
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/grh/
%{gap_libdir}/pkg/%{gap_upname}/lib/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%docdir %{gap_libdir}/pkg/%{gap_upname}/htm/
%{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/htm/

%changelog
%autochangelog
