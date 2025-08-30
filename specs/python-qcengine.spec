# There's a dependency loop with psi4 which needs to be broken for new Python bootstrap
%bcond tests 0

Name:           python-qcengine
Version:        0.30.0
Release:        %autorelease
Summary:        A compute wrapper for Quantum Chemistry

License:        BSD-3-Clause
URL:            https://github.com/MolSSI/QCEngine
Source:         %{pypi_source qcengine}
Patch0:         https://github.com/MolSSI/QCEngine/pull/451.patch

BuildArch:      noarch
BuildRequires:  python3-devel
# for testing
BuildRequires:  python3-pytest
# https://kojipkgs.fedoraproject.org//work/tasks/9840/108019840/build.log
BuildRequires:  python3-msgpack

%if %{with tests}
# For running the tests
#BuildRequires:  xtb # requires xtb-python which is not available in Fedora and whose development appears to be ceased
BuildRequires:  psi4
BuildRequires:  mrchem
#BuildRequires: python3-dftd4 # Package still in review https://bugzilla.redhat.com/show_bug.cgi?id=2310392
%endif

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
%setup -n qcengine-%{version}
%patch 0 -p1 -b .psi4

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files qcengine

%check
%pyproject_check_import -e *.tests.*
%if %{with tests}
%pytest
%endif

%files -n python3-qcengine -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/qcengine

%changelog
%autochangelog
