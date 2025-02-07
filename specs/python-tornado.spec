%global srcname tornado
%global common_description %{expand:
Tornado is an open source version of the scalable, non-blocking web
server and tools.

The framework is distinct from most mainstream web server frameworks
(and certainly most Python frameworks) because it is non-blocking and
reasonably fast. Because it is non-blocking and uses epoll, it can
handle thousands of simultaneous standing connections, which means it is
ideal for real-time web services.}

Name:           python-%{srcname}
Version:        6.4.2
Release:        %autorelease
Summary:        Scalable, non-blocking web server and tools

License:        Apache-2.0 
URL:            https://www.tornadoweb.org
Source0:        https://github.com/tornadoweb/tornado/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel

%description %{common_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{common_description}

%package doc
Summary:        Examples for %{name}

%description doc %{common_description}

This package contains some example applications.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
# Skip the same timing-related tests that upstream skips when run in Travis CI.
# https://github.com/tornadoweb/tornado/commit/abc5780a06a1edd0177a399a4dd4f39497cb0c57
export TRAVIS=true

# Increase timeout for tests on riscv64
%ifarch riscv64
export ASYNC_TEST_TIMEOUT=80
%endif

%{py3_test_envvars} %{python3} -m tornado.test

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%files doc
%license LICENSE
%doc demos

%changelog
%autochangelog
