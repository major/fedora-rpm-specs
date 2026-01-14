Name:           R-readxl
Version:        %R_rpm_version 1.4.5
Release:        %autorelease
Summary:        Read Excel Files

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  libxls-devel

# Patched-in functionality, so not removeable.
Provides:       bundled(rapidxml-devel) = 1.13

%description
Import excel files into R. Supports '.xls' via the 'libxls' C library
<https://github.com/libxls/libxls> and '.xlsx' via the embedded
'RapidXML' C++ library <http://rapidxml.sourceforge.net>.

%prep
%autosetup -c
# Remove bundled libxls.
rm -rf readxl/src/{Makevars.win,libxls,unix,windows}
sed -i '5,$d' readxl/src/Makevars
echo "PKG_LIBS=-lxlsreader" > readxl/src/Makevars
find readxl/src -type f -exec sed -i 's@include "libxls/xls.h"@include <xls.h>@g' {} \;

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
