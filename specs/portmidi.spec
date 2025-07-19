%global __cmake_in_source_build 1

%if 0%{?fedora} >= 36
# Leave undefined if not 1:
%ifarch %{java_arches}
%global JAVA 1
%endif
%else
%global JAVA 1
%endif

%bcond docs %{undefined flatpak}

Summary:        Real-time Midi I/O Library
Name:           portmidi
Version:        217
Release:        %autorelease
License:        MIT
URL:            http://portmedia.sourceforge.net/
Source0:        http://downloads.sourceforge.net/portmedia/%{name}-src-%{version}.zip
Source1:        pmdefaults.desktop
# Build fixes:
Patch0:         portmidi-cmake.patch
# Fix multilib conflict RHBZ#831432
Patch1:         portmidi-no_date_footer.patch
Patch2:         portmidi-217-format-security.patch
Patch3:         portmidi-no.c++.patch
Patch4:         portmidi-cyrex-0.21.patch
Patch5:         portmidi-c99.patch
Patch6:         portmidi-PtTime.patch
# Number no java patches 100 and above
Patch100:       portmidi-no.java.patch
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
BuildRequires:  python3-Cython
%if %{with docs}
BuildRequires:  doxygen
BuildRequires:  tex(latex)
%endif
BuildRequires:  gcc
%if 0%{?JAVA}
BuildRequires:  java-devel >= 1.7
BuildRequires:  javapackages-tools
%endif

%description
PortMedia is a set of simple clean APIs and cross-platform library
implementations for music and other media. PortMidi sub-project provides a
real-time MIDI input/output library. This package contains the PortMidi
libraries.

%package devel
Summary:        Headers for developing programs that will use %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
PortMedia is a set of simple clean APIs and cross-platform library
implementations for music and other media. PortMidi sub-project provides a
real-time MIDI input/output library. This package contains the header files
and the documentation of PortMidi libraries.

%package -n python3-%{name}
Summary:        Python 3 wrapper for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
PortMedia is a set of simple clean APIs and cross-platform library
implementations for music and other media. PortMidi sub-project provides a
real-time MIDI input/output library. This package contains the python
bindings of PortMidi libraries. It can send and receive MIDI data in
real-time from Python 3.

%package tools
Summary:          Tools to configure and use %{name}
Requires:         hicolor-icon-theme
Requires:         java >= 1.7
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description tools
PortMedia is a set of simple clean APIs and cross-platform library
implementations for music and other media. PortMidi sub-project provides a
real-time MIDI input/output library. This package contains
%{?JAVA:the PortMidi configuration utility "pmdefaults" and 
}some test applications.

%prep
%autosetup -n %{name} -N
%autopatch -p 1 -M 99
%if ! 0%{?JAVA}
%autopatch -p 1 -m 100
%endif


# generate Cython C files during build
rm -f pm_python/pyportmidi/_pyportmidi.c

# we do not use setup.py
rm -f pm_python/setup.py

