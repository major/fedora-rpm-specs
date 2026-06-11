Name:           mathicgb
Version:        1.4
Release:        %autorelease
Summary:        Groebner basis computations

License:        GPL-2.0-or-later
URL:            https://github.com/Macaulay2/mathicgb
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    cmake
BuildOption(conf): -DBUILD_SHARED_LIBS:BOOL=ON
BuildOption(conf): -DBUILD_TESTING:BOOL=ON
BuildOption(conf): -DCMAKE_SKIP_RPATH:BOOL=ON
BuildOption(conf): -Dwith_tbb:BOOL=ON

BuildRequires:  cmake(GTest)
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(mathic)
BuildRequires:  pkgconfig(tbb)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
Mathicgb is a program for computing Groebner basis and signature Groebner
bases.  Mathicgb is based on the fast data structures from mathic.

%package devel
Summary:        Development files for mathicgb
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Files for developing applications that use mathicgb.

%package libs
Summary:        Mathicgb libraries

%description libs
Library interface to mathicgb.

%prep
%autosetup

# Fix the installation directory
sed -i 's, lib, ${LIB_INSTALL_DIR},' CMakeLists.txt

# Add an soname
sed -e '/compile_options/iset_target_properties(mathicgb PROPERTIES VERSION 0.0.4 SOVERSION 0)' \
    -i src/CMakeLists.txt

%build -p
export LD_LIBRARY_PATH=$PWD/%{_vpath_builddir}/src

%install -a
# These files are not installed by cmake
cp -p src/mathicgb.h %{buildroot}%{_includedir}

# Move the man page to the right directory
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_mandir}/mgb.1 %{buildroot}%{_mandir}/man1

# Install the pkgconfig file for backwards compatibility
# Fix the URL in the pkgconfig file
mkdir -p %{buildroot}%{_libdir}/pkgconfig
sed -e 's,@prefix@,%{_prefix},' \
    -e 's,@exec_prefix@,%{_prefix},' \
    -e 's,@libdir@,%{_libdir},' \
    -e 's,@includedir@,%{_includedir},' \
    -e 's,@PACKAGE_VERSION@,%{version},' \
    -e 's,broune,Macaulay2,' \
    build/autotools/mathicgb.pc.in \
    > %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

# We install these files in a different place
rm -fr %{buildroot}%{_prefix}/licenses %{buildroot}%{_mandir}/mgb.1

%check
export LD_LIBRARY_PATH=$PWD/%{_vpath_builddir}/src
%{_vpath_builddir}/src/mathicgb-unit-tests

%files
%doc README.md doc/description.txt doc/slides.pdf
%license gpl-2.0.txt gpl-3.0.txt
%{_bindir}/mgb
%{_mandir}/man1/mgb.1*

%files devel
%{_includedir}/%{name}.h
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files libs
%{_libdir}/lib%{name}.so.0{,.*}

%changelog
%autochangelog
