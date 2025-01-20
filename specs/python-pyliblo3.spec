%global commit 91d17815b911ccc2c1d1408412e7885c32f2d460
%global snapdate 20240801

Name:           python-pyliblo3
%global snapinfo ^%{snapdate}git%{sub %{commit} 1 7}
Version:        0.16.2%{snapinfo}
Release:        4%{?dist} 
Summary:        Python bindings for the liblo Open Sound Control (OSC) library
# Main code is LGPL-2.1-or-later
License:        LGPL-2.1-or-later
URL:            https://github.com/gesellkammer/pyliblo3
Source:         https://github.com/gesellkammer/pyliblo3/archive/%{commit}/pyliblo3-%{commit}.tar.gz
Patch:          https://github.com/gesellkammer/pyliblo3/pull/11/commits/6f0c8a73fd25fd05f528f79ac204a25657cebab7.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-cython
BuildRequires:  liblo-devel

%global _description %{expand:
python-pyliblo3 is a Python wrapper for the liblo OSC library.
It supports almost the complete functionality of liblo,
allowing you to send and receive OSC messages using a nice and simple
Python API.

This is a Python3 fork of the original bindings for liblo.}

%description %_description

%package -n     python3-pyliblo3
Summary:        %{summary}
Obsoletes:      python3-pyliblo < 0.10.0-30

%description -n python3-pyliblo3 %_description

%package doc
Summary:        Documentation for python-pyliblo3
BuildArch:      noarch

%description doc
This package contains HTML documentation, including tutorials and API
reference for python-pyliblo3.

%prep
%autosetup -p1 -n pyliblo3-%{commit}
# Remove pregenerated Cython C sources and build it again
rm -rf pyliblo3/_liblo.c

# Fix permissions (fix for rpmlint warning "spurious-executable-perm")
chmod 644 NEWS README.md COPYING

# Fix all Python shebangs recursively in .
%py3_shebang_fix .

%generate_buildrequires
%pyproject_buildrequires

%build
cython -I pyliblo3 pyliblo3/_liblo.pyx
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pyliblo3

mkdir -p %{buildroot}%{_mandir}/man1
cp -a scripts/dump_osc.1 scripts/send_osc.1 %{buildroot}%{_mandir}/man1/

%check
%{py3_test_envvars} %{python3} -P -m unittest discover -s ./test -p '*.py'

%files -n python3-pyliblo3 -f %{pyproject_files}
%doc README.md NEWS
%{_bindir}/dump_osc.py
%{_bindir}/send_osc.py
%_mandir/*/*

%files doc
%doc doc/
%doc examples/

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2^20240801git91d1781-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 25 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.16.2^20240801git91d1781-3
- remove pyhton3-pyliblo3 from the doc package

* Tue Sep 24 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.16.2^20240801git91d1781-2
- add python3-pyliblo3 subpackage
- move 'Obsoletes:' tag to python3-pyliblo3 subpackage
- move doc subpackage after the python3-pyliblo3 subpackage
- remove 'Recommends:' tag 
- rename python-pyliblo3 to python3-pyliblo3
- remove macro %%{modname} for better readability

* Wed Sep 04 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.16.2^20240801git91d1781-1
- Add patch `type-erase lo_blob_dataptr input` for _liblo.pyx
- Add obsolete for older version of pyliblo
- Add Requires to doc subpackage

* Tue Sep 03 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.16.2-0.4.git91d1781
- Use correct source tag address
- Recompile `.pyx` file
- Fix permission of NEWS README.md and COPYING

* Wed Aug 28 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.16.2-0.3.git91d1781
- remove Provides and Obsolutes, dnf should automatically remove any transient dependencies by itself
- remove -r option from  macro pyproject_buildrequires
- use macro %%{pyproject_files} and %%pyproject_save_files pyliblo3}
- remove python3 requirements, because the macro %%pyproject_buildrequires is used

* Tue Aug 27 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.16.2-0.2.git91d1781
- remove Cython generated files
- use macro %%pyproject_wheel
- use macro %%py3_shebang_fix

* Sun Aug 25 2024 Martin Gansser <martinkg@fedoraproject.org> - 0.16.2-0.1.git91d1781
- initial build
