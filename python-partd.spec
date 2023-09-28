%global srcname partd

Name:           python-%{srcname}
Version:        1.4.1
Release:        %autorelease
Summary:        Appendable key-value storage

License:        BSD-3-Clause
URL:            https://github.com/dask/partd
Source0:        %pypi_source %{srcname}
# compatibility with Python 3.12
Patch:          https://github.com/dask/partd/pull/70.patch

BuildArch:      noarch

%global _description %{expand:
Key-value byte store with appendable values: Partd stores key-value pairs.
Values are raw bytes. We append on old values. Partd excels at shuffling
operations.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

Recommends:     python3-%{srcname}+complete

%description -n python3-%{srcname} %{_description}

%pyproject_extras_subpkg -n python3-%{srcname} complete

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -rx complete

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%{pytest}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
%autochangelog
