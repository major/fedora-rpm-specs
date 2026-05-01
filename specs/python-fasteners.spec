%bcond tests %{undefined rhel}

Name:           python-fasteners
Version:        0.20
Release:        %autorelease
Summary:        A python package that provides useful locks

License:        Apache-2.0
URL:            https://github.com/harlowja/fasteners
# We need to use the GitHub archive instead of the PyPI sdist to get tests.
Source:         %{url}/archive/%{version}/fasteners-%{version}.tar.gz

BuildSystem:            pyproject
%if %{with tests}
BuildOption(generate_buildrequires): -g test
%endif
BuildOption(install):   -l fasteners
BuildOption(check):     -e 'fasteners.pywin32*'

BuildArch:      noarch

%global common_description %{expand:
Cross platform locks for threads and processes}

%description %{common_description}


%package -n python3-fasteners
Summary:        A python package that provides useful locks

%description -n python3-fasteners %{common_description}


%prep -a
# Omit eventlet integration tests: retired since Fedora 41
%pyproject_patch_dependency eventlet:ignore


%check -a
%if %{with tests}
# See notes in %%prep:
ignore="${ignore-} --ignore=tests/test_eventlet.py"

%pytest ${ignore-} -rs -v
%endif


%files -n python3-fasteners -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
