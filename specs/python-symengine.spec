%global srcname symengine.py

%global common_description %{expand:
Python wrappers to the C++ library SymEngine, a fast C++ symbolic manipulation
library.}

Name:           python-symengine
Version:        0.13.0
Release:        %autorelease
Summary:        SymEngine Python Wrappers
License:        MIT
URL:            https://symengine.org/
ExcludeArch:    %{ix86}

Source0:        https://github.com/symengine/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  cereal-devel
BuildRequires:  cmake
BuildRequires:  flint-devel
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  python3-devel
BuildRequires:  symengine-devel

%description    %{common_description}

%package -n python3-symengine
Summary:        %{summary}
Requires:       symengine%{?_isa} >= %{version}

%description -n python3-symengine %{common_description}

%package -n python3-symengine-tests
Summary:        %{summary} tests
Requires:       python3-symengine%{?_isa} = %{version}-%{release}

%description -n python3-symengine-tests %{common_description}

This package contains tests for SymEngine.py.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# Dirty hack to recreate a wheel that goes all into python3_sitearch:
wheel=$(basename pyproject-wheeldir/*.whl)
unzip -qd temp pyproject-wheeldir/$wheel
pushd temp
  cp -ar symengine-%{version}.data/purelib/symengine/* symengine/
  rm -fr symengine-%{version}.data
  zip -qr $wheel *
popd
mv temp/$wheel pyproject-wheeldir/
rm -fr temp

%install
%pyproject_install
%pyproject_save_files -l symengine

%check
# Tests don't produce any output:
for i in symengine/tests/test_*.py; do
  %{py3_test_envvars} %{python3} $i
done

%files -n  python3-symengine -f %{pyproject_files}
%license LICENSE
%doc AUTHORS README.md
%exclude %{python3_sitearch}/symengine/test_utilities.py
%exclude %{python3_sitearch}/symengine/tests
%exclude %{python3_sitearch}/symengine/__pycache__/test_utilities.*.pyc

%files -n python3-symengine-tests
%{python3_sitearch}/symengine/test_utilities.py
%{python3_sitearch}/symengine/tests
%{python3_sitearch}/symengine/__pycache__/test_utilities.*.pyc

%changelog
%autochangelog
