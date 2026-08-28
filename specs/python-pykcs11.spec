# TODO: tox tests
# E: NO TESTS RAN
# /usr/bin/python3 -m unittest discover pid=413
#   py312: FAIL code 5
%bcond_with tests

%global pypi_name PyKCS11
%global srcname pykcs11

Name:           python-%{srcname}
Version:        1.5.19
Release:        %autorelease
Summary:        A Full PKCS11 wrapper for Python

License:        GPL-2.0-only
URL:            https://github.com/LudovicRousseau/PyKCS11
Source:         %{pypi_source}

BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  swig
%if %{with tests}
BuildRequires:  opensc
BuildRequires:  softhsm
%endif

%global _description %{expand:
A complete PKCS11 wrapper for Python. You can use any PKCS11 (aka CryptoKi)
module such as the PSM which comes as part of mozilla or the various modules
supplied by vendors of hardware crypto tokens, and almost all PKCS11 functions
and data types. The wrapper has been generated with the help of the SWIG
compiler.}

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %{_description}

%package -n python-%{srcname}-doc
Summary:        %{pypi_name} documentation
BuildArch:      noarch
%description -n python-%{srcname}-doc
Documentation for %{pypi_name}.

%prep
%autosetup -p1 -n pykcs11-%{version}
# rpmlint fixes
#   * E: env-script-interpreter
#     - Remove shebang from Python libraries
for lib in samples/{*.py,LowLevel/*.py}; do
 sed '1{\@^#!/usr/bin/env python3@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done
#     - Add shebang
sed -i -e '1i#!/usr/bin/python3' samples/{*.py,LowLevel/*.py}

# There is no swig python module in Fedora. Instead we using 'swig' package.
sed -i 's/, "swig"//' pyproject.toml
%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo,nojekyll}

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import
%if %{with tests}
./get_PYKCS11LIB.py > tox.env
%tox
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md Changes.txt
%license docs/license.rst COPYING

%files -n python-%{srcname}-doc
%doc html/ samples/
%license COPYING

%changelog
%autochangelog
