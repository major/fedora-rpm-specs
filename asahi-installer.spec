%global pypi_name asahi_firmware

# This package is arched because of the runtime requirement on liblzfse but
# it doesn't ship any binary objects itself
%global debug_package %{nil}

# For the generated library symbol suffix
%if 0%{?__isa_bits} == 32
%global libsymbolsuffix %{nil}
%else
%global libsymbolsuffix ()(%{__isa_bits}bit)
%endif

%global liblzfse_majver 1

Name:           asahi-installer
Version:        0.5pre9
Release:        %autorelease
Summary:        Asahi Linux installer

License:        MIT
URL:            https://github.com/AsahiLinux/asahi-installer
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  sed

BuildRequires:  python3dist(asn1)

# LZFSE isn't supported on big-endian architectures
# https://github.com/lzfse/lzfse/issues/23
ExcludeArch:    s390x

%description
Asahi Linux installer

%package -n     python3-%{pypi_name}
Summary:        Asahi Linux firmware tools

# Ensure runtime dependencies are pulled in
Requires:       liblzfse.so.%{liblzfse_majver}%{libsymbolsuffix}
Requires:       python3dist(asn1)

%description -n python3-%{pypi_name}
Asahi Linux firmware tools

%prep
%autosetup -p1
# Replace bundled asn1 module with the system one and fix soname for liblzfse
rm asahi_firmware/asn1.py
sed -i asahi_firmware/img4.py \
  -e 's/from . import asn1/import asn1/' \
  -e 's/liblzfse.so/liblzfse.so.%{liblzfse_majver}/'

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

# remove this as it conflicts with the wrapper shipped in asahi-scripts
rm %{buildroot}%{_bindir}/asahi-fwextract

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
