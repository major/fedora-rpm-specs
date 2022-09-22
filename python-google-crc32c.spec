# tests are enabled by default
%bcond_without tests

# The main source is the python wrapper.
%global         srcname     google-crc32c
%global         reponame    python-crc32c
%global         forgeurl    https://github.com/googleapis/%{reponame}
Version:        1.1.2
%forgemeta -a

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Python wrapper for CRC32C hashing algorithm

License:        ASL 2.0
URL:            %forgeurl0
Source0:        %forgesource

BuildRequires:  gcc-c++
BuildRequires:  google-crc32c
BuildRequires:  google-crc32c-devel
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros


%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
%endif


%global _description %{expand:
This package wraps the google/crc32c hardware-based implementation of the
CRC32C hashing algorithm. Multiple wheels are distributed as well as source.
If a wheel is not published for the python version and platform you are using,
you will need to compile crc32c using a C toolchain.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
Obsoletes:      python3-azure-sdk < 5.0.1
%description -n python3-%{srcname} %{_description}

%pyproject_extras_subpkg -n python3-%{srcname} testing


%prep
%forgesetup


%generate_buildrequires
%pyproject_buildrequires -r


%build
PIP_VERBOSE=1 %pyproject_wheel


%install
%pyproject_install
%pyproject_save_files google_crc32c


%if %{with tests}
%check
%pytest tests/test___init__.py
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md


%changelog
%autochangelog
