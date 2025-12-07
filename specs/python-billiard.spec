%bcond tests 1

Name:           python-billiard
Version:        4.2.4
Release:        %autorelease
Epoch:          1
Summary:        Python multiprocessing fork with improvements and bugfixes

License:        BSD-3-Clause
URL:            https://github.com/celery/billiard
Source:         %{pypi_source billiard}

BuildRequires:  python3-devel

BuildArch:      noarch

%global _description %{expand:
billiard is a fork of the Python multiprocessing package. The multiprocessing
package itself is a renamed and updated version of R Oudkerk’s pyprocessing
package. This standalone variant draws its fixes/improvements from python-trunk
and provides additional bug fixes and improvements.}

%description %{_description}

%package -n python3-billiard
Summary:        %{summary}

%description -n python3-billiard %{_description}

%prep
%autosetup -p1 -n billiard-%{version}

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:requirements/test.txt}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l billiard

%check
%pyproject_check_import -e billiard.popen_spawn_win32
%if %{with tests}
%pytest
%endif

%files -n python3-billiard -f %{pyproject_files}
%doc CHANGES.txt README.rst

%changelog
%autochangelog
