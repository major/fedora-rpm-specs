%global pypi_name bioframe

%bcond tests 1

Name:           python-%{pypi_name}
Version:        0.8.0
Release:        %{autorelease}
Summary:        Operations and utilities for Genomic Interval Dataframes

%global forgeurl https://github.com/open2c/bioframe
%forgemeta

# SPDX
License:        MIT
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Bioframe enables flexible and scalable operations on genomic interval
dataframes in Python.

Bioframe is built directly on top of Pandas. Bioframe provides:

- A variety of genomic interval operations that work directly on
  dataframes.
- Operations for special classes of genomic intervals, including
  chromosome arms and fixed-size bins.
- Conveniences for diverse tabular genomic data formats and loading
  genome assembly summary information.

Bioframe is an Affiliated Project of NumFOCUS.}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}
Recommends:     python3dist(biopython)
Recommends:     python3dist(pysam)
Recommends:     python3dist(pybbi)

%description -n python3-%{pypi_name} %_description


%prep
%forgeautosetup -p1

# Remove linter from `dev` extra
sed -i '/"ruff"/ d' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x dev}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%check
%if %{with tests}
# Disable tests requiring network
k="${k-}${k+ and }not test_fetch"
%pytest -r fEs ${k+-k "${k-}"}
%else
%pyproject_check_import
%endif


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CONTRIBUTING.md CITATION.cff CHANGES.md


%changelog
%autochangelog
