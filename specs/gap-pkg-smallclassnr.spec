%global gap_pkgname smallclassnr
%global gap_upname  SmallClassNr
%global giturl      https://github.com/stertooy/SmallClassNr

Name:           gap-pkg-%{gap_pkgname}
Version:        1.4.3
Release:        %autorelease
Summary:        Library of finite groups with small class number

License:        GPL-2.0-or-later
URL:            https://stertooy.github.io/SmallClassNr/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): data lib tst
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-packagemanager-doc

Requires:       gap-core

%description
The SmallClassNr package provides access to finite groups with small class
number.  Currently, the package contains the finite groups of class number at
most 14.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        SmallClassNr documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
Recommends:     gap-pkg-packagemanager-doc

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%files
%doc CHANGES.md CITATION.cff README.md
%license LICENSE.txt
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/data/
%{gap_libdir}/pkg/%{gap_upname}/lib/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
