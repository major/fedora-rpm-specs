Summary:       The Gerrit client tools
Name:          gerrymander
Version:       1.5
Release:       %autorelease
Source0:       %{pypi_source}
URL:           https://pypi.python.org/pypi/gerrymander
License:       Apache-2.0

BuildArch:     noarch

BuildRequires: python3-pytest
BuildRequires: python3-devel
Requires:      python3-gerrymander = %{version}-%{release}

%package -n python3-gerrymander
Summary: The Gerrit python3 client


%description
The gerrymander package provides a set of command line tools
for interacting with Gerrit

%description -n python3-gerrymander
The python3-gerrymander package provides a set of python3
modules for interacting with Gerrit.

%prep
%autosetup -p1
# Remove any bundled egg-info
rm -rf *.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files gerrymander

%check
%pyproject_check_import
%pytest

%files
%doc conf/gerrymander.conf-example
%{_bindir}/gerrymander

%files -n python3-gerrymander -f %{pyproject_files}
%doc README
%license LICENSE

%changelog
%autochangelog
