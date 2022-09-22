%global pypi_name sklearn-nature-inspired-algorithms
%global pretty_name sklearn_nature_inspired_algorithms
%global github_name Sklearn-Nature-Inspired-Algorithms

# Pulls in fonts, currently disabled
# We refer to upstream's documentation.
%bcond_with generated_docs
%bcond_with tests

%global _description %{expand:
Nature inspired algorithms for hyper-parameter tuning of scikit-learn models.
This package uses algorithms implementation from NiaPy.

Documentation is available at:
https://sklearn-nature-inspired-algorithms.readthedocs.io/en/stable/ }

Name:           python-%{pypi_name}
Version:        0.9.0
Release:        3%{?dist}
Summary:        Nature-inspired algorithms for scikit-learn

License:        MIT
URL:            https://github.com/timzatko/%{github_name}
Source0:        %{url}/archive/v%{version}/%{pretty_name}-%{version}.tar.gz
# Update pyproject.toml to match Fedora package versions

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  pyproject-rpm-macros
BuildRequires: %{py3_dist lockfile}
BuildRequires: %{py3_dist packaging}
BuildRequires: %{py3_dist pep517}
BuildRequires: %{py3_dist poetry}
BuildRequires: %{py3_dist wheel}
BuildRequires:  %{py3_dist toml-adapt}

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%if %{with generated_docs}
%package doc
Summary:        %{summary}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-cov}
%endif

%description doc
Generated documentation for %{name}.
%endif

%prep
%autosetup -n %{pretty_name}-%{version}
rm -rf %{pretty_name}.egg-info
rm -fv poetry.lock

# Make deps consistent with Fedora deps
toml-adapt -path pyproject.toml -a change -dep ALL -ver X

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

#not included in Pypi package
%if %{with generated_docs}
PYTHONPATH=. make -C docs SPHINXBUILD=sphinx-build-3 html
rm -rf docs/_build/html/{.doctrees,.buildinfo} -vf
%endif

%install
%pyproject_install
%pyproject_save_files sklearn_nature_inspired_algorithms

%check
%if %{with tests}
PYTHONPATH=%{buildroot}/%{python3_sitelib} %{__python3} -m unittest tests
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%if %{with generated_docs}
%files doc
%license LICENSE
%doc docs/_build/html
%endif

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 04 2022 Python Maint <python-maint@redhat.com> - 0.9.0-2
- Rebuilt for Python 3.11

* Mon May 23 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.9.0-1
- Update to the latest upstream's release

* Wed Apr 6 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.8.1-1
- Update to the latest upstream's release

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 31 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.7.1-1
- Update to the latest upstream's release

* Sat Oct 16 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.6.1-1
- Update to the latest upstream's release

* Fri Oct 8 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.6.0-3
- Use default scikit-learn dependency

* Sun Aug 22 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.6.0-2
- New version tag

* Sun Aug 1 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.6.0-1
- Update to the latest upstream's release

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.2-3
- Rebuilt for Python 3.10

* Fri May 14 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.5.2-2
- Re-enable tests

* Thu May 13 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.5.2-1
- Update to the latest upstream release
- Remove patch
- Remove unneeded macros

* Tue Apr 6 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.5.1-1
- New version

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.6-3
- Do not test - scikit problems (Will be re-enabled)

* Fri Oct 09 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.6-2
- Do not include generated docs: bundle lots of fonts
- Correct doc generation command

* Fri Aug 14 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.5-1
- Update to use poetry
- correct URLS
- add conditionals for test and docs

* Mon Jul 27 2020 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.5-1
- Initial package
