%bcond falcon 1

%global srcname openapi-core
%global modname openapi_core

Name:           python-%{srcname}
Version:        0.19.5
Release:        %autorelease
Summary:        OpenAPI client-side and server-side support

License:        BSD-3-Clause
URL:            https://github.com/python-openapi/%{srcname}
Source:         %{pypi_source %{modname}}

# Allow Starlette 0.45 and 0.46
# https://github.com/python-openapi/openapi-core/pull/977
# (Without changes to poetry.lock)
# https://github.com/python-openapi/openapi-core/pull/977/commits/6714b46bbc20933dad48d5907908166cde7fa0c0.
#
# Allow FastAPI 0.116 and Starlette 0.47
# https://github.com/python-openapi/openapi-core/pull/1027
# (Without changes to poetry.lock)
#
# Allow Starlette 0.48
# We can’t offer this upstream until a released version of FastAPI
# officially supports Starlette 0.48.x.
Patch:          openapi-core-0.19.5-starlette-0.48.patch

# Downstream-only: remove werkzeug version pin
#
# Upstream added this to fix
# https://github.com/python-openapi/openapi-core/issues/938, but we have no
# choice: we must use the version that is packaged, even if this breaks things.
Patch:          0001-Downstream-only-remove-werkzeug-version-pin.patch

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
%autosetup -n %{modname}-%{version} -p1
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
%pyproject_save_files %{modname}


%check
# [Bug]: Regression in Python 3.14: TestImportModelCreate::test_dynamic_model
# https://github.com/python-openapi/openapi-core/issues/1009
k="${k-}${k+ and }not (TestImportModelCreate and test_dynamic_model)"

%if %{without falcon}
ignore="${ignore-} --ignore=tests/integration/contrib/falcon"
%endif

%pytest ${ignore-} -k "${k-}"


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
%autochangelog
