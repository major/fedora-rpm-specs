# This package has a dependency loop with psi4 which has to be broken to bootstrap new Python in Fedora
%bcond tests 1

Name:           python-optking
Version:        0.3.0
Release:        5%{?dist}
Summary:        A Python version of the PSI4 geometry optimization program by R.A. King
License:        BSD-3-Clause
URL:            https://github.com/psi-rking/optking
Source0:        https://github.com/psi-rking/optking/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pint
BuildRequires:  psi4
%endif

%description
optking (also known as pyoptking) is a rewrite of the c++ optking
module in psi4. This rewrite was undertaken to enable future
development and for use with recent interoperability efforts
(e.g. MolSSI QCArchive and QCDB). optking is focused on optimization
of molecular geometries: finding minima, transition states, and
reaction paths. Current work is focused especially on expanding the
reaction path methods.

%package -n     python3-optking
Summary:        %{summary}
%{?python_provide:%python_provide python3-optking}

%description -n python3-optking
optking (also known as pyoptking) is a rewrite of the c++ optking
module in psi4. This rewrite was undertaken to enable future
development and for use with recent interoperability efforts
(e.g. MolSSI QCArchive and QCDB). optking is focused on optimization
of molecular geometries: finding minima, transition states, and
reaction paths. Current work is focused especially on expanding the
reaction path methods.

%prep
%setup -q -n optking-%{version}
# Remove bundled egg-info
rm -rf optking.*-info
# Remove test that requires internet access to pubchem
\rm optking/tests/test_frozen_internals.py

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files optking -l

%check
%pyproject_check_import -e *.tests.*
%if %{with tests}
%pytest -m "not long" optking
%endif

%files -n python3-optking -f %{pyproject_files}
%doc README.rst

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.0-4
- Turn on tests.

* Mon Sep 02 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.0-3
- Removed explicit requires.

* Mon Sep 02 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.0-2
- Review fixes.

* Wed Aug 28 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.0-1
- First release.
