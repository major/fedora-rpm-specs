%if 0%{?rhel}
%bcond_with tests
%else
%bcond_without tests
%endif

# The python-diskcache package, used in some of the tests, has been retired.
%bcond_with diskcache

Name:           python-fasteners
Version:        0.18
Release:        %autorelease
Summary:        A python package that provides useful locks

License:        Apache-2.0
URL:            https://github.com/harlowja/fasteners
# We need to use the GitHub archive instead of the PyPI sdist to get tests.
Source:         %{url}/archive/%{version}/fasteners-%{version}.tar.gz

# Backport 80a3eaed75276faf21034e7e6c626fd19485ea39 “Move eventlet tests to
# main folder and to child process”. Fixes “Tests hang with eventlet support”
# https://github.com/harlowja/fasteners/issues/101. (As an alternative, we
# could run pytest on tests/ and tests_eventlet/ in separate invocations.) See
# https://github.com/harlowja/fasteners/issues/101#issuecomment-1249462951.
Patch:          %{url}/commit/80a3eaed75276faf21034e7e6c626fd19485ea39.patch

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
%autosetup -p1 -n fasteners-%{version}
%if %{without diskcache}
sed -r -i '/\b(diskcache)\b/d' requirements-test.txt
%endif


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:requirements-test.txt}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files fasteners


%check
%if %{with tests}
%pytest %{?!with_diskcache:--ignore=tests/test_reader_writer_lock.py} -v
%else
%pyproject_check_import -e 'fasteners.pywin32*'
%endif


%files -n python3-fasteners -f %{pyproject_files}
# pyproject_files handles LICENSE; verify with “rpm -qL -p …”
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
