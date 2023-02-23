Name:           PyDrive2
Version:        1.15.1
Release:        %autorelease
Summary:        Google Drive API Python wrapper library, maintained fork of PyDrive

License:        ASL 2.0
URL:            https://github.com/iterative/PyDrive2
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

Obsoletes:      python3-PyDrive <= 1.3.1-21

%description
Google Drive API Python wrapper library. Maintained fork of PyDrive.

%package -n     python3-%{name}
Summary:        %{summary}

%description -n python3-%{name}
Google Drive API Python wrapper library. Maintained fork of PyDrive.

%prep
%autosetup

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pydrive2

# No check as requires credentials for GoogleAuth

%files -n python3-%{name} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