# ewwww... binaries
rm -f portmidi_cdt.zip */*.exe */*/*.exe

# Fix permissons and encoding issues:
find . -name "*.c" -exec chmod -x {} \;
find . -name "*.h" -exec chmod -x {} \;
for i in *.txt */*.txt */*/*.txt ; do
   chmod -x $i
   sed 's|\r||' $i > $i.tmp
   touch -r $i $i.tmp
   mv -f $i.tmp $i
done

%if 0%{?JAVA}
# Fedora's jni library location is different
sed -i 's|loadLibrary.*|load("%{_libdir}/%{name}/libpmjni.so");|' \
   pm_java/jportmidi/JPortMidiApi.java

# Add shebang, lib and class path
sed -i -e 's|^java|#!/bin/sh\njava \\\
   -Djava.library.path=%{_libdir}/%{name}/|' \
   -e 's|/usr/share/java/|%{_libdir}/%{name}/|' \
   pm_java/pmdefaults/pmdefaults

# Don't hardcode the java path as it might be different in i.e. Flatpak builds
sed -i -e 's|/usr/share/java|%{_javadir}|' \
   pm_java/CMakeLists.txt

# CMP0058 makes ninja fail to see that *.java provides *.class dependencies.
# Fix the build the easy way
sed -i -e '/DEPENDS \${PMDEFAULTS_ALL_CLASSES}/d' \
   pm_java/CMakeLists.txt

%endif

# CMake 3.20 introduces CMP0115 which breaks builds
sed -i -e 's|^cmake_minimum_required.*$|cmake_minimum_required(VERSION 3.5...3.19)|' \
   CMakeLists.txt

%build
export JAVA_HOME=%{java_home}
%cmake \
  -DCMAKE_SKIP_BUILD_RPATH=1 \
  -DCMAKE_CACHEFILE_DIR=%{_builddir}/%{name}/build \
  -DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \
  -DLIB_INSTALL_DIR:PATH=%{_libdir} \
  -DVERSION=%{version} \
  %if "%{?_lib}" == "lib64"
     %{?_cmake_lib_suffix64} \
  %endif
  -B.
# direct parallel make works, but cmake_build (using make) fails without -j1
# "-j1" can be removed with ninja
%cmake_build -j1

%if %{with docs}
# Build the doxygen documentation:
doxygen
%endif

# Build python modules
pushd pm_python/pyportmidi
   cython -2 _pyportmidi.pyx
   gcc %{optflags} -pthread -fPIC -c -o _pyportmidi.o -I../../pm_common \
       -I../../porttime $(python3-config --includes) _pyportmidi.c
   gcc -shared -o _pyportmidi.so _pyportmidi.o -lportmidi $(python3-config --libs) \
       -L../../build/Release
popd

%install
%cmake_install

# Install the test applications:
install -d %{buildroot}%{_libdir}/%{name}
for app in latency midiclock midithread midithru mm qtest sysex test; do
   install -m 0755 build/Release/$app %{buildroot}%{_libdir}/%{name}/
done

%if 0%{?JAVA}
# Fedora's jni library location is different
mv %{buildroot}%{_libdir}/libpmjni.so \
   %{buildroot}%{_libdir}/%{name}/
mv %{buildroot}%{_javadir}/pmdefaults.jar \
   %{buildroot}%{_libdir}/%{name}/

# pmdefaults icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
install -pm 644 pm_java/pmdefaults/pmdefaults-icon.png \
   %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/

# desktop file
mkdir -p %{buildroot}%{_datadir}/applications/
desktop-file-install \
   --dir=%{buildroot}%{_datadir}/applications \
   %{SOURCE1}
%endif

# Why don't they install this header file?
install -pm 644 pm_common/pmutil.h %{buildroot}%{_includedir}/

# Install python modules
mkdir -p %{buildroot}%{python3_sitearch}/pyportmidi
pushd pm_python/pyportmidi
   install -pm 755 _pyportmidi.so %{buildroot}%{python3_sitearch}/pyportmidi/
   install -pm 644 *.py %{buildroot}%{python3_sitearch}/pyportmidi/
popd

# we don't want to provide private python extension libs
%{?filter_setup:
%filter_provides_in %{python3_sitearch}/.*\.so$
%filter_setup
}

# Remove duplicate library
rm -f %{buildroot}%{_libdir}/libportmidi_s.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc CHANGELOG.txt
%license license.txt
%{_libdir}/lib*.so.*

%files tools
%doc pm_java/pmdefaults/README.txt pm_cl/*
%{_libdir}/%{name}/
%if 0%{?JAVA}
%{_bindir}/pmdefaults
%{_datadir}/icons/hicolor/128x128/apps/pmdefaults-icon.png
%{_datadir}/applications/pmdefaults.desktop
%endif

%files -n python3-%{name}
%{python3_sitearch}/pyportmidi/

%files devel
%doc README.txt
%if %{with docs}
%doc html
%endif
%{_includedir}/*
%{_libdir}/lib*.so

%changelog
%autochangelog
