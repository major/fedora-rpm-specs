%define modname zope_deprecation

Name:           python-zope-deprecation
Version:        5.1
Release:        %autorelease
Summary:        Zope 3 Deprecation Infrastructure

License:        ZPL-2.1
URL:            https://pypi.python.org/pypi/zope.deprecation
Source0:        https://files.pythonhosted.org/packages/source/z/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%global _description\
This package provides a simple function called 'deprecated(names, reason)' to\
deprecate the previously mentioned Python objects.

%description %_description

%package -n python3-zope-deprecation
Summary:        Zope 3 Deprecation Infrastructure
%{?python_provide:%python_provide python3-zope-deprecation}


%description -n python3-zope-deprecation
This package provides a simple function called 'deprecated(names, reason)' to
deprecate the previously mentioned Python objects.

%prep
%autosetup -p1 -n %{modname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l zope

%check
%tox

%files -n python3-zope-deprecation -f %{pyproject_files}
%doc README.rst LICENSE.txt
%{python3_sitelib}/zope.deprecation-5.1-py3.13-nspkg.pth


%changelog
%autochangelog
