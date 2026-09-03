%global srcname cachelib

Name:           python-%{srcname}
Version:        0.16.1
Release:        %autorelease
Summary:        A collection of cache libraries with a common API
License:        BSD-3-Clause
URL:            https://github.com/pallets-eco/cachelib
Source0:        %{url}/archive/%{version}/cachelib-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
A collection of cache libraries with a common API.

Extracted from Werkzeug.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  memcached
BuildRequires:  redis
BuildRequires:  valkey
BuildRequires:  python3-boto3
BuildRequires:  python3-devel
BuildRequires:  python3-pylibmc
BuildRequires:  python3-pymongo
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-xprocess
BuildRequires:  python3-redis
BuildRequires:  python3-valkey

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l cachelib

%check
# uWSGI is not packaged for Fedora, and MongoDB / DynamoDB require external
# services without embedded mocks in upstream tests, so skip these backends.
%pytest -v -r s -k 'not Uwsgi and not DynamoDb and not MongoDb'

%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGES.rst README.md

%changelog
%autochangelog
