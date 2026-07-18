# There's a dependency loop with psi4 which needs to be broken for new Python bootstrap
%bcond tests 0

Name:           python-qcengine
Version:        0.50.0
Release:        3%{?dist}
Summary:        A compute wrapper for Quantum Chemistry
License:        BSD-3-Clause
URL:            https://github.com/MolSSI/QCEngine
Source0:        https://github.com/MolSSI/QCEngine/archive/v%{version}%{?rc}/%{name}-%{version}%{?rc}.tar.gz

# Don't try to query git for version
Patch0:         python-qcengine-0.50-nogit.patch

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
BuildRequires:  python3-dftd4
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
%setup -n QCEngine-%{version}%{?rc}
%patch -P 0 -p1 -b .nogit
# Put in the version in pyproject.toml
sed -i 's|@VERSION@|%{version}%{?rc}|g' pyproject.toml

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
* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.50.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Thu Jun 04 2026 Python Maint <python-maint@redhat.com> - 0.50.0-2
- Rebuilt for Python 3.15

%autochangelog
