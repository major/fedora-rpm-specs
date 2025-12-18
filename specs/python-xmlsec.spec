%global srcname xmlsec

Name:           python-%{srcname}
Version:        1.3.17
Release:        %autorelease
Summary:        Python bindings for the XML Security Library

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/x/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  libxml2-devel >= 2.9.1
BuildRequires:  xmlsec1-devel >= 1.2.33
BuildRequires:  xmlsec1-openssl-devel
BuildRequires:  libtool-ltdl-devel

%description
%{summary}.


%package -n python3-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Requires: libxml2 >= 2.9.1
Requires: xmlsec1 >= 1.2.33
Requires: xmlsec1-openssl


%description -n python3-%{srcname}
%{summary}.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l %{srcname}


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
