%bcond_with tests

%global pypi_name scikit-uplift
%global short_name sklift
%global pretty_name scikit_uplift

%global _description %{expand:
scikit-uplift (sklift) is an uplift modeling python package that provides 
fast sklearn-style models implementation, evaluation metrics and visualization
tools. Uplift modeling estimates a causal effect of treatment and uses it to 
effectively target customers that are most likely to respond to a marketing
campaign.}

Name:           python-%{pypi_name}
Version:        0.5.1
Release:        9%{?dist}
Summary:        Uplift modeling in scikit-learn style in python

License:        MIT
URL:            https://github.com/maks-sh/scikit-uplift
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%package -n python-%{pypi_name}-doc
Summary:        Scikit-uplift documentation

%description -n python-%{pypi_name}-doc
Documentation for scikit-uplift package

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
# No setup.cfg, tox.ini or pyproject.toml
echo 'python3dist(pip) >= 19'
echo 'python3dist(packaging)'
echo 'python3dist(setuptools) >= 40.8'
echo 'python3dist(wheel)'
echo 'python3dist(sphinx)'
echo 'python3dist(myst-parser)'
echo 'python3dist(recommonmark)'
echo 'python3dist(sphinxcontrib-bibtex)'
echo 'python3dist(sphinx-rtd-theme)'
echo 'python3dist(pytest)'
echo 'python3dist(scikit-learn)'
echo 'python3dist(pandas)'
echo 'python3dist(myst-parser)'
echo 'python3dist(tqdm)'

%build
%pyproject_wheel

# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install

# Remove extra install files
rm -rf %{buildroot}/%{python3_sitelib}/tests

%pyproject_save_files %{short_name}

%check
%if %{with tests}
# Disable network tests
%pytest -k 'not test_fetch_hillstrom and not test_fetch_criteo10 and not test_return_X_y_t'
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc Readme.rst

%files -n python-%{pypi_name}-doc
%doc html
%doc notebooks/
%license LICENSE

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.5.1-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Python Maint <python-maint@redhat.com> - 0.5.1-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Aug 28 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.5.1-1
- Upgrade to 0.5.1

* Tue Aug 9 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.5.0-1
- Upgrade to 0.5.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 04 2022 Python Maint <python-maint@redhat.com> - 0.4.1-2
- Rebuilt for Python 3.11

* Sat Jun 18 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.1-1
- Update to 0.4.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 10 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.0-1
- New version of package

* Fri Jul 23 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.2-1
- Initial package
