%global srcname toolz
%global desc Toolz provides a set of utility functions for iterators, functions, and\
dictionaries. These functions interoperate well and form the building blocks\
of common data analytic operations. They extend the standard libraries\
itertools and functools and borrow heavily from the standard libraries of\
contemporary functional languages.\
\
Toolz provides a suite of functions which have the following functional\
virtues:\
\
    Composable: They interoperate due to their use of core data structures.\
    Pure: They don’t change their inputs or rely on external state.\
    Lazy: They don’t run until absolutely necessary, allowing them to support\
          large streaming data sets.\
\
Toolz functions are pragmatic. They understand that most programmers have\
deadlines.\
\
    Low Tech: They’re just functions, no syntax or magic tricks to learn\
    Tuned: They’re profiled and optimized\
    Serializable: They support common solutions for parallel computing\
\
This gives developers the power to write powerful programs to solve complex\
problems with relatively simple code. This code can be easy to understand\
without sacrificing performance. Toolz enables this approach, commonly\
associated with functional programming, within a natural Pythonic style\
suitable for most developers.

Name:           python-%{srcname}
Version:        1.2.0
Release:        %autorelease
Summary:        A functional standard library for Python

# The project is released under the BSD-3-Clause license.
# The _version.py file created by versioneer is licensed CC0-1.0; this will
# change to Unlicense when versioneer is updated to a newer version.
License:        BSD-3-Clause AND CC0-1.0
URL:            https://github.com/pytoolz/%{srcname}/
Source0:        %{pypi_source %{srcname}}
BuildArch:      noarch

%description
%{desc}


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        A functional standard library for Python %{python3_version}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%description -n python%{python3_pkgversion}-%{srcname}
%{desc}


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l toolz tlz


%check
# shakespeare test downloads a file
%pytest -v -k 'not test_shakespeare'


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license LICENSE.txt


%changelog
%autochangelog
