Name:           python-texttable
Version:        1.6.7
Release:        %autorelease
Summary:        Python module to create simple ASCII tables
License:        MIT
URL:            https://github.com/foutaise/texttable
Source:         %{pypi_source texttable}
BuildArch:      noarch

%global common_description %{expand:
Texttable is a module to generate a formatted text table, using ASCII characters.}


%description %{common_description}


%package -n python3-texttable
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest


%description -n python3-texttable %{common_description}


%prep
%autosetup -n texttable-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files texttable


%check
%pytest --verbose tests.py


%files -n python3-texttable -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
