%global srcname asgiref

%global common_description %{expand:
ASGI is a standard for Python asynchronous web apps and servers to communicate
with each other, and positioned as an asynchronous successor to WSGI.  This
package includes ASGI base libraries, such as:

* Sync-to-async and async-to-sync function wrappers, asgiref.sync
* Server base classes, asgiref.server
* A WSGI-to-ASGI adapter, in asgiref.wsgi}

%bcond_without  tests


Name:           python-%{srcname}
Version:        3.4.1
Release:        %autorelease
Summary:        ASGI specs, helper code, and adapters
# This is BSD + bundled async-timeout ASL 2.0
License:        BSD and ASL 2.0
URL:            https://github.com/django/asgiref
# PyPI tarball doesn't have tests
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch


%description %{common_description}


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
# https://github.com/django/asgiref/commit/9c6df6e02700092eb19adefff3552d44388f69b8
Provides:       bundled(python3dist(async-timeout)) == 3.0.1


%description -n python3-%{srcname} %{common_description}


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-e %{toxenv}-test}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%if %{with tests}
%check
%tox -e %{toxenv}-test
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
%autochangelog
