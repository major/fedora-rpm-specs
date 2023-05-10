# Run tests by default.
%bcond_without  tests

%global srcname isodate

Name:           python-%{srcname}
Version:        0.6.1
Release:        %autorelease
Summary:        An ISO 8601 date/time/duration parser and formatter
License:        BSD-3-Clause
URL:            https://pypi.org/project/isodate/
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif


%global _description This module implements ISO 8601 date, time and duration \
parsing. The implementation follows ISO8601:2004 standard, and implements only \
date/time\ representations mentioned in the standard. If something is not \
mentioned there, then it is treated as non existent, and not as an allowed \
option.\
\
For instance, ISO8601:2004 never mentions 2 digit years. So, it is not intended\
by this module to support 2 digit years. (while it may still be valid as ISO\
date, because it is not explicitly forbidden.) Another example is, when no time\
zone information is given for a time, then it should be interpreted as local\
time, and not UTC.\
\
As this module maps ISO 8601 dates/times to standard Python data types, like\
date, time, datetime and timedelta, it is not possible to convert all possible\
ISO 8601 dates/times. For instance, dates before 0001-01-01 are not allowed by\
the Python date and datetime classes. Additionally fractional seconds are\
limited to microseconds. That means if the parser finds for instance\
nanoseconds it will round it to microseconds.

%description
%{_description}

%package -n python3-%{srcname}
Summary: %summary
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%if %{with tests}
%check
%pytest
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGES.txt README.rst TODO.txt


%changelog
%autochangelog
