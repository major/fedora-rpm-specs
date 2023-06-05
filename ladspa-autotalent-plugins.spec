Name:           ladspa-autotalent-plugins
Version:        0.2
Release:        %autorelease
Summary:        A pitch-correcting LADSPA plugin

# From COPYING:
#
#   Autotalent (autotalent.c) is released under GPL2.  However, the FFT
#   routine was taken from PureData
#   (http://crca.ucsd.edu/~msp/software.html), which was released under a
#   license that is similar to the BSD license.  So with the exception of
#   the mayer_fft.* files, everything should fall under GPL2.  The license
#   pertinent to mayer_fft.* is contained in COPYING-mayer_fft.
#
#   -Tom
#
# The copyright and license statement in the header comment of autotalent.c
# makes clear that GPL-2.0-or-later is intended. The obsolete FSF postal
# address in COPYING, autotalent.c, and Makefile was reported upstream by email
# on 2023-04-26.
#
# The files mayer_fft.h and mayer_fft.c are BSD-3-Clause.
#
# Additionally, ladspa.h is LGPL-2.1-or-later, but it is removed in %%prep and
# is not used in compiling the plugins, so it does not contribute to the
# licenses of the binary RPMs.
#
# The reference card http://tombaran.info/autotalent-%%{version}_refcard.pdf
# was previously packaged as useful documentation. Icons in the bottom right
# corners of the PDF indicate its license is CC-BY-ND, but do not specify a
# version, so we are not able to determine the correct SPDX expression. In any
# case, the CC-BY-ND-* licenses are approved for content but not for
# documentation.
License:        GPL-2.0-or-later AND BSD-3-Clause
URL:            http://tombaran.info/autotalent.html
Source:         http://tombaran.info/autotalent-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  make

BuildRequires:  ladspa-devel

# For %%{_libdir}/ladspa/
Requires:       ladspa

%description
Autotalent is a real-time pitch correction plugin. You specify the notes that a
singer is allowed to hit, and Autotalent makes sure that they do. You can also
use Autotalent for more exotic effects, making your voice sound like a
chiptune, adding artificial vibrato, or messing with your formants.  Autotalent
can also be used as a harmonizer that knows how to sing in the scale with you.
Or, you can use Autotalent to change the scale of a melody between major and
minor or to change the musical mode.

A reference card is available at:

http://tombaran.info/autotalent-%{version}_refcard.pdf


%prep
%setup -q -n autotalent-%{version}

# Use the system ladspa.h
rm -v ladspa.h
sed -i 's|ladspa.h||' Makefile


%build
# Upstream default CFLAGS:
#   -I. -O3 -Wall -fomit-frame-pointer -fstrength-reduce -funroll-loops
#   -ffast-math -c -fPIC -DPIC
# Of these,
#   -O3 -fomit-frame-pointer -fstrength-reduce -funroll-loops -ffast-math
# are optimization flags. In the spirit of
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_compiler_flags,
# and in the absence of benchmarks showing their benefit, we omit these, except
# for -ffast-math, which we argue is not a generic optimization flag but a
# statement about the level of floating-point standards-conformance that the
# software is designed to require.
export CFLAGS="-I. ${CFLAGS-} -Wall -ffast-math -c -fPIC -DPIC"
# Upstream default LDFLAGS
#   -nostartfiles -shared -Wl,-Bsymbolic -lc -lm -lrt
# These are generally OK; -lc is not required, and since glibc 2.17, -lrt is
# not needed for clock_* functions. We are not sure exactly what -Wl,-Bsymbolic
# is doing, so we leave it alone.
export LDFLAGS="${LDFLAGS-} -nostartfiles -shared -Wl,-Bsymbolic -lm"

%make_build CC="${CC-gcc}" CFLAGS="${CFLAGS}" LDFLAGS="${LDFLAGS}"


%install
%make_install INSTALL_PLUGINS_DIR='%{buildroot}%{_libdir}/ladspa'


%files
%license COPYING COPYING-mayer_fft
%doc README

%{_libdir}/ladspa/autotalent.so


%changelog
%autochangelog
