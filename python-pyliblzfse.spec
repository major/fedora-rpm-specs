%global pypi_name pyliblzfse

Name:           python-%{pypi_name}
Version:        0.4.1
Release:        %autorelease
Summary:        Python bindings for the LZFSE reference implementation

License:        MIT
URL:            https://github.com/ydkhatri/pyliblzfse
Source:         %{pypi_source}
# Use system library for lzfse
Patch:          use-system-lzfse.patch

BuildRequires:  python3-devel
BuildRequires:  lzfse-devel
BuildRequires:  gcc

# LZFSE isn't supported on big-endian architectures
# https://github.com/lzfse/lzfse/issues/23
ExcludeArch:    s390x

%global _description %{expand:
pyliblzfse is a Python (https://www.python.org/) module that provides LZFSE
and LZVN compression and decompression through the reference implementation
provided by Apple (https://github.com/lzfse/lzfse).}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -p1 -n pyliblzfse-%{version}

# remove bundled library
rm -r lzfse LICENSE.lzfse

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files liblzfse

%check
%pyproject_check_import

%files -n python3-pyliblzfse -f %{pyproject_files}
%license COPYING
%doc AUTHORS README

%changelog
%autochangelog
