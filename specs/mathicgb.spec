Name:           mathicgb
Version:        1.5
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

%build -p
export LD_LIBRARY_PATH=$PWD/%{_vpath_builddir}/src

%install -a
# We install these files in a different place
rm -fr %{buildroot}%{_docdir}/%{name}

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
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%files libs
%{_libdir}/lib%{name}.so.0{,.*}

%changelog
%autochangelog
