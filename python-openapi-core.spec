%global srcname openapi-core
%global modname openapi_core

Name:           python-%{srcname}
Version:        0.16.5
Release:        %autorelease
Summary:        OpenAPI client-side and server-side support

License:        BSD-3-Clause
URL:            https://github.com/p1c2u/%{srcname}
# The GitHub archive has the tests; the PyPI sdist does not.
Source:         %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

# Test dependencies; see [tool.poetry.dev-dependencies], but note that this
# contains both test dependencies and unwanted linters etc.
BuildRequires:  python3dist(djangorestframework)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(responses)
BuildRequires:  python3dist(starlette)
BuildRequires:  python3dist(strict-rfc3339)
BuildRequires:  python3dist(webob)

%global _description %{expand:
Openapi-core is a Python library that adds client-side and server-side
support for the OpenAPI v3.0 and OpenAPI v3.1 specification.}

%description %_description


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%pyproject_extras_subpkg -n python3-openapi-core django falcon flask requests starlette


%prep
%autosetup -n %{srcname}-%{version} -p1
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i '/^--cov[-=]/d' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -x django -x falcon -x flask -x requests -x starlette


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{modname}


%check
%pytest


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
%autochangelog
