Summary:        Python package with an object-oriented approach to text processing
Name:           pyparsing
Version:        3.1.2
Release:        %autorelease

# SPDX
License:        MIT
URL:            https://github.com/pyparsing/pyparsing
Source0:        https://github.com/%{name}/%{name}/archive/%{name}_%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  dos2unix

# python3 bootstrap: this is built before the final build of python3, which
# adds the dependency on python3-rpm-generators, so we require it manually
# (python BuildRequires systemtap-sdt-devel which requires python3-pyparsing)
BuildRequires:  python3-rpm-generators
# We need those for the same reason:
%bcond doc      1
%bcond tests    1
%bcond extras   %{undefined rhel}

BuildRequires:  python%{python3_pkgversion}-devel

%if %{with doc}
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx-theme-alabaster
%endif
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
%endif


%description
pyparsing is a module that can be used to easily and directly configure syntax
definitions for any number of text parsing applications.


%package -n python%{python3_pkgversion}-pyparsing
Summary:        %{summary}

%description -n python%{python3_pkgversion}-pyparsing
pyparsing is a module that can be used to easily and directly configure syntax
definitions for any number of text parsing applications.


%if %{with doc}
%package        doc
Summary:        Documentation for %{name}

# Most examples are under the project's license, MIT
# pymicko.py is under GPL-3.0-or-later
# snmp_api.h is under MIT-CMU
# sparser.py is under GPL-2.0-or-later
# searchparser.py and booleansearchparser.py are under BSD-3-Clause
# btpyparse.py is under "Simplified BSD license" -> BSD-2-Clause
License:        MIT AND MIT-CMU AND GPL-2.0-or-later AND GPL-3.0-or-later AND BSD-3-Clause AND BSD-2-Clause

%description    doc
The package contains documentation for pyparsing.
%endif

%if %{with extras}
%pyproject_extras_subpkg -n python%{python3_pkgversion}-pyparsing diagrams
%endif


%prep
%autosetup -p1 -n %{name}-%{name}_%{version}

dos2unix -k examples/*


%generate_buildrequires
# tox lists only the [diagrams] extra and coverage as deps, so we bypass it
%pyproject_buildrequires %{?with_extras:-x diagrams}


%build
%pyproject_wheel

%if %{with doc}
pushd docs
sphinx-build -b html . html
popd
%endif


%install
%pyproject_install
%pyproject_save_files pyparsing


%check
%pyproject_check_import %{!?with_extras:-e pyparsing.diagram}
%if %{with tests}
# skip tests which rely on extras if disabled
%pytest -v %{!?with_extras:-k 'not test_range_check and not testEmptyExpressionsAreHandledProperly' --ignore tests/test_diagram.py}
%endif


%files -n python%{python3_pkgversion}-pyparsing -f %{pyproject_files}
%license LICENSE
%doc CHANGES README.rst

%if %{with doc}
%files doc
%license LICENSE
%doc CHANGES README.rst docs/html examples
%endif


%changelog
%autochangelog
