%bcond_without tests
%global srcname kombu
# Packaging unstable?
# %%global prerel b3
%global general_version 5.3.1
%global upstream_version %{general_version}%{?prerel}

Name:           python-%{srcname}
Version:        %{general_version}%{?prerel:~%{prerel}}
Release:        %autorelease
Epoch:          1
Summary:        An AMQP Messaging Framework for Python

# utils/functional.py contains a header that says Python
License:        BSD and Python
URL:            http://kombu.readthedocs.org/
Source0:        https://github.com/celery/kombu/archive/v%{upstream_version}/%{srcname}-%{upstream_version}.tar.gz

# Python 3.12: https://github.com/celery/kombu/commit/6ef88c3445143dde9aeaef3a95c0fb399dcb1e20
#Patch01:        6ef88c3445143dde9aeaef3a95c0fb399dcb1e20.patch

BuildArch: noarch

%description
AMQP is the Advanced Message Queuing Protocol, an open standard protocol
for message orientation, queuing, routing, reliability and security.

One of the most popular implementations of AMQP is RabbitMQ.

The aim of Kombu is to make messaging in Python as easy as possible by
providing an idiomatic high-level interface for the AMQP protocol, and
also provide proven and tested solutions to common messaging problems.

%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       python3-amqp
Requires:       python3-vine

# Remove once https://github.com/celery/kombu/issues/1668 gets resolved
Requires:       python3-cached_property

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
BuildRequires:  python3-amqp
BuildRequires:  python3-pymongo
BuildRequires:  python3-vine
BuildRequires:  python3-pytz
BuildRequires:  python3-sqlalchemy
BuildRequires:  python3-boto3
BuildRequires:  python3-pytest
BuildRequires:  python3-pyro
BuildRequires:  python3-pycurl
BuildRequires:  python3-azure-mgmt-servicebus
BuildRequires:  python3-azure-mgmt-storage
BuildRequires:  python3-brotli
BuildRequires:  python3-hypothesis
BuildRequires:  python3-pytest-freezegun
BuildRequires:  python3-azure-identity

# Remove once https://github.com/celery/kombu/issues/1668 gets resolved
BuildRequires:  python3-cached_property
%endif

%description -n python3-%{srcname}
AMQP is the Advanced Message Queuing Protocol, an open standard protocol
for message orientation, queuing, routing, reliability and security.

One of the most popular implementations of AMQP is RabbitMQ.

The aim of Kombu is to make messaging in Python as easy as possible by
providing an idiomatic high-level interface for the AMQP protocol, and
also provide proven and tested solutions to common messaging problems.

%prep
%autosetup -n %{srcname}-%{upstream_version} -p1

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
# https://github.com/celery/kombu/issues/1765
# Seems like test/tooling failures, not the actual code issues, eg.
# AttributeError: 'called_once' is not a valid assertion. Use a spec for the mock if 'called_once' is meant to be an attribute.
%pytest -k 'not test_entrypoints and not test_call_soon_uses_lock and not test__pop_ready_uses_lock'
%endif

%files -n python3-%{srcname}
%doc AUTHORS FAQ READ* THANKS TODO examples/
%license LICENSE
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}*.egg-info

%changelog
%autochangelog
