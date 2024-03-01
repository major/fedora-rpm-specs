%global srcname cachelib

Name:           python-%{srcname}
Version:        0.12.0
Release:        %autorelease
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
#BuildRequires:  python3-pymongo
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
# MongoDb is new as of 0.12.0, however, it fails the test suite even with
# pymongo installed. Leave it disabled until fixed.
%pytest -v -r s -k 'not Uwsgi and not DynamoDb and not MongoDb'


%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGES.rst
%doc README.rst


%changelog
%autochangelog
