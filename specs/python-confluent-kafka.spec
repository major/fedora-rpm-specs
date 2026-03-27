%global sname confluent-kafka
%global pypi_name confluent-kafka

Name:           python-%{sname}
Version:        2.12.0
Release:        %autorelease
Summary:        Confluent's Apache Kafka client for Python

License:        Apache-2.0
URL:            https://github.com/confluentinc/confluent-kafka-python
Source0:        %{pypi_source confluent_kafka}


%global _description %{expand:
confluent-kafka-python is the Confluent Python client for Apache Kafka
and the Confluent Platform}

%description %_description


%package -n     python3-%{sname}
Summary:        %{summary}
BuildRequires:  gcc
BuildRequires:  librdkafka-devel
BuildRequires:  python3-devel
# Unit tests are present in the upstream repo, but not in the PyPi distribution
# https://github.com/confluentinc/confluent-kafka-python/issues/508
#BuildRequires:  python3dist(pytest)
Requires:       librdkafka >= 2.4.0


%description -n python3-%{sname} %_description


%prep
%autosetup -n confluent_kafka-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l confluent_kafka


%check
# Unit tests are present in the upstream repo, but not in the PyPi distribution
# So just import test
%py3_check_import confluent_kafka
#py.test-3 -v --ignore=tests/integration ./tests/


%files -n python3-%{sname} -f %{pyproject_files}
%doc README.md
%license LICENSE


%changelog
%autochangelog
