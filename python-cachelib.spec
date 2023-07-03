%global srcname cachelib

Name:           python-%{srcname}
Version:        0.10.0
Release:        4%{?dist}
Summary:        A collection of cache libraries with a common API

License:        BSD-3-Clause
URL:            https://pypi.org/project/cachelib/
Source0:        %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
A collection of cache libraries with a common API.

Extracted from Werkzeug.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  memcached
BuildRequires:  redis
BuildRequires:  python3-devel
BuildRequires:  python3-pylibmc
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-xprocess
BuildRequires:  python3-redis
BuildRequires:  python3dist(setuptools)

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files cachelib


%check
# uWSGI is not packaged for Fedora and there is no straightforward way to test
# Amazon DynamoDB so skip tests for these backends.
%pytest -v -r s -k 'not Uwsgi and not DynamoDb'


%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGES.rst
%doc README.rst


%changelog
* Sat Jul 01 2023 Python Maint <python-maint@redhat.com> - 0.10.0-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Matěj Grabovský <mgrabovs@redhat.com> - 0.10.0-2
- Fix tests runner

* Tue Jan 10 2023 Matěj Grabovský <mgrabovs@redhat.com> - 0.10.0-1
- New upstream release

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Matěj Grabovský <mgrabovs@redhat.com> - 0.9.0-2
- Fix link to unit tests

* Mon Jun 27 2022 Matěj Grabovský <mgrabovs@redhat.com> - 0.9.0-1
- New upstream release

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.7.0-2
- Rebuilt for Python 3.11

* Mon May 16 2022 Matěj Grabovský <mgrabovs@redhat.com> - 0.7.0-1
- New upstream release

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Matěj Grabovský <mgrabovs@redhat.com> - 0.6.0-1
- New upstream release

* Fri Jan 07 2022 Matěj Grabovský <mgrabovs@redhat.com> - 0.5.0-1
- New upstream release 0.5.0

* Tue Oct 05 2021 Matěj Grabovský <mgrabovs@redhat.com> - 0.4.1-1
- New upstream release

* Mon Oct 04 2021 Matěj Grabovský <mgrabovs@redhat.com> - 0.4.0-1
- New upstream release

* Sat Aug 14 2021 Matěj Grabovský <mgrabovs@redhat.com> - 0.3.0-1
- New upstream release

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 25 2021 Matěj Grabovský <mgrabovs@redhat.com> - 0.2.0-1
- New upstream release

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Matěj Grabovský <mgrabovs@redhat.com> - 0.1.1-1
- Initial package
