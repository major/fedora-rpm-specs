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
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-pytest

%description
pyparsing is a module that can be used to easily and directly configure syntax
definitions for any number of text parsing applications.


%package -n python%{python3_pkgversion}-pyparsing
Summary:        %{summary}

%description -n python%{python3_pkgversion}-pyparsing
pyparsing is a module that can be used to easily and directly configure syntax
definitions for any number of text parsing applications.


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


%prep
%autosetup -p1 -n %{name}-%{name}_%{version}

dos2unix -k examples/*


%generate_buildrequires
# tox lists only the [diagrams] extra and coverage as deps, so we bypass it
%pyproject_buildrequires -x diagrams


%build
%pyproject_wheel

# build docs
pushd docs
# Theme is not available
sed -i '/alabaster/d' conf.py
sphinx-build -b html . html
popd


%install
%pyproject_install
%pyproject_save_files pyparsing


%check
%pytest -v


%files -n python%{python3_pkgversion}-pyparsing -f %{pyproject_files}
%license LICENSE
%doc CHANGES README.rst

%files doc
%license LICENSE
%doc CHANGES README.rst docs/html examples


%changelog
%autochangelog
