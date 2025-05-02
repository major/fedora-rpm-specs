# debuginfo not supported for static libraries, RB #209316
%global debug_package %{nil}

# Avoid -Werror=incompatible-pointer-type on 32-bit arches
%ifarch %{ix86}
%global build_type_safety_c 2
%endif

Name:           qm-dsp
Version:        1.8.0
Release:        %autorelease
Summary:        Library for DSP and Music Informatics purposes

%global forgeurl https://github.com/c4dm/qm-dsp
%global tag qm-vamp-plugins-v%{version}
%forgemeta

License:        GPL-2.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}
# build flags (not intended for upstream)
Patch0:         qm-dsp-flags.patch
# install header files
# http://vamp-plugins.org/forum/index.php/topic,270.0.html
Patch1:         qm-dsp-install.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  imake
BuildRequires:  kiss-fft-static
%ifarch %{valgrind_arches}
BuildRequires:  valgrind
%endif
BuildRequires:  boost-devel

%description
%{name} is a C++ library of functions for DSP and Music Informatics purposes
developed at Queen Mary, University of London. It is used by the QM Vamp
Plugins (q.v.) among other things.


%package devel
Summary:        %{summary}
Provides:       %{name}-static = %{version}-%{release}
Provides:       bundled(clapack)

%description devel
%{name} is a C++ library of functions for DSP and Music Informatics purposes
developed at Queen Mary, University of London. It is used by the QM Vamp
Plugins (q.v.) among other things.

This package contains header files and static library for development with
qm-dsp.


%prep
%autosetup -n %{topdir} -N -Sgendiff
cp -p build/linux/Makefile.linux32 Makefile
%autopatch -p1
# use specified CFLAGS for tests
cat >> tests/Makefile <<EOF

%.o: %.cpp
	\$(CXX) \$(CPPFLAGS) \$(CFLAGS) -c \$<
EOF
# unbundle cblas and kiss-fft
rm -rf ext/cblas ext/kiss-fft
# helper Makefile without valgrind
sed -e 's/$(VG) //' tests/Makefile > tests/Makefile.novg


%build
# unbundle kiss-fft
make depend

# extra cflags used in upstream
%ifarch %{ix86}
EXTRA_CFLAGS="-msse -mfpmath=sse"
%endif
%ifarch x86_64
EXTRA_CFLAGS="-msse -msse2 -mfpmath=sse"
%endif

# build
CFLAGS="$EXTRA_CFLAGS %{?optflags} -I%{_includedir}/kissfft" \
LDFLAGS="%{?__global_ldflags}" \
%make_build

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}

# Tests are broken

%files devel
%license COPYING
%doc README.md
%{_libdir}/libqm-dsp.a
%{_includedir}/%{name}/


%changelog
%autochangelog
