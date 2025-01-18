# The different tarballs have been at different versions
%global shortv %(echo %version|awk -F. '{print $1 "." $2}')
# Has been different from cubelib/cube
%global cubew_vers %version
%global shortwv %(echo %cubew_vers|awk -F. '{print $1 "." $2}')
%if 0%{?el7}
%global dts devtoolset-9
%endif
%{!?bash_completion_dir:%global bash_completion_dir /usr/share/bash-completion/comlpetions}
# Interface version (used by fake cubelib-config in build)
%global intver 12:0:2

Name:           cube
Version:        4.8.2
Release:        5%{?dist}
Summary:        CUBE Uniform Behavioral Encoding generic presentation component
License:        BSD-3-Clause
URL:            http://www.scalasca.org/software/cube-4.x/download.html
Source0:        http://apps.fz-juelich.de/scalasca/releases/cube/%shortwv/dist/cubegui-%{version}.tar.gz
Source1:        http://apps.fz-juelich.de/scalasca/releases/cube/%shortwv/dist/cubew-%{cubew_vers}.tar.gz
Source2:        http://apps.fz-juelich.de/scalasca/releases/cube/%shortwv/dist/cubelib-%{version}.tar.gz
%if 0
Source0:        https://perftools.pages.jsc.fz-juelich.de/cicd/cubegui/tags/cubegui-4.8-rc1/cubegui-4.8-rc1.tar.gz
Source1:        https://perftools.pages.jsc.fz-juelich.de/cicd/cubew/tags/cubew-4.8-rc1/cubew-4.8-rc1.tar.gz
Source2:        https://perftools.pages.jsc.fz-juelich.de/cicd/cubelib/tags/cubelib-4.8-rc1/cubelib-4.8-rc1.tar.gz
%endif
BuildRequires:  dbus-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  zlib-devel
BuildRequires: 	make
BuildRequires:  %{?dts:%dts-}gcc-c++
%ifarch %qt5_qtwebengine_arches
# Not in ppc64le el9, for instance
BuildRequires:  qt5-qtwebengine-devel
%endif
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%global ver %version

%description
CUBE (CUBE Uniform Behavioral Encoding) is a generic presentation component
suitable for displaying a wide variety of performance metrics for parallel
programs including MPI and OpenMP applications. CUBE allows interactive
exploration of a multidimensional performance space in a scalable fashion.
Scalability is achieved in two ways: hierarchical decomposition of individual
dimensions and aggregation across different dimensions. All performance
metrics are uniformly accommodated in the same display and thus provide the
ability to easily compare the effects of different kinds of performance
behavior.


%package        libs
Summary:        Non-GUI libraries for %{name}

%description    libs
Non-GUI libraries required by %{name}

%package  	libs-devel
Summary:	Development files for %{name}-libs
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description	libs-devel
Development files for %{name}-libs.

%package        guilib
Summary:        GUI library for %{name}

%description    guilib
GUI library for %{name}.

%package  	guilib-devel
Summary:	Development files for %{name}-guilib
Requires:       %{name}-guilib%{?_isa} = %{version}-%{release}

%description	guilib-devel
Development files for %{name}-guilib.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs-devel = %{version}-%{release}
Requires:	%{name}-guilib-devel = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}, including GUI applications.


%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation for %{name}.


%prep
%setup -q -c
tar fx %SOURCE0
tar fx %SOURCE1
tar fx %SOURCE2
# Fiddle for cubelib not being installed when building cubegui
cat <<+ >cubelib-config
#!/bin/sh
case \$1 in
--cppflags|--cflags) printf '%s\n' -I$(pwd)/cubelib-%ver/inst%_includedir/cubelib ;;
--ldflags)  printf '%s\n' -L$(pwd)/cubelib-%ver/inst%_libdir ;;
--libs) printf '%s\n' '-lcube4 -lz' ;;
--interface-version) printf '%s\n' %intver ;;
esac
+
chmod +x cubelib-config
# In v4.7 these files define compiler flags overriding the supplied
# ones in configure, which actually breaks the test for working CC due
# to -fPIE inconsistency.
# for d in cubew-* cubelib-%ver cubegui-*; do
#   printf 'CC=gcc\nCXX=g++\n' >$d/build-config/common/platforms/platform-backend-linux
# done


%build
%{?dts:. /opt/rh/%dts/enable}
# This may not be the best way to eliminate rpath from the -config binaries.
# rpmlint still complains, apparently about a string which doesn't
# affect --ldflags or show up in chrpath -l.
%global unhardcode \
  sed -i -e 's/HARDCODE_INTO_LIBS"]="1"/HARDCODE_INTO_LIBS"]="0"/' \\\
         -e "s/hardcode_into_libs='yes'/hardcode_into_libs='no'/"
