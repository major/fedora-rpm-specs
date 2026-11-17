
%global srcname hl7
%global sum  Python library parsing HL7 v2.x and v3.x messages

Name:           python-%{srcname}
Version:        0.4.5
Release:        %autorelease
Summary:        Python library parsing HL7 v2.x and v3.x messages

License:        BSD-3-Clause
URL:            http://pypi.python.org/pypi/%{srcname}

Source0:        %{pypi_source %{srcname}}
Source1:        https://raw.githubusercontent.com/johnpaulett/python-hl7/master/AUTHORS

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six

%description
python-%{srcname} is a simple library for parsing messages of
Health Level 7 (HL7) v2.x into Python objects.

%package -n python3-%{srcname}
Summary: %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
python-%{srcname} is a simple library for parsing messages of
Health Level 7 (HL7) v2.x into Python objects.

%prep
%setup -q  -n %{srcname}-%{version}
rm -rf *egg-info
cp %{SOURCE1} .

%build

%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%{_bindir}/mllp_send
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%license LICENSE

%changelog
%autochangelog
