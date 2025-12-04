Name:           python-pbs-installer
Version:        2025.11.20
Release:        %autorelease

Summary:        Installer for Python Build Standalone

License:        MIT
URL:            https://pypi.org/project/pbs-installer/
Source:         %{pypi_source pbs_installer}

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
An installer for @indygreg's python-build-standalone (https://github.com/astral-sh/python-build-standalone).}

%description %_description

%package -n     python3-pbs-installer
Summary:        %{summary}

%description -n python3-pbs-installer %_description

%pyproject_extras_subpkg -n python3-pbs-installer all,download,install


%prep
%autosetup -p1 -n pbs_installer-%{version}


%generate_buildrequires
%pyproject_buildrequires -x all,download,install


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L pbs_installer


%check
%pyproject_check_import


%files -n python3-pbs-installer -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/pbs-install


%changelog
%autochangelog
