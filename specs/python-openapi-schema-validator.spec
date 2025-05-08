%bcond tests 1

Name:           python-openapi-schema-validator
Version:        0.6.3
Release:        %autorelease
Summary:        OpenAPI schema validator for Python

License:        BSD-3-Clause
URL:            https://github.com/python-openapi/openapi-schema-validator
# The GitHub tarball contains tests; the PyPI sdist does not.
Source:         %{url}/archive/%{version}/openapi-schema-validator-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -L openapi_schema_validator

BuildArch:      noarch

%if %{with tests}
# See [tool.poetry.dev-dependencies] in pyproject.toml, which also includes
# coverage/formatter/linter/typechecker type dependencies that we do not need
# or want. Upstream pins a major version of pytest, but we do not have that
# luxury.
BuildRequires:  %{py3_dist pytest} >= 7
%endif

%global common_description %{expand:
Openapi-schema-validator is a Python library that validates schema against:

  • OpenAPI Schema Specification v3.0 which is an extended subset of the JSON
    Schema Specification Wright Draft 00.
  • OpenAPI Schema Specification v3.1 which is an extended superset of the JSON
    Schema Specification Draft 2020-12.}

%description %{common_description}


%package -n python3-openapi-schema-validator
Summary:        %{summary}

%description -n python3-openapi-schema-validator %{common_description}


%prep -a
# Patch coverage analysis out of [tool.pytest.ini_options]:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i '/^--cov\b/d' pyproject.toml


%check -a
%if %{with tests}
%pytest
%endif


%files -n python3-openapi-schema-validator -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
%autochangelog
