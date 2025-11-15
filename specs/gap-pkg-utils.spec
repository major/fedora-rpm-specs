%global gap_pkgname utils
%global giturl      https://github.com/gap-packages/utils

Name:           gap-pkg-%{gap_pkgname}
Version:        0.93
Release:        %autorelease
Summary:        Utility functions for GAP

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/utils/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/v%{version}/%{gap_upname}-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    gap
BuildOption(build): --packagedirs ..
BuildOption(install): lib tst
BuildOption(check): tst/testall.g

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-curlinterface-doc
BuildRequires:  gap-pkg-io-doc

Requires:       gap-core

Recommends:     gap-pkg-curlinterface

%description
The Utils package provides a collection of utility functions gleaned from many
packages.

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
This package contains documentation for gap-pkg-%{gap_pkgname}.

%prep
%autosetup -n %{gap_upname}-%{version}

%check -p
# The download test cannot be run on the koji builders, which provide no
# network access during a package build.
rm %{buildroot}%{gap_libdir}/pkg/%{gap_upname}/tst/download.tst

%check -a
cp -p tst/download.tst %{buildroot}%{gap_libdir}/pkg/%{gap_upname}/tst

%files
%doc CHANGES.md README.md
%license LICENSE.txt
%dir %{gap_libdir}/pkg/%{gap_upname}/
%{gap_libdir}/pkg/%{gap_upname}/*.g
%{gap_libdir}/pkg/%{gap_upname}/lib/
%{gap_libdir}/pkg/%{gap_upname}/tst/

%files doc
%docdir %{gap_libdir}/pkg/%{gap_upname}/doc/
%{gap_libdir}/pkg/%{gap_upname}/doc/

%changelog
%autochangelog
