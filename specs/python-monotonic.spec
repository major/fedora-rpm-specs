Name:           python-monotonic
Version:        1.6
Release:        %autorelease
Summary:        An implementation of time.monotonic() for Python 2 & < 3.3
License:        Apache-2.0
URL:            https://github.com/atdt/monotonic
Source:         %{pypi_source monotonic}
BuildArch:      noarch


%global _description %{expand:
This module provides a monotonic() function which returns the value (in
fractional seconds) of a clock which never goes backwards.  On Python 3.3 or
newer, monotonic will be an alias of time.monotonic from the standard library.
On older versions, it will fall back to an equivalent implementation.}


%description %_description


%package -n python3-monotonic
Summary:        %{summary}
BuildRequires:  python3-devel


%description -n python3-monotonic %_description


%prep
%autosetup -n monotonic-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l monotonic


%check
%pyproject_check_import


%files -n python3-monotonic -f %{pyproject_files}


%changelog
%autochangelog
