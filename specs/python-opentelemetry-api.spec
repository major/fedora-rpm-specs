Name:           python-opentelemetry-api
Version:        1.39.1
Release:        %autorelease
Summary:        OpenTelemetry Python API

License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/opentelemetry-api
Source:         %{pypi_source opentelemetry_api}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest


%global _description %{expand:
OpenTelemetry Python API.}

%description %_description

%package -n     python3-opentelemetry-api
Summary:        %{summary}

%description -n python3-opentelemetry-api %_description


%prep
%autosetup -p1 -n opentelemetry_api-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l opentelemetry


%check
%pyproject_check_import

# The ignored tests have a dependency on the top-level test folder from
# openetelemetry monorepository. To make the packaging simpler, we ignore those
# for now.
%pytest \
    --ignore=tests/events/test_event_logger_provider.py \
    --ignore=tests/events/test_proxy_event.py \
    --ignore=tests/logs/test_logger_provider.py \
    --ignore=tests/logs/test_proxy.py \
    --ignore=tests/metrics/test_meter_provider.py \
    --ignore=tests/trace/test_globals.py \
    --ignore=tests/trace/test_proxy.py \
    --ignore=tests/util/test_once.py

%files -n python3-opentelemetry-api -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
