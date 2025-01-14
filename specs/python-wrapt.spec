Name:           python-wrapt
Version:        1.17.1
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


%check -a
%pytest -v


%files -n python3-wrapt -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
