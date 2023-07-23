%global pypi_name requests-unixsocket

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        8%{?dist}
Summary:        Use requests to talk HTTP via a UNIX domain socket

License:        ASL 2.0
URL:            https://github.com/msabramo/requests-unixsocket
Source0:        https://pypi.python.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%description
%{summary}.

%package -n     python3-%{pypi_name}
Summary:        Use requests to talk HTTP via a UNIX domain socket
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(requests)

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pbr)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(urllib3)
BuildRequires:  python3dist(waitress)

%description -n python3-%{pypi_name}
%{summary}.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove shebangs
sed -i '1d' requests_unixsocket/tests/test_requests_unixsocket.py
sed -i '1d' setup.py

# Remove pytest-pep8 invocation. Not packaged in Fedora
rm pytest.ini
sed -i '/pytest-pep8/d' test-requirements.txt
# pytest-capturelog isn't actually used, removing it. it's not in Fedora either
sed -i '/pytest-capturelog/d' test-requirements.txt

%build
%py3_build

%install
%py3_install


%check
%{__python3} -m pytest -v

%files -n python3-%{pypi_name} 
%doc README.rst
%license LICENSE
%{python3_sitelib}/requests_unixsocket
%{python3_sitelib}/requests_unixsocket-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.2.0-7
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.0-4
- Rebuilt for Python 3.11

* Tue Feb 08 2022 Dan Radez <dradez@redhat.com> - 0.2.0-3
- Don't remove egginfo

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 04 2022 Dan Radez <dradez@redhat.com> - 0.2.0-1
- update to 0.2.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 0.1.5-10
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 2 2019 Dan Radez <dradez@redhat.com> - 0.1.5-2
- Updates to initial package to address review comments
* Tue Mar  8 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 0.1.5-1
- Initial package.
