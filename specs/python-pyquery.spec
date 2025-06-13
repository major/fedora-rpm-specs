%global real_name pyquery

%if 0%{?rhel}
%bcond_with tests
%else
%bcond_without tests
%endif

Name:           python-%{real_name}
Version:        2.0.1
Release:        %autorelease
Summary:        A jQuery-like library for python
License:        BSD-3-Clause
URL:            http://pypi.python.org/pypi/pyquery
Source0:        %pypi_source pyquery

# skip a test that needs network
Patch:          python-pyquery-skip-test-requiring-net-connection.patch
BuildArch:      noarch


%global _description\
python-pyquery allows you to make jQuery queries on XML documents. The API is\
as much as possible the similar to jQuery. python-pyquery uses lxml for fast\
XML and HTML manipulation.

%description %_description

%package -n python3-pyquery
Summary:        A jQuery-like library for python3
BuildRequires:  python3-devel

# test deps
BuildRequires:  python3-cssselect
BuildRequires:  python3-lxml >= 2.1
BuildRequires:  python3-requests
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-webob
BuildRequires:  python3-webtest
%endif

Requires:       python3-lxml >= 2.1
Requires:       python3-cssselect

%description -n python3-pyquery
python3-pyquery allows you to make jQuery queries on XML documents. The API is 
as much as possible the similar to jQuery. python-pyquery uses lxml for fast 
XML and HTML manipulation.


%prep
%autosetup -n %{real_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l pyquery


%check
%if %{with tests}
%pytest
%endif

%files -n python3-pyquery -f %{pyproject_files}
%doc CHANGES.rst README.rst

%changelog
%autochangelog
