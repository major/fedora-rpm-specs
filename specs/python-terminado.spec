%{?python_enable_dependency_generator}
%global srcname terminado
# python2-tornado package is too old on EPEL

Name:           python-%{srcname}
Version:        0.18.1
Release:        %autorelease
Summary:        Terminals served to term.js using Tornado websockets

License:        BSD-2-Clause
URL:            https://github.com/jupyter/terminado
Source0:        https://github.com/jupyter/terminado/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
This is a Tornado websocket backend for the term.js Javascript terminal
emulator library.



%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Terminals served to term.js using Tornado websockets
BuildRequires:  python%{python3_pkgversion}-devel
# For tests
BuildRequires:  python%{python3_pkgversion}-pytest

%description -n python%{python3_pkgversion}-%{srcname}
This is a Tornado websocket backend for the term.js Javascript terminal
emulator library.


%prep
%setup -q -n %{srcname}-%{version}

# Remove test dependencies on pre-commit (used for linting) and pytest-cov; see
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters.
sed -i -r 's/"pre-commit", //' pyproject.toml
sed -i -r '/"pytest-cov"/d' pyproject.toml

%if 0%{?rhel} == 9
sed -i 's/hatchling>=1.5/hatchling>=0.25/g' pyproject.toml
%endif

%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
# Workaround error in tests, for more info see
# https://bugzilla.redhat.com/show_bug.cgi?id=1914880
echo "set enable-bracketed-paste off" > .inputrc
export INPUTRC=$PWD/.inputrc
%pytest -v -W ignore::DeprecationWarning
 

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.md README.md


%changelog
%autochangelog
