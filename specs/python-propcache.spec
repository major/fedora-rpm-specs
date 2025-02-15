%global pypi_name propcache

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        %autorelease
Summary:        Module for fast property caching

License:        Apache-2.0
URL:            https://github.com/aio-libs/propcache
Source:        https://github.com/aio-libs/propcache/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-xdist)

%global _description %{expand:
Module for fast property caching.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Disable coverage
sed -r -e 's/(-.*cov.*$)/#\1/g' -i pytest.ini

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGES.rst README.rst

%changelog
%autochangelog
