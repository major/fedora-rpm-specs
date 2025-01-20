Name: routino
Summary: Router for OpenStreetMap Data
Version: 3.4.1
Release: 6%{?dist}
License: AGPL-3.0-or-later AND MIT
URL: http://www.routino.org/
Source0: http://www.routino.org/download/routino-%{version}.tgz
# documentation for how to set up Routino for use with Marble
Source1: README-MARBLE.txt
# https://github.com/sharkcz/routino/commits/fedora
Patch0: routino-3.4-fedora.patch
BuildRequires: make
BuildRequires: gcc
BuildRequires: bzip2-devel
BuildRequires: xz-devel
BuildRequires: zlib-devel
BuildRequires: perl-generators
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
Routino is a command-line application for finding a route between two points
using the dataset of topographical information collected by OpenStreetMap. It
can be used as a routing tool in Marble.

%package libs
Summary: Routing library for OpenStreetMap Data
Requires: %{name}-data = %{version}-%{release}

%description libs
The Routino library is a library for finding a route between two points using
the dataset of topographical information collected by OpenStreetMap. It can be
used by applications to embed Routino, as long as the application's license is
compatible with the AGPLv3.

%package data
Summary: Data files for %{name} and %{name}-libs
BuildArch: noarch

%description data
This package contains the architecture-independent data files used by %{name}
and %{name}-libs.

%package doc
Summary: Documentation files for %{name} and %{name}-libs
BuildArch: noarch
# ensure the version matches the actual library (and application if installed)
Requires: %{name}-libs = %{version}-%{release}

%description doc
This package contains the architecture-independent documentation files for
%{name} and %{name}-libs.

%package devel
Summary: Development files for %{name}-libs
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains the files required to compile applications that use
%{name}-libs.


%prep
%autosetup -p1

cp -p %{SOURCE1} doc/

# Get rid of installation documentation which is not applicable to the RPM
rm -f INSTALL*.txt doc/INSTALL*.txt doc/html/installation.html
# The web stuff needs more work to be packaged. The makefiles will copy things
# into the web directory if it's present, so get rid of it now.
rm -rf web
# Upstream builds but does not install extras. Don't waste build time, nor
# bother fixing the parallel make breakage there.
rm -rf extras


%build
%make_build libdir=%{_libdir}


%install
%make_install libdir=%{_libdir}


%files
%{_bindir}/%{name}-*

%files libs
%{_libdir}/lib%{name}*.so.*

%files data
%license agpl-3.0.txt
%{_datadir}/%{name}/

