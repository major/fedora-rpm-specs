%bcond falcon 1

%global srcname openapi-core
%global modname openapi_core

Name:           python-%{srcname}
Version:        0.19.4
Release:        %autorelease
Summary:        OpenAPI client-side and server-side support

License:        BSD-3-Clause
URL:            https://github.com/python-openapi/%{srcname}
Source:         %{pypi_source %{modname}}

# Bump aioitertools from 0.11.0 to 0.12.0
# https://github.com/python-openapi/openapi-core/pull/907
Patch:          0001-Bump-aioitertools-from-0.11.0-to-0.12.0.patch
# Allow Starlette 0.41.x and FastAPI 0.115.x
# https://github.com/python-openapi/openapi-core/pull/933/commits/6db7a187939753a292b2b4704bd620632491d196
#
# From:
#
# Allow Starlette 0.41.x and FastAPI 0.115.x; bump to 0.41.2 and 0.115.4,
# respectively
# https://github.com/python-openapi/openapi-core/pull/933
Patch:          0002-Allow-Starlette-0.41.x-and-FastAPI-0.115.x.patch
# Allow Starlette 0.45.x
#
# We can’t offer this upstream until a released version of FastAPI
# officially supports Starlette 0.45.x.
Patch:          0003-Allow-Starlette-0.45.x.patch

BuildArch:      noarch
BuildRequires:  python3-devel

# Test dependencies; see [tool.poetry.dev-dependencies], but note that this
# contains both test dependencies and unwanted linters etc., as well as some
# packages that are not directly required by the tests, such as webob and
# strict-rfc3339.
BuildRequires:  python3dist(pytest) >= 8
BuildRequires:  python3dist(pytest-aiohttp)
BuildRequires:  python3dist(responses)

# This is not directly imported in the tests, but is implicitly required for
# some of the Django integration tests.
BuildRequires:  python3dist(djangorestframework)
# This is not directly imported in the tests, but is implicitly required for
# some of the FastAPI and Starlette integration tests.
BuildRequires:  python3dist(httpx)

%global _description %{expand:
Openapi-core is a Python library that adds client-side and server-side
support for the OpenAPI v3.0 and OpenAPI v3.1 specification.}

%description %_description


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%pyproject_extras_subpkg -n python3-openapi-core aiohttp django %{?with_falcon:falcon} fastapi flask requests starlette


%prep
%autosetup -n %{modname}-%{version} -p1
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i '/^--cov[-=]/d' pyproject.toml
# We cannot respect a SemVer or version range pin on FastAPI; it updates
# frequently, with usually-tiny breaking changes.
sed -r -i \
    -e 's/(fastapi = \{version = ")\^/\1>=/' \
    -e 's/(fastapi = \{version = ".*),<[^"]+/\1/' \
    pyproject.toml


%generate_buildrequires

%pyproject_buildrequires -x aiohttp -x django %{?with_falcon:-x falcon} -x fastapi -x flask -x requests -x starlette


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{modname}


%check
%if %{without falcon}
ignore="${ignore-} --ignore=tests/integration/contrib/falcon"
%endif
%pytest ${ignore-}


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
%autochangelog
