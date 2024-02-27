%global _description \
future is the missing compatibility layer between Python 2 and \
Python 3. It allows you to use a single, clean Python 3.x-compatible \
code base to support both Python 2 and Python 3 with minimal overhead. \
\
It provides ``future`` and ``past`` packages with backports and forward \
ports of features from Python 3 and 2. It also comes with ``futurize`` and \
``pasteurize``, customized 2to3-based scripts that helps you to convert \
either Py2 or Py3 code easily to support both Python 2 and 3 in a single \
clean Py3-style code base, module by module.

%global pypi_name future

Name: future
Summary: Easy, clean, reliable Python 2/3 compatibility
Version: 1.0.0
Release: %autorelease
License: MIT-0
URL: http://python-future.org/
Source0: https://github.com/PythonCharmers/python-future/archive/refs/tags/v%{version}/python-future-%{version}.tar.gz
BuildArch: noarch

BuildRequires: pyproject-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3dist(pytest)

Patch0: future-1.0.0-PR635.patch
Patch1: future-1.0.0-PR636.patch
Patch2: future-1.0.0-skip_tests_with_connection_errors.patch
Patch3: future-1.0.0-fix_setup.patch

%description
%{_description}

%package -n python%{python3_pkgversion}-%{name}
Summary: Easy, clean, reliable Python 2/3 compatibility

%py_provides python3-%{name}
%py_provides %{name}


%description -n python%{python3_pkgversion}-%{name}
%{_description}

%prep
%autosetup -n python-future-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x tests

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name} libfuturize libpasteurize past

%py3_shebang_fix %{buildroot}%{python3_sitelib}/%{pypi_name}/backports/test/pystone.py
chmod a+x %{buildroot}%{python3_sitelib}/%{pypi_name}/backports/test/pystone.py

%check
%pytest -k "not recursion_limit"

%files -n python3-%{name} -f %{pyproject_files}
%doc README.rst
%{_bindir}/futurize
%{_bindir}/pasteurize

%changelog
%autochangelog
