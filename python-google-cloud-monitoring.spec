Name:           python-google-cloud-monitoring
Version:        2.19.1
Release:        %autorelease
Summary:        Google Cloud Monitoring API client library
License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-monitoring
Source:         %{pypi_source google-cloud-monitoring}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
Stackdriver Monitoring: collects metrics, events, and metadata from Google
Cloud, Amazon Web Services (AWS), hosted uptime probes, and application
instrumentation. Using the BindPlane service, you can also collect this
data from over 150 common application components, on-premise systems,
and hybrid cloud systems. Stackdriver ingests that data and generates
insights via dashboards, charts, and alerts. BindPlane is included with
your Google Cloud project at no additional cost.}

%description %_description

%package -n     python3-google-cloud-monitoring
Summary:        %{summary}

%description -n python3-google-cloud-monitoring %_description

%prep
%autosetup -p1 -n google-cloud-monitoring-%{version}
# https://github.com/googleapis/google-cloud-python/pull/12317
sed -i 's/^import mock$/from unittest import mock/g' tests/unit/test_query.py

%generate_buildrequires
%pyproject_buildrequires -x pandas

%build
%pyproject_wheel

%install
%pyproject_install
# See https://bugzilla.redhat.com/1935266 for why not google/cloud/monitoring_v3
%pyproject_save_files google

%check
%pyproject_check_import
%pytest tests/unit

%files -n python3-google-cloud-monitoring -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
