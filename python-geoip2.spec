%global pypi_name geoip2
%global srcname GeoIP2-python
%global desc This package provides an API for the GeoIP2 web services.
%global test_data MaxMind-DB
%global test_data_rls 2b37923df61aa3b5fb6c7edfbf4dc5fafa10258a

Name:           python-%{pypi_name}
Version:        4.7.0
Release:        2%{?dist}
Summary:        MaxMind GeoIP2 API

License:        Apache-2.0
URL:            https://www.maxmind.com/
Source0:        https://github.com/maxmind/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
Source1:        https://github.com/maxmind/%{test_data}/archive/%{test_data_rls}/%{test_data}-%{test_data_rls}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{_bindir}/sphinx-build

%description
%{desc}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{desc}

%package doc
Summary:        Documentation for %{name}

%description doc
This package provides the documentation for %{pypi_name}.

%prep
%autosetup -n %{srcname}-%{version} -a 1
rmdir tests/data
mv -f %{test_data}-%{test_data_rls} tests/data

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
sphinx-build -b html docs html
rm -rf html/.{buildinfo,doctrees}

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# tests/webservice_test.py requires mocket not available in Fedora
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} -m unittest tests/database_test.py tests/models_test.py

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%files doc
%doc html/
%license LICENSE

%changelog
* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 4.7.0-2
- Rebuilt for Python 3.12

* Mon May 15 2023 Lumír Balhar <lbalhar@redhat.com> - 4.7.0-1
- Update to 4.7.0 (rhbz#2198523)
- SPDX License

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 23 2022 Lumír Balhar <lbalhar@redhat.com> - 4.6.0-1
- Update to 4.6.0
Resolves: rhbz#2100065

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 4.5.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 19 2021 Lumír Balhar <lbalhar@redhat.com> - 4.5.0-1
- Update to 4.5.0
Resolves: rhbz#2024761

* Tue Oct 05 2021 Lumír Balhar <lbalhar@redhat.com> - 4.4.0-1
- Update to 4.4.0
Resolves#2006211

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.2.0-2
- Rebuilt for Python 3.10

* Fri May 14 2021 Lumír Balhar <lbalhar@redhat.com> - 4.2.0-1
- Update to 4.2.0
Resolves: rhbz#1960142

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 2020 Lumír Balhar <lbalhar@redhat.com> - 4.1.0-1
- Update to 4.1.0 (#1882861)

* Wed Jul 22 2020 Lumír Balhar <lbalhar@redhat.com> - 4.0.2-1
- Update to 4.0.2 (#1859400)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-2
- Rebuilt for Python 3.9

* Wed Feb 05 2020 Lumír Balhar <lbalhar@redhat.com> - 3.0.0-1
- New upstream version 3.0.0 (#1785833)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.9.0-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.9.0-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.9.0-5
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 23 2018 Carl George <carl@george.computer> - 2.9.0-3
- EPEL compatibility

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.9.0-2
- Rebuilt for Python 3.7

* Mon May 28 2018 Lumir Balhar <lbalhar@redhat.com> - 2.9.0-1
- Update to 2.9.0

* Thu Apr 12 2018 Lumir Balhar <lbalhar@redhat.com> - 2.8.0-1
- Update to 2.8.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.7.0-1
- Update to 2.7.0

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.6.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Nov 01 2017 Lumir Balhar <lbalhar@redhat.com> - 2.6.0-1
- New upstream version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 10 2017 Lumir Balhar <lbalhar@redhat.com> - 2.5.0-1
- Update to 2.5.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.4.2-2
- Rebuild for Python 3.6

* Tue Dec 13 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.4.2-1
- Update to 2.4.2

* Tue Nov 22 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.4.1-1
- Update to 2.4.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 15 2016 Lumir Balhar <lbalhar@redhat.com> - 2.4.0-1
- Initial package.
