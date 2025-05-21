Name:           python-pigpio
Version:        1.78
Release:        %autorelease
Summary:        Raspberry Pi GPIO module

License:        Unlicense
URL:            http://abyz.co.uk/rpi/pigpio/python.html
Source0:        %{pypi_source pigpio}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Raspberry Pi Python module to access the pigpio daemon.

%package -n     python3-pigpio
Summary:        %{summary}

%description -n python3-pigpio
Raspberry Pi Python module to access the pigpio daemon.


%prep
%autosetup -n pigpio-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pigpio

%check
%pyproject_check_import

%files -n python3-pigpio -f %{pyproject_files}

%changelog
%autochangelog
