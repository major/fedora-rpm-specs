%global srcname pytest-arraydiff
%global modname pytest_arraydiff
%global sum Pytest plugin to help with comparing array output from tests

Name:           python-%{srcname}
Version:        0.6.1
Release:        %autorelease
Summary:        %{sum}

License:        BSD-2-Clause
URL:            https://github.com/astropy/pytest-arraydiff
Source0:        %{pypi_source}

BuildArch:      noarch
# pytable is missing in the following arch
ExcludeArch:    %{ix86} 
BuildRequires:  python3-devel

%global _description %{expand:
This is a py.test plugin to facilitate the generation and comparison of
data arrays produced during tests.

The basic idea is that you can write a test that generates a Numpy array
(or other related objects depending on the format). You can then either
run the tests in a mode to generate reference files from the arrays, or
you can run the tests in comparison mode, which will compare the results
of the tests to the reference ones within some tolerance.

At the moment, the supported file formats for the reference files are:
* A plain text-based format (baed on Numpy loadtxt output)
* The FITS format (requires astropy). With this format, tests can return
  either a Numpy array for a FITS HDU object.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

# Remove egg files from source
rm -r %{modname}.egg-info

%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{modname}


%check
%pytest


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc CHANGES.md README.rst


%changelog
%autochangelog
