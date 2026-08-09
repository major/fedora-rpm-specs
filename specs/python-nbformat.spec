# Unset -s on python shebang - ensure that extensions installed with pip
# to user locations are seen and properly loaded
%global py3_shebang_flags %(echo %py3_shebang_flags | sed s/s//)

%global srcname nbformat

Name:           python-%{srcname}
Version:        5.11.0
Release:        %autorelease
Summary:        The Jupyter Notebook format

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
# Removed dependency on hatch-nodejs-version
Patch0:         nbformat-build-test.patch

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
# For tests
BuildRequires:  python%{python3_pkgversion}-fastjsonschema
BuildRequires:  python%{python3_pkgversion}-testpath

%description
This package contains the base implementation of the Jupyter Notebook format,
and Python APIs for working with notebooks.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        The Jupyter Notebook format
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
This package contains the base implementation of the Jupyter Notebook format,
and Python APIs for working with notebooks.


%prep
%autosetup -p1 -n %{srcname}-%{version}
mkdir -p nbformat/tests

# Remove useless test dependencies
sed -i '/"pre-commit",/d' pyproject.toml
sed -i '/"check-manifest",/d' pyproject.toml

# Set version statically
# {VERSION} is a part of Patch0
sed -i "s/{VERSION}/%{version}/" pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -r -x test

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
# Ignore failure for now
# https://github.com/jupyter/nbformat/issues/405
%pytest -p no:unraisableexception

 
%files -n python%{python3_pkgversion}-%{srcname} -f %pyproject_files
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/jupyter-trust

%changelog
%autochangelog
