Name:           pngcheck
Version:        4.0.1
Release:        %autorelease
Summary:        Command-line utility to check PNG image files

# The source is under a minimal MIT-style license that matches SPDX HPND:
#   https://gitlab.com/fedora/legal/fedora-license-data/-/issues/85
#   https://tools.spdx.org/app/license_requests/187/
#   https://github.com/spdx/license-list-XML/issues/1725
# …except that third_party/wildargs/ is BSL-1.0. Since it’s needed only on
# non-“UNIX” platforms, we remove it in %%prep and it does not contribute to
# the licenses of the binary RPMs.
License:        HPND
SourceLicense:  %{license} AND BSL-1.0
URL:            https://github.com/pnggroup/pngcheck
Source:         %{url}/archive/v%{version}/pngcheck-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

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
# Remove bundled libraries (currently: wildargs) that are not needed on this
# platform, in order to prove they do not contribute to the binary RPMs.
rm -rv third_party/


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
