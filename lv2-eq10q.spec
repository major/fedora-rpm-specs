Name:           lv2-eq10q
Version:        2.2
Release:        %autorelease
Summary:        LV2 audio plugin suite

# All source file headers indicate GPL-2.0-or-later, but the COPYING file
# contains the GPLv3 license text. Since there are no source files without
# license statements in their headers, we assume this is an error, but we have
# asked upstream to clarify:
#
#   Please clarify the license
#   https://sourceforge.net/p/eq10q/bugs/24/
License:        GPL-2.0-or-later
URL:            https://eq10q.sourceforge.net/
Source0:        https://downloads.sourceforge.net/project/eq10q/eq10q-%{version}.tar.gz

# The upstream project has been dormant since 2016, so while I and others
# submitted the following patches upstream, I don’t expect them to be applied.

# Customizable paths and flags
# https://sourceforge.net/p/eq10q/patches/13/
Patch:          lv2-eq10q-2.2-path-and-flags.patch
# Use exp10 instead of pow10 (newer glibc).
# https://sourceforge.net/p/eq10q/patches/12/
Patch:          lv2-eq10q-2.2-exp10.patch
# Specify a minimum of cmake-3.5 as compatibility with older versions will be
# removed from a future version of cmake.
# https://sourceforge.net/p/eq10q/patches/14/
Patch:          lv2-eq10q-2.2-cmake-3.5.patch
# Older versions of lv2 had an _LV2UI_Descriptor type/alias, this was removed.
# https://sourceforge.net/p/eq10q/patches/15/
Patch:          lv2-eq10q-2.2-typefix.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gtkmm-2.4)
BuildRequires:  fftw-devel
BuildRequires:  lv2-devel
Requires:       lv2%{?_isa}

# This resurrects the retired lv2-EQ10Q-plugins package whose name doesn't
# comply with Fedora package naming guidelines.
Obsoletes:      lv2-EQ10Q-plugins < 2.2.1
Provides:       lv2-EQ10Q-plugins = %{version}-%{release}

%description
EQ10Q is an audio plugin bundle using the LV2 standard which implements
powerful and flexible parametric equalizers, compressors, a harmonic enhancer
for bass frequencies and mid/side encoders/decoders.

%prep
%autosetup -p1 -n eq10q-%{version}

# Get rid of warnings about spurious exec permissions in debuginfo package
find . -type f -perm /0111 -exec chmod -v a-x '{}' '+'

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_compiler_flags
sed -i -e 's|-msse -mfpmath=sse||g' -e 's|-O3||g' CMakeLists.txt

%build
%cmake -DCMAKE_INSTALL_PREFIX="%{_libdir}/lv2"
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc README
%{_libdir}/lv2/*

%changelog
%autochangelog
