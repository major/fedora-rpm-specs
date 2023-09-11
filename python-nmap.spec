%global srcname nmap

Name:           python-%{srcname}
Version:        0.7.1
Release:        %autorelease
Summary:        Python library which helps in using nmap port scanner

License:        GPL-3.0-or-later
URL:            https://xael.org/pages/python-nmap-en.html
Source0:        https://xael.org/pages/%{name}-%{version}.tar.gz

# https://bitbucket.org/xael/python-nmap/pull-requests/4
Patch0:         setup.py.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

Requires:       nmap

%description
python-nmap is a Python library which helps in using nmap port scanner. It
allows to easily manipulate nmap scan results and will be a perfect tool
for systems administrators who want to automatize scanning task and reports.
It also supports nmap script outputs.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
python3-nmap is a Python library which helps in using nmap port scanner. It
allows to easily manipulate nmap scan results and will be a perfect tool
for systems administrators who want to automatize scanning task and reports.
It also supports nmap script outputs.

%prep
%autosetup -n %{name}-%{version} -p0

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files nmap

%check
# test_nmap is writen in nose, which has been broken since Python 3.9 (https://github.com/nose-devs/nose/issues/1099)
%pyproject_check_import -e nmap.test_nmap

%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGELOG README.rst 
%license gpl-3.0.txt

%changelog
%autochangelog
