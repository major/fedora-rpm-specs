%global pypi_name jplephem

Name:           python-%{pypi_name}
Version:        2.24
Release:        %autorelease
Summary:        Use a JPL ephemeris to predict planet positions

License:        MIT
URL:            https://github.com/brandon-rhodes/%{name}/
# The GitHub tarball contains tests; the PyPI sdist does not.
Source:         %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

# Backport upstream patch to fix test failure
Patch:          810ff57.patch

BuildArch:      noarch
BuildRequires:  python3-pytest

%global _description %{expand:
This package can load and use a Jet Propulsion Laboratory (JPL)
ephemeris for predicting the position and velocity of a planet
or other Solar System body. It currently supports binary SPK files
(extension .bsp) like those distributed by the Jet Propulsion
Laboratory.}

%description %_description


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%check
%pyproject_check_import
pushd ci
%{py3_test_envvars} %{python3} ./jpltest.py
%pytest ../jplephem/test.py
popd


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
