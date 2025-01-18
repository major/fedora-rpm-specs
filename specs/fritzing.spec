Name:           fritzing
%global rtld_name org.fritzing.Fritzing

Summary:        Electronic Design Automation software; from prototype to product
License:        GPL-3.0-or-later
URL:            http://fritzing.org/

Version:        1.0.0
%global baserelease 6

# The fritzing-app repo does not contain a tag for v1.0.0.
%global app_date 20230425
%global app_commit 7b75a63c264b31b9ed69481f1f2c84c53f940e03

# The fritzing-parts repository no longer uses git tags for marking releases.
# Upstream build scripts seem to just take the latest commit
# from fritzing-parts's "develop" branch.
#
# The app commit we're using is dated 2023-04-25.
# In the parts repo, the last commit made before that date is from 2023-04-24.
# Use the fritzing-parts repo as of said commit.
%global parts_date 20230424
%global parts_commit e270ebfd8ee7dd40a6ef29ad0d3dba006e9eee61

# Include the commit date in the release numbers
%global app_release %{baserelease}.%{app_date}%{?dist}
%global parts_release %{baserelease}.%{parts_date}%{?dist}

Release:        %{app_release}

Source0:        https://github.com/%{name}/%{name}-app/archive/%{app_commit}/%{name}-app-%{app_commit}.tar.gz
Source1:        https://github.com/%{name}/%{name}-parts/archive/%{parts_commit}/%{name}-parts-%{parts_commit}.tar.gz

# Fedora-specific patch to disable internal auto-updating feature.
# Also removes dependency of libgit2 (used only during the auto-update process).
Patch0:         0000-disable-autoupdate.patch
# Use the system quazip library instead of the bundled one.
Patch1:         0001-unbundle-quazip.patch
# Remove references to example sketches that use twitter4j library
Patch2:         0002-remove-twitter4j.patch

BuildRequires:  pkgconfig(ngspice)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5SerialPort)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(quazip1-qt5)
BuildRequires:  pkgconfig(zlib)

BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make

Requires:       %{name}-parts = %{version}-%{parts_release}
%if %{undefined flatpak}
Requires:       electronics-menu
%endif
Requires:       google-droid-sans-fonts
Requires:       google-droid-sans-mono-fonts

%description
Fritzing is a free software tool to support designers, artists and
hobbyists to work creatively with interactive electronics.


%package parts
Version: %{version}
Release: %{parts_release}
Summary: Parts library for the Fritzing electronic design application
BuildArch: noarch

# The overall distribution is licensed as CC-BY-SA (see LICENSE.txt), but
# many individual SVG parts in the svg/ directory are licensed as GPL+;
# please see the fz:attr elements named "dist-license", "use-license", and
# "license-url" under the rdf:RDF section of each SVG document for details.
License:       CC-BY-SA-3.0 AND GPL-1.0-or-later

%description parts
A library of part definitions for the Fritzing electronic design application,
containing both metadata and related graphics.


%prep
%setup -q -n %{name}-app-%{app_commit}

%setup -q -T -D -a 1 -n %{name}-app-%{app_commit}
mv %{name}-parts-%{parts_commit}/ parts/

# Remove some GitHub-specific files
rm -rf .github || true
rm -rf parts/.github || true

# We don't want the autoupdater.
%patch -P 0 -p1 -b .disable-updates

# We use the unbundled version of quazip.
%patch -P 1 -p1 -b .unbundle-quazip
rm -rf src/lib/quazip

# The TwitterSaurus examples use (a bundled) twitter4j library, whose license
# is incompatible with Fedora.
%patch -P 2 -p1 -b .remove-twitter4j
rm -f sketches/core/Fritzing\ Creator\ Kit\ DE+EN/creator-kit-*/Fritzing/TwitterSaurus.fzz
rm -f sketches/core/Fritzing\ Creator\ Kit\ DE+EN/creator-kit-*/Processing/twitter4j-core-2.2.5.jar
rm -rf sketches/core/Fritzing\ Creator\ Kit\ DE+EN/creator-kit-*/Processing/TwitterSaurus*
rm -f sketches/core/obsolete/TwitterSaurus.fzz

