%bcond_without check

%global _description %{expand: 
Scikit-learn integrates machine learning algorithms in the tightly-knit 
scientific Python world, building upon numpy, scipy, and matplotlib. 
As a machine-learning module, it provides versatile tools for data mining 
and analysis in any field of science and engineering. It strives to be 
simple and efficient, accessible to everybody, and reusable 
in various contexts.}

%global base_version 1.8.0
# Comment this line out when updating to stable
%global prerel rc1
%global upstream_version %{base_version}%{?prerel}

Name: python-scikit-learn
Version: %{base_version}%{?prerel:~%{prerel}}
Release: %autorelease
Summary: Machine learning in Python
# sklearn/externals/_arff.py is MIT
# sklearn/externals/_packaging is BSD-2-Clause
# sklearn/metrics/_scorer.py is BSD-2-Clause
# sklearn/datasets/images/china.jpg  is CC-BY-2.0
# sklearn/datasets/images/flower.jpg is CC-BY-2.0
# sklearn/utils/_pprint.py is PSF-2.0
License: BSD-3-Clause AND CC-BY-2.0 AND MIT AND BSD-2-Clause AND PSF-2.0

URL: http://scikit-learn.org/
Source0: %{pypi_source scikit_learn}

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: python3-devel
BuildRequires: %{py3_dist setuptools}
BuildRequires: %{py3_dist psutil}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%description %_description

%package -n python3-scikit-learn
Summary: %{summary}

# For a brief moment, this package was accidentally named this way
# The Obsoletes clears the upgrade path and can be removed when Rawhide is F44
Obsoletes: python3-scikit_learn < 1.5.2-2

%if %{with check}
BuildRequires: %{py3_dist pytest} >= 7.1.2
BuildRequires: %{py3_dist joblib} >= 1.2.0
BuildRequires: %{py3_dist threadpoolctl} >= 2.0.0
%endif

%{?python_provide:%python_provide python3-sklearn}

%description -n python3-scikit-learn
%_description

%prep
%autosetup -n scikit_learn-%{upstream_version} -p1
sed -i -e 's|numpy>=2,<2.4.0|numpy|' pyproject.toml
# EPEL 10 has Cython 3.0.9, and the only reason Cython 3.0.10
# is required upstream is for Windows, see
# https://github.com/scikit-learn/scikit-learn/pull/28743
sed -i -e 's|cython>=3.1.2|cython>=3.0.9|' pyproject.toml
sed -i -e 's|CYTHON_MIN_VERSION = "3.1.2"|CYTHON_MIN_VERSION = "3.0.9"|' sklearn/_min_dependencies.py
find sklearn/metrics/_dist_metrics.pyx.tp -type f | xargs sed -i 's/cdef inline {{INPUT_DTYPE_t}} rdist/cdef {{INPUT_DTYPE_t}} rdist/g'
# Remove upper bound on meson-python version; weirdly, this is in the PyPI
# sdist but not in git.
sed -r -i 's/"(meson-python[^"]+.*),<[^"]+"/"\1"/' pyproject.toml

%generate_buildrequires
# Some tests packages not in Fedora
%pyproject_buildrequires -p

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files sklearn

%check
%if %{with check}
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_ADDOPTS='-p no:cacheprovider'
pushd %{buildroot}%{python3_sitearch}
  pytest  \
%if 0%{?el10}
  --deselect "sklearn/tests/test_common.py::test_estimators[ARDRegression(max_iter=5)-check_dont_overwrite_parameters]" \
  --deselect "sklearn/tests/test_common.py::test_estimators[ARDRegression(max_iter=5)-check_f_contiguous_array_estimator]" \
  --deselect "sklearn/tests/test_common.py::test_estimators[ARDRegression(max_iter=5)-check_regressors_no_decision_function]" \
  --deselect "sklearn/tests/test_common.py::test_estimators[ARDRegression(max_iter=5)-check_methods_sample_order_invariance]" \
  --deselect "sklearn/tests/test_common.py::test_estimators[ARDRegression(max_iter=5)-check_methods_subset_invariance]" \
  --deselect "sklearn/tests/test_common.py::test_estimators[ARDRegression(max_iter=5)-check_fit2d_1feature]" \
  --deselect "sklearn/tests/test_common.py::test_estimators[ARDRegression(max_iter=5)-check_dict_unchanged]" \
  --deselect "sklearn/tests/test_common.py::test_estimators[ARDRegression(max_iter=5)-check_fit2d_predict1d]" \
  --deselect "sklearn/tests/test_common.py::test_estimators[EllipticEnvelope()-check_fit2d_1feature]" \
  --deselect "sklearn/tests/test_common.py::test_estimators[EmpiricalCovariance()-check_fit2d_1feature]" \
  --deselect "sklearn/tests/test_common.py::test_estimators[FastICA(max_iter=5)-check_dont_overwrite_parameters]" \
  --deselect "sklearn/tests/test_common.py::test_estimators[FastICA(max_iter=5)-check_methods_sample_order_invariance]" \
  --deselect "sklearn/tests/test_common.py::test_estimators[FastICA(max_iter=5)-check_methods_subset_invariance]" \
  --deselect "sklearn/tests/test_common.py::test_estimators[FastICA(max_iter=5)-check_fit2d_1feature]" \
  --deselect "sklearn/tests/test_common.py::test_estimators[FastICA(max_iter=5,n_components=1)-check_dict_unchanged]" \
  --deselect "sklearn/tests/test_common.py::test_estimators[FastICA(max_iter=5)-check_fit2d_predict1d]" \
  --deselect "sklearn/tests/test_common.py::test_estimators[KernelPCA()-check_fit2d_1sample]" \
  --deselect "sklearn/tests/test_common.py::test_estimators[LedoitWolf()-check_fit2d_1feature]" \
  --deselect "sklearn/tests/test_common.py::test_estimators[MinCovDet()-check_fit2d_1feature]" \
  --deselect "sklearn/tests/test_common.py::test_estimators[OAS()-check_fit2d_1feature]" \
  --deselect "sklearn/tests/test_common.py::test_estimators[RidgeCV()-check_fit2d_1sample]" \
  --deselect "sklearn/tests/test_common.py::test_estimators[RidgeClassifierCV()-check_fit2d_1sample]" \
  --deselect "sklearn/tests/test_common.py::test_estimators[ShrunkCovariance()-check_fit2d_1feature]" \
  --deselect "sklearn/tests/test_common.py::test_check_inplace_ensure_writeable[ARDRegression(max_iter=5)]" \
%endif
  sklearn
popd

%else
%py3_check_import sklearn
%endif

%files -n python3-scikit-learn -f %{pyproject_files}
%doc examples/
%license COPYING sklearn/svm/src/liblinear/COPYRIGHT

%changelog
%autochangelog
