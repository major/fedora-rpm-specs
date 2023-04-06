Summary:        Python package with an object-oriented approach to text processing
Name:           pyparsing
Version:        3.0.9
Release:        %autorelease

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

BuildRequires:  python%{python3_pkgversion}-devel

%if %{with doc}
BuildRequires:  python%{python3_pkgversion}-sphinx
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
# pymicko.py is under GPLv3+
# snmp_api.h is under CMU-UC (MIT)
# sparser.py is under GPLv2+
# searchparser.py is under BSD (3-clause, with advertising)
# btpyparse.py is under "Simplified BSD license"
License:        MIT and GPLv2+ and GPLv3+ and BSD

%description    doc
The package contains documentation for pyparsing.
%endif


%prep
%autosetup -p1 -n %{name}-%{name}_%{version}

dos2unix -k examples/*


%generate_buildrequires
# tox lists only the [diagrams] extra and coverage as deps, so we bypass it
%pyproject_buildrequires %{?with_tests:-x diagrams}


%build
%pyproject_wheel

%if %{with doc}
pushd docs
# Theme is not available
sed -i '/alabaster/d' conf.py
sphinx-build -b html . html
popd
%endif


%install
%pyproject_install
%pyproject_save_files pyparsing


%check
%pyproject_check_import %{!?with_tests:-e pyparsing.diagram}
%if %{with tests}
%pytest -v
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
