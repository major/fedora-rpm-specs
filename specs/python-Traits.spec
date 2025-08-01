%global srcname Traits
%global modname traits
%global commit ac5d0296def6a389f932add5fbcab2eef6e7334e
%global shortcommit %(c=%{commit}; echo ${c:0:7})

# Circular test deps with traitsui
%bcond_with bootstrap

Name:           python-%{srcname}
Version:        6.4.3
Release:        %autorelease
Summary:        Explicitly typed attributes for Python
# Images have different licenses. For image license breakdown check
# image_LICENSE.txt file.
License:        BSD-3-Clause AND CC-BY-3.0
URL:            http://docs.enthought.com/traits/
#Source0:        https://github.com/enthought/traits/archive/%{commit}/%{modname}-%{shortcommit}.tar.gz
Source0:        https://github.com/enthought/%{modname}/archive/%{version}/%{modname}-%{version}.tar.gz
# Upstream fix for Python 3.13
Patch:          https://github.com/enthought/traits/pull/1767.patch
BuildRequires:  gcc
BuildRequires:  xorg-x11-server-Xvfb

%description
The traits package developed by Enthought provides a special type
definition called a trait. Although they can be used as normal Python object
attributes, traits also have several additional characteristics:

* Initialization: A trait can be assigned a default value.
* Validation: A trait attribute's type can be explicitly declared.
* Delegation: The value of a trait attribute can be contained either
  in another object.
* Notification: Setting the value of a trait attribute can trigger
  notification of other parts of the program.
* Visualization: User interfaces that permit the interactive
  modification of a trait's value can be automatically constructed
  using the trait's definition.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
# For tests
BuildRequires:  python%{python3_pkgversion}-Cython
BuildRequires:  python%{python3_pkgversion}-numpy
BuildRequires:  python%{python3_pkgversion}-sphinx
%if %{without bootstrap}
BuildRequires:  python%{python3_pkgversion}-traitsui
%endif
Requires:       python%{python3_pkgversion}-numpy
Provides:       python%{python3_pkgversion}-%{modname} = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{srcname}
The traits package developed by Enthought provides a special type
definition called a trait. Although they can be used as normal Python object
attributes, traits also have several additional characteristics:

* Initialization: A trait can be assigned a default value.
* Validation: A trait attribute's type can be explicitly declared.
* Delegation: The value of a trait attribute can be contained either
  in another object.
* Notification: Setting the value of a trait attribute can trigger
  notification of other parts of the program.
* Visualization: User interfaces that permit the interactive
  modification of a trait's value can be automatically constructed
  using the trait's definition.

Python 3 version.

%prep
%autosetup -n %{modname}-%{version} -p1
# we already have a bit another flags
sed -i -e '/extra_compile_args=/d' setup.py

%generate_buildrequires
# -x test has unpackaged deps
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %modname

%check
pushd build/lib.%{python3_platform}-*
  export PYTHONPATH=%{buildroot}%{python3_sitearch}
  xvfb-run %__python3 -s -m unittest discover -v
popd

%files -n python%{python3_pkgversion}-%{srcname} -f %pyproject_files
%doc CHANGES.rst examples/tutorials README.rst

%changelog
%autochangelog
