%global pypi_name asahi_firmware

# This package is arched because of the runtime requirement on liblzfse but
# it doesn't ship any binary objects itself
%global debug_package %{nil}

# The installer package for macOS depends on m1n1-stage1, which is only
# available on aarch64
%ifarch aarch64
%bcond installer_package 1
%else
%bcond installer_package 0
%endif

# For the generated library symbol suffix
%if 0%{?__isa_bits} == 32
%global libsymbolsuffix %{nil}
%else
%global libsymbolsuffix ()(%{__isa_bits}bit)
%endif

# This should match the version in asahi_firmware/img4.py
%global liblzfse_majver 1

# These should match the versions in build.sh
%global installer_libffi_version 3.4.6
%global installer_python_version 3.9.6
%global installer_python_asn1_version 2.5.0

# These are prebuilt binary macOS packages. We cannot build them in Fedora
# because that requires macOS itself and other proprietary tools.
# FESCo exception: https://pagure.io/fesco/issue/3212
%global installer_libffi_package libffi-%{installer_libffi_version}-macos.tar.gz
%global installer_python_package python-%{installer_python_version}-macos11.pkg

Name:           asahi-installer
Version:        0.7.9
Release:        %autorelease
Summary:        Asahi Linux installer

License:        MIT
URL:            https://github.com/AsahiLinux/asahi-installer
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# This is a libffi build for macOS from Homebrew
# https://formulae.brew.sh/formula/libffi
# See the logic in build.sh for how it's downloaded
Source1:        %{installer_libffi_package}
# This is an official upstream build of the Python interpeter for macOS
Source2:        https://www.python.org/ftp/python/%{installer_python_version}/%{installer_python_package}
Source3:        https://www.python.org/ftp/python/%{installer_python_version}/%{installer_python_package}.asc
# Per https://www.python.org/downloads/ this is Ned Deily's key, who signs the
# Python release binaries for macOS
Source4:        https://keybase.io/nad/pgp_keys.asc?fingerprint=0d96df4d4110e5c43fbfb17f2d347ea6aa65421d#/key.asc

BuildRequires:  gnupg2
BuildRequires:  python3-devel
BuildRequires:  python3dist(asn1)

%if %{with installer_package}
BuildRequires:  bash
BuildRequires:  cpio
BuildRequires:  coreutils
BuildRequires:  gzip
BuildRequires:  m1n1-stage1
BuildRequires:  p7zip-plugins
BuildRequires:  python3
BuildRequires:  python3dist(certifi)
BuildRequires:  system-logos
BuildRequires:  tar
%endif

# LZFSE isn't supported on big-endian architectures
# https://github.com/lzfse/lzfse/issues/23
ExcludeArch:    s390x

%description
Asahi Linux installer

%if %{with installer_package}
%package        package
Summary:        Asahi Linux Installer macOS package
# The installer itself is MIT, and so are the vendored libffi and python-asn1.
# The rest comes from m1n1-stage1 and Python.
License:        MIT AND (MIT AND CC0-1.0 AND OFL-1.1-RFN AND Zlib AND (BSD-2-Clause OR GPL-2.0-or-later) AND (BSD-3-Clause OR GPL-2.0-or-later) AND (Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0)) AND Python

# These are vendored macOS dependencies that are included in the installer
Provides:       bundled(libffi) = %{installer_libffi_version}
Provides:       bundled(python) = %{installer_python_version}
Provides:       bundled(python-asn1) = %{installer_python_asn1_version}

%description    package
macOS package for the Asahi Linux installer
%endif

%package -n     python3-%{pypi_name}
Summary:        Asahi Linux firmware tools

# Ensure runtime dependencies are pulled in
Requires:       liblzfse.so.%{liblzfse_majver}%{libsymbolsuffix}
Requires:       python3dist(asn1)
Requires:       tar

%description -n python3-%{pypi_name}
Asahi Linux firmware tools

%prep
%autosetup -p1
%{gpgverify} --keyring='%{SOURCE4}' --signature='%{SOURCE3}' --data='%{SOURCE2}'

# Set version
echo "%{version}" > version.tag

# Put the binary packages where the build script expects them
mkdir -p dl
ln -s %SOURCE1 %SOURCE2 dl/

%generate_buildrequires
%pyproject_buildrequires -r

%build
%if %{with installer_package}
M1N1_STAGE1="%{_libdir}/m1n1-stage1/m1n1.bin" \
LOGO="%{_datadir}/pixmaps/bootloader/fedora.icns" \
  ./build.sh
%endif

# Drop bundled asn1 module in favor of the system one; we do this here because
# the macOS package needs it.
rm asahi_firmware/asn1.py

%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%if %{with installer_package}
install -Dpm0644 -t %{buildroot}%{_libdir}/%{name}/releases releases/*
%endif

%check
%pyproject_check_import

%if %{with installer_package}
%files package
%license LICENSE
%doc README.md
%{_libdir}/%{name}/
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/asahi-fwextract

%changelog
%autochangelog
