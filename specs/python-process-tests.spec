%global srcname process-tests

Name:           python-%{srcname}
Version:        3.0.0
Release:        %autorelease
Summary:        Tools for testing processes

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/ionelmc/python-process-tests
Source0:        https://pypi.python.org/packages/source/p/process-tests/process-tests-%{version}.tar.gz

BuildArch:      noarch

%description
Tools for testing processes.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Tools for testing processes
BuildRequires:  python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-%{srcname}
Tools for testing processes for Python 3.


%prep
%setup -q -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l process_tests


%files -n python%{python3_pkgversion}-%{srcname} -f %pyproject_files
%doc README.rst


%changelog
%autochangelog
