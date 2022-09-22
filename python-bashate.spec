%global pypi_name bashate


Name:           python-%{pypi_name}
Version:        2.1.0
Release:        5%{?dist}
Summary:        A pep8 equivalent for bash scripts

License:        ASL 2.0
URL:            https://pypi.org/project/%{pypi_name}/
Source0:        %{pypi_source}

BuildArch:      noarch

%description
It is a pep8 equivalent for bash scripts.
This program attempts to be an automated style checker for bash scripts
to fill the same part of code review that pep8 does in most OpenStack
projects. It started from humble beginnings in the DevStack project,
and will continue to evolve over time.

%package -n python3-%{pypi_name}
Summary:        A pep8 equivalent for bash scripts
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3dist(fixtures)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(pbr)
# deps for check
BuildRequires:  python3dist(autopage)
BuildRequires:  python3dist(stestr)

Requires:       python3dist(babel)
Requires:       python3dist(pbr)
Requires:       python3dist(setuptools)


%description -n python3-%{pypi_name}
It is a pep8 equivalent for bash scripts.
This program attempts to be an automated style checker for bash scripts
to fill the same part of code review that pep8 does in most OpenStack
projects. It started from humble beginnings in the DevStack project,
and will continue to evolve over time.


%package -n python-%{pypi_name}-doc
Summary: Documentation for bashate module

BuildRequires:  python3-oslo-sphinx
BuildRequires:  python3dist(openstackdocstheme)
BuildRequires:  python3dist(reno)
BuildRequires:  python3dist(sphinx)


%description -n python-%{pypi_name}-doc
Documentation for the bashate module

%prep
%autosetup -S git -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
rm -rf {test-,}requirements.txt

%build
#remove shebang
sed -i -e '1{\@^#!/usr/bin/env python@d}' bashate/bashate.py
# doc
sphinx-build-3 -b html -d build/doctrees  doc/source doc/build/html
rm -rf doc/build/html/.{doctrees,buildinfo}

%py3_build

%install
%py3_install

%check
stestr --test-path ./bashate/tests run

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%exclude %{python3_sitelib}/%{pypi_name}/tests

%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 2.1.0-4
- Rebuilt for Python 3.11

* Wed Jan 26 2022 Mikel Olasagasti Uranga <mikel@olasagasti.info> 2.1.0-3
- Add missing BR for autopage now required for rawhide/F36

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 23 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> 2.1.0-1
- Update to 2.1.0 (#2003597)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Mikel Olasagasti Uranga <mikel@olasagasti.info> 2.0.0-2
- BZ#1900508 fix for Python-3.10

* Tue Oct 27 2020 Mikel Olasagasti Uranga <mikel@olasagasti.info> 2.0.0-1
- Update to 2.0.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Alan Pevec <alan.pevec@redhat.com> 0.6.0-1
- Update to 0.6.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-11
- Subpackage python2-bashate has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-8
- Rebuilt for Python 3.7

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.1-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Jun 25 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 0.5.1-1
- Upstream 0.5.1
- Fix python3 support (RHBZ#1314529)
- Use pypi.io URL

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 22 2015 Chandan Kumar <chkumar246@gmail.com> - 0.3.2-1
- Bumped to version 0.3.2
- Added missing test dependencies

* Wed Sep 30 2015 Chandan Kumar <chkumar246@gmail.com> -0.3.1-2
- Added python2 and python3 subpackage

* Wed Aug 12 2015 chandankumar <chkumar246@gmail.com> - 0.3.1-1
- Initial package.