cd cubew-%cubew_vers
# The configure configuration now ignores $CFLAGS etc. in the
# environment and actually fails for want of -fPIC, sigh, but not if
# they're given as args.
%configure --enable-shared --disable-static --disable-silent-rules \
   CXXFLAGS="$CXXFLAGS" CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS"
%unhardcode build-backend/config.status
%make_build
cd ../cubelib-%ver
%configure --enable-shared --disable-static --disable-silent-rules \
   CXXFLAGS="$CXXFLAGS" CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS"
%unhardcode build-frontend/config.status
%make_build
# Collect it for use by cubegui
make install DESTDIR=$(pwd)/inst
# Wrong paths in .la cause trouble
rm inst%_libdir/*.la
cd ../cubegui-%ver
# Kludge: For some reason the Qt dependencies are found as .so paths
# in Fedora (only), and libtool re-orders them with libcube4gui after what it
# should link against, and linking fails.
%{?fedora:export LIBS="$LIBS -lQt5PrintSupport -lQt5Widgets -lQt5Gui -lQt5Network -lQt5Concurrent -lQt5Core"}
%configure --disable-static \
  --disable-silent-rules \
  --with-platform=linux \
  --with-cubelib=$(pwd)/.. \
   CXXFLAGS="$CXXFLAGS" CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS"
%unhardcode build-frontend/config.status
%make_build


%install
%make_install -C cubew-%cubew_vers
%make_install -C cubelib-%ver
%make_install -C cubegui-%ver
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Don't duplicate large files
ln -sf ../../cubelib/example/{trace,summary}.cubex %buildroot%_docdir/cubegui/example

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/CUBE.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright (c) 2014 Forschungszentrum Juelich GmbH, Germany -->

<application>
 <id type="desktop">CUBE.desktop</id>
 <metadata_license>CC0-1.0</metadata_license>
 <project_license>BSD-3-Clause</project_license>
 <name>Cube</name>
 <summary>A presentation component suitable for displaying
performance data for parallel programs</summary>
 <description>
  <p>
    "Cube" (CUBE Uniform Behavioral Encoding) is a presentation
    component suitable for displaying a wide variety of performance
    data for parallel programs including MPI and OpenMP applications.
  </p>
  <p>
    Program performance is represented in a multi-dimensional space including various program and
    system resources. The tool allows the interactive exploration of this
    space in a scalable fashion and browsing the different kinds of
    performance behavior with ease.  All metrics are uniformly accommodated in the 
    same display and thus provide the ability to easily compare the effects of 
    different kinds of program behavior.
  </p>
  <p>
    "Cube" also includes a library to
    read and write performance data as well as operators to compare,
    integrate, and summarize data from different experiments. 
  </p>
  <p>
    The Cube 4.x release series uses an incompatible API and
    file format compared to previous versions, however,
    existing files in CUBE3 format can still be processed
    for backwards-compatibility.    
  </p>
 </description>
 <screenshots>
  <screenshot type="default" width="1152" height="648">http://apps.fz-juelich.de/scalasca/releases/cube/screenshots/topo1.png</screenshot>
  <screenshot width="1152" height="648">http://apps.fz-juelich.de/scalasca/releases/cube/screenshots/topo2.png</screenshot>
  <screenshot width="1152" height="648">http://apps.fz-juelich.de/scalasca/releases/cube/screenshots/box.png</screenshot>
  <screenshot width="1152" height="648">http://apps.fz-juelich.de/scalasca/releases/cube/screenshots/flat.png</screenshot>
  <screenshot width="1152" height="648">http://apps.fz-juelich.de/scalasca/releases/cube/screenshots/palette.png</screenshot>
 </screenshots>
 <url type="homepage">http://www.scalasca.org/software/cube-4.x/download.html</url>
 <updatecontact>scalasca_at_fz-juelich.de</updatecontact>
</application>
EOF

# Strip rpath
chrpath -d -k %{buildroot}%{_bindir}/* %{buildroot}%{_libdir}/{,cube-plugins/}*.so  || :

# Install desktop file
cat <<EOF >CUBE.desktop
[Desktop Entry]
Comment=Performance profile browser CUBE
Exec=%_bindir/cube
Icon=%_datadir/icons/cubegui/Cube.xpm
InitialPreference=3
MimeType=application/cube;
Name=Cube (scalasca.org)
Terminal=false
Type=Application
Categories=Science;ComputerScience;DataVisualization;
EOF
desktop-file-install --dir=%{buildroot}%{_datadir}/applications CUBE.desktop

# For abipkgdiff/taskotron; fixme: is there a conventional place to put it?
cat >%{buildroot}%{_libdir}/cube-plugins/plugins.abignore <<EOF
[suppress_file]
file_name_regexp = .*-plugin\\.so.*
EOF

mkdir -p %{buildroot}%{bash_completion_dir}
mv %{buildroot}%{_bindir}/cubegui-autocompletion.sh %{buildroot}%{bash_completion_dir}/cubegui
# For MacOS?
rm %{buildroot}%{_bindir}/maccubegui.sh


%check
%{?dts:. /opt/rh/%dts/enable}
make -C cubelib-%ver check || { cat test/test*/*log && false; }
make -C cubew-%cubew_vers check || { cat test/test*/*log && false; }


%if 0%{?el7}
%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/update-desktop-database &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
/usr/bin/update-desktop-database &> /dev/null || :

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%ldconfig_scriptlets libs
%ldconfig_scriptlets guilib


%files
%license cubegui-%ver/COPYING
%doc cubegui-%ver/AUTHORS
%doc cubegui-%ver/ChangeLog
%doc cubegui-%ver/OPEN_ISSUES
%doc cubegui-%ver/README
%{_bindir}/cube
%{_bindir}/cube3to4
%{_bindir}/cube4to3
%{_bindir}/cube_calltree
%{_bindir}/cube_canonize
%{_bindir}/cube_clean
%{_bindir}/cube_cmp
%{_bindir}/cube_commoncalltree
%{_bindir}/cube_cut
%{_bindir}/cube_derive
%{_bindir}/cube_diff
%{_bindir}/cube_dump
%{_bindir}/cube_exclusify
%{_bindir}/cube_inclusify
%{_bindir}/cube_info
%{_bindir}/cube_is_empty
%{_bindir}/cube_mean
%{_bindir}/cube_merge
%{_bindir}/cube_nodeview
%{_bindir}/cube_part
%{_bindir}/cube_rank
%{_bindir}/cube_regioninfo
%{_bindir}/cube_remap2
%{_bindir}/cube_sanity
%{_bindir}/cube_stat
%{_bindir}/cube_test
%{_bindir}/cube_topoassist
%{_bindir}/tau2cube
%{_libdir}/libgraphwidgetcommon-plugin.so.10*
%{_libdir}/cube-plugins/
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/CUBE.desktop
%{_datadir}/icons/*
%{_datadir}/cubegui/
%{bash_completion_dir}/cubegui

%files devel

%files libs
%license cubegui-%ver/COPYING
%{_bindir}/cube_server
%exclude %{_libdir}/lib%{name}4gui*.so*
%{_libdir}/lib%{name}*.so.12*
%{_datadir}/cubelib/
%{_datadir}/cubew/

%files libs-devel
%{_bindir}/cubelib-config
%{_bindir}/cubew-config
%{_includedir}/cubew
%{_includedir}/cubelib
%{_libdir}/lib%{name}*.so
%doc cubegui-%ver/examples

%files guilib
%license cubegui-%ver/COPYING
%{_libdir}/lib%{name}4gui.so.10*
%{_libdir}/libgraphwidgetcommon-plugin.so

%files guilib-devel
%{_bindir}/cubegui-config
%{_includedir}/cubegui
%{_libdir}/lib%{name}4gui.so

%files doc
%license cubegui-%ver/COPYING
%doc %_docdir/cubew
%doc %_docdir/cubelib
%doc %_docdir/cubegui


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 18 2023 Dave Love <loveshack@fedoraproject.org> - 4.8.2-1
- Update to v4.8.2
- Drop patch

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 20 2023 Florian Weimer <fweimer@redhat.com> - 4.8.1-2
- Port configure script to C99 (#2179882)

* Wed Mar 15 2023  <vagrant@rhel8.localdomain> - 4.8,1-1
- New version

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Dave Love <loveshack@fedoraproject.org> - 4.8-1
- New version (#2074718)

* Thu Sep  8 2022 Dave Love <loveshack@fedoraproject.org> - 4.7-4
- Use SPDX licence TAG

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Apr 13 2022 Dave Love <loveshack@fedoraproject.org> - 4.7-2
- Fix %%intver

* Tue Apr 12 2022 Dave Love <loveshack@fedoraproject.org> - 4.7-1
- New version
- Update source URLs
- Use webengine conditionally

* Mon Feb 28 2022 Dave Love <loveshack@fedoraproject.org> - 4.6-4
- BR qt5-qtwebengine-devel

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun  9 2020 Dave Love <loveshack@fedoraproject.org> - 4.5-1
- New version, with some build changes

* Fri May 29 2020 Dave Love <loveshack@fedoraproject.org> - 4.4.4-3
- Always build with Qt5 and kludge around the Fedora failure

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug  1 2019 Dave love <loveshack@fedoraproject.org> - 4.4.4-1
- New version

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 21 2019 Dave Love <loveshack@fedoraproject.org> - 4.4.3-1
- New version
- Drop qt patch

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Dave Love <loveshack@fedoraproject.org> - 4.4.2-4
- Add empty %%files so cube-devel actually built

* Wed Jan 16 2019 Dave Love <loveshack@fedoraproject.org> - 4.4.2-3
- Remove /usr/lib64/libcube4gui.so from cube-libs

* Mon Dec  3 2018 Dave Love <loveshack@fedoraproject.org> - 4.4.2-2
- Adapt to el8, with qt5
- Add guilib{,-devel} sub-packages really to separate GUI dependency
- Add missing license files

* Mon Oct 22 2018 Dave Love <loveshack@fedoraproject.org> - 4.4.2-1
- Update to cubew 4.4.1, cubelib and cubeGUI 4.4.2

* Mon Oct 22 2018 Dave Love <loveshack@fedoraproject.org> - 4.4-6
- Avoid rpath in -config program ldflags
- Only ship one copy of .cubex example files

* Fri Oct 12 2018 Dave Love <loveshack@fedoraproject.org> - 4.4-5
- Bump release for f28 rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 4.4-4
- Rebuild with fixed binutils

* Fri Jul 27 2018 Dave Love <loveshack@fedoraproject.org> - 4.4-3
- Add .abignore file
- Fix desktop file
- Move libcube4gui to cube package to avoid cube-libs requiring Qt

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 14 2018 Dave Love <loveshack@fedoraproject.org> - 4.4-1
- New version
- Considerably restructured for new source structure, but keeping the
  same built packages

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Dave Love <loveshack@fedoraproject.org> - 4.3.5-1
- Update to 4.3.5 (#1456614)

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 09 2017 Kalev Lember <klember@redhat.com> - 4.3.4-6
- Fix icon path in the desktop file

* Fri Oct 21 2016 Orion Poplawski <orion@cora.nwra.com> - 4.3.4-5
- Add patch to not wrap includes in extern "C" {}

* Tue May 10 2016 Dave Love <loveshack@fedoraproject.org> - 4.3.4-4
- Run ldconfig for both main as well as libs (for libgraphwidgetcommon-plugin)

* Mon May  9 2016 Dave Love <loveshack@fedoraproject.org> - 4.3.4-3
- Run ldconfig for libs package, not main

* Thu May  5 2016 Dave Love <loveshack@fedoraproject.org> - 4.3.4-2
- Have cube require matching cube-libs
- Don't do network check for new version

* Wed May  4 2016 Dave Love <loveshack@fedoraproject.org> - 4.3.4-1
- Update to 4.3.4
- Adjust for desktop and module files removed from distribution
- Remove xerces from configure
- Reinstate smp make

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 11 2015 Orion Poplawski <orion@cora.nwra.com> - 4.3.3-1
- Update to 4.3.3

* Sat Oct  3 2015 Dave Love <loveshack@fedoraproject.org> - 4.3.2-3
- Have devel package depend on cube-libs, not cube

* Fri Jun 26 2015 Dave Love <d.love@liverpool.ac.uk> - 4.3.2-2
- Make separate libs package (for scorep)
- Don't BR Java stuff

* Fri Jun 19 2015 Orion Poplawski <orion@cora.nwra.com> - 4.3.2-1
- Update to 4.3.2
- Drop java sub-package, moved to separate release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 5 2015 Orion Poplawski <orion@cora.nwra.com> - 4.3.1-1
- Update to 4.3.1

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.2.3-5
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 4.2.3-4
- Add an AppData file for the software center

* Tue Mar  3 2015 Peter Robinson <pbrobinson@fedoraproject.org> 4.2.3-3
- rebuild (gcc5)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Orion Poplawski <orion@cora.nwra.com> - 4.2.3-1
- Update to 4.2.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 3 2014 Orion Poplawski <orion@cora.nwra.com> - 4.2.2-1
- Update to 4.2.2
- Fix doc duplication
- Add icon and destop-database scriptlets
- Use chrpath to strip rpaths

* Fri Feb 28 2014 Orion Poplawski <orion@cora.nwra.com> - 4.2.1-2
- Add %%check

* Wed Feb 26 2014 Orion Poplawski <orion@cora.nwra.com> - 4.2.1-1
- Update to 4.2.1

* Fri Nov 8 2013 Orion Poplawski <orion@cora.nwra.com> - 4.2-3
- Fix 32bit build

* Wed Oct 2 2013 Orion Poplawski <orion@cora.nwra.com> - 4.2-2
- Use patch to fix up various libdir paths
- Modify configure to remove rpath

* Fri Sep 27 2013 Orion Poplawski <orion@cora.nwra.com> - 4.2-1
- Initial package
