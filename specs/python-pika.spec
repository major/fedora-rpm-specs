%global srcname pika
%global srcurl  https://github.com/%{srcname}/%{srcname}
%global desc \
Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that \
tries to stay fairly independent of the underlying network support \
library.

Name:           python-%{srcname}
Version:        1.3.2
Release:        %autorelease
Summary:        AMQP 0-9-1 client library for Python

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{srcurl}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Fix tests with Python 3.14, except RuntimeError from asyncio.get_event_loop
# https://github.com/pika/pika/pull/1524
Patch:          python3.14.patch

BuildArch:      noarch

# Python 3 requirements
BuildRequires:  python3-devel
BuildRequires:  python3-twisted
BuildRequires:  python3-tornado

# Documentation requirements
BuildRequires:  python3-sphinx

# Test requirements
BuildRequires:  python3-nose2

%description
%{desc}


%package -n python3-%{srcname}
Summary:        AMQP 0-9-1 client library for Python 3
%{?python_provide:%python_provide python3-%{srcname}}
Recommends:     python3-tornado
Recommends:     python3-twisted

%description -n python3-%{srcname}
%{desc}

This package provides the Python 3 implementation.

%package -n python-%{srcname}-doc
Summary:        Additional API documentation for python-%{srcname}
# There used to be two docs packages, but the API isn't version dependent.
Provides: python3-%{srcname}-doc = %{version}-%{release}
Obsoletes: python2-%{srcname}-doc <= 0.12.0-5
Obsoletes: python3-%{srcname}-doc <= 0.12.0-5

%description -n python-%{srcname}-doc
%{summary}.


%prep
%autosetup -p1 -n %{srcname}-%{version}
# These require a broker and should be run as part of the new CI/CD stuff
rm -rf tests/acceptance
sed -i -e s#tests=tests/unit,tests/acceptance#tests=tests/unit#g nose2.cfg
# don't run code coverage
sed -i 's/with-coverage = 1/with-coverage = 0/g' nose2.cfg

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
sphinx-build -b html -d doctrees docs html


%install
%pyproject_install
%pyproject_save_files pika


%check
PYTHONPATH=%{buildroot}%{python3_sitelib} nose2


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst CHANGELOG.md


%files -n python-%{srcname}-doc
%license LICENSE
%doc examples/
%doc html/


%changelog
%autochangelog
