Name:           python-pydocket
Version:        0.17.9
Release:        %autorelease
Summary:        A distributed background task system for Python functions

# The entire source code for pydocket is licensed under MIT, with exception of:
#
# * Apache-2.0:
#   - This comes from ./src/docket/_prometheus_exporter.py, a vendored
#   OpenTelemetry Prometheus Exporter that is providing a minimal imlementation
#   of PrometheusMetricReader.
License:        MIT AND Apache-2.0
URL:            https://docket.lol/
Source:         %{pypi_source pydocket}

# Remove some unrecognized arguments for pytest (coverage, xdist, etc...)
Patch:          remove-pytest-unrecognized-arguments.diff
# Fix unpack in lua script for execution
Patch:          fix-lua-unpack.diff

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  tomcli
# Test depedencies
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
# Needed for the `worker_id` fixture that pytest-xdist brings
BuildRequires:  python3-pytest-xdist
BuildRequires:  python3-docker
BuildRequires:  python3-fakeredis


%global _description %{expand:
Docket is a distributed background task system for Python functions with a
focus on the scheduling of future work as seamlessly and efficiently as
immediate work.}

%description %_description

%package -n     python3-pydocket
Summary:        %{summary}

%description -n python3-pydocket %_description

%prep
%autosetup -p1 -n pydocket-%{version}

# Croniter is available in Fedora repositories starting from version 5, but the
# project requires >=6. While this is a major version change, it seems that the
# changes from 5.x to 6.x have not affected this project.
tomcli set pyproject.toml arrays replace project.dependencies "croniter>=([0-9]+)" "croniter>=5"

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l docket


%check
%pyproject_check_import

# We need to set this to `memory` otherwise the tests will try to use docker to
# spawn multiple redis containers.
export REDIS_VERSION=memory
# Depends on opentelemetry-sdk, which is not packaged in Fedora (and is an
# optional for this package).
%pytest --ignore tests/instrumentation/test_tracing.py -k "not test_exports_metrics_as_prometheus_metrics and not test_json_logging_format"


%files -n python3-pydocket -f %{pyproject_files}
%doc README.md
%doc SECURITY.md
%{_bindir}/docket


%changelog
%autochangelog
