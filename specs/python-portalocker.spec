# tests are enabled by default
%bcond_without  tests

# python-redis is missing from EPEL 9, but many of the tests will still run without
# it being present at test time. See BZ 2063713.
%if 0%{?el9} || 0%{?centos} >= 9
%global test_with_redis 0
%else
%global test_with_redis 1
%endif

%global         srcname     portalocker
%global         forgeurl    https://github.com/WoLpH/portalocker
Version:        3.2.0
%global         tag         v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Library to provide an easy API to file locking

License:        BSD-3-Clause
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(flaky)
%if 0%{?test_with_redis}
BuildRequires:  python3dist(redis)
%endif
%endif

%global _description %{expand:
%{summary}}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%description -n python3-%{srcname} %{_description}


%prep
%forgeautosetup
# Upstream uses some coverage plugins we don't have, and also set it to fail
# under 100 coverage, but they don't have anywhere near that coverage so turn
# a lot of that nonsense off. Upstream CI seems to eternally fail so...
sed -i 's/^plugins =.*coverage_conditional_plugin.*$/plugins = []/' pyproject.toml
sed -i 's/^timeout =.*$//' pyproject.toml
sed -i 's/^fail_under = 100$//' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l portalocker


%check
%if %{test_with_redis}
%pyproject_check_import
%else
%pyproject_check_import -e portalocker.redis
%endif

%if %{with tests}
# These two tests are failing and upstream CI has no recent successes.
%pytest %{?test_with_redis:--ignore=portalocker_tests/test_redis.py} \
  --deselect=portalocker_tests/test_multiprocess.py::test_shared_processes[True] \
  --deselect=portalocker_tests/test_multiprocess.py::test_shared_processes[False]
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
