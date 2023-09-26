Name:           python-outcome
Version:        1.2.0
Release:        %autorelease
Summary:        Capture the outcome of Python function calls
License:        MIT OR Apache-2.0
URL:            https://github.com/python-trio/outcome
Source:         %{pypi_source outcome}
BuildArch:      noarch

%global _description %{expand:
Outcome provides a function for capturing the outcome of a Python function
call, so that it can be passed around.}


%description %_description


%package -n python3-outcome
Summary:        %{summary}
BuildRequires:  python3-devel


%description -n python3-outcome %_description


%prep
%autosetup -n outcome-%{version}
sed -i '/^pytest-cov\b/d' test-requirements.txt


%generate_buildrequires
%pyproject_buildrequires test-requirements.txt


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files outcome


%check
%pytest


%files -n python3-outcome -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
