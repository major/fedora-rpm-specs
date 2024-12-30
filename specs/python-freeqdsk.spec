Name:           python-freeqdsk
Version:        0.5.0
Release:        %{autorelease}
Summary:        Read and write G-EQDSK, A-EQDSK, and P-EQDSK file formats

License:        MIT
URL:            https://github.com/freegs-plasma/FreeQDSK
Source:         %pypi_source freeqdsk

Patch:          https://github.com/freegs-plasma/FreeQDSK/pull/25.patch#./setuptools.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Read and write G-EQDSK, A-EQDSK, and P-EQDSK file formats, which are
used to describe the tokamak fusion devices.
}

%description %_description

%package -n python3-freeqdsk
Summary:        %{summary}

%description -n python3-freeqdsk %_description


%prep
%autosetup -p1 -n freeqdsk-%{version}


%generate_buildrequires
%pyproject_buildrequires -x tests


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files freeqdsk


%check
%pytest


%files -n python3-freeqdsk -f %{pyproject_files}
%doc README.*


%changelog
%autochangelog
