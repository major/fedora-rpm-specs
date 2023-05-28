Name:           flintqs
Version:        1.0
Release:        %autorelease
Summary:        William Hart’s quadratic sieve

# The entire source is GPL-2.0-or-later, except the following files, all of
# which are part of the build system, and do not contribute to the license of
# the binary RPM:
#   - INSTALL is FSFAP
#   - aclocal.m4 is FSFULLR
#   - config.guess and config.sub are GPL-3.0-or-later
#   - configure is FSFUL, or, more likely (FSFUL AND GPL-2.0-or-later)
#   - install-sh is X11
License:        GPL-2.0-or-later
URL:            https://github.com/sagemath/FlintQS
Source:         %{url}/archive/v%{version}/flintqs-%{version}.tar.gz
# Use of the register storage class is deprecated
# https://github.com/sagemath/FlintQS/pull/2
Patch:          flintqs-register.patch
# Add "const" keywords to silence writable string warnings
# https://github.com/sagemath/FlintQS/pull/2
Patch:          flintqs-writable-string.patch
# Fix mixed signed/unsigned operations
# https://github.com/sagemath/FlintQS/pull/2
Patch:          flintqs-signed.patch
# Remove an unused variable
# https://github.com/sagemath/FlintQS/pull/2
Patch:          flintqs-unused.patch
# Account for possibly unset TMPDIR environment variable
Patch:          flintqs-tmpdir.patch
# Plug memory leaks
# https://github.com/sagemath/FlintQS/pull/1
Patch:          flintqs-memleak.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRequires:  make
BuildRequires:  gcc-c++

BuildRequires:  gmp-devel

%description
This package contains William Hart’s quadratic sieve implementation, as
modified for sagemath.


%prep
%autosetup -n FlintQS-%{version} -p1

# There is no m4 directory
sed -i '/m4/d' configure.ac

# Generate the configure script
AUTOMAKE='automake --foreign' autoreconf --force --install --verbose .


%build
%configure
%make_build


%install
%make_install


%check
# Example from
# https://doc.sagemath.org/html/en/reference/interfaces/sage/interfaces/qsieve.html
factors="$(
  echo '1000000000000000005490000000000000001989' |
  %{buildroot}%{_bindir}/QuadraticSieve |
  awk 'f; /^FACTORS:$/ {f=1}' | sort -n -u | tr '\n' ' '
)"
[ "${factors}" = '10000000000000000051 100000000000000000039 ' ]


%files
%license COPYING
%doc AUTHORS
%doc NEWS
%doc README
%{_bindir}/QuadraticSieve


%changelog
%autochangelog
