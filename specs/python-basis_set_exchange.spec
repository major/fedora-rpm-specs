%{?!python3_pkgversion:%global python3_pkgversion 3}

Name:           python-basis_set_exchange
Version:        0.11
Release:        6%{?dist}
Summary:        A repository for quantum chemistry basis sets
License:        BSD-3-Clause
URL:            https://github.com/MolSSI-BSE/basis_set_exchange
Source0:        %{pypi_source basis_set_exchange %{version}}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-pytest

%{?python_enable_dependency_generator}

%description
This project is a library containing basis sets for use in quantum
chemistry calculations. In addition, this library has functionality
for manipulation of basis set data.

The goal of this project is to create a consistent, thoroughly curated
database of basis sets, and to provide a standard nomenclature for
quantum chemistry.

The data contained within this library is being thoroughly evaluated
and checked against relevant literature, software implementations, and
other databases when available. The original data from the PNNL Basis
Set Exchange is also available.

This library is used to form the backend of the new Basis Set Exchange
website.

This project is a collaboration between the Molecular Sciences
Software Institute (https://molssi.org) and the Environmental
Molecular Sciences Laboratory (https://www.emsl.pnl.gov)

When publishing results obtained from use of the Basis Set Exchange
software, please cite:

* A New Basis Set Exchange: An Open, Up-to-date Resource for the
  Molecular Sciences Community Benjamin P. Pritchard, Doaa Altarawy,
  Brett Didier, Tara D. Gibson, and Theresa L. Windus
  J. Chem. Inf. Model. 2019, 59(11), 4814-4820
  doi:10.1021/acs.jcim.9b00725

For citing the previous EMSL/PNNL Basis Set Exchange, please cite the
following references:

* The Role of Databases in Support of Computational Chemistry
  Calculations, Feller, D., J. Comp. Chem. 1996, 17(13), 1571-1586,
  doi:10.1002/(SICI)1096-987X(199610)17:13<1571::AID-JCC9>3.0.CO;2-P
* Basis Set Exchange: A Community Database for Computational Sciences
  Schuchardt, K.L., Didier, B.T., Elsethagen, T., Sun, L.,
  Gurumoorthi, V., Chase, J., Li, J., and Windus,
  T.L. J. Chem. Inf. Model. 2007, 47(3), 1045-1052,
  doi:10.1021/ci600510

%package -n python%{python3_pkgversion}-basis_set_exchange
Summary:        %{summary}
%{?python_provide:%python_provide python3-basis_set_exchange}

%if %{undefined python_enable_dependency_generator} && %{undefined python_disable_dependency_generator}
# Put manual requires here:
Requires:       python%{python3_pkgversion}-foo
%endif

%description -n python%{python3_pkgversion}-basis_set_exchange
This project is a library containing basis sets for use in quantum
chemistry calculations. In addition, this library has functionality
for manipulation of basis set data.

The goal of this project is to create a consistent, thoroughly curated
database of basis sets, and to provide a standard nomenclature for
quantum chemistry.

The data contained within this library is being thoroughly evaluated
and checked against relevant literature, software implementations, and
other databases when available. The original data from the PNNL Basis
Set Exchange is also available.

This library is used to form the backend of the new Basis Set Exchange
website.

This project is a collaboration between the Molecular Sciences
Software Institute (https://molssi.org) and the Environmental
Molecular Sciences Laboratory (https://www.emsl.pnl.gov)

When publishing results obtained from use of the Basis Set Exchange
software, please cite:

* A New Basis Set Exchange: An Open, Up-to-date Resource for the
  Molecular Sciences Community Benjamin P. Pritchard, Doaa Altarawy,
  Brett Didier, Tara D. Gibson, and Theresa L. Windus
  J. Chem. Inf. Model. 2019, 59(11), 4814-4820
  doi:10.1021/acs.jcim.9b00725

For citing the previous EMSL/PNNL Basis Set Exchange, please cite the
following references:

* The Role of Databases in Support of Computational Chemistry
  Calculations, Feller, D., J. Comp. Chem. 1996, 17(13), 1571-1586,
  doi:10.1002/(SICI)1096-987X(199610)17:13<1571::AID-JCC9>3.0.CO;2-P
* Basis Set Exchange: A Community Database for Computational Sciences
  Schuchardt, K.L., Didier, B.T., Elsethagen, T., Sun, L.,
  Gurumoorthi, V., Chase, J., Li, J., and Windus,
  T.L. J. Chem. Inf. Model. 2007, 47(3), 1045-1052,
  doi:10.1021/ci600510j

%prep
%setup -q -n basis_set_exchange-%{version}
# Remove spurious files
find basis_set_exchange/data/ -name fix_template.py -delete
find basis_set_exchange/data/ -name move.py -delete
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l basis_set_exchange

%check
%pytest

%files -n python%{python3_pkgversion}-basis_set_exchange -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/bse
%{_bindir}/bsecurate

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jun 04 2025 Python Maint <python-maint@redhat.com> - 0.11-5
- Rebuilt for Python 3.14

* Tue Mar 11 2025 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.11-4
- Drop %%tox and -t flag in %%pyproject_buildrequires.

* Sat Mar 01 2025 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.11-3
- Remove spurious files.

* Fri Feb 28 2025 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.11-2
- Switch to pypi source to have all necessary files in the tarball.
- Add missing buildrequires.

* Fri Feb 28 2025 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.11-1
- First release.
