Name:           fmidi
Version:        0.1.1
%global so_version 0.1
Release:        %autorelease
Summary:        A library to read and play back MIDI files

License:        BSL-1.0
URL:            https://github.com/jpcima/fmidi
Source:         %{url}/archive/v%{version}/fmidi-%{version}.tar.gz

# Accepted PR to add man pages: https://github.com/jpcima/fmidi/pull/4
Patch:          https://github.com/jpcima/fmidi/pull/4.patch

# Make compatible with newer fmt
# https://github.com/jpcima/fmidi/commit/20916421656e89a1303a85e76e89db8bd551a31e
Patch:          %{url}/commit/20916421656e89a1303a85e76e89db8bd551a31e.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
# This is our choice; the makefile backend would work fine too
BuildRequires:  ninja-build

BuildRequires:  boost-devel
BuildRequires:  libev-devel
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(rtmidi)
BuildRequires:  pkgconfig(fmt)

%global common_description %{expand:
Fmidi is a library to read and play back MIDI files. It supports both standard
MIDI files and RIFF MIDI files.

The functionality is exposed as a C programming interface, and it is
implemented with C++.

It is a simple library which is good for implementing a MIDI file player, or
any program taking MIDI files as inputs. In fact, a player with a terminal
interface is provided as an example.}

%description %{common_description}


%package tools
Summary:        Command-line tools based on the fmidi library
Requires:       fmidi-libs%{?_isa} = %{version}-%{release}

%description tools %{common_description}

The fmidi-tools package contains command-line tools based on the fmidi library.


%package libs
Summary:        Libraries for fmidi

%description libs %{common_description}

The fmidi-libs package contains the fmidi libraries.


%package devel
Summary:        Development files for fmidi
Requires:       fmidi-libs%{?_isa} = %{version}-%{release}

%description devel
The fmidi-devel package contains libraries and header files for
developing applications that use fmidi.


%prep
%autosetup -p1
# Fix library installation paths to match Fedora’s multilib layout. This is a
# quick and dirty patch; I don’t know the “right” way to do this with CMake, so
# I haven’t asked upstream to change anything.
sed -r -i \
    -e 's|"lib(["/])|"%{_libdir}\1|g' \
    -e 's|\\\$\{prefix\}/lib\b|%{_libdir}|g' \
    CMakeLists.txt


%build
%cmake \
    -DFMIDI_ENABLE_DEBUG=OFF \
    -DFMIDI_PIC=ON \
    -DFMIDI_STATIC=OFF \
    -GNinja
%cmake_build


%install
%cmake_install


# The base package has no %%files; there is no “fmidi” binary RPM


%check
# Upstream does not provide any tests.


%files tools
%{_bindir}/fmidi-{convert,grep,play,read,seq}
%{_mandir}/man1/fmidi-{convert,grep,play,read,seq}.1*


%files libs
%license LICENSE.md
%{_libdir}/libfmidi.so.%{so_version}


%files devel
%doc README.md
%{_includedir}/fmidi.h
%{_libdir}/libfmidi.so
%{_libdir}/pkgconfig/fmidi.pc


%changelog
%autochangelog
