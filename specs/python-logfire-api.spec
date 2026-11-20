Name:           python-logfire-api
Version:        5.6.0
Release:        %autorelease
Summary:        Shim for the Logfire SDK which does nothing unless Logfire is installed

License:        MIT
# The sources are https://github.com/pydantic/logfire/tree/main/logfire-api
URL:            https://pypi.org/project/logfire-api/
Source:         %{pypi_source logfire_api}
# Include LICENSE file in logfire-api PyPI tarball
# https://github.com/pydantic/logfire/pull/2839
Source1:        https://github.com/pydantic/logfire/raw/refs/tags/v%{version}/LICENSE

BuildSystem:    pyproject
BuildOption(install):  --assert-license logfire_api

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand: 
Shim for the logfire SDK Python API which does
nothing unless logfire is installed.

This package is designed to be used by packages that want to provide opt-in
integration with Logfire.

The package provides a clone of the Python API exposed by the logfire package
which does nothing if the logfire package is not installed, but makes real
calls when it is.
}

%description %_description

%package -n     python3-logfire-api
Summary:        %{summary}

%description -n python3-logfire-api %_description


%prep -a
# Copy in missing license text
cp --preserve '%{SOURCE1}' .

# upstream test are not in pypi archive and uses opentelemetry.instrumentation
# that is not package. So leaving just to check_import.

%files -n python3-logfire-api -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
