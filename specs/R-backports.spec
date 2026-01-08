Name:           R-backports
Version:        %R_rpm_version 1.5.0
Release:        %autorelease
Summary:        Reimplementations of Functions Introduced Since R-3.0.0

# Automatically converted from old format: GPLv2 or GPLv3 - review is highly recommended.
License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Functions introduced or changed since R v3.0.0 are re-implemented in this
package. The backports are conditionally exported in order to let R resolve
the function name to either the implemented backport, or the respective
base version, if available. Package developers can make use of new
functions or arguments by selectively importing specific backports to
support older installations.

%prep
%autosetup -c
rm -f backports/tests/test_dotlibPaths.R # wrong conditional

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
