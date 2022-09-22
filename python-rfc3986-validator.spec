%global srcname  rfc3986_validator
%global slugname rfc3986_validator
%global pkgname  rfc3986-validator
%global forgeurl https://github.com/naimetti/rfc3986-validator

%global common_description %{expand:
A pure python RFC3986 validator.
}

%bcond_without tests

Name:           python-%{pkgname}
Version:        0.1.1
%forgemeta
Release:        %autorelease
Summary:        Pure python RFC3986 validator
License:        MIT
URL:            %{forgeurl}
Source:         %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

#This patch removes the pytest-runner from the setup.py config, because of its
#deprecation upstream (see https://pypi.org/project/pytest-runner/ deprecation notice)
#It also adds some missing test dependecies.
#
#An issue has been submited upstream regarding it
#https://github.com/naimetti/rfc3986-validator/issues/2
Patch0:         0001_removing_pytest_runner_and_adding_test_requirements.patch

%description %{common_description}

%package -n python3-%{pkgname}
Summary: %summary

%description -n python3-%{pkgname} %{common_description}

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -r %{?with_tests:-x test}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{slugname}

%check
%pyproject_check_import
%if %{with tests}
PYTHONWARNINGS=ignore %pytest -vv tests
%endif

%files -n python3-%{pkgname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
