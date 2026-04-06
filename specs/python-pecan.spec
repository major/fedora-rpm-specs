%global pypi_name pecan
%{!?_licensedir:%global license %%doc}

Name:           python-%{pypi_name}
Version:        1.8.0
Release:        %autorelease
Summary:        A lean WSGI object-dispatching web framework

# Everything is BSD-3-Clause but pecan/middleware/recursive.py which is MIT
License:        BSD-3-Clause AND MIT
URL:            https://github.com/pecan/pecan
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel


%description
A WSGI object-dispatching web framework, designed to be lean and
fast with few dependencies


%package -n python3-%{pypi_name}
Summary:        A lean WSGI object-dispatching web framework


%description -n python3-%{pypi_name}
A WSGI object-dispatching web framework, designed to be lean and
fast with few dependencies


%prep
%autosetup -n %{pypi_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%check
%pyproject_check_import %{pypi_name} -e pecan.tests.*


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%{_bindir}/pecan
%{_bindir}/gunicorn_pecan


%changelog
%autochangelog