# Remove a <url> entry which causes the appstream file to fail validation.
sed -e '/<url type="forum">/d' -i '%{rtld_name}.appdata.xml'



%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build V=1

# Generate the parts database
./Fritzing -platform minimal -f ./parts -db ./parts/parts.db


%install
%make_install INSTALL_ROOT=%{buildroot}

# A few files in /usr/share/fritzing end up executable.
find %{buildroot}%{_datadir}/%{name} -type f -exec chmod 644 '{}' ';'
find %{buildroot}%{_datadir}/%{name} -type d -exec chmod 755 '{}' ';'


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rtld_name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{rtld_name}.appdata.xml

if [[ "$(find %{buildroot}%{_datadir}/%{name} -name 'TwitterSaurus*' -o -name 'twitter4j*' | wc -l)" -gt 0 ]]; then
  echo "Found TwitterSaurus / twitter4j files - these should NOT be included in the final package" >&2
  exit 1
fi


%files
%doc README.md LICENSE.GPL2 LICENSE.GPL3 LICENSE.CC-BY-SA
%{_bindir}/Fritzing
%{_datadir}/applications/%{rtld_name}.desktop
%{_datadir}/mime/packages/fritzing.xml
%{_datadir}/pixmaps/fritzing.png
%{_metainfodir}/%{rtld_name}.appdata.xml
%{_mandir}/man?/*

%files parts
%doc parts/README.md
%license parts/LICENSE.txt
%{_datadir}/%{name}


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6.20230425
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5.20230425
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4.20230425
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3.20230425
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2.20230425
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.0.0-1.20230425
- Update to v1.0.0
- Convert License tag to SPDX

* Fri May 05 2023 Nicolas Chauvet <kwizart@gmail.com> - 0.9.10-4.20220514
- Rebuilt for quazip 1.4

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-3.20220514
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-2.20220514
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.10-1.20220514
- Update to v0.9.10

* Mon Apr 18 2022 Miro Hrončok <mhroncok@redhat.com> - 0.9.9-2.20210922
- Rebuilt for quazip 1.3

* Wed Mar 16 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.9-1.20210922
- Update to v0.9.9

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 19 2021 Björn Esser <besser82@fedoraproject.org> - 0.9.6-3
- Rebuild (quazip)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Mar 14 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.6-1
- Update to v0.9.6
- Drop Patch1 (build against system quazip library - now supported upstream)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4.CD498-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 20 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.4.CD498-1
- Update to latest stable release
- Drop Patch2 (fix bug in parts intaller python script - fixed upstream)
- Fix the "remove TwitterSaurus examples" part of spec
- Move parts into a -parts sub-package

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2b-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2b-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2b-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2b-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 30 2018 Ed Marshall <esm@logic.net> - 0.9.2b-16
- Update Qt5 dependencies, remove unnecessary dependency on minizip.
- Add zlib-devel dependency for now.

* Tue Sep 04 2018 Pavel Raiskup <praiskup@redhat.com> - 0.9.2b-16
- rebuild against minizip-compat-devel, rhbz#1609830, rhbz#1615381

* Tue Aug 28 2018 Ed Marshall <esm@logic.net> - 0.9.2b-15
- Remove pre-built Twitter4J libraries with proprietary JSON.org license.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2b-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Ed Marshall <esm@logic.net> - 0.9.2b-13
- Add BuildRequires for gcc-c++ per packaging guidelines.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2b-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 06 2017 Ed Marshall <esm@logic.net> - 0.9.2b-11
- Patch script in parts library so python bytecompilation succeeds.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2b-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2b-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2b-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2b-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.9.2b-6
- Rebuilt for Boost 1.63

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2b-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 0.9.2b-4
- use %%qmake_qt5 to ensure proper build flags

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 0.9.2b-3
- Rebuilt for Boost 1.60

* Sun Dec 27 2015 Ed Marshall <esm@logic.net> - 0.9.2b-2
- Modify build to use quazip-qt5 rather than quazip.
- Use upstream-provided .appdata.xml and .desktop files.

* Sat Dec  5 2015 Ed Marshall <esm@logic.net> - 0.9.2b-1
- Updated to 0.9.2b release.

* Sat Dec  5 2015 Ed Marshall <esm@logic.net> - 0.9.0b-8
- Update to .appdata.xml and .desktop files.

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.9.0b-7
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0b-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.9.0b-5
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0b-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.0b-3
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.9.0b-2
- Rebuild for boost 1.57.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.8.7b-1
- Rebuild for boost 1.55.0

* Sun Feb 16 2014 Ed Marshall <esm@logic.net> - 0.8.7b-0
- Updated to 0.8.7b release.

* Sat Aug 10 2013 Ed Marshall <esm@logic.net> - 0.8.3b-0
- Updated to 0.8.3b release.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.12b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.7.12b-2
- Rebuild for boost 1.54.0

* Mon Feb 25 2013 Ed Marshall <esm@logic.net> - 0.7.12b-1
- Updated to 0.7.12b release.
- Internal quazip is now configurable, boost is no longer bundled.
- Panelizer include fixes merged upstream.
- Backported missing parts.db fix no longer needed.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.11b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan  8 2013 Ed Marshall <esm@logic.net> - 0.7.11b-2
- Backport upstream patch for gracefully handling missing parts database.

* Mon Jan  7 2013 Ed Marshall <esm@logic.net> - 0.7.11b-1
- Updated to 0.7.11b release.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul  3 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.7.5b-1
- Updated to 0.7.5b release.
- Update patches
- Cleanup and modernise spec

* Sat Mar 10 2012 Ed Marshall <esm@logic.net> - 0.7.1b-1
- Updated to 0.7.1b release.

* Fri Feb  3 2012 Ed Marshall <esm@logic.net> - 0.7.0b-1
- Add Droid font requirement.
- Updated to 0.7.0b release.

* Wed Jan  4 2012 Ed Marshall <esm@logic.net> - 0.6.5b-2
- Make rpmlint happier with line-endings on documentation.

* Wed Jan  4 2012 Ed Marshall <esm@logic.net> - 0.6.5b-1
- Updated to 0.6.5b release.

* Tue Dec 20 2011 Ed Marshall <esm@logic.net> - 0.6.4b-2
- Add LICENSE.CC-BY-SA to package.
- Add minizip-devel as a build dependency.

* Sat Dec 17 2011 Ed Marshall <esm@logic.net> - 0.6.4b-1
- Updated to 0.6.4b release.

* Thu Feb 24 2011 Ed Marshall <esm@logic.net> - 0.5.2b-1
- Updated to 0.5.2b release.

* Thu Feb 17 2011 Ed Marshall <esm@logic.net> - 0.5.1b-3
- Add patch to remove auto-update feature.

* Tue Feb 15 2011 Ed Marshall <esm@logic.net> - 0.5.1b-2
- Fixed hard-coded path to qtlockedfile qmake project file (fixes x86_64).

* Tue Feb 15 2011 Ed Marshall <esm@logic.net> - 0.5.1b-1
- Updated to 0.5.1b release
- Don't manually strip resulting executables
- Don't bundle third-party libraries; use Fedora-provided libs
- Provide CXXFLAGS to qmake
- Updated summary to be a little closer to the Fritzing tagline

* Mon Feb 14 2011 Ed Marshall <esm@logic.net> - 0.5.0b-1
- Updated to latest release
- zlib patch included upstream, removed from RPM

* Mon Dec 6 2010 Ed Marshall <esm@logic.net> - 0.4.3b-1
- Updated to latest release
- Added desktop file, and install icon
- Include man page (from Debian)
- Patch to set application folder location to /usr/share/fritzing, instead of
  being relative to the binary directory (from Debian)

* Tue Jul 7 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.3.5b-1
- initial package for Fedora
