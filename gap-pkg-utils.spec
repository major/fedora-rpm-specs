%global pkgname utils

Name:           gap-pkg-%{pkgname}
Version:        0.85
Release:        %autorelease
Summary:        Utility functions for GAP

License:        GPL-2.0-or-later
BuildArch:      noarch
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
URL:            https://gap-packages.github.io/utils/
VCS:            https://github.com/gap-packages/utils
Source0:        %{vcs}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-curlinterface-doc
BuildRequires:  gap-pkg-io-doc

Recommends:     gap-pkg-curlinterface

%description
The Utils package provides a collection of utility functions gleaned
from many packages.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        GAP utils documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-curlinterface-doc
Requires:       gap-pkg-io-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version} -p1

%build
export LC_ALL=C.UTF-8
gap -l "$PWD/..;" makedoc.g

%install
mkdir -p %{buildroot}%{gap_libdir}/pkg/%{pkgname}/doc
cp -a *.g lib tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8

# The download test cannot be run on the koji builders, which provide no
# network access during a package build.
rm %{buildroot}%{gap_libdir}/pkg/%{pkgname}/tst/download.tst
gap -l "%{buildroot}%{gap_libdir};" tst/testall.g
cp -p tst/download.tst %{buildroot}%{gap_libdir}/pkg/%{pkgname}/tst

%files
%doc CHANGES.md README.md
%license LICENSE.txt
%{gap_libdir}/pkg/%{pkgname}/
%exclude %{gap_libdir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{gap_libdir}/pkg/%{pkgname}/doc/
%{gap_libdir}/pkg/%{pkgname}/doc/

%changelog
%autochangelog
