# what it's called on pypi
%global srcname gearbox
%global modname gearbox

Name:               python-gearbox
Version:            0.3.2
Release:            %autorelease
Summary:            Command line toolkit born as a PasteScript replacement for TurboGears2

License:            MIT
URL:                https://github.com/TurboGears/gearbox
Source0:            %pypi_source

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-pytest
BuildRequires:      python3-legacy-cgi

%global _description\
gearbox is a paster command replacement for TurboGears2. It has been\
created during the process of providing Python3 support to the TurboGears2\
web framework, while still being backward compatible with the existing\
TurboGears projects.\


%description %_description

%package -n python3-gearbox
Summary:            Command line toolkit born as a PasteScript replacement for TurboGears2

%description -n python3-gearbox
gearbox is a paster command replacement for TurboGears2. It has been
created during the process of providing Python3 support to the TurboGears2
web framework, while still being backward compatible with the existing
TurboGears projects.

%generate_buildrequires
%pyproject_buildrequires -t

%prep
%setup -q -n %{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%pytest

%files -n python3-gearbox -f %{pyproject_files}
%doc README.rst
%{_bindir}/gearbox

%changelog
%autochangelog
