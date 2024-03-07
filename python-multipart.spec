%global common_description %{expand:
python-multipart is an Apache2 licensed streaming multipart parser for Python.}

Name:           python-multipart
Version:        0.0.9
Release:        %autorelease
Summary:        A streaming multipart parser for Python
License:        Apache-2.0
URL:            https://github.com/Kludex/python-multipart
Source:         %{pypi_source python_multipart}
BuildArch:      noarch


%description %{common_description}


%package -n python3-multipart
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pyyaml


%description -n python3-multipart %{common_description}


%prep
%autosetup -n python_multipart-%{version} -p 1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l multipart


%check
%pytest


%files -n python3-multipart -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
