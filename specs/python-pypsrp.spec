Summary:        PowerShell Remoting Protocol and WinRM for Python
Name:           python-pypsrp
Version:        0.9.1
Release:        %autorelease
License:        MIT
URL:            https://github.com/jborean93/pypsrp
Source:         %{pypi_source pypsrp}
Patch:          0001-Relax-to-setuptools-69.patch
BuildArch:      noarch
BuildRequires:  python3-devel
%global _description %{expand:
pypsrp is a Python client for the PowerShell Remoting Protocol (PSRP)
and Windows Remote Management (WinRM) service. It allows your to
execute commands on a remote Windows host from any machine that can
run Python.}
%description %_description

%package     -n python3-pypsrp
Summary:        %{summary}
%description -n python3-pypsrp %_description

%pyproject_extras_subpkg -n python3-pypsrp kerberos

%prep
%autosetup -p1 -n pypsrp-%{version}

%generate_buildrequires
%pyproject_buildrequires -x kerberos

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pypsrp

%check
%pyproject_check_import
# needs xmldiff
#pytest

%files -n python3-pypsrp -f %{pyproject_files}

%changelog
%autochangelog
