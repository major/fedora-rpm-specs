%global srcname openapi-core
%global modname openapi_core

Name:           python-%{srcname}
Version:        0.16.4
Release:        %autorelease
Summary:        OpenAPI client-side and server-side support

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/%{srcname}
Source:         %{pypi_source openapi_core}

# https://github.com/p1c2u/openapi-core/pull/450
Patch:          openapi-core_0.16.4_avoid-dependency.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  poetry

# Dependencies not automatically pulled in
BuildRequires:  python3dist(starlette)

%global _description %{expand:
Openapi-core is a Python library that adds client-side and server-side
support for the OpenAPI v3.0 and OpenAPI v3.1 specification.}

%description %_description


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%pyproject_extras_subpkg -n python3-openapi-core django flask requests starlette


%prep
%autosetup -n %{modname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x django -x falcon -x flask -x requests -x starlette


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{modname}


%check
%pyproject_check_import


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
%autochangelog
