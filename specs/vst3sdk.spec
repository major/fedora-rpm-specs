Name:           vst3sdk
Version:        3.8.0
Release:        %autorelease
Summary:        VST 3 Plug-In SDK

%global giturl  https://github.com/steinbergmedia/vst3
%global buildno 66
%global verstr  %{version}_build_%{buildno}
%global tutcom  33b73dfbb87f3fde3bce8c0a10cae934dc66ad34

# Files with licenses other than MIT:
# - cmake/templates/projectversion.h.in: not used in the build
# - public.sdk/samples/vst/adelay: not built
# - public.sdk/samples/vst/again: not built
# - public.sdk/samples/vst/dataexchange: not built
# - public.sdk/samples/vst/hostchecker: not built
# - public.sdk/samples/vst/note_expression_synth_auv3: not built
# - public.sdk/source/vst/moduleinfo: not built
License:        MIT
URL:            https://steinbergmedia.github.io/vst3_doc/vstsdk/
VCS:            git:%{giturl}sdk.git
Source0:        %{giturl}sdk/archive/v%{verstr}/%{name}-%{version}.tar.gz
Source1:        %{giturl}_base/archive/v%{verstr}/vst3_base-%{version}.tar.gz
Source2:        %{giturl}_cmake/archive/v%{verstr}/vst3_cmake-%{version}.tar.gz
Source3:        %{giturl}_pluginterfaces/archive/v%{verstr}/vst3_pluginterfaces-%{version}.tar.gz
Source4:        %{giturl}_public_sdk/archive/v%{verstr}/vst3_public_sdk-%{version}.tar.gz
# Build shared libraries instead of static libraries.
# Prefix the library names with "vst3" to avoid name clashes.
# Make symbols weak as needed to avoid linking issues with shared libraries.
Patch:          %{name}-shared.patch
# Fix some incorrect format specifiers
Patch:          %{name}-format.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  help2man

Requires:       %{name}-common%{?_isa} = %{version}-%{release}

%global _desc %{expand:A VST® plug-in is an audio processing component that is utilized within a host
application.  This host application provides the audio or/and event streams
that are processed by the plug-in's code.  Generally speaking, a VST plug-in
can take a stream of audio data, apply a process to the audio, and return the
result to the host application.  A VST plug-in performs its process normally
using the processor of the computer.  The audio stream is broken down into a
series of blocks.  The host supplies the blocks in sequence.  The host and its
current environment control the block-size.  The VST plug-in maintains the
status of all its own parameters relating to the running process: The host
does not maintain any information about what the plug-in did with the last
block of data it processed.

From the host application's point of view, a VST plug-in is a black box with
an arbitrary number of inputs, outputs (Event (MIDI) or Audio), and associated
parameters.  The host needs no implicit knowledge of the plug-in's process to
be able to use it.  The plug-in process can use whatever parameters it wishes,
internally to the process, but depending on the capabilities of the host, it
can allow the changes to user parameters to be automated by the host.

VST 3 is a general rework of the long-serving VST plug-in interface.  It is
not compatible with the older VST versions, but it includes some new features
and possibilities.  We have redesigned the API to make it not only far easier
and more reliable for developers to work with, but have also provided
completely new possibilities for plug-ins.

VST is a registered trademark of Steinberg Media Technologies GmbH.}

%description
%_desc

This package contains the VST 3 Plug-In library.

%package        hosting
Summary:        VST 3 Hosting SDK
Requires:       %{name}-common%{?_isa} = %{version}-%{release}

%description    hosting
%_desc

This package contains the VST 3 Hosting library.

%package        common
Summary:        VST 3 Common SDK

%description    common
%_desc

This package contains a library of common code for the Plug-In and Hosting
libraries.

%package        devel
Summary:        Development files for the VST 3 SDK
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-common%{?_isa} = %{version}-%{release}
Requires:       %{name}-hosting%{?_isa} = %{version}-%{release}

%description    devel
%_desc

This package contains files needed to develop VST 3 plugins and host
applications.

%package        tools
Summary:        VST 3 SDK tools
Requires:       %{name}-hosting%{?_isa} = %{version}-%{release}

%description    tools
%_desc

This package contains the vst3moduleinfotool and vst3validator tools.  Note
that both tools have a "vst3" prefix to prevent name clashes.

%prep
%autosetup -N -n %{name}-%{verstr}
tar -xf %{SOURCE1} --strip-components=1 -C base
tar -xf %{SOURCE2} --strip-components=1 -C cmake
tar -xf %{SOURCE3} --strip-components=1 -C pluginterfaces
tar -xf %{SOURCE4} --strip-components=1 -C public.sdk

# Apply patches once all the sources are in place
%autopatch -p1

# Remove sources with other licenses to be sure they are not built
rm -fr public.sdk/samples/vst

%build
export LD_LIBRARY_PATH=$PWD/%{_vpath_builddir}/lib/RelWithDebInfo
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_SKIP_RPATH:BOOL=ON \
    -DSMTG_ENABLE_VST3_HOSTING_EXAMPLES:BOOL=OFF \
    -DSMTG_ENABLE_VST3_PLUGIN_EXAMPLES:BOOL=OFF \
    -DSMTG_ENABLE_VSTGUI_SUPPORT:BOOL=OFF
%cmake_build

%install
#%%cmake_install does nothing, so do this by hand
mkdir -p %{buildroot}%{_libdir}
cp -a %{_vpath_builddir}/lib/RelWithDebInfo/lib*so* %{buildroot}%{_libdir}

mkdir -p %{buildroot}%{_includedir}/%{name}
find . -name \*.h -exec tar -cf - {} + | \
    tar -C %{buildroot}%{_includedir}/%{name} -xf -

mkdir -p %{buildroot}%{_bindir}
for f in moduleinfotool validator; do
    cp -p %{_vpath_builddir}/bin/RelWithDebInfo/$f %{buildroot}%{_bindir}/vst3$f
done

export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_mandir}/man1
help2man -N \
    --version-string=%{version} \
    -n 'Get information about a VST 3 module' \
    -o %{buildroot}%{_mandir}/man1/vst3moduleinfotool.1 \
    %{buildroot}%{_bindir}/vst3moduleinfotool
help2man -N \
    --version-string=%{version} \
    -n 'Check a plugin for VST 3 conformity' \
    -o %{buildroot}%{_mandir}/man1/vst3validator.1 \
    %{buildroot}%{_bindir}/vst3validator

%files
%{_libdir}/libvst3sdk.so.0{,.*}

%files common
%doc README.md VST3_Usage_Guidelines.pdf
%license LICENSE.txt
%{_libdir}/libvst3sdk_common.so.0{,.*}

%files hosting
%{_libdir}/libvst3sdk_hosting.so.0{,.*}

%files devel
%{_includedir}/%{name}/
%{_libdir}/libvst3sdk.so
%{_libdir}/libvst3sdk_common.so
%{_libdir}/libvst3sdk_hosting.so

%files tools
%{_bindir}/vst3moduleinfotool
%{_bindir}/vst3validator
%{_mandir}/man1/vst3moduleinfotool.1*
%{_mandir}/man1/vst3validator.1*

%changelog
%autochangelog