%files doc
%{_docdir}/%{name}/

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}*.so


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 01 2023 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.4.1-1
- Update to 3.4.1 (rhbz#2219076)

* Mon Jun 12 2023 Dan Horák <dan[at]danny.cz> - 3.4-1
- updated to 3.4 (rhbz#2214067)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Dan Horák <dan[at]danny.cz> - 3.3.3-1
- updated to 3.3.3 (#1911697)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 04 2019 Dan Horák <dan[at]danny.cz> - 3.3.2-1
- updated to 3.3.2 (#1750029)

* Sat Sep 07 2019 Dan Horák <dan[at]danny.cz> - 3.3-1
- updated to 3.3 (#1750029)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 27 2017 Dan Horák <dan[at]danny.cz> - 3.2-1
- updated to 3.2 (#1315033)

* Fri Mar 24 2017 Dan Horák <dan[at]danny.cz> - 3.0-6
- add missing BR (#1424266)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 31 2015 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.0-3
- Move the documentation to a -doc noarch subpackage

* Sat Oct 31 2015 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.0-2
- Move the data to a noarch subpackage required by -libs, the lib also needs it

* Sat Oct 31 2015 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.0-1
- Update to 3.0 (#1262582)
- Rebase patches
- Backport upstream patch that versions the shared library
- Pass the libdir to make because it depends on the architecture
- Add new -libs and -devel subpackages
- README-MARBLE.txt: update version number reference
- Remove obsolete specfile constructs

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 12 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.7.3-1
- Update to 2.7.3 (#1163331)
- README-MARBLE.txt: update version number reference

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.7.2-1
- Update to 2.7.2 (#1114341)
- README-MARBLE.txt: update: compatible with data files from 2.7.1, but no older

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 31 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.7.1-1
- Update to 2.7.1 (#1080898)
- README-MARBLE.txt: update: data files from versions 2.6 and 2.7 no longer work

* Sat May 31 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.7-1
- Update to 2.7 (last version compatible with databases from 2.6)
- Rebase patches
- Enable xz support, BuildRequires: xz-devel
- README-MARBLE.txt: update: 2.6 database compatibility, .xz support

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.6-1
- Update to 2.6 (#983011)
- Rebase makefiles patch
- README-MARBLE.txt: update: data files from 2.4.x/2.5.x versions no longer work
- Do not compile the extras that don't get installed anyway

* Mon May 13 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.5.1-1
- Update to 2.5.1 (#954303, bugfix release)

* Fri Feb 15 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.5-1
- Update to 2.5 (#909929)
- Rebase patches
- BuildRequires (changed by upstream): -flex, +bzip2-devel, +zlib-devel
- README-MARBLE.txt: update: .pbf, .gz, .bz2 input now directly supported

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 24 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.4.1-1
- Update to 2.4.1 (#885455)
- README-MARBLE.txt: update: data files from 2.2.x/2.3.x versions no longer work

* Sun Oct 07 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.3.2-1
- Update to 2.3.2 (#863789)

* Mon Aug 13 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.3.1-1
- Update to 2.3.1 (#847663)
- README-MARBLE.txt: 2.3.x is, in fact, compatible with data files from 2.2

* Sun Jul 22 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.3-1
- Update to 2.3 (#842086)
- README-MARBLE.txt: update: data files from 2.2 (probably) no longer work
- Rebase makefiles patch

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 05 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.2-1
- Update to 2.2
- README-MARBLE.txt: update: data files from 2.1(.x) versions no longer work
- makefiles patch: revert a makefile "fix" which breaks parallel make

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 17 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.1.2-1
- Update to 2.1.2 (#753752, bugfix release)
- Rebase makefiles patch

* Thu Oct 27 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.1.1-2
- makefiles patch: add one more check for WEBDATADIR existence

* Thu Oct 27 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.1.1-1
- Update to 2.1.1 (#748392, bugfix release)
- README-MARBLE.txt: update version number reference (2.1 → 2.1.x)
- Drop filedumper-printf patch, fixed upstream
- Rebase makefiles patch, upstream fixed a makefile bug

* Sat Oct 15 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.1-2
- Fix filedumper.c printf format string warnings (fatal on 64-bit BE platforms)

* Sat Oct 15 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.1-1
- Update to 2.1 (#742903)
- README-MARBLE.txt: update: data files from 2.0(.x) versions no longer work
- Rebase makefiles patch and fix 3 new makefile errors

* Fri Aug 05 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.0.3-1
- Update to 2.0.3 (#728490, bugfix release)

* Mon Jul 11 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.0.2-1
- Update to 2.0.2 (#716876, bugfix release)
- Rebase makefiles patch

* Sun Jun 12 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.0.1-2
- README-MARBLE.txt: update version number references

* Thu Jun 09 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.0.1-1
- Update to 2.0.1 (#709309, bugfix release)
- Drop planetsplitter-segfault patch (fixed upstream)

* Tue May 31 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.0-3
- README-MARBLE.txt: update time indication (planetsplitter is faster in 2.0)

* Tue May 31 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.0-2
- README-MARBLE.txt: mention that data files from old versions no longer work
- Fix segmentation fault in planetsplitter (at least on austria.osm)

* Tue May 31 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.0-1
- Update to 2.0 (#709309, adds turn restriction support among other things)

* Tue Apr 26 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.5.1-5
- README-MARBLE.txt: clarify minimum Marble version (1.0.0 / kdeedu 4.6.0)

* Mon Apr 25 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.5.1-4
- Better Group and BuildRoot tags (Volker Fröhlich)
- Add -b to the patch invocation (suggested by Volker Fröhlich)
- Add a README-MARBLE.txt documenting how to set up Routino for use with Marble
- Get rid of installation documentation which is not applicable to the RPM

* Mon Apr 25 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.5.1-3
- Use install -p instead of cp -pf to install executables, to ensure 755 perms

* Sun Apr 24 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.5.1-2
- Install ChangeLog

* Sat Apr 23 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.5.1-1
- Initial Fedora package
