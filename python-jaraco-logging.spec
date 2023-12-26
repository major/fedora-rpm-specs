# TODO adjust once this is implemented:
# https://bugzilla.redhat.com/show_bug.cgi?id=1935266
%global modname  jaraco
%global projname %{modname}.logging
%global pkgname  %{modname}-logging

Name:           python-%{pkgname}
Version:        3.3.0
Release:        %autorelease
Summary:        Support for Python logging facility

License:        MIT
URL:            https://github.com/jaraco/%{projname}
Source0:        %{pypi_source %{projname}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Support for Python logging facility.}

%description %_description

%package     -n python3-%{pkgname}
Summary:        %{summary}
Requires:       python3-jaraco

%description -n python3-%{pkgname} %_description

%prep
%autosetup -n %{projname}-%{version}

%if 0%{?rhel}
# relax setuptools requirement in EPEL
sed -i 's/setuptools>=56/setuptools/' pyproject.toml
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
# This package has currently no tests other than linters, so only do
# an import test.
%pyproject_check_import

%files -n python3-%{pkgname} -f %{pyproject_files}
%license LICENSE
%doc README.rst NEWS.rst
# Owned by python3dist(jaraco)
%exclude %dir %{python3_sitelib}/jaraco 

%changelog
%autochangelog
