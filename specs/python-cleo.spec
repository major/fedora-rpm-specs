%global common_description %{expand:
Create beautiful and testable command-line interfaces.

Cleo is mostly a higher level wrapper for CliKit, so a lot of the
components and utilities comes from it. Refer to its documentation for
more information.}

#global prerel ...
%global base_version 2.2.1

Name:           python-cleo
Summary:        Create beautiful and testable command-line interfaces
Version:        %{base_version}%{?prerel:~%{prerel}}
Release:        %autorelease
License:        MIT

URL:            https://github.com/sdispater/cleo
Source0:        %{pypi_source cleo}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock

%description %{common_description}


%package -n     python3-cleo
Summary:        %{summary}

%description -n python3-cleo %{common_description}


%prep
%autosetup -n cleo-%{base_version}%{?prerel} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files cleo


%check
%pytest


%files -n python3-cleo -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
%autochangelog
