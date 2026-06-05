%global pypi_name asyncinotify

Name:           python-%{pypi_name}
Version:        4.4.4
Release:        2%{?dist}
Summary:        A simple optionally-async Python inotify library

License:        MPL-2.0
URL:            https://github.com/ProCern/asyncinotify
Source:         %{pypi_source %{pypi_name}}

BuildArch:      noarch

BuildRequires:  python3-devel


%global _description %{expand:
An async python inotify package.  Kept as simple and easy-to-understand as
possible, while still being flexible and powerful.  This is built on no
external dependencies, and works through ctypes in a very obvious fashion.}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Library modules ship an env shebang but are not meant to be executed
sed -i '1{/^#!/d}' src/%{pypi_name}/__init__.py src/%{pypi_name}/_ffi.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%check
%pyproject_check_import


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst


%changelog
* Wed Jun 03 2026 Python Maint <python-maint@redhat.com> - 4.4.4-2
- Rebuilt for Python 3.15

* Thu May 28 2026 Jonathan Wright <jonathan@almalinux.org> - 4.4.4-1
- Initial package build
