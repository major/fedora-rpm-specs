%bcond_with check

%global srcname astroplan

Name:           python-%{srcname}
Version:        0.8
Release:        9%{?dist}
Summary:        Python package to help astronomers plan observations

License:        BSD
URL:            https://pypi.org/project/astroplan/
Source0:        %{pypi_source}
# https://github.com/astropy/astroplan/issues/416
Patch:          astroplan-fixed-apo.patch

BuildArch:      noarch


%global _description %{expand:
astroplan is an observation planning package for 
astronomers that can help you plan for everything but the clouds.

It is an in-development Astropy affiliated package that seeks to make your 
life as an observational astronomer a little less infuriating.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist setuptools_scm}
%if %{with check}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist astropy}
BuildRequires:  %{py3_dist pytz}
BuildRequires:  %{py3_dist pytest-astropy}
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist astroquery}
%endif
%{?python_provide:%python_provide python3-%{srcname}}
Recommends: %{py3_dist matplotlib}
Recommends: %{py3_dist astroquery}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_ADDOPTS='-p no:cacheprovider'
pushd %{buildroot}/%{python3_sitelib}
   pytest-%{python3_version} --remote-data=none astroplan 
popd
%endif


%files -n python3-%{srcname}
%license LICENSE.rst
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.8-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Python Maint <python-maint@redhat.com> - 0.8-2
- Rebuilt for Python 3.10

* Fri Jun 04 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 0.8-1
- New release 0.8
- Patch test that requires network access

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Sergio Pascual <sergio.pasra at gmail.com> - 0.6-1
- New release 0.6

* Sat Dec 07 2019 Sergio Pascual <sergio.pasra at gmail.com> - 0.5-2
- Fix project url
- Add check section

* Mon Nov 11 2019 Sergio Pascual <sergio.pasra at gmail.com> - 0.5-1
- Initial spec file

