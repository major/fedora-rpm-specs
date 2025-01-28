%global with_check 1
%global pypi_name biopython
%global module %{pypi_name}

Name:             python-%{pypi_name}
Version:          1.85
Release:          %autorelease
Summary:          Python tools for computational molecular biology
Source:           %{pypi_source}

# Starting from biopython-1.69, BioPython is released under the
# "Biopython License Agreement"; it looks like a MIT variant
# rhbz #1440337
License:          MIT AND BSD-3-Clause
URL:              https://biopython.org/
BuildRequires:    gcc
BuildRequires:    pyproject-rpm-macros

%description
A set of freely available Python tools for computational molecular
biology.


%package -n python3-%{module}
Summary: Python3 tools for computational molecular biology

%py_provides      python3-%{module}
BuildRequires:    python3-devel
BuildRequires:    python3dist(reportlab)
Requires:         flex%{?_isa}

%description -n python3-%{module}
A set of freely available Python3 tools for computational molecular
biology.


%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x tests

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files Bio BioSQL

%if 0%{?with_check}
%check
pushd Tests
for test in `ls test_*.py | grep -v test_Align_bigbed.py | grep -v test_Tutorial.py`; do
%{py3_test_envvars} %{python3} run_tests.py --offline --verbose -v ${test}
done
%endif


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc Doc
%doc Scripts


%changelog
%autochangelog
