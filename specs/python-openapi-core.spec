%bcond falcon 1

%global srcname openapi-core
%global modname openapi_core

%global commit 4cfa26d1fbde422fbe4138b23c7268dd869240ac
%global snapdate 20260303

Name:           python-%{srcname}
Version:        0.23.0~b1^%{snapdate}.%{sub %{commit} 1 7}
%global srcversion %(echo '%{version}' | cut -d '^' -f 1 | tr -d '~')
Release:        %autorelease
Summary:        OpenAPI client-side and server-side support

License:        BSD-3-Clause
URL:            https://github.com/python-openapi/%{srcname}
# Source:         %%{pypi_source %%{modname} %%{srcversion}}
Source:         %{url}/archive/%{commit}/%{srcname}-%{commit}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  tomcli

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
%autosetup -C -p1
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i '/^--cov[-=]/d' pyproject.toml
# We cannot respect a SemVer or version range pin on FastAPI; it updates
# frequently, with usually-tiny breaking changes.
sed -r -i \
    -e 's/(fastapi = \{version = ")\^/\1>=/' \
    -e 's/(fastapi = \{version = ".*),<[^"]+/\1/' \
    pyproject.toml
# Erroring on DeprecationWarnings makes sense upstream, but is probably too
# strict for distribution packaging.
#
# This specifically works around:
#
# DeprecationWarning: 'asyncio.get_event_loop_policy' is deprecated and slated
# for removal in Python 3.16
tomcli set pyproject.toml lists delitem \
    tool.pytest.ini_options.filterwarnings error


%generate_buildrequires

%pyproject_buildrequires -x aiohttp -x django %{?with_falcon:-x falcon} -x fastapi -x flask -x requests -x starlette


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{modname}


%check
%if %{without falcon}
ignore="${ignore-} --ignore=tests/integration/contrib/falcon"
%endif

%pytest -k "${k-}" ${ignore-}


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
