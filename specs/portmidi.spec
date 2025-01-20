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
Release:        60%{?dist}
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
BuildRequires: make
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
%endif

%build
export JAVA_HOME=%{java_home}
%cmake -DCMAKE_SKIP_BUILD_RPATH=1 -DCMAKE_CACHEFILE_DIR=%{_builddir}/%{name}/build -DVERSION=%{version} -B.
make %{?_smp_flags}

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
%make_install

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
* Sat Jan 18 2025 Michael J Gruber <mjg@fedoraproject.org> - 217-60
- fix FTBFS with newer gcc

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 217-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 217-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 217-57
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 217-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 217-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 217-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 217-53
- Rebuilt for Python 3.12

* Wed Mar 29 2023 Michael J Gruber <mjg@fedoraproject.org> - 217-52
- Adjust patch macro usage to rpm >= 4.18

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 217-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 09 2023 Florian Weimer <fweimer@redhat.com> - 217-50
- C99 compatibility fixes

* Tue Dec 06 2022 Michael J Gruber <mjg@fedoraproject.org> - 217-49
- SPDX migration

* Tue Jul 26 2022 Michael J Gruber <mjg@fedoraproject.org> - 217-48
- fix FTBFS caused by Drop_i686_JDKs

* Tue Jul 26 2022 Michael J Gruber <mjg@fedoraproject.org> - 217-47
- clarify java utils/tools dependencies

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 217-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 217-45
- Rebuilt for Python 3.11

* Fri Apr 01 2022 Tomas Popela <tpopela@redhat.com> - 217-44
- Don't hardcode the java path as it might be different in i.e. Flatpak builds

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 217-43
- Rebuilt for java-17-openjdk as system jdk

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 217-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 217-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 217-40
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 217-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Michael J Gruber <mjg@fedoraproject.org> - 217-38
- original PR: Thu Jul 30 2020 Michael J Gruber <mjg@fedoraproject.org> - 217-37
- adjust to new cmake macros

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 217-37
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 217-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 217-35
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jun 24 2020 Michael J Gruber <mjg@fedoraproject.org> - 217-34
- Make it clear that we do not use setup.py
- Remove obsolete README.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 217-33
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 217-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 217-31
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 217-30
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 217-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 20 2019 Michael J Gruber <mjg@fedoraproject.org> - 217-28
- Generate Cython C files during build

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 217-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 01 2018 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 217-26
- Removed the Python2 binding

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 217-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 217-24
- Rebuilt for Python 3.7

* Thu Mar 08 2018 Michael J Gruber <mjg@fedoraproject.org> - 217-23
- Adjust to new guidelines (BR gcc)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 217-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 217-21
- Python 2 binary package renamed to python2-portmidi
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 217-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 217-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 217-18
- Rebuild due to bug in RPM (RHBZ #1468476)

* Thu Jun 08 2017 Gwyn Ciesla <limburgher@gmail.com> - 217-17
- Python 3 support.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 217-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 217-15
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 217-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 217-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 217-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 09 2014 Brendan Jones <brendan.jones.it@gmail.com> 217-11
- -Wformat-security patch

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 217-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 11 2013 Brendan Jones <brendan.jones.it@gmail.com> 217-9
- Correct desktop file

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 217-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 217-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 217-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 217-6
- Fix multilib conflict RHBZ#831432
- Don't bulid PDF doc, as it causes another multilib conflict
- Specfile cleanup. Drop old GCJ-Java and Python bits

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 217-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 23 2011 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 217-4
- Fix FTBFS due to changes in cmake. RHBZ #715668

* Sat May 14 2011 Daniel Drake <dsd@laptop.org> - 217-3
- move Requires:Java to tools subpackage, its not needed by the main package

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 217-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 09 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 217-1
- Update to 217

* Fri Jul 23 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 200-4
- Fix python module build

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 200-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Jan 30 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 200-2
- Remove duplicate library

* Sat Jan 30 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 200-1
- Update to 200.
- Add python subpackage

* Fri Nov 27 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 184-1
- Update to 184. Build system uses cmake now.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 131-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 131-3
- Include pmutil.h in the devel package

* Tue Jan 27 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 131-2
- Build and add doxygen documentation
- Preserve some timestamps

* Sun Jan 11 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 131-1
- New upstream release.

* Sun Dec 07 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 82-1
- Initial release.
