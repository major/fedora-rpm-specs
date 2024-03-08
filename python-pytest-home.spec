Name:           python-pytest-home
Version:        0.5.1
Release:        %autorelease
Summary:        A temporary home directory fixture

License:        MIT
URL:            https://github.com/jaraco/pytest-home
Source:         %{pypi_source pytest-home}

BuildArch:      noarch
BuildRequires:  python3-devel
# for tests
BuildRequires:  git-core

%global _description %{expand:
Configures the home directory to a temporary directory,
hiding the user's dotfiles and other home-bound state.

Before the fixture is enacted, home resolves to the user's
usual home dir.}

%description %_description

%package -n python3-pytest-home
Summary:        %{summary}

%description -n python3-pytest-home %_description


%prep
%autosetup -p1 -n pytest-home-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pytest_home


%check
mv pytest_home _pytest_home
%pytest


%files -n python3-pytest-home -f %{pyproject_files}
%doc README.*


%changelog
%autochangelog

