# F39FailsToInstall: python3-falcon
# https://bugzilla.redhat.com/show_bug.cgi?id=2220217
%bcond falcon 0

%global srcname openapi-core
%global modname openapi_core

Name:           python-%{srcname}
Version:        0.17.1
Release:        %autorelease
Summary:        OpenAPI client-side and server-side support

License:        BSD-3-Clause
URL:            https://github.com/python-openapi/%{srcname}
Source:         %{pypi_source %{modname}}

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

%if %{without falcon}
Obsoletes:      python3-%{srcname}+falcon < 0.17.1-4
%endif

%global _description %{expand:
Openapi-core is a Python library that adds client-side and server-side
support for the OpenAPI v3.0 and OpenAPI v3.1 specification.}

%description %_description


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%pyproject_extras_subpkg -n python3-openapi-core django %{?with_falcon:falcon} flask requests starlette


%prep
%autosetup -n %{modname}-%{version} -p1
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i '/^--cov[-=]/d' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -x django %{?with_falcon:-x falcon} -x flask -x requests -x starlette


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
