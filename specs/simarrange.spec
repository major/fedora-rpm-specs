%global commit 8238ce568c3ce23e1ad5fbfec55031907bd23f77
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global datestamp 20170316
%global relstring %{datestamp}git%{shortcommit}
Name:           simarrange
Version:        0.0^%{relstring}
Release:        %autorelease
Summary:        STL 2D plate packer with collision simulation
License:        AGPL-3.0-or-later
URL:            https://github.com/kliment/%{name}
Source:         %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch:          simarrange-opencv4.patch
BuildRequires:  gcc-c++
BuildRequires:  admesh-devel
BuildRequires:  argtable-devel
BuildRequires:  opencv-devel
BuildRequires:  uthash-devel

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11
ExcludeArch:    %{ix86}
%endif

%description
Simarrange is a program that simulates collisions between STL meshes in 2D in
order to generate tightly packed sets of parts. It takes a directory of STL
files as input and outputs STL files with combined plates of parts.
The parts are assumed to be in the correct printable orientation already.

%prep
%autosetup -p1 -n %{name}-%{commit}

# bundling
rm utlist.h

%build
# the build script is one line and would need patching, so just skip it
# TODO update to use Makefile
g++ $CXXFLAGS $LDFLAGS simarrange.c -o ./%{name} -lm `pkg-config --cflags --libs opencv` \
    -ladmesh -largtable2 -fopenmp -DPARALLEL

%install
install -Dpm0755 ./%{name} %{buildroot}%{_bindir}/%{name}
install -Dpm0644 ./%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%changelog
%autochangelog
