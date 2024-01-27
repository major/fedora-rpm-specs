%global sname aiokafka
%global owner aio-libs

Name:       python-%{sname}
Version:    0.8.1
Release:    5%{?dist}
Summary:    Asyncio client for Kafka
License:    ASL 2.0
Source0:    https://github.com/%{owner}/%{sname}/archive/v%{version}/%{sname}-%{version}.tar.gz
URL:        https://github.com/%{owner}/%{sname}
BuildArch:  noarch

BuildRequires:  python3-devel python3-pytest python3-docker python3-snappy snappy-devel python3-lz4 python3-zstd
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
AIOKAFKA_NO_EXTENSIONS=1 py.test -s -p no:warnings\
 -k 'not test_read_write_serde_v0_v1_with_compression and not test_create_ssl_context and not test_txn_manager and not test_read_write_serde_v2 and not test_unavailable_codec' tests

%files -n python3-%{sname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 13 2023 Roman Inflianskas <rominf@aiven.io> - 0.8.1-2
- Rebuilt for Python 3.12 (fedora#2220104)

* Thu Jun 29 2023 Roman Inflianskas <rominf@aiven.io> - 0.8.1-1
- Update to 0.8.1 (resolve rhbz#2211696)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Italo Garcia <italo.garcia@aiven.io> - 0.8.0-1
- Update to version 0.8.0

* Tue Jul 12 2022 Italo Garcia <italo.garcia@aiven.io> - 0.7.2-1
- Initial package
