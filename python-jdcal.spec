%global modname jdcal

Name:           python-%{modname}
Version:        1.4.1
Release:        %autorelease
Summary:        Julian dates from proleptic Gregorian and Julian calendars

License:        BSD
URL:            https://github.com/phn/jdcal
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description
This module contains functions for converting between Julian dates and calendar
dates.

A function for converting Gregorian calendar dates to Julian dates, and another
function for converting Julian calendar dates to Julian dates are defined.
Two functions for the reverse calculations are also defined.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{modname}
This module contains functions for converting between Julian dates and calendar
dates.

A function for converting Gregorian calendar dates to Julian dates, and another
function for converting Julian calendar dates to Julian dates are defined.
Two functions for the reverse calculations are also defined.

Python 3 version.

%prep
%autosetup -n %{modname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{modname}
%doc README.rst
%{python3_sitelib}/%{modname}*
%{python3_sitelib}/__pycache__/%{modname}*

%changelog
%autochangelog
