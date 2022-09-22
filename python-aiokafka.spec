%global sname aiokafka
%global owner aio-libs

Name:       python-%{sname}
Version:    0.7.2
Release:    3%{?dist}
Summary:    Asyncio client for Kafka
License:    ASL 2.0
Source0:    https://github.com/%{owner}/%{sname}/archive/v%{version}/%{sname}-%{version}.tar.gz
URL:        https://github.com/%{owner}/%{sname}
BuildArch:  noarch

BuildRequires:  python3-devel python3-pytest python3-docker python3-snappy snappy-devel python3-lz4
Requires:       python3

%description
%{summary}

%package -n python3-%{sname}
Summary:    %{summary}

%description -n python3-%{sname}
%{summary}

%prep
%autosetup -p1 -n %{sname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
rm aiokafka/record/_crecords/crc32c.[ch]
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{sname}

%check
# Some tests cannot be run due to incompatibility issues and lack of certificates
# The flag 'no:warnings' was added since the 'distutils' is now deprecated in Python 3.10 and 3.11, to be removed in Python 3.12
AIOKAFKA_NO_EXTENSIONS=1 py.test -s -p no:warnings -k 'not test_read_write_serde_v0_v1_with_compression and not test_create_ssl_context' tests

%files -n python3-%{sname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
* Tue Jul 12 2022 Italo Garcia <italo.garcia@aiven.io> - 0.7.2-1
- Initial package
