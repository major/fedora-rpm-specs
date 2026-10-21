Summary:        Yet Another Terminal Spinner for Python
Name:           python-yaspin
Version:        3.5.1
Release:        %autorelease
License:        MIT
URL:            https://github.com/pavdmyt/yaspin
Source:         %{pypi_source yaspin}
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
%global _description %{expand:
Yaspin provides a full-featured terminal spinner to show the
progress during long-hanging operations.}

%description %_description

%package -n     python3-yaspin
Summary:        %{summary}
%description -n python3-yaspin %_description

%prep
%autosetup -p1 -n yaspin-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
%pytest

%install
%pyproject_install
%pyproject_save_files -l yaspin

%check
%pyproject_check_import

%files -n python3-yaspin -f %{pyproject_files}

%changelog
%autochangelog
