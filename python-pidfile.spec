%global module_name pidfile
%global pypi_name python-%{module_name}
Name:			%{pypi_name}
Version:		3.0.0
Release:		3%{?dist}
Summary:		Python context manager for managing pid files
License:		MIT
URL:			https://pypi.org/project/python-pidfile
Source0:		%pypi_source
Source1:		https://raw.githubusercontent.com/mosquito/python-pidfile/master/LICENSE
BuildArch:		noarch

%global _description %{expand:
Python context manager for managing pid files.}

%description %_description

%package -n python3-%{module_name}
Summary:		%{summary}

BuildRequires:	python3-devel

%description -n python3-%{module_name} %_description

%prep
%autosetup %{name}-%{version}
cp -p %{SOURCE1} .

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %{module_name}

%check
%pyproject_check_import

%files -n python3-pidfile -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
* Tue Oct 04 2022 Vishal Vijayraghavan<vishalvvr@fedoraproject.org> - 3.0.0-3
- add license source and test

* Sun Oct 02 2022 Vishal Vijayraghavan<vishalvvr@fedoraproject.org> - 3.0.0-2
- specfile cleanup

* Tue Sep 27 2022 Vishal Vijayraghavan<vishalvvr@fedoraproject.org> - 3.0.0-1
- Initial fedora build.
