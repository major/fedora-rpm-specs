%global forgeurl https://github.com/jackrosenthal/python-cgi
Version:        2.6.2
%forgemeta

Name:           python-legacy-cgi
Release:        %autorelease
Summary:        Fork of the standard library cgi and cgitb modules
License:        Python-2.0.1
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Python CGI This is a fork of the standard library modules cgi and cgitb.
They are slated to be removed from the Python standard library in
Python 3.13. The purpose of this fork is to support existing CGI
scripts using these modules.}

%description %_description


%package -n     python3-legacy-cgi
Summary:        %{summary}
%py_provides python3-cgi

%description -n python3-legacy-cgi %_description


%prep
%autosetup -p1 -n legacy-cgi-%{version}

%py3_shebang_fix cgi.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files cgi cgitb


%check
%pyproject_check_import
%pytest


%files -n python3-legacy-cgi -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
%autochangelog
