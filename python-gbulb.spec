%global srcname gbulb

Name:           python-%{srcname}
Version:        0.6.4
Release:        %autorelease
Summary:        GLib event loop for tulip (PEP 3156)

License:        Apache-2.0
URL:            https://github.com/beeware/gbulb
Source:         %{pypi_source}
# Update test suite to remove use of generators as co-routines
Patch:          %{url}/commit/864cdb8a0b1f0d3fb5c0d84703fedb2bf1e1491e.patch

BuildArch:      noarch
BuildRequires:  gtk3-devel
BuildRequires:  python3-devel

%global _description %{expand:
Gbulb is a Python library that implements a PEP 3156 interface for the GLib
main event loop under UNIX-like systems.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%tox

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst AUTHORS.rst CHANGELOG.rst

%changelog
%autochangelog
