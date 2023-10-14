Name:           mt32emu
Version:        2.7.1
Release:        %autorelease
Summary:        C/C++ library for emulating Roland MT-32, CM-32L and LAPC-I synthesizer modules

%global version_ %(v=%{version}; tr . _ <<< $v)

# general license - LGPL-2.1-or-later
# Hash implementation at mt32emu/src/sha1 - BSD-3-Clause
License:        LGPL-2.1-or-later AND BSD-3-Clause
URL:            http://munt.sourceforge.net/
Source0:        https://github.com/munt/munt/archive/refs/tags/lib%{name}_%{version_}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

# Not needed for multilib
ExcludeArch: %{ix86}

%description
mt32emu is a part of the Munt project. It represents a C/C++ library named
libmt32emu which allows to emulate (approximately) the Roland MT-32, CM-32L and
LAPC-I synthesizer modules.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       cmake-filesystem
Requires:       pkgconf-pkg-config

%description devel
%{summary}.

%prep
%autosetup -p1 -n munt-lib%{name}_%{version_}
# Remove other subprojects than mt32emu
rm -rf DOSBox-mt32-patch FreeBSD mt32emu_{alsadrv,smf2wav,qt,win32drv{,_setup}}


%build
# Build only the library
%cmake \
    -Dmunt_WITH_MT32EMU_SMF2WAV=FALSE \
    -Dmunt_WITH_MT32EMU_QT=FALSE \
    -Dlibmt32emu_WITH_VERSION_TAGGING=TRUE \
    -Dlibmt32emu_WITH_SYMBOL_VERSIONING=TRUE
%cmake_build

%install
%cmake_install
# Remove a license that is not actually used
# Upstream explanation for its existence: https://github.com/munt/munt/issues/68#issuecomment-882524417
rm %{buildroot}/%{_docdir}/munt/lib%{name}/COPYING.txt

%check
# No tests available
# %%ctest

%files
%{_libdir}/lib%{name}.so.2*
%license %{_docdir}/munt/lib%{name}/{COPYING.LESSER,AUTHORS}.txt
%dir %{_docdir}/munt
%dir %{_docdir}/munt/lib%{name}
%doc %{_docdir}/munt/lib%{name}/{README.md,NEWS.txt}

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}{.h,}
%{_libdir}/cmake/MT32Emu/
%{_libdir}/pkgconfig/%{name}.pc
%doc %{_docdir}/munt/lib%{name}/TODO.txt

%changelog
%autochangelog
