Name:           python-testing.common.database
Version:        2.0.3
Release:        %autorelease
Summary:        Utilities for testing.* packages

License:        Apache-2.0
URL:            https://github.com/tk0miya/testing.common.database
Source:         %{pypi_source testing.common.database}

# Support Callable in collections.abc
# https://github.com/tk0miya/testing.common.database/pull/25
Patch:          %{url}/pull/25.patch

BuildSystem:            pyproject
# Note that testing is a namespace package; other packages in this namespace
# could co-own it, but in practice will most likely depend on this package.
# This is true of python-testing.postgresql and (if it packaged in the future)
# python-testing.mysqld.
BuildOption(install):   -l testing
# Upstream has no (non-linter) tests.

BuildArch:      noarch

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n     python3-testing.common.database
Summary:        %{summary}

%description -n python3-testing.common.database %{common_description}


%files -n python3-testing.common.database -f %{pyproject_files}
%doc README.rst
%{python3_sitelib}/testing.common.database-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
