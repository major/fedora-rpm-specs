%global srcname openapi-spec-validator
%global modname openapi_spec_validator

Name:           python-%{srcname}
Version:        0.7.1
Release:        %autorelease
Summary:        Python library for OpenAPI specs validation

License:        Apache-2.0
URL:            https://github.com/python-openapi/%{srcname}
Source:         %{pypi_source %{modname}}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
OpenAPI Spec Validator is a Python library that validates OpenAPI Specs against
the OpenAPI 2.0 (aka Swagger), OpenAPI 3.0 and OpenAPI 3.1 specification. The
validator aims to check for full compliance with the Specification.}

%description %_description


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1 -n %{modname}-%{version}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i '/^--cov[-=]/d' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{modname}


%check
%pytest -m 'not network'


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/%{srcname}


%changelog
%autochangelog
