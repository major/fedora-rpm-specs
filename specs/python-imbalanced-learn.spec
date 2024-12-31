%bcond_without tests

Name:           python-imbalanced-learn
Version:        0.13.0
Release:        %autorelease
Summary:        A Python Package to Tackle the Imbalanced Datasets in Machine Learning

%global forgeurl https://github.com/scikit-learn-contrib/imbalanced-learn
%global tag %{version}
%forgemeta

# The entire source is (SPDX) MIT; some other licenses are mentioned in
# doc/sphinxext/LICENSE.txt, but the code to which they apply does not seem to
# be present, and the directory is removed in %%prep anyway.
License:        MIT
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel

# tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-xdist)
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

%pyproject_extras_subpkg -n python3-imbalanced-learn optional


%prep
%forgeautosetup -p1

# Remove the bundled Sphinx extensions. We don’t build the documentation, so we
# don’t need to make an effort to unbundle them.
rm -vrf doc/sphinxext/

# Remove obsolete sklearn-compat dependency. Upstream dropped it post
# release and it's not packaged for Fedora.
# https://github.com/scikit-learn-contrib/imbalanced-learn/commit/e511ddbf44f819f3777a2689eb7a87e77bf2a0e5
sed -i '/sklearn-compat/d' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -x optional


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
%pytest -v "${k+-k $k}" imblearn
%endif


%files -n python3-imbalanced-learn -f %{pyproject_files}
%doc README.rst examples/


%changelog
%autochangelog
