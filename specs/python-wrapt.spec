Name:           python-wrapt
Version:        2.0.1
Release:        %autorelease
Summary:        A Python module for decorators, wrappers and monkey patching

License:        BSD-2-Clause
URL:            https://github.com/GrahamDumpleton/wrapt
Source:         %{url}/archive/%{version}/wrapt-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -l wrapt

BuildRequires:  gcc

# We bypass tox and instead use pytest directly; this is simpler and avoids the
# need to patch out coverage analysis.
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
# See also [tool.uv.dev-dependencies] in pyproject.toml.
BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
The aim of the wrapt module is to provide a transparent object proxy for
Python, which can be used as the basis for the construction of function
wrappers and decorator functions.}

%description %{common_description}


%package -n python3-wrapt
Summary:        %{summary}

# We stopped building documentation for Fedora 42; this can be removed after
# Fedora 44.
Obsoletes:      python-wrapt-doc < 1.16.0-8

%description -n python3-wrapt %{common_description}


%install -a
# Including this file in binary distributions is not likely to be useful to
# users; it is in the debugsource RPM anyway. It is not immediately obvious
# what to suggest that upstream should do to avoid this.
rm '%{buildroot}%{python3_sitearch}/wrapt/_wrappers.c'
sed -r -i 's@^.*/wrapt/_wrappers\.c$@# &@' %{pyproject_files}


%check -a
# This file contains mypy typechecking tests:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
ignore="${ignore-} --ignore=tests/conftest.py"

%pytest ${ignore-} -v
WRAPT_DISABLE_EXTENSIONS=true %pytest ${ignore-} -v


%files -n python3-wrapt -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
