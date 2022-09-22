%bcond_without tests

%global pretty_name imbalanced-learn
%global lib_name imblearn
%global extract_name imbalanced_learn

%global _description %{expand:
imbalanced-learn is a python package offering a number of re-sampling techniques
commonly used in datasets showing strong between-class imbalance. It is
compatible with scikit-learn and is part of scikit-learn-contrib projects.}


Name:           python-%{pretty_name}
Version:        0.9.1
Release:        1%{?dist}
Summary:        A Python Package to Tackle the Imbalanced Datasets in Machine Learning

License:        MIT
URL:            https://github.com/scikit-learn-contrib/%{pretty_name}
Source0:        %{pypi_source imbalanced-learn}

BuildArch:      noarch

%description %_description

%package -n python3-%{pretty_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}

#main deps
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist scikit-learn}
BuildRequires:  %{py3_dist joblib}
BuildRequires:  %{py3_dist matplotlib}

#for tests
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-cov}

%description -n python3-%{pretty_name} %_description

%prep
%autosetup -n %{pretty_name}-%{version}
rm -rvf %{pretty_name}.egg-info

%build
%py3_build

%install
%py3_install
# Remove extra install files
rm -rvf %{buildroot}/%{python3_sitelib}/tests

%if %{with tests}
%check
# some tests are skipped, because of keras and tensorflow deps
%pytest -k 'not test_all_estimators and not test_classification_report_imbalanced_multiclass_with_unicode_label and not test_rusboost and not test_cluster_centroids_n_jobs and not test_fit_docstring and not keras and not test_function_sampler_validate'
%endif

%files -n python3-%{pretty_name}
%license LICENSE
%doc README.rst examples/
%{python3_sitelib}/%{extract_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{lib_name}

%changelog
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

