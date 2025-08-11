%global srcname lz4

Name:           python-%{srcname}
Version:        4.4.4
Release:        %autorelease
URL:            https://github.com/%{name}/%{name}
Summary:        LZ4 Bindings for Python
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
Source:         https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
# Reduce setuptools_scm dep to >= 6
Patch:          python-lz4-deps.patch
# Support Python 3.14
Patch:          https://github.com/python-lz4/python-lz4/pull/303.patch

BuildRequires:  lz4-devel
BuildRequires:  python3-devel
BuildRequires:  gcc

# For tests
BuildRequires:  python3-psutil
# For docs
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-bootstrap-theme


%description
Python bindings for the lz4 compression library.


%package -n python3-lz4
Summary:        LZ4 Bindings for Python 3
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-lz4
Python 3 bindings for the lz4 compression library.


%prep
%autosetup -n %{srcname}-%{version} -p1
sed -i -e '/pytest-cov/d' setup.py
sed -i -e 's/--cov=lz4\/block --cov=lz4\/frame//' tox.ini

rm lz4libs/lz4*.[ch]

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files lz4
# Fix permissions on shared objects
find %{buildroot}%{python3_sitearch} -name 'lz4*.so' \
    -exec chmod 0755 {} \;

# Build HTML docs
pushd docs
PYTHONPATH=$RPM_BUILD_ROOT%{python3_sitearch} make html
popd
mv docs/_build/html ./html


%check
%tox


%files -n python3-lz4 -f %{pyproject_files}
%license LICENSE
%doc README.rst html


%changelog
%autochangelog
