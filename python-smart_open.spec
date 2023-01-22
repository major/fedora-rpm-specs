%bcond_without tests

%global pypi_name smart_open
%global src_name smart_open

%global _description %{expand:
smart_open is a Python 3 library for efficient streaming of very large files
from/to storages such as S3, GCS, Azure Blob Storage, HDFS, WebHDFS, HTTP,
HTTPS, SFTP, or local filesystem. It supports transparent, on-the-fly
(de-)compression for a variety of different formats.

smart_open is a drop-in replacement for Python's built-in open(): it can do
anything open can (100% compatible, falls back to native open wherever
possible), plus lots of nifty extra stuff on top.}

Name:           python-%{src_name}
Version:        5.2.1
Release:        5%{?dist}
Summary:        Utils for streaming large files (S3, HDFS, gzip, bz2, and more)

License:        MIT
URL:            https://github.com/RaRe-Technologies/%{src_name}
Source0:        https://github.com/RaRe-Technologies/%{src_name}/archive/v%{version}/%{src_name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{src_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}

Requires:       %{py3_dist boto}
Requires:       %{py3_dist boto3}
Requires:       %{py3_dist requests}
Suggests:       %{py3_dist mock}
Suggests:       %{py3_dist google-compute-engine}

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist numpy}
%endif

%py_provides python3-%{src_name}

%description -n python3-%{src_name} %_description

%prep
%autosetup -n %{src_name}-%{version}

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
# Other tests require internet or aws/gcp/azure access keys
%pytest integration-tests/test_207.py
%endif

%files -n python3-%{src_name}
%doc README.rst
%license LICENSE

%{python3_sitelib}/%{src_name}/
%{python3_sitelib}/%{src_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 5.2.1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 09 2021 Aniket Pradhan <major AT fedoraproject DOT org> - 5.2.1-1
- Update to v5.2.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 03 2021 Aniket Pradhan <major AT fedoraproject DOT org> - 5.1.0-1
- Update to v5.1.0

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.0.0-2
- Rebuilt for Python 3.10

* Mon May 17 2021 Aniket Pradhan <major AT fedoraproject DOT org> - 5.0.0-1
- Initial build
