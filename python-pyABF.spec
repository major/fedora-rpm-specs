Name:           python-pyABF
Version:        2.3.6
Release:        %autorelease
Summary:        Python library for reading files in Axon Binary Format

License:        MIT
URL:            https://github.com/swharden/pyABF
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
pyABF is a Python package for reading electrophysiology 
data from Axon Binary Format (ABF) files.}

%description %_description

%package -n python3-pyABF
Summary:        %{summary}

%description -n python3-pyABF %_description


%prep
%autosetup -n pyABF-%{version} 

%generate_buildrequires
cd src/
%pyproject_buildrequires -r


%build
cd src/
%pyproject_wheel


%install
cd src/
%pyproject_install
%pyproject_save_files pyabf

%check
%pytest


%files -n python3-pyABF -f %{pyproject_files}
%doc README.*

%changelog
%autochangelog
