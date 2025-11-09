%global pypi_name bodhi-messages
%global src_name bodhi_messages
%global pypi_version 25.11.1

Name:           %{pypi_name}
Version:        %{pypi_version}
Release:        %autorelease
Summary:        JSON schema for messages sent by Bodhi

License:        GPL-2.0-or-later
URL:            https://github.com/fedora-infra/bodhi
Source0:        %{pypi_source bodhi_messages}
BuildArch:      noarch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3dist(fedora-messaging)
BuildRequires:  python3dist(setuptools)

%description
Bodhi Messages This package contains the schema for messages published by
Bodhi.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
%description -n python3-%{pypi_name}

%prep
%autosetup -n %{src_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files bodhi

%check
%pyproject_check_import
%{pytest} -v

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
