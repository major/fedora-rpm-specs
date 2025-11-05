Name:               python-mccabe
Version:            0.7.0
Release:            %autorelease
Summary:            McCabe complexity checker
License:            MIT
URL:                http://pypi.python.org/pypi/mccabe
Source:             %{pypi_source mccabe}
# Make hypothesis / hypothesmith truly optional
# https://github.com/PyCQA/mccabe/pull/92
Patch:              https://github.com/PyCQA/mccabe/pull/92.patch

BuildArch:          noarch
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-pytest

%global _description %{expand:
Ned's script to check McCabe complexity.

This module provides a plugin for flake8, the Python code
checker.}

%description %_description


%package -n python%{python3_pkgversion}-mccabe
Summary:            %{summary}

%description -n python%{python3_pkgversion}-mccabe %_description


%prep
%autosetup -p1 -n mccabe-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files mccabe


%check
%pytest -r fEs


%files -n python%{python3_pkgversion}-mccabe -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
