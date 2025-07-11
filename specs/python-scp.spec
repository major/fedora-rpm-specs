%global srcname scp
%global pypi_name scp
%global forgeurl https://github.com/jbardin/scp.py

Name:    python-%{srcname}
Version: 0.15.0
%forgemeta
Release: %autorelease
Summary: Scp module for paramiko

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     %{forgeurl}
Source0: %{forgesource}

BuildArch: noarch

BuildRequires: python3-devel

%global common_description %{expand:
The scp.py module uses a paramiko transport to send and receive files via the
scp1 protocol. This is the protocol as referenced from the openssh scp program,
and has only been tested with this implementation.
}

%description %{common_description}

%package -n python3-%{srcname}
Summary: %{summary}
%py_provides python%{python3_pkgversion}-%{srcname}
%description -n python%{python3_pkgversion}-%{srcname} %{common_description}

%prep
%forgeautosetup
%generate_buildrequires

%pyproject_buildrequires
%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%check
%pyproject_check_import


%files -n python%{python3_pkgversion}-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
