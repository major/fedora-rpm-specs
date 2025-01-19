Name:       golly
Version:    4.3
Release:    3%{?dist}
Summary:    Cellular automata simulator (includes Conway's Game of Life)
# The license for the code is GPLv2+ and for the included python parts Python-2.0.1
#    see  /usr/share/licenses/golly/License.html
# The license for the Life Lexicon (in -data subpackage) is CC-BY-SA-3.0
#    see /usr/share/licenses/golly-data/lex.htm from https://conwaylife.com/ref/lexicon/lex_home.htm
License:    GPL-2.0-or-later AND Python-2.0.1
URL:        https://golly.sourceforge.net/
Source0:    https://downloads.sourceforge.net/%{name}/%{name}-%{version}-src.tar.gz
# patch to use system lua library rather than bundled
Patch1:     golly-4.3-lua-dyn.patch
# patch to avoid using deprecated Python modules
Patch2:     golly-4.3-python.patch

BuildRequires:  gcc-c++
BuildRequires:  wxGTK-devel
BuildRequires:  SDL2-devel
BuildRequires:  python3-devel
BuildRequires:  lua-devel
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  chrpath
Recommends:     golly-data = %{version}-%{release}

%description
Golly is an open source application for exploring Conway's Game of
Life and other cellular automata.  Golly supports unbounded universes
with up to 256 states.  Golly supports multiple algorithms, including
Bill Gosper's super fast hashlife algorithm.  Many different types of
CA are included: John von Neumann's 29-state CA, Wolfram's 1D rules,
WireWorld, Generations, Langton's Loops, Paterson's Worms, etc.

%package data
Summary:    Data for %{name}
License:    GPL-2.0-or-later AND Python-2.0.1 AND CC-BY-SA-3.0
Requires:   %{name} = %{version}-%{release}
BuildArch:  noarch

%description data
This package contains data for %{name}: Help, rules, patterns and scripts.

%package devel
Summary:    Development files for Golly cellular automata simulator
Requires:   %{name} = %{version}-%{release}
BuildArch:  noarch

%description devel
Development files for Golly celluar automata simulator.

%prep
%autosetup -n %{name}-%{version}-src -p 1
# fix permissions - no normal files should have execute permissions set
find . -type f -exec chmod 644 {} \;
# remove bundled lua
rm -rf lua

%build
pushd gui-wx
export GOLLYDIR=%{_datadir}/%{name}
%make_build -f makefile-gtk
popd
# remove RPATH
chrpath --delete golly bgolly

convert gui-wx/icons/appicon48.ico golly.png
cat <<EOF >golly.desktop
[Desktop Entry]
Name=Golly
GenericName=Golly cellular automata simulator
Exec=golly
Icon=golly
Terminal=false
Type=Application
Categories=GNOME;Game;LogicGame;
EOF

%install
# install binaries
install -d %{buildroot}%{_bindir}/
install -m 755 golly bgolly %{buildroot}%{_bindir}/

# install data files, but not scripts used only for build
for d in gui-wx/bitmaps Help Patterns Rules Scripts
do
  find $d -type d -exec install -d %{buildroot}%{_datadir}/%{name}/{} \;
  find $d -type f -exec install -m 644 {} %{buildroot}%{_datadir}/%{name}/{} \;
done
rm %{buildroot}%{_datadir}/%{name}/Help/Lexicon/*.pl

# move docs to top level of build dir to simplify files section
mv docs/* .
rmdir docs

# install application icon and desktop file
install -D -p -m 644 %{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -D -p -m 644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/golly
%{_bindir}/bgolly
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/Rules
%{_datadir}/%{name}/gui-wx
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%license License.html
%doc ReadMe.html

%files data
%{_datadir}/%{name}/Help
%{_datadir}/%{name}/Patterns
%{_datadir}/%{name}/Rules/*
%{_datadir}/%{name}/Scripts
%exclude %{_datadir}/%{name}/Rules/TableGenerators/
%exclude %{_datadir}/%{name}/Rules/TreeGenerators/
%license License.html
%license Help/Lexicon/lex.htm

%files devel
%{_datadir}/%{name}/Rules/TableGenerators/
%{_datadir}/%{name}/Rules/TreeGenerators/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Christian Krause <chkr@fedoraproject.org> - 4.3-1
- Fix FTBFS (#2261207)
- Update to latest upstream release 4.3
- Update patch for linking lua dynamically
- Add patch to avoid using deprecated Python modules

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 05 2023 Christian Krause <chkr@fedoraproject.org> - 4.2-3
- Let main package own /usr/share/golly/Rules to avoid an unowned
  directory if only the -devel subpackage would be installed

* Tue Oct 03 2023 Christian Krause <chkr@fedoraproject.org> - 4.2-2
- Move license tag (and license file) with CC-BY-SA-3.0 license
  to appropriate sub-package
- Change URL tag to https
- Correct sourceforge-specific Source URL
- Change dependencies: sub-packages now require the fully-versioned
  main package and the main package recommends the -data subpackage
- Move desktop-file-validate to %%check section

* Tue Sep 05 2023 Christian Krause <chkr@fedoraproject.org> - 4.2-1
- Unretire golly (#2237768)
- Migrated to SPDX license
- Update to latest upstream release 4.2
- Cleanup specfile

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.8-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 23 2016 Eric Smith <brouhaha@fedoraproject.org> 2.8-1
- Updated to latest upstream release. Note that upstream release no longer
  supports Perl scripting, but has added Lua scripting.

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.4-17
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.4-14
- Perl 5.22 rebuild

* Sun May 03 2015 Kalev Lember <kalevlember@gmail.com> - 2.4-13
- Rebuilt for GCC 5 C++11 ABI change

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.4-12
- Perl 5.20 rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.4-8
- Perl 5.18 rebuild

* Mon Jun 10 2013 Eric Smith <brouhaha@fedoraproject.org> 2.4-7
- Add patch to avoid error in automake.

* Mon Apr 29 2013 Eric Smith <brouhaha@fedoraproject.org> 2.4-6
- Add use of configure, necessary for autoreconf to actually do anything
  useful.

* Mon Apr 29 2013 Eric Smith <brouhaha@fedoraproject.org> 2.4-5
- Add autoreconf in prep section to support aarch64 (Bug #925468).

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Petr Pisar <ppisar@redhat.com> - 2.4-2
- Perl 5.16 rebuild

* Sun Jul 08 2012 Eric Smith <brouhaha@fedoraproject.org> 2.4-1
- Updated to latest upstream release.

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 2.3-4
- Perl 5.16 rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-3
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 05 2011 Eric Smith <brouhaha@fedoraproject.org> 2.3-1
- Updated to latest upstream release.  No longer needs patch for Perl 5.14.

* Tue Jul 26 2011 Eric Smith <brouhaha@fedoraproject.org> 2.2-6
- Added patch for compatibility with Perl 5.14, from Toby Corkindale.

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 2.2-5
- Perl mass rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.2-4
- Perl mass rebuild

* Thu Jun 09 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.2-3
- Perl 5.14 mass rebuild

* Tue Apr  5 2011 Eric Smith <brouhaha@fedoraproject.org> 2.2-2
- Include HTML file from official Life Lexicon web page giving CC-BY-SA
  license notice.

* Mon Dec 13 2010 Eric Smith <brouhaha@fedoraproject.org> 2.2-1
- Updated to latest upstream release, several patches no longer necessary

* Wed Jun  2 2010 Eric Smith <brouhaha@fedoraproject.org> 2.1-7
- Fixed space/tab rpmlint complaint about spec

* Tue Jun  1 2010 Terje Rosten <terje.rosten@> 2.1-6
- Add patch to let golly locate libperl.so 

* Mon May 31 2010 Eric Smith <brouhaha@fedoraproject.org> 2.1-5
- Added patch to use Perl 5.10.1

* Wed May 12 2010 Eric Smith <brouhaha@fedoraproject.org> 2.1-4
- Added patch to use libpython2.6 as default, from Terje RÃ¸sten
- Included upstream patch for 64-bit issue

* Tue May 11 2010 Eric Smith <brouhaha@fedoraproject.org> 2.1-3
- Changed optflags patch to remove -O5
- Fixed appdir patch
- Consistent use of buildroot var
- Fixed directory ownership by using exclude
- Removed echo command left over from debugging

* Sun May  9 2010 Eric Smith <brouhaha@fedoraproject.org> 2.1-2
- Changed appdir patch to use arg defined by makefile

* Sat May  8 2010 Eric Smith <brouhaha@fedoraproject.org> 2.1-1
- Initial version
