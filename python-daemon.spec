Name:           python-daemon
Version:        2.3.2
Release:        %autorelease
Summary:        Library to implement a well-behaved Unix daemon process

# Some build scripts and test framework are licensed GPL-3.0-or-later but those aren't shipped
License:        Apache-2.0
URL:            https://pagure.io/python-daemon
Source:         %{pypi_source python-daemon}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This library implements the well-behaved daemon specification of PEP 3143,
"Standard daemon process library".}


%description %_description


%package -n python3-daemon
Summary:        %{summary}


%description -n python3-daemon %_description


%prep
%autosetup -p1
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -e '/"coverage"/d' -i setup.py


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files daemon


%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %python3 -m setup test


%files -n python3-daemon -f %{pyproject_files}


%changelog
%autochangelog
