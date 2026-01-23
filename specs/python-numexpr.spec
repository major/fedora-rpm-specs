Summary:        Fast numerical array expression evaluator for Python and NumPy
Name:           python-numexpr
Version:        2.14.1
Release:        %autorelease
URL:            https://github.com/pydata/numexpr
License:        MIT
Source:         https://github.com/pydata/numexpr/archive/v%{version}/numexpr-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-numpy
BuildRequires:  python%{python3_pkgversion}-setuptools

%global _description %{expand:
The numexpr package evaluates multiple-operator array expressions many times
faster than NumPy can. It accepts the expression as a string, analyzes it,
rewrites it more efficiently, and compiles it to faster Python code on the
fly. It’s the next best thing to writing the expression in C and compiling it
with a specialized just-in-time (JIT) compiler, i.e. it does not require a
compiler at runtime.}

%description %_description

%package -n python%{python3_pkgversion}-numexpr
Summary:        %{summary}
Requires:       python%{python3_pkgversion}-numpy >= 1.6
%{?python_provide:%python_provide python%{python3_pkgversion}-numexpr}

%description -n python%{python3_pkgversion}-numexpr %_description

%prep
%autosetup -n numexpr-%{version} -p1

%build
%py3_build

%install
%py3_install
chmod 0755 %{buildroot}%{python3_sitearch}/numexpr/cpuinfo.py
sed -i "1s|/usr/bin/env python$|%{python3}|" %{buildroot}%{python3_sitearch}/numexpr/cpuinfo.py

%check
pushd build/lib.linux*
%py3_test_envvars %python3 -c 'import numexpr, sys; sys.exit(not numexpr.test().wasSuccessful())'
popd

%files -n python%{python3_pkgversion}-numexpr
%license LICENSE.txt
%doc ANNOUNCE.rst RELEASE_NOTES.rst README.rst
%{python3_sitearch}/numexpr/
%{python3_sitearch}/numexpr-%{version}-py*.egg-info

%changelog
%autochangelog
