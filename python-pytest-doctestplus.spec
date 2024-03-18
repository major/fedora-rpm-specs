%global srcname pytest-doctestplus
%global pythonicname pytest_doctestplus
%global sum Pytest plugin with advanced doctest features

Name:           python-%{srcname}
Version:        1.2.1
Release:        %autorelease
Summary:        Pytest plugin with advanced doctest features

License:        BSD-3-Clause
URL:            https://github.com/scientific-python/pytest-doctestplus
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
The doctestplus plugin provides advanced features for testing example Python
code that is included in Python docstrings and in standalone documentation
files.

Good documentation for developers contains example code. This is true of both
standalone documentation and of documentation that is integrated with the
code itself. Python provides a mechanism for testing code snippets that are
provided in Python docstrings. The unit test framework pytest provides a
mechanism for running doctests against both docstrings in source code and in
standalone documentation files.

This plugin augments the functionality provided by Python and pytest by
providing the following features:
* approximate floating point comparison for doctests that produce floating 
  point results 
* skipping particular classes, methods, and functions when running doctests
* handling doctests that use remote data in conjunction with the
  pytest-remotedata plugin
* optional inclusion of *.rst files for doctests}

%description %_description


%package -n python3-%{srcname}
Summary:        %{summary}


%description -n python3-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version}

# Remove egg files from source
rm -r %{pythonicname}.egg-info

%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pythonicname}


%check
%pyproject_check_import


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.rst
%doc CHANGES.rst README.rst


%changelog
%autochangelog
