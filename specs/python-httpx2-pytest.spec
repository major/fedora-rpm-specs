Summary:        Send responses to HTTPX2 using pytest
Name:           python-httpx2-pytest
Version:        2.0.0
Release:        %autorelease
License:        MIT
URL:            https://github.com/angryfoxx/httpx2-pytest
Source:         %{pypi_source httpx2_pytest}
Patch:          python-httpx2-pytest-2.0.0-relax-dep.patch
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest-cov
%global _description %{expand:
This package provides python module httpx2-pytest which follows in the
spirit of pytest-httpx but cover HTTPX2.}

%description %_description
%package -n     python3-httpx2-pytest
Summary:        %{summary}
%description -n python3-httpx2-pytest %_description

%pyproject_extras_subpkg -n python3-httpx2-pytest testing

%prep
%autosetup -p1 -n httpx2_pytest-%{version}

%generate_buildrequires
%pyproject_buildrequires -x testing

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l pytest_httpx2

%check
%pyproject_check_import
export COVERAGE_PROCESS_START=$(pwd)/.coveragerc
touch $(pwd)/.coveragerc
%pytest

%files -n python3-httpx2-pytest -f %{pyproject_files}

%changelog
%autochangelog

