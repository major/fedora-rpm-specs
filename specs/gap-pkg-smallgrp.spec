%global gap_pkgname smallgrp
%global giturl      https://github.com/gap-packages/smallgrp

Name:           gap-pkg-%{gap_pkgname}
Version:        1.5.4
Release:        %autorelease
Summary:        Small groups library

License:        Artistic-2.0
URL:            https://gap-packages.github.io/smallgrp/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --bare
BuildOption(install): gap id* small* tst
BuildOption(check): --bare tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  parallel

Requires:       gap-core

%description
The Small Groups library gives access to all groups of certain "small" orders.
The groups are sorted by their orders and they are listed up to isomorphism;
that is, for each of the available orders a complete and irredundant list of
isomorphism type representatives of groups is given.

%package doc
# The content is Artistic-2.0.  The remaining licenses cover the various
# fonts embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        Artistic-2.0 AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Small groups library documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%conf
# Fix permissions
chmod a-x id9/idgrp9.g id10/idgrp10.g

%build -a
# Compress large group files
parallel %{?_smp_mflags} --no-notice gzip --best -f ::: id*/* small*/*

%files
%doc CHANGES.md README README.md
%license COPYRIGHT.md LICENSE
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/gap/
%{gap_libdir}/pkg/%{gap_upname}/id*
%{gap_libdir}/pkg/%{gap_upname}/small*
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
