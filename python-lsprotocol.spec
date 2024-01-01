Name:           python-lsprotocol
Version:        2023.0.0
Release:        %autorelease
Summary:        Python implementation of the Language Server Protocol

License:        MIT
URL:            https://pypi.org/project/lsprotocol/
Source:         %{pypi_source lsprotocol}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
lsprotocol is a python implementation of object types used in the Language
Server Protocol (LSP).}

%description %_description

%package -n     python3-lsprotocol
Summary:        %{summary}

%description -n python3-lsprotocol %_description

%prep
%autosetup -p1 -n lsprotocol-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files lsprotocol

%check
%pyproject_check_import

%files -n python3-lsprotocol -f %{pyproject_files}

%changelog
%autochangelog
