# Run tests by default.
%bcond_without     tests

%global         srcname     azure-eventhub

Name:           python-%{srcname}
Version:        5.10.1
Release:        %autorelease
Summary:        Microsoft Azure Event Hubs Client Library for Python 
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(azure-devtools)
BuildRequires:  python3dist(azure-identity)
BuildRequires:  python3dist(azure-mgmt-keyvault)
BuildRequires:  python3dist(azure-mgmt-resource)
BuildRequires:  python3dist(azure-sdk-tools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-aiohttp)
BuildRequires:  python3dist(python-dotenv)
%endif

%global _description %{expand:
The Azure Event Hubs client library allows for publishing and
consuming of Azure Event Hubs events and may be used to: 

- Emit telemetry about your application for business intelligence and
  diagnostic purposes. 

- Publish facts about the state of your application which interested
  parties may observe and use as a trigger for taking action. 

- Observe interesting operations and interactions happening within
  your business or other ecosystem, allowing loosely coupled systems
  to interact without the need to bind them together.

- Receive events from one or more publishers, transform them to better
  meet the needs of your ecosystem, then publish the transformed
  events to a new stream for consumers to observe.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files azure


%check
%pyproject_check_import

%if %{with tests}
# Skip some tests which depend on a uamqp_transport fixture which is not
# included in the PyPi package.
%pytest tests/unittest \
    -k "not test_amqp_message_str_repr \
        and not test_sys_properties \
        and not test_event_data_batch \
        and not test_event_data_from_message \
        and not test_amqp_message_from_message"
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md


%changelog
%autochangelog
