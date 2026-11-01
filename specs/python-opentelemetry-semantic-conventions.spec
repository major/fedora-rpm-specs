Name:           python-opentelemetry-semantic-conventions
Version:        0.65~b0
Release:        %autorelease
Summary:        OpenTelemetry Semantic Conventions

License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/opentelemetry-semantic-conventions
Source:         %{pypi_source opentelemetry_semantic_conventions 0.65b0}

BuildArch:      noarch
BuildRequires:  python3-pytest


%global _description %{expand:
This library contains generated code for the semantic conventions
defined by the OpenTelemetry specification. These conventions define
standardized names and values for common attributes used in traces,
metrics, and logs produced by OpenTelemetry instrumentation.}

%description %_description

%package -n     python3-opentelemetry-semantic-conventions
Summary:        %{summary}

%description -n python3-opentelemetry-semantic-conventions %_description


%prep
%autosetup -p1 -n opentelemetry_semantic_conventions-0.65b0


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l opentelemetry


%check
%pyproject_check_import
%pytest tests


%files -n python3-opentelemetry-semantic-conventions -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
