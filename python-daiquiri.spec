%global pypi_name daiquiri

Name:           python-%{pypi_name}
Version:        3.0.1
Release:        1%{?dist}
Summary:        Library to configure Python logging easily

License:        ASL 2.0
URL:            https://github.com/jd/daiquiri
Source0:        %pypi_source
BuildArch:      noarch
 
 
%description
The %{pypi_name} library provides an easy way to configure Python logging.
It also provides some custom formatters and handlers.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        Library to configure Python logging easily

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

BuildRequires:  python%{python3_pkgversion}-devel
Requires:       python%{python3_pkgversion}-json-logger

%description -n python%{python3_pkgversion}-%{pypi_name}
The %{pypi_name} library provides an easy way to configure Python logging.
It also provides some custom formatters and handlers.


%package -n python-%{pypi_name}-doc
Summary:        daiquiri documentation

BuildRequires:  python%{python3_pkgversion}-sphinx

%description -n python-%{pypi_name}-doc
Documentation for daiquiri

%generate_buildrequires
%pyproject_buildrequires -x test

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%pyproject_wheel

# generate html docs 
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files daiquiri

%check
%pytest

%files -n python%{python3_pkgversion}-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Tue Jan 31 2023 Joel Capitao <jcapitao@redhat.com> - 3.0.1-1
- Update to latest upstream (#1482280)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.5.0-14
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.0-11
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.5.0-2
- Subpackage python2-daiquiri has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sun Sep 16 2018 Haïkel Guémar <hguemar@fedoraproject.org> - 1.5.0-1
- Upstream 1.5.0
- Fix FTFBS (RHBZ#1605649)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.1-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Jul 26 2017 Pradeep Kilambi <pkilambi@redhat.com> - 1.2.1-1
- Rebase to 1.2.1

* Mon Jun 12 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 0.1.0-1
- Upstream 0.1.0

* Thu May 25 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 0.0.1-1
- Initial package.
