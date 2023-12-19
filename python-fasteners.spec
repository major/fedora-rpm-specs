%bcond tests %{undefined rhel}

Name:           python-fasteners
Version:        0.19
Release:        %autorelease
Summary:        A python package that provides useful locks

License:        Apache-2.0
URL:            https://github.com/harlowja/fasteners
# We need to use the GitHub archive instead of the PyPI sdist to get tests.
Source:         %{url}/archive/%{version}/fasteners-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%global common_description %{expand:
Cross platform locks for threads and processes}

%description %{common_description}


%package -n python3-fasteners
Summary:        A python package that provides useful locks

# The mkdocs-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# The Provides/Obsoletes can be removed after F38 reaches end-of-life.
Provides:       python-fasteners-doc = %{version}-%{release}
Obsoletes:      python-fasteners-doc < 0.18-1

%description -n python3-fasteners %{common_description}


%prep
%autosetup -n fasteners-%{version}


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:requirements-test.txt}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l fasteners


%check
%if %{with tests}
%pytest -v
%else
%pyproject_check_import -e 'fasteners.pywin32*'
%endif


%files -n python3-fasteners -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
