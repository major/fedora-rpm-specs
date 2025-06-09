%global srcname bmaptool
%global module_name bmaptools

%global _description %{expand:
Bmaptool is a generic tool for creating the block map (bmap) for a file and
copying files using the block map. The idea is that large files, like raw
system image files, can be copied or flashed a lot faster and more reliably
with bmaptool than with traditional tools, like dd or cp.

Bmaptool was originally created for the "Tizen IVI" project and it was used for
flashing system images to USB sticks and other block devices. Bmaptool can also
be used for general image flashing purposes, for example, flashing Fedora Linux
OS distribution images to USB sticks.}

Name:           bmap-tools
Version:        3.9.0
Release:        %autorelease
Summary:        Generate and flash images using the "block map" (bmap) format

License:        GPL-2.0-or-later
URL:            https://github.com/yoctoproject/bmaptool
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-six
BuildRequires:  gnupg2

Requires:       python3-%{module_name} = %{version}-%{release}
Requires:       bzip2
Requires:       pbzip2
Requires:       gzip
Requires:       xz
Requires:       tar
Requires:       unzip
Requires:       lzop
Requires:       pigz
Requires:       zstd

%description    %{_description}

%package -n python3-%{module_name}
Summary:        Python library for bmap-tools

%description -n python3-%{module_name} %{_description}

This package provides a Python library to manipulate bmap images.

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

install -Dpm0644 -t %{buildroot}/%{_mandir}/man1 docs/man1/bmaptool.1

%check
%pytest -v

%files
%doc README.md CHANGELOG.md
%{_bindir}/bmaptool
%{_mandir}/man1/bmaptool.1*

%files -n python3-%{module_name} -f %{pyproject_files}

%changelog
%autochangelog
