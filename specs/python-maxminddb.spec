%global pypi_name maxminddb
%global desc \
This is a Python module for reading MaxMind DB files.  The module includes both\
a pure Python reader and an optional C extension. MaxMind DB is a binary file\
format that stores data indexed by IP address subnets (IPv4 or IPv6).

Name:           python-%{pypi_name}
Version:        2.6.3
Release:        %autorelease
Summary:        Reader for the MaxMind DB format

# SPDX
License:        Apache-2.0
URL:            https://www.maxmind.com/
Source0:        %{pypi_source}

BuildRequires:  gcc
BuildRequires:  libmaxminddb-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description %{desc}

%package doc
Summary:        Documentation for %{pypi_name}

%description doc
This package provides the documentation for %{pypi_name}.

%package -n python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{desc}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled libmaxminddb
rm -r extension/libmaxminddb

%generate_buildrequires
%pyproject_buildrequires -r

%build
export MAXMINDDB_USE_SYSTEM_LIBMAXMINDDB=1
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest

%files doc
%doc docs/*
%license LICENSE

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
