Name:           ini2toml
Version:        0.13
Release:        %autorelease
Summary:        Automatic conversion of .ini/.cfg files to TOML equivalents

License:        MPLv2.0
URL:            https://github.com/abravalheri/ini2toml/
Source0:        %{pypi_source ini2toml}

BuildArch:      noarch
BuildRequires:  python3-devel

# Provide the python3-* namespace as the package
# can also be used as a library.
%py_provides python3-ini2toml

%global _description %{expand:
The original purpose of this project is to help migrating setup.cfg files to PEP 621, but by extension it can also be used to convert any compatible .ini/.cfg file to TOML.

Please notice, the provided .ini/.cfg files should follow the same syntax supported by Python’s ConfigParser library (here referred to as INI syntax) and more specifically abide by ConfigUpdater restrictions (e.g., no interpolation or repeated fields).}

%description %_description

%pyproject_extras_subpkg -n ini2toml full lite

%prep
%autosetup -p1 -n ini2toml-%{version}

# Remove the coverage cmd arguments from pytest
sed -Ei '/(-|pytest)-cov(-report)?/d' setup.cfg

# Remove test dependency on validate-pyproject, not yet packaged
# Tests requiring it are excluded in %%check
sed -i '/validate-pyproject/d' setup.cfg


%generate_buildrequires
%pyproject_buildrequires -x full,lite,testing


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files ini2toml


%check
%pyproject_check_import

# the test_examples.py requires the validate-pyproject package which is not packaged yet
# tests/test_cli.py::test_auto_formatting requires python-fmt which is not packaged yet
%pytest -vv --ignore tests/test_examples.py --deselect tests/test_cli.py::test_auto_formatting


%files -f %{pyproject_files}
%doc README.rst
%{_bindir}/ini2toml


%changelog
%autochangelog
