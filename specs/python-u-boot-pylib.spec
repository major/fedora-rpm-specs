Name:           python-u-boot-pylib
Version:        0.0.6
Release:        %autorelease
Summary:        U-Boot Python library

License:        GPL-2.0-or-later
URL:            https://docs.u-boot.org
Source:         %{pypi_source u_boot_pylib}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This is a Python library used by various U-Boot tools, including patman,
buildman and binman.}

%description %_description

%package -n     python3-u-boot-pylib
Summary:        %{summary}

%description -n python3-u-boot-pylib %_description

%prep
%autosetup -p1 -n u_boot_pylib-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files u_boot_pylib

%check
%pyproject_check_import

%files -n python3-u-boot-pylib -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
