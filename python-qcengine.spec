Name:           python-qcengine
Version:        0.27.0
Release:        %autorelease
Summary:        A compute wrapper for Quantum Chemistry

License:        BSD-3-Clause
URL:            https://github.com/MolSSI/QCEngine
Source:         %{pypi_source qcengine}

BuildArch:      noarch
BuildRequires:  python3-devel
# for testing
BuildRequires:  python3-pytest

%global _description %{expand:
Quantum chemistry program executor and IO standardizer (QCSchema) for quantum
chemistry.}

%description
%{_description}

%package -n     python3-qcengine
Summary:        %{summary}

%description -n python3-qcengine
%{_description}

%prep
%autosetup -n qcengine-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files qcengine

%check
%pytest

%files -n python3-qcengine -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/qcengine

%changelog
%autochangelog
