Name:           pngcheck
Version:        4.0.0
Release:        %autorelease
Summary:        Command-line utility to check PNG image files

# Note that the main package contains only pngcheck, compiled from a single
# source file, pngcheck.c, under a minimal MIT-style license that matches SPDX
# HPND:
#   https://gitlab.com/fedora/legal/fedora-license-data/-/issues/85
#   https://tools.spdx.org/app/license_requests/187/
#   https://github.com/spdx/license-list-XML/issues/1725
# For now, the source archive still contains a couple of utilities licensed
# under GPL-2.0-or-later, in the gpl/ subdirectory. These were previously
# packaged an the extras subpackage, but since they were removed upstream
# immediately after the 4.0.0 release, we choose to stop packaging them now.
%global extras_license GPL-2.0-or-later
License:        HPND
SourceLicense:  %{license} AND %{extras_license}
URL:            https://github.com/pnggroup/pngcheck
Source:         %{url}/archive/v%{version}/pngcheck-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  dos2unix

BuildRequires:  cmake
BuildRequires:  gcc

BuildRequires:  cmake(zlib)

# Removed for Fedora 43; Obsoletes can be removed after Fedora 45.
Obsoletes:      pngcheck-extras < 4.0.0-2

%description
pngcheck is a command-line utility to check PNG image files, including animated
PNG, for validity and to give information about metadate inside the file (apart
from the actual image data).


%prep
%autosetup

dos2unix --keepdate README.md


%conf
%cmake


%build
%cmake_build


%install
%cmake_install


# Upstream provides no tests


%files
%license LICENSE
%doc CHANGELOG
%doc README.md
%doc README-303
%{_bindir}/pngcheck
%{_mandir}/man1/pngcheck.1*


%changelog
%autochangelog
