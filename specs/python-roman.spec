%global pypi_name roman

Name:           python-%{pypi_name}
Version:        5.2
Release:        %autorelease
Summary:        Integer to Roman numerals converter

%global forgeurl https://github.com/zopefoundation/roman
%global tag %{version}
%forgemeta

License:        ZPL-2.1
URL:            %forgeurl
Source:         %forgesource
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  tomcli

%global _description %{expand:
Small helper library to convert arabic to roman numerals.

There are two ways to use this library:

  1. Importing it into your application
  2. `roman` CLI command}

%description %_description


%package -n python3-%{pypi_name}
Summary:        Integer to Roman numerals converter
Provides:       roman = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-%{pypi_name} %_description


%prep
%forgeautosetup -p1

# Drop version constraint from setuptools
tomcli set pyproject.toml arrays replace \
    build-system.requires "^(setuptools)[<>= ]+[0-9.]+.*" "\1"


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%check
# We would like to run tests the simple way by just calling %%tox, which
# in turn calls zope-testrunner. But that currently fails with:
#
# ModuleNotFoundError: No module named 'tests'
#
# Since upstream does just that, albeit using `uvx`, I assume zope-testrunner
# needs an update to 7.x.
# Let's just call `unittest` directly for now. There aren't that many tests.

%{py3_test_envvars} %{python3} -m unittest src/tests.py


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst CHANGES.rst
%{_bindir}/%{pypi_name}


%changelog
%autochangelog
                   -