Name:           python-packbits
Version:        0.6
Release:        %autorelease
Summary:        PackBits encoder/decoder

License:        MIT
URL:            https://github.com/kmike/packbits
# PyPI tarball doesn't include tests
Source:         %{url}/archive/%{version}/packbits-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This module implements a PackBits encoder/decoder for Python. PackBits encoding
is used in PSD and TIFF files.}

%description %_description

%package -n     python3-packbits
Summary:        %{summary}

%description -n python3-packbits %_description

%prep
%autosetup -p1 -n packbits-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l packbits

%check
%tox

%files -n python3-packbits -f %{pyproject_files}
%doc README.rst AUTHORS.rst

%changelog
%autochangelog
