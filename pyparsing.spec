%global srcname pyparsing

# when bootstrapping Python 3, pyparsing needs to be rebuilt before dependency generator is available
%bcond_with bootstrap
%if %{without bootstrap}
%global build_wheel 1
%global python_wheelname %{srcname}-%{version}-py2.py3-none-any.whl
%endif


Summary:        Python package with an object-oriented approach to text processing
Name:           pyparsing
Version:        3.0.9
Release:        %autorelease

License:        MIT
URL:            https://github.com/pyparsing/pyparsing
Source0:        https://github.com/%{name}/%{name}/archive/%{name}_%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  dos2unix
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%if %{without bootstrap}
BuildRequires:  python%{python3_pkgversion}-sphinx
%endif

%if 0%{?build_wheel}
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-wheel
%endif

BuildRequires:  python%{python3_pkgversion}-pytest

%description
pyparsing is a module that can be used to easily and directly configure syntax
definitions for any number of text parsing applications.


%package -n python%{python3_pkgversion}-pyparsing
Summary:        %{summary}
%if %{with bootstrap}
Provides:       python%{python3_pkgversion}dist(pyparsing) = %{version}
Provides:       python%{python3_version}dist(pyparsing) = %{version}
Requires:       python(abi) = %{python3_version}
%endif

%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-pyparsing
pyparsing is a module that can be used to easily and directly configure syntax
definitions for any number of text parsing applications.


%if %{without bootstrap}
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


%if 0%{?build_wheel}
%generate_buildrequires
%pyproject_buildrequires -t
%endif

%build
%if 0%{?build_wheel}
%pyproject_wheel
%else
%py3_build
%endif

%if %{without bootstrap}
# build docs
pushd docs
# Theme is not available
sed -i '/alabaster/d' conf.py
sphinx-build -b html . html
popd
%endif

%install
%if 0%{?build_wheel}
%pyproject_install
%else
%py3_install
%endif


%check
%pytest -v


%files -n python%{python3_pkgversion}-pyparsing
%license LICENSE
%doc CHANGES README.rst
%{python3_sitelib}/pyparsing/
%{python3_sitelib}/pyparsing-%{version}.dist-info/

%if %{without bootstrap}
%files doc
%license LICENSE
%doc CHANGES README.rst docs/html examples
%endif


%changelog
%autochangelog
