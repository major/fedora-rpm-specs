%global releasename matrix-python-common
%global pymodulename matrix_common

Name:           python-matrix-common
Version:        1.3.0
Release:        %autorelease
Summary:        Common utilities for Synapse, Sydent and Sygnal

License:        Apache-2.0
URL:            https://github.com/matrix-org/%{releasename}
Source0:        %{url}/archive/v%{version}/matrix-common-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Common utilities for Synapse, Sydent and Sygnal.}

%description %_description

%package -n python3-matrix-common
Summary:        %{summary}

%description -n python3-matrix-common %_description


%prep
%autosetup -p1 -n %{releasename}-%{version}


%generate_buildrequires
%pyproject_buildrequires -e py


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pymodulename}


%check
%tox


%files -n python3-matrix-common -f %{pyproject_files}
%doc README.md
%license LICENSE


%changelog
%autochangelog
