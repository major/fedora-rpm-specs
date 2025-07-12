%global srcname partd

Name:           python-%{srcname}
Version:        1.4.2
Release:        %autorelease
Summary:        Appendable key-value storage

License:        BSD-3-Clause
URL:            https://github.com/dask/partd
Source:         %pypi_source %{srcname}

BuildArch:      noarch

# Needed for the zeromq test
BuildRequires:  systemd-resolved

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
%pyproject_buildrequires -x complete

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%{pytest}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
