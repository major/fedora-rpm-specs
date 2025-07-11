%global pypi_name spec2scl

Name:           %{pypi_name}
Version:        1.2.2
Release:        %autorelease
Summary:        Convert RPM specfiles to be SCL ready

License:        MIT
URL:            https://github.com/sclorg/spec2scl
Source0:        %{pypi_source}

# Drop pytest-runner and "setup.py test" support
# https://github.com/sclorg/spec2scl/pull/40
# https://fedoraproject.org/wiki/Changes/DeprecatePythonPytestRunner
# This version omits changes to tox.ini, since it is not included in the sdist.
Patch:          spec2scl-1.2.2-no-pytest-runner.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist flexmock} >= 0.9.3
BuildRequires:  %{py3_dist jinja2}
BuildRequires:  %{py3_dist pytest}

%description
spec2scl is a tool to convert RPM specfiles to SCL-style specfiles.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}
install -D -m 644 spec2scl.1 %{buildroot}%{_mandir}/man1/spec2scl.1

%check
%pyproject_check_import

%if 0%{?fedora}
%pytest
%endif

%files -f %{pyproject_files}
%doc README.rst
%{_bindir}/%{pypi_name}
%{_mandir}/man1/spec2scl.1*

%changelog
%autochangelog
