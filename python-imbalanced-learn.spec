%bcond_without tests

Name:           python-imbalanced-learn
Version:        0.10.0
Release:        2%{?dist}
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
%pyproject_save_files imblearn


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
# pyproject_files handles LICENSE; verify with “rpm -qL -p …”
%doc README.rst examples/


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 0.10.0-1
- Update to 0.10.0 (close RHBZ#2152162)

* Wed Dec 14 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 0.9.1-2
- Remove bundled Sphinx extensions in %%prep
- Confirm License is SPDX MIT
- Drop unnecessary pytest-cov BR
- Port to pyproject-rpm-macros

* Sun Sep 11 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.9.1-1
- New version - 0.9.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 04 2022 Python Maint <python-maint@redhat.com> - 0.9.0-4
- Rebuilt for Python 3.11

* Thu Jan 27 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.9.0-3
- Disable one additional test

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.9.0-1
- New version - 0.9.0

* Wed Sep 29 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.8.1-1
- New version - 0.8.1

* Wed Jul 21 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.8.0-5
- Install additional docs

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.0-4
- Rebuilt for Python 3.10

* Tue Apr 20 22:59:49 CEST 2021 Robert-André Mauchin <zebob.m@gmail.com> - 0.8.0-3
- Remove unneeded patch
- Reenable tests

* Tue Mar 23 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.8.0-2
- New patch: use Fedora dependencies
- Remove provides macro

* Sat Mar 13 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.8.0-1
- New version - 0.8.0

* Sun Feb 14 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.7.0-5
- Removing dependency generator
- Fresh rebuilt

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.7.0-3
- disabling tests - too many problems with missing keras/tensorflow dependencies

* Fri Jan 8 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.7.0-2
- disabling one test - test_cluster_centroids_n_jobs

* Sun Nov 29 2020 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.7.0-1
- Initial package

