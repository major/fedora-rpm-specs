Name:       bcal
Version:    2.4
Release:    %autorelease
Summary:    Storage conversion and expression calculator

License:    GPL-3.0-or-later
URL:        https://github.com/jarun/bcal
Source:     %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Patch for GCC 15 compatibility
# https://github.com/jarun/bcal/pull/39
Patch:      0001-Add-fix-to-use-with-GCC-15.patch

# Only available for 64bits system
ExclusiveArch:  x86_64 aarch64 ppc64le s390x riscv64

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  readline-devel

%description
bcal (Byte CALculator) is a command-line utility for storage conversions
and calculations. Storage, hardware and firmware developers work
with numerical calculations regularly e.g., storage unit conversions,
address calculations etc. If you are one and can't calculate the hex address
offset for (512 - 16) MiB immediately, or the value when the 43rd bit of
a 64-bit address is set, bcal is for you

%prep
%autosetup -p1 -n %{name}-%{version}
sed -i '/STRIP ?= strip/d;s/install: bcal/install: /;s/$(CFLAGS)/$(CFLAGS) $(LDFLAGS)/' Makefile

%build
%{set_build_flags}
export CFLAGS="-fPIC %{optflags}"
%make_build bcal

%install
%make_install PREFIX=%{_prefix}

%files
%doc CHANGELOG README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
%autochangelog
