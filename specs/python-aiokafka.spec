%global sname aiokafka
%global owner aio-libs

# crc32c does not support big-endian arch:
# https://github.com/aio-libs/aiokafka/blob/bb15ecfb4c85026b2bded912ab7ba7c7e1db3271/aiokafka/record/_crecords/crc32c.c#L101
%bcond c_extensions %["%{_arch}" != "s390x"]

%{!?with_c_extensions:%global debug_package %{nil}}

Name:       python-%{sname}
Version:    0.12.0
Release:    %autorelease
Summary:    Asyncio client for Kafka
License:    Apache-2.0
Source0:    https://github.com/%{owner}/%{sname}/archive/v%{version}/%{sname}-%{version}.tar.gz
URL:        https://github.com/%{owner}/%{sname}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  python3dist(docker)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  snappy-devel
BuildRequires:  zlib-devel

%description
%{summary}

%package -n python3-%{sname}
Summary:    %{summary}

%description -n python3-%{sname}
%{summary}

%prep
%autosetup -p1 -n %{sname}-%{version}

%if %{without c_extensions}
sed -i "s/    ext_modules/#    ext_modules/" setup.py
%endif

%generate_buildrequires
%pyproject_buildrequires -x snappy,lz4,zstd,gssapi,all

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{sname}

%check
%{!?with_c_extensions:AIOKAFKA_NO_EXTENSIONS=1} %pytest --import-mode append ${tests_dir}

%files -n python3-%{sname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
