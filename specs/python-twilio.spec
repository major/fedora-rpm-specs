%global github_name twilio-python
%global pypi_name twilio

Name:           python-%{pypi_name}
Version:        9.4.3
Release:        1%{?dist}
Summary:        Twilio API client and TwiML generator

License:        MIT
URL:            https://github.com/twilio/twilio-python
Source0:        %{url}/archive/%{version}/%{github_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-jwt
# Tests requirements:
BuildRequires:  python3dist(aiounittest)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(django)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(multidict)
BuildRequires:  python3dist(pytest)

%global desc \
The Twilio REST SDK simplifies the process of making calls using the Twilio \
REST API. \
The Twilio REST API lets to you initiate outgoing calls, list previous calls, \
and much more.

%description
%{desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -p1 -n %{github_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# avoid 'import file mismatch:'
rm twilio/rest/events/v1/sink/sink_test.py
# Disable checks requiring network access to api.twilio.com
# Disable webbook test requiring proprietary ngrok binary
rm tests/cluster/test_webhook.py
rm tests/cluster/test_cluster.py
%pytest \
  --deselect tests/unit/rest/test_client.py::TestUserAgentClients::test_set_default_user_agent \
  --deselect tests/unit/rest/test_client.py::TestUserAgentClients::test_set_user_agent_extensions


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 9.1.0-2
- Rebuilt for Python 3.13

%autochangelog
