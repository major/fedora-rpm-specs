%global pypi_name sklearn-genetic-opt

%bcond tests 1

Name:           python-%{pypi_name}
Version:        0.11.1
Release:        %autorelease
Summary:        Hyperparameters tuning and feature selection

%global forgeurl https://github.com/rodrigo-arenas/Sklearn-genetic-opt
%global tag %{version}
%forgemeta

# SPDX
License:        MIT
URL:            https://github.com/rodrigo-arenas/Sklearn-genetic-opt
Source0:        %{forgesource}

# Adjust two tests for scikit-learn 1.6
# https://github.com/rodrigo-arenas/Sklearn-genetic-opt/pull/161
Patch:          %{forgeurl}/pull/161.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pandas}
BuildRequires:  %{py3_dist matplotlib}
%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
scikit-learn models hyperparameters tuning and feature selection, using
evolutionary algorithms.

This is meant to be an alternative to popular methods inside
scikit-learn such as Grid Search and Randomized Grid Search for
hyperparameters tuning, and from RFE (Recursive Feature Elimination),
Select From Model for feature selection.

Sklearn-genetic-opt uses evolutionary algorithms from the DEAP
(Distributed Evolutionary Algorithms in Python) package to choose the
set of hyperparameters that optimizes (max or min) the cross-validation
scores, it can be used for both regression and classification problems.

Documentation: https://sklearn-genetic-opt.readthedocs.io/}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
Obsoletes:      python-%{pypi_name}-doc < 0.11.1

%description -n python3-%{pypi_name} %_description

# `mlflow`, `tensorflow` and, by extension, `all` extras cannot be
# provided due to required dependencies not being available in Fedora.
%pyproject_extras_subpkg -n python3-%{pypi_name} seaborn

%prep
%forgeautosetup -p1
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/ --cov[^[:blank:]]+//g' pytest.ini

%generate_buildrequires
%pyproject_buildrequires -x seaborn

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l sklearn_genetic

%check
%if %{with tests}
# test_tensorboard_callback fails due to missing tensorflow dep
# https://github.com/rodrigo-arenas/Sklearn-genetic-opt/issues/134
k="${k-}${k+ and }not test_tensorboard_callback"
# Two failing tests in Python3.12. Disable for now.
# TODO: Investigate and report failing tests upstream.
k="${k-}${k+ and }not test_wrong_scheduler_methods"
k="${k-}${k+ and }not test_wrong_dimension"
# Exclude `test_mlflow` (`mlflow` is not packaged in Fedora)
%pytest -v --ignore sklearn_genetic/tests/test_mlflow.py ${k+-k }"${k-}"
%else
%pyproject_check_import
%endif

%files -n python3-sklearn-genetic-opt -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
