# Tests require network so disabled by default
# To run locally, use: fedpkg mockbuild --enable-network --with=network
%bcond_with network

Name:           python-pooch
Version:        1.5.2
Release:        %autorelease
Summary:        A friend to fetch your data files

License:        BSD
URL:            https://pypi.org/project/pooch/
Source0:        %{pypi_source pooch}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%if %{with network}
BuildRequires:  python3-paramiko
BuildRequires:  python3-tqdm
BuildRequires:  python3-xxhash
%endif

%global _description %{expand:
Pooch manages your Python library's sample data files: 
it automatically downloads and stores them in a local directory, 
with support for versioning and corruption checks.}

%description %_description

%package -n python3-pooch
Summary:        %{summary}

%description -n python3-pooch %_description


%prep
%autosetup -n pooch-%{version}

%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pooch


%check
%pyproject_check_import
%if %{with network}
# requires pytest-localftpserver which is not currently packaged in Fedora
%pytest -k "not ftp_downloader and not downloader_progressbar_ftp"
%endif

%files -n python3-pooch -f %{pyproject_files}
%doc README.* CITATION.* CODE_OF_CONDUCT.* CONTRIBUTING.* MAINTENANCE.*

%changelog
%autochangelog
