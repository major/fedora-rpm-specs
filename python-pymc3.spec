
# Disabled by default
%bcond_with check

%global srcname pymc3

Name: python-%{srcname}
Version: 3.11.4
Release: 6%{?dist}
Summary: Exploratory analysis of Bayesian models

License: ASL 2.0 and MIT and BSD
# pymc3/variational/updates.py is MIT
# the following files are generated from sphinx templates
# the license of the template is BSD
# these files are not currently installed
# pymc3/source/semantic_sphinx/static/searchtools.js
# pymc3/source/semantic_sphinx/static/highlight.min.js
# pymc3/source/semantic_sphinx/search.html
URL: https://docs.pymc.io/
Source0: %{pypi_source}

BuildArch: noarch

%global _description %{expand:
PyMC3 is a Python package for Bayesian statistical modeling 
and Probabilistic Machine Learning focusing on advanced 
Markov chain Monte Carlo (MCMC) and 
variational inference (VI) algorithms. 
Its flexibility and extensibility make it applicable 
to a large suite of problems.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with check}
# Testing is extremely slow
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist semver}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist theano-pymc}
BuildRequires:  %{py3_dist dill}
BuildRequires:  %{py3_dist cachetools}
BuildRequires:  %{py3_dist pandas}
BuildRequires:  %{py3_dist arviz}
BuildRequires:  %{py3_dist h5py}
BuildRequires:  %{py3_dist tqdm}
%endif
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{pypi_name}.egg-info
# Remove shebang
sed -i -e "1d" pymc3/distributions/multivariate.py

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_ADDOPTS='-p no:cacheprovider'
pushd %{buildroot}%{python3_sitelib}
  py.test-%{python3_version} -v pymc3 
popd
%endif

%files -n python3-%{srcname}
#%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.11.4-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.11.4-3
- Rebuilt for Python 3.11

* Fri Feb 11 2022 Sergio Pascual <sergiopr@fedoraproject.org> - 3.11.4-2
- New upstream source (3.11.4)
- Now with sources

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 3.11.2-2
- New upstream source (3.11.2)
- Do not edit requirements.txt

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.9.3-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 3.9.3-3
- Require theano-pymc

* Sun Sep 20 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 3.9.3-2
- Remove egg info

* Wed Jul 08 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 3.9.3-1
- New upstream source (3.9.3)

* Tue Jun 09 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 3.8-3
- Add additional licenses

* Wed May 27 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 3.8-2
- Add a conditional for tests

* Tue May 26 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 3.8-1
- Initial spec file

