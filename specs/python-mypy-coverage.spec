Name:           python-mypy-coverage
Version:        0.2.4
Release:        %autorelease
Summary:        Report mypy annotation coverage for a Python codebase

License:        GPL-3.0-or-later
URL:            https://github.com/mfisherlevine/mypy_coverage
Source:         %{url}/archive/v%{version}/mypy_coverage-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-mypy

%global _description %{expand:
A fast, stdlib-only CLI that reports how much of a Python codebase
is actually type-checked by mypy.}

%description %_description

%package -n     python3-mypy-coverage
Summary:        %{summary}

%description -n python3-mypy-coverage %_description

%prep
%autosetup -p1 -n mypy_coverage-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l mypy_coverage


%check
%pyproject_check_import
%pytest

%files -n python3-mypy-coverage -f %{pyproject_files}
%doc README.md
%{_bindir}/mypy-coverage


%changelog
%autochangelog
