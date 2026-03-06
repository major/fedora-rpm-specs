# tests require a running Redis server
%bcond tests 0

%global pypi_name django-redis
%global modname django_redis

Name:           python-%{pypi_name}
Version:        6.0.0
Release:        %autorelease
Summary:        Full featured redis cache backend for Django

License:        BSD-3-Clause
URL:            https://github.com/niwinz/django-redis
Source0:        https://github.com/niwinz/%{pypi_name}/archive/%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%description
Full featured redis cache backend for Django.


%package -n     python3-%{pypi_name}
Summary:        Full featured redis cache backend for Django

BuildRequires:  python3-devel
%if %{with tests}
# from the testenv section in setup.cfg
# the macro can't pick these up
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(lz4) >= 0.15
BuildRequires:  python3dist(msgpack) >= 0.6.0
BuildRequires:  python3dist(pyzstd) >= 0.15
%endif

%description -n python3-%{pypi_name}
Full featured redis cache backend for Django.


%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{modname}


%check
%if %{with tests}
%pyproject_check_import
%pytest -v
%else
%pyproject_check_import -e django_redis.compressors.lz4 -e django_redis.compressors.zstd  -e django_redis.serializers.msgpack
%endif


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
