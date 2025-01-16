%global pkgname smallgrp
%global giturl  https://github.com/gap-packages/smallgrp

Name:           gap-pkg-%{pkgname}
Version:        1.5.4
Release:        %autorelease
Summary:        Small groups library

License:        Artistic-2.0
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/smallgrp/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  parallel

Requires:       gap-core

%description
The Small Groups library gives access to all groups of certain "small"
orders.  The groups are sorted by their orders and they are listed up to
isomorphism; that is, for each of the available orders a complete and
irredundant list of isomorphism type representatives of groups is given.

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
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

# Fix permissions
chmod a-x id9/idgrp9.g id10/idgrp10.g

%build
gap --bare makedoc.g

# Compress large group files
parallel %{?_smp_mflags} --no-notice gzip --best -f ::: id*/* small*/*

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g gap id* small* tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
gap -l '%{buildroot}%{gap_libdir};' --bare tst/testall.g

%files
%doc CHANGES.md README README.md
%license COPYRIGHT.md LICENSE
%dir %{gap_libdir}/pkg/%{pkgname}/
%{gap_libdir}/pkg/%{pkgname}/*.g
%{gap_libdir}/pkg/%{pkgname}/gap/
%{gap_libdir}/pkg/%{pkgname}/id*
%{gap_libdir}/pkg/%{pkgname}/small*
%{gap_libdir}/pkg/%{pkgname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/

%changelog
%autochangelog
