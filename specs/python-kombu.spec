%bcond_without tests
%global srcname kombu
# Packaging unstable?
# %%global prerel b3
%global general_version 5.6.1
%global upstream_version %{general_version}%{?prerel}

Name:           python-%{srcname}
Version:        %{general_version}%{?prerel:~%{prerel}}
Release:        %autorelease
Epoch:          1
Summary:        An AMQP Messaging Framework for Python

# utils/functional.py contains a header that says Python
# Automatically converted from old format: BSD and Python - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-Python
URL:            http://kombu.readthedocs.org/
Source0:        https://github.com/celery/kombu/archive/v%{upstream_version}/%{srcname}-%{upstream_version}.tar.gz

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

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-amqp
BuildRequires:  python3-pymongo
BuildRequires:  python3-vine
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
# Fedora has tzdata present, and doesn't need nor package this fallback
sed -i 's/tzdata.*$//' requirements/default.txt

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%if %{with tests}
%pytest --ignore=t/unit/transport/test_gcpubsub.py
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc AUTHORS FAQ READ* THANKS TODO examples/

%changelog
%autochangelog
