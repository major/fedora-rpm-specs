%global         pypi_name setproctitle
%global         forgeurl https://github.com/dvarrazzo/py-setproctitle

Name:           python-%{pypi_name}
Version:        1.3.6
%global tag     version-%{version}
%forgemeta
Release:        %{autorelease}
Summary:        Python module to customize a process title

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc
BuildRequires:  python3-devel
# Tests
BuildRequires:  procps-ng


%global _description %{expand:
Python module allowing a process to change its title as displayed by
system tool such as ps and top.

It's useful in multiprocess systems, allowing to identify tasks each forked
process is busy with. This technique has been used by PostgreSQL and OpenSSH.

It is based on PostgreSQL implementation which has proven to be portable.}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Python module allowing a process to change its title as displayed by
system tool such as ps and top.

It's useful in multi-process systems, allowing to identify tasks each forked
process is busy with. This technique has been used by PostgreSQL and OpenSSH.

It's based on PostgreSQL implementation which has proven to be portable.


%prep
%forgesetup

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pypi_name}


%check
%tox


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license COPYRIGHT

%changelog
%autochangelog

