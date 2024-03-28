%bcond_without tests

%global _description %{expand:
smart_open is a Python 3 library for efficient streaming of very large files
from/to storages such as S3, GCS, Azure Blob Storage, HDFS, WebHDFS, HTTP,
HTTPS, SFTP, or local filesystem. It supports transparent, on-the-fly
(de-)compression for a variety of different formats.

smart_open is a drop-in replacement for Pythons built-in open(): it can do
anything open can (100% compatible, falls back to native open wherever
possible), plus lots of nifty extra stuff on top.}

%global forgeurl https://github.com/RaRe-Technologies/smart_open


Name:           python-smart_open
Version:        7.0.4
Release:        %autorelease
Summary:        Utils for streaming large files (S3, HDFS, gzip, bz2, and more)

%forgemeta

License:        MIT
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

%description %_description

%package -n python3-smart_open
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

%py_provides python3-smart_open

%description -n python3-smart_open %_description

%prep
%forgesetup

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files smart_open

%check
%if %{with tests}
# Other tests require internet or aws/gcp/azure access keys
%pytest integration-tests/test_207.py
%endif

%files -n python3-smart_open -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
