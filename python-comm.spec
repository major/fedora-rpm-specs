Name:           python-comm
Version:        0.2.2
Release:        %autorelease
Summary:        Jupyter Python Comm implementation, for usage in ipykernel, xeus-python etc.
License:        BSD-3-Clause
URL:            https://github.com/ipython/comm
Source:         %{url}/archive/v%{version}/comm-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
Comm provides a way to register a Kernel Comm implementation,
as per the Jupyter kernel protocol. It also provides a base Comm
implementation and a default CommManager that can be used.}


%description %_description

%package -n     python3-comm
Summary:        %{summary}

%description -n python3-comm %_description


%prep
%autosetup -p1 -n comm-%{version}


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files comm


%check
%pytest


%files -n python3-comm -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog