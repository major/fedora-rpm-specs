%global pypi_name diskcache

Name:           python-%{pypi_name}
Version:        5.2.1
Release:        4%{?dist}
Summary:        Disk and file backed persistent cache

License:        ASL 2.0
URL:            http://www.grantjenks.com/docs/diskcache/
Source0:        https://github.com/grantjenks/python-diskcache/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
DiskCache is an Apache 2 licensed disk and file backed cache library,
written in pure-Python, and compatible with Django. The cloud-based
computing of 2019 puts a premium on memory. Gigabytes of empty space 
is left on disks asprocesses vie for memory. Among these processes is
Memcached (and sometimes Redis) which is used as a cache. Wouldn't it 
be nice to leverage.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-django)
BuildRequires:  python3dist(django)
BuildRequires:  python3dist(pytest-xdist)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
DiskCache is an Apache 2 licensed disk and file backed cache library,
written in pure-Python, and compatible with Django. The cloud-based
computing of 2019 puts a premium on memory. Gigabytes of empty space 
is left on disks asprocesses vie for memory. Among these processes is
Memcached (and sometimes Redis) which is used as a cache. Wouldn't it 
be nice to leverage.

%prep
%autosetup -n python-%{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.2.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 23 2021 Fabian Affolter <mail@fabian-affolter.ch> - 5.2.1-1
- Update to latest upstream release 5.2.1

* Sun Dec 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 5.1.0-1
- Update to latest upstream release 5.1.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-3
- Rebuilt for Python 3.9

* Sun Jan 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.1.0-2
- Address issues (#1795068)

* Sun Jan 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.1.0-1
- Initial package
