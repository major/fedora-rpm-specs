%bcond_without tests

%global pretty_name maya

%global fullversion 0.6.1

%global _description %{expand:
Datetimes are very frustrating to work with in Python, especially when dealing
with different locales on different systems. This library exists to make the 
simple things much easier, while admitting that time is an 
illusion (timezones doubly so).}


Name:           python-%{pretty_name}
Version:        %{?fullversion}
Release:        8%{?dist}
Summary:        Datetimes for Humans

License:        MIT
URL:            https://github.com/timofurrer/%{pretty_name}
Source0:        %{url}/archive/v%{version}/%{pretty_name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{pretty_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-snaptime
BuildRequires:  python3-pendulum
BuildRequires:  python3-humanize
BuildRequires:  python3-dateparser
BuildRequires:  python3-pytz
BuildRequires:  python3-tzlocal
BuildRequires:  python3-pytzdata
BuildRequires:  python3-pytest
BuildRequires:  python3-freezegun

#For docs
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%description -n python3-%{pretty_name} %_description

%package -n python-%{pretty_name}-doc
Summary:        maya documentation
%description -n python-%{pretty_name}-doc
Documentation for maya package

%prep
%autosetup -n %{pretty_name}-%{fullversion}
rm -rf %{pretty_name}.egg-info

%build
%py3_build

# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install
# Remove extra install files
rm -rf %{buildroot}/%{python3_sitelib}/tests

%check
%if %{with tests}
%pytest
%endif

%files -n python3-%{pretty_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pretty_name}-%{fullversion}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pretty_name}

%files -n python-%{pretty_name}-doc
%doc html
%license LICENSE

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 0.6.1-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.6.1-4
- Use pytest macro

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.1-3
- Rebuilt for Python 3.10

* Mon Apr 26 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.6.1-2
- Subpage for docs

* Sun Feb 14 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.6.1-1
- Removing dependency generator

* Mon Feb 8 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.6.1-1
- Initial package
