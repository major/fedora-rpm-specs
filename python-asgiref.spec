%global common_description %{expand:
ASGI is a standard for Python asynchronous web apps and servers to communicate
with each other, and positioned as an asynchronous successor to WSGI.  This
package includes ASGI base libraries, such as:

* Sync-to-async and async-to-sync function wrappers, asgiref.sync
* Server base classes, asgiref.server
* A WSGI-to-ASGI adapter, in asgiref.wsgi}

%bcond tests 1

Name:           python-asgiref
Version:        3.7.2
Release:        %autorelease
Summary:        ASGI specs, helper code, and adapters
# main source code is BSD-3-Clause
# bundled async-timeout is Apache-2.0
License:        BSD-3-Clause AND Apache-2.0
URL:            https://github.com/django/asgiref
Source:         %{pypi_source asgiref}
BuildArch:      noarch


%description %{common_description}


%package -n python3-asgiref
Summary:        %{summary}
BuildRequires:  python3-devel
# https://github.com/django/asgiref/commit/9c6df6e02700092eb19adefff3552d44388f69b8
# This code is modified and probably cannot be unvendored.
Provides:       bundled(python3dist(async-timeout)) == 3.0.1


%description -n python3-asgiref %{common_description}


%prep
%autosetup -n asgiref-%{version}

# avoid additional mypy build requirement
sed '/^\s*mypy\s*>=/d' -i setup.cfg



%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x tests}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files asgiref


%check
%if %{with tests}
%pytest --verbose
%else
%pyproject_check_import
%endif


%files -n python3-asgiref -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
