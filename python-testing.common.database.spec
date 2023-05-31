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

BuildArch:      noarch

BuildRequires:  python3-devel

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n     python3-testing.common.database
Summary:        %{summary}

%description -n python3-testing.common.database %{common_description}


%prep
%autosetup -n testing.common.database-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Note that testing is a namespace package, and the directory is co-owned with
# python-testing.postgresql and python-testing.mysqld. Furthermore, each
# installs an __init__.py to the namespace package, which is co-owned
# and—wonderfully—is *actually* identical among the packages in question.
%pyproject_save_files testing


%check
# Upstream has no (non-linter) tests.
%pyproject_check_import


%files -n python3-testing.common.database -f %{pyproject_files}
# pyproject-rpm-macros handles the LICENSE file; verify with “rpm -qL -p …”
%doc README.rst
%{python3_sitelib}/testing.common.database-%{version}-py%{python3_version}-nspkg.pth


%changelog
%autochangelog
