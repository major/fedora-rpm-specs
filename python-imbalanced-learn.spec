%bcond_without tests

Name:           python-imbalanced-learn
Version:        0.11.0
Release:        %autorelease
Summary:        A Python Package to Tackle the Imbalanced Datasets in Machine Learning

# The entire source is (SPDX) MIT; some other licenses are mentioned in
# doc/sphinxext/LICENSE.txt, but the code to which they apply does not seem to
# be present, and the directory is removed in %%prep anyway.
License:        MIT
URL:            https://github.com/scikit-learn-contrib/imbalanced-learn
Source0:        %{pypi_source imbalanced-learn}

BuildArch:      noarch

BuildRequires:  python3-devel

# We cannot generate BR’s from the “optional” extra because some of the
# dependencies that are added are not packaged. This also applies to the
# “tests” extra.i See imblearn/_min_dependencies.py for the actual definitions
# of extras and for minimum versions of dependencies. However, we still want
# any dependencies (other than coverage analysis, linters, etc.) that *are*
# available for testing, so we add them manually:

# optionals, docs, examples, tests:
BuildRequires:  python3dist(pandas) >= 1.0.5
# Not packaged:
# BuildRequires:  python3dist(keras) >= 2.4.3
# BuildRequires:  python3dist(tensorflow) >= 2.4.3

# tests
BuildRequires:  python3dist(pytest) >= 5.0.1
# Dependencies such as pytest-cov, flake8, black, and mypy are omitted:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters

%global _description %{expand:
imbalanced-learn is a python package offering a number of re-sampling
techniques commonly used in datasets showing strong between-class imbalance. It
is compatible with scikit-learn and is part of scikit-learn-contrib projects.}

%description %_description


%package -n python3-imbalanced-learn
Summary:        %{summary}

%description -n python3-imbalanced-learn %_description


%prep
%autosetup -n imbalanced-learn-%{version}

# Remove the bundled Sphinx extensions. We don’t build the documentation, so we
# don’t need to make an effort to unbundle them.
rm -vrf doc/sphinxext/


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l imblearn


%if %{with tests}
%check
# some tests are skipped, because of keras and tensorflow deps
k="${k-}${k+ and }not test_all_estimators"
k="${k-}${k+ and }not test_classification_report_imbalanced_multiclass_with_unicode_label"
k="${k-}${k+ and }not test_rusboost"
k="${k-}${k+ and }not test_cluster_centroids_n_jobs"
k="${k-}${k+ and }not test_fit_docstring"
k="${k-}${k+ and }not keras"
k="${k-}${k+ and }not test_function_sampler_validate"
%pytest -k "${k-}"
%endif


%files -n python3-imbalanced-learn -f %{pyproject_files}
%doc README.rst examples/


%changelog
%autochangelog
