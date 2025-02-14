Name:           python-dependency-groups
Version:        1.3.0
Release:        %autorelease
Summary:        An implementation of Dependency Groups (PEP 735)
License:        MIT
URL:            https://pypi.org/project/dependency-groups/
Source:         %{pypi_source dependency_groups}

BuildArch:      noarch
BuildRequires:  python3-devel
# Upstream test deps contains coverage
BuildRequires:  python3-pytest


%global _description %{expand:
An implementation of Dependency Groups (PEP 735).
This is a library which is able to parse dependency groups,
following includes, and provide that data as output.}

%description %_description

%package -n     python3-dependency-groups
Summary:        %{summary}

%description -n python3-dependency-groups %_description


%prep
%autosetup -p1 -n dependency_groups-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files dependency_groups


%check
%pytest


%files -n python3-dependency-groups -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst CHANGELOG.rst
%{_bindir}/dependency-groups
%{_bindir}/lint-dependency-groups
%{_bindir}/pip-install-dependency-groups


%changelog
%autochangelog
