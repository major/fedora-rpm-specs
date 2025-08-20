%global srcname elastic-transport
%global _desc %{expand: \
Transport classes and utilities shared among Python Elastic client libraries

This library was lifted from elasticsearch-py and then transformed to be used
across all Elastic services rather than only Elasticsearch.}

Name:		python-%{srcname}
Version:	9.1.0
Release:	%autorelease
Summary:	Transport classes and utilities shared among Python Elastic

License:	Apache-2.0
URL:		https://github.com/elastic/elastic-transport-python
Source0:	%{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	python3-pytest

%description %{_desc}

%package -n python3-%{srcname}
Summary:	%{summary}

%description -n python3-%{srcname} %{_desc}

%prep
%autosetup -n %{srcname}-python-%{version}

# opentelemetry* not in fedora
sed -i '/opentelemetry-api/d' setup.py
sed -i '/opentelemetry-sdk/d' setup.py

%generate_buildrequires
%pyproject_buildrequires -r -x develop

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files elastic_transport

%check
%pytest -v --ignore=tests/test_otel.py -k 'not test_debug_logging and not test_assert_fingerprint_in_cert_chain and not test_assert_fingerprint_in_cert_chain_failure and not test_ssl_assert_fingerprint and not test_supported_tls_versions and not test_unsupported_tls_version'

%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.md README.md

%changelog
%autochangelog
