%global svndate 20241208
%global svnrev 13596
%global snapshot 0%{?svndate}
%if %{snapshot}
%global svnrelease .%{svndate}svn%{svnrev}
%endif

Name:		codeblocks
Version:	20.03
Release:	31%{?svnrelease}%{?dist}
Summary:	An open source, cross platform, free C++ IDE
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		http://www.codeblocks.org/
%if %{snapshot}
# fedora-getsvn codeblocks svn://svn.code.sf.net/p/codeblocks/code/trunk %%{svnrev}
Source0:	%{name}-svn%{svnrev}.tar.bz2
%else
Source0:	https://sourceforge.net/projects/%{name}/files/Sources/%{version}/%{name}-%{version}.tar.xz
%endif
Patch0:		codeblocks-autorev.patch
# use distro compiler standards
Patch1:		codeblocks-flags.patch
# GCC 15 fixes
Patch2:		0001-clangd_client-include-missing-header.patch
Patch3:		0002-sdk-drop-including-ciso646.patch

BuildRequires:	astyle-devel >= 3.1
BuildRequires:	boost-devel
BuildRequires:	bzip2-devel
BuildRequires:	desktop-file-utils
BuildRequires:	dos2unix
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	hunspell-devel
BuildRequires:	libappstream-glib
BuildRequires:	libICE-devel
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	tinyxml-devel
BuildRequires:	wxGTK-devel
BuildRequires:	zip
BuildRequires:	zlib-devel

Requires:	%{name}-libs = %{version}-%{release}
Requires:	shared-mime-info
Requires:	xterm
Provides:	bundled(wxScintilla) = 3.53.0
# patched with https://github.com/albertodemichelis/squirrel/issues/230 (svn rev 12365)
Provides:	bundled(squirrel) = 3.1

%global		pkgdatadir	%{_datadir}/%{name}
%global		pkglibdir	%{_libdir}/%{name}
%global		plugindir	%{pkglibdir}/plugins

%global __provides_exclude_from ^%{plugindir}/.*\\.so$

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}


%description
Code::Blocks is a free C++ IDE built specifically to meet the most demanding
needs of its users. It was designed, right from the start, to be extensible
and configurable. Built around a plug-in framework, Code::Blocks can be
extended with plug-in DLLs. It includes a plugin wizard, so you can compile
your own plug-ins.

%package libs
Summary:	Libraries needed to run Code::Blocks and its plug-ins

%description libs
Libraries needed to run Code::Blocks and its plug-ins.

%package devel
Summary:	Files needed to build Code::Blocks plug-ins
Requires:	%{name}-libs = %{version}-%{release}
Requires:	pkgconfig

%description devel
Development files needed to build Code::Blocks plug-ins.

%package contrib-libs
Summary:	Libraries needed to run Code::Blocks contrib plug-ins

%description contrib-libs
Libraries needed to run Code::Blocks contrib plug-ins.

%package contrib-devel
Summary:	Files needed to build Code::Blocks contrib plug-ins
Requires:	%{name}-contrib-libs = %{version}-%{release}

%description contrib-devel
Development files needed to build Code::Blocks contrib plug-ins.

%package contrib
Summary:	Additional Code::Blocks plug-ins
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-contrib-libs = %{version}-%{release}
Recommends:	cppcheck
Recommends:	cscope
Recommends:	valgrind

%description contrib
Additional Code::Blocks plug-ins.


%prep
%if %{snapshot}
%setup -q -n %{name}
%patch -P 0 -p1
%else
%setup -q
%endif
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1


%if %{snapshot}
# generate revision.m4
echo "m4_define([SVN_REV], %{svnrev})" > revision.m4
echo "m4_define([SVN_REVISION], svn%{svnrev})" >> revision.m4
echo "m4_define([SVN_DATE], %{svndate})" >> revision.m4

./bootstrap
%else
autoreconf -f -i
%endif


# convert EOLs
find . -type f -and -not -name "*.cpp" -and -not -name "*.h" -and -not -name "*.png" -and -not -name "*.bmp" -and -not -name "*.c" -and -not -name "*.cxx" -and -not -name "*.ico" -exec dos2unix -q --keepdate {} \;

%build

%configure \
    --with-contrib-plugins="all" \
    --with-boost-libdir=%{_libdir}

# remove unbundled stuff
rm -rf src/include/tinyxml src/base/tinyxml
rm -rf src/plugins/astyle/astyle
rm -rf src/plugins/contrib/SpellChecker/hunspell
rm -rf src/plugins/contrib/devpak_plugin/bzip2
rm -rf src/plugins/contrib/help_plugin/{bzip2,zlib}

# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.{appdata,metainfo}.xml
desktop-file-validate	%{buildroot}/%{_datadir}/applications/codeblocks.desktop

find %{buildroot} -type f -name "*.la" -delete

# set a fixed timestamp (source archive creation) to generated resource archives
/bin/touch -r %{SOURCE0} %{buildroot}/%{pkgdatadir}/*.zip

# generate linker config file for wxContribItems libraries
mkdir -p %{buildroot}/%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/%{name}/wxContribItems" > %{buildroot}/%{_sysconfdir}/ld.so.conf.d/%{name}-contrib-%{_arch}.conf

%ldconfig_scriptlets libs

%ldconfig_scriptlets contrib-libs

rm -f %{buildroot}/%{pkgdatadir}/docs/index.ini


%files
%license COPYING
%doc README AUTHORS BUGS COMPILERS NEWS
%{_bindir}/codeblocks
%{_bindir}/cb_*
%{_mandir}/man1/codeblocks.*.gz
%{_mandir}/man1/cb_console_runner.*.gz
%{_mandir}/man1/cb_share_config.*.gz

%dir %{pkglibdir}
%dir %{plugindir}
%{plugindir}/libAstyle.so
%{plugindir}/libabbreviations.so
%{plugindir}/libautosave.so
%{plugindir}/libclasswizard.so
%{plugindir}/libcodecompletion.so
%{plugindir}/libcompiler.so
%{plugindir}/libdebugger.so
%{plugindir}/libdefaultmimehandler.so
%{plugindir}/liboccurrenceshighlighting.so
%{plugindir}/libopenfileslist.so
%{plugindir}/libprojectsimporter.so
%{plugindir}/libscriptedwizard.so
%{plugindir}/libtodo.so

%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/mimetypes/*.png
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/%{name}.png

%dir %{pkgdatadir}
%{pkgdatadir}/icons
%dir %{pkgdatadir}/images
%{pkgdatadir}/images/*.png
%{pkgdatadir}/images/settings
%{pkgdatadir}/lexers
%{pkgdatadir}/scripts
%{pkgdatadir}/templates
%{pkgdatadir}/Astyle.zip
%{pkgdatadir}/abbreviations.zip
%{pkgdatadir}/autosave.zip
%{pkgdatadir}/classwizard.zip
%{pkgdatadir}/codecompletion.zip
%{pkgdatadir}/compiler.zip
%{pkgdatadir}/debugger.zip
%{pkgdatadir}/defaultmimehandler.zip
%{pkgdatadir}/manager_resources.zip
%{pkgdatadir}/occurrenceshighlighting.zip
%{pkgdatadir}/openfileslist.zip
%{pkgdatadir}/projectsimporter.zip
%{pkgdatadir}/resources.zip
%{pkgdatadir}/scriptedwizard.zip
%{pkgdatadir}/start_here.zip
%{pkgdatadir}/todo.zip
%{pkgdatadir}/tips.txt
%dir %{pkgdatadir}/compilers
%{pkgdatadir}/compilers/*.xml

%files libs
%doc COPYING
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}/
%exclude %{_includedir}/%{name}/wxContribItems/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files contrib-libs
%{_sysconfdir}/ld.so.conf.d/%{name}-contrib-%{_arch}.conf
%{_libdir}/libwxsmithlib.so.*
%{_libdir}/%{name}/wxContribItems/*.so.*
%exclude %{_libdir}/libwxsmithlib.so

%files contrib-devel
%{_includedir}/wxsmith
%{_includedir}/%{name}/wxContribItems/
%{_libdir}/%{name}/wxContribItems/*.so
%{_libdir}/pkgconfig/cb_wx*.pc
%{_libdir}/pkgconfig/wxsmith.pc
%{_libdir}/pkgconfig/wxsmithaui.pc
%{_libdir}/pkgconfig/wxsmith-contrib.pc

%files contrib
%{_mandir}/man1/codesnippets.*.gz

%{pkgdatadir}/AutoVersioning.zip
%{pkgdatadir}/BrowseTracker.zip
%{pkgdatadir}/Cccc.zip
%{pkgdatadir}/CppCheck.zip
%{pkgdatadir}/Cscope.zip
%{pkgdatadir}/DoxyBlocks.zip
%{pkgdatadir}/EditorConfig.zip
%{pkgdatadir}/EditorTweaks.zip
%{pkgdatadir}/FileManager.zip
%{pkgdatadir}/HexEditor.zip
%{pkgdatadir}/IncrementalSearch.zip
%{pkgdatadir}/MouseSap.zip
%{pkgdatadir}/ThreadSearch.zip
%{pkgdatadir}/ToolsPlus.zip
%{pkgdatadir}/Valgrind.zip
%{pkgdatadir}/byogames.zip
%{pkgdatadir}/cb_koders.zip
%{pkgdatadir}/clangd_client.zip
%{pkgdatadir}/codesnippets.zip
%{pkgdatadir}/codestat.zip
%{pkgdatadir}/copystrings.zip
%{pkgdatadir}/dragscroll.zip
%{pkgdatadir}/envvars.zip
%{pkgdatadir}/exporter.zip
%{pkgdatadir}/headerfixup.zip
%{pkgdatadir}/help_plugin.zip
%{pkgdatadir}/keybinder.zip
%{pkgdatadir}/lib_finder.zip
%{pkgdatadir}/Profiler.zip
%{pkgdatadir}/ProjectOptionsManipulator.zip
%{pkgdatadir}/RegExTestbed.zip
%{pkgdatadir}/ReopenEditor.zip
%{pkgdatadir}/SymTab.zip
%{pkgdatadir}/wxsmith.zip
%{pkgdatadir}/wxSmithAui.zip
%{pkgdatadir}/wxsmithcontribitems.zip
%{pkgdatadir}/images/wxsmith
%{pkgdatadir}/lib_finder
%{pkgdatadir}/NassiShneiderman.zip
%{pkgdatadir}/SpellChecker.zip
%{pkgdatadir}/SpellChecker
%{pkgdatadir}/SmartIndent*.zip
%{pkgdatadir}/rndgen.zip

%{plugindir}/libAutoVersioning.so
%{plugindir}/libBrowseTracker.so
%{plugindir}/libCccc.so
%{plugindir}/libCppCheck.so
%{plugindir}/libCscope.so
%{plugindir}/libDoxyBlocks.so
%{plugindir}/libEditorConfig.so
%{plugindir}/libEditorTweaks.so
%{plugindir}/libFileManager.so
%{plugindir}/libHexEditor.so
%{plugindir}/libIncrementalSearch.so
%{plugindir}/libMouseSap.so
%{plugindir}/libThreadSearch.so
%{plugindir}/libToolsPlus.so
%{plugindir}/libValgrind.so
%{plugindir}/libbyogames.so
%{plugindir}/libcb_koders.so
%{plugindir}/libclangd_client.so
%{plugindir}/libcodesnippets.so
%{plugindir}/libcodestat.so
%{plugindir}/libcopystrings.so
%{plugindir}/libdragscroll.so
%{plugindir}/libenvvars.so
%{plugindir}/libexporter.so
%{plugindir}/libheaderfixup.so
%{plugindir}/libhelp_plugin.so
%{plugindir}/libkeybinder.so
%{plugindir}/liblib_finder.so
%{plugindir}/libProfiler.so
%{plugindir}/libProjectOptionsManipulator.so
%{plugindir}/libRegExTestbed.so
%{plugindir}/libReopenEditor.so
%{plugindir}/libSymTab.so
%{plugindir}/libwxsmith.so
%{plugindir}/libwxSmithAui.so
%{plugindir}/libwxsmithcontribitems.so
%{plugindir}/libNassiShneiderman.so
%{plugindir}/libSpellChecker.so
%{plugindir}/libSmartIndent*.so
%{plugindir}/librndgen.so
%{_datadir}/metainfo/%{name}-contrib.metainfo.xml


%changelog
* Fri Jan 31 2025 Dan Horák <dan[at]danny.cz> - 20.03-31.20241208svn13596
- fix build with GCC 15 (rhbz#2339982)

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20.03-30.20241208svn13596
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Dec 19 2024 Dan Horák <dan[at]danny.cz> - 20.03-29.20241208svn13596
- updated to nightly 20241208 rev 13596
- rebuilt for astyle 3.6.6 (rhbz#2323142)

* Sat Oct 12 2024 Dan Horák <dan[at]danny.cz> - 20.03-28.20241012svn13584
- updated to nightly 20241012 rev 13584

* Fri Oct 11 2024 Dan Horák <dan[at]danny.cz> - 20.03-27.20240914svn13570
- updated to nightly 20240914 rev 13570
- rebuilt for astyle 3.6.3 (rhbz#2311785)

* Fri Sep 06 2024 Dan Horák <dan[at]danny.cz> - 20.03-26.20240815svn13542
- updated to nightly 20240815 rev 13542
- rebuilt for astyle 3.6.1 (rhbz#2303916)

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 20.03-25.20240525svn13524
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20.03-24.20240525svn13524
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Dan Horák <dan[at]danny.cz> - 20.03-23.20240525svn13524
- rebuilt for astyle 3.5.2 (rhbz#2276712)

* Wed Jun 12 2024 Dan Horák <dan[at]danny.cz> - 20.03-22.20240525svn13524
- updated to nightly 20240525 rev 13524

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20.03-21.20230124svn13161
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20.03-20.20230124svn13161
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 20.03-19.20230124svn13161
- Rebuilt for Boost 1.83

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20.03-18.20230124svn13161
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 20.03-17.20230124svn13161
- Rebuilt for Boost 1.81

* Fri Jan 20 2023 Scott Talbert <swt@techie.net> - 20.03-16.20230124svn13161
- Update to new upstream snapshot
- Rebuild with wxWidgets 3.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20.03-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20.03-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 20.03-13
- Rebuilt for Boost 1.78

* Wed Feb 23 2022 Dan Horák <dan[at]danny.cz> - 20.03-12
- drop libtool hack

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20.03-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 20.03-10
- Rebuilt for Boost 1.76

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.03-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.03-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 20.03-7
- Rebuilt for Boost 1.75

* Wed Jan 20 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 20.03-6
- Disable FileManager contrib plugin (replacation of DE Filemnanager)

* Sun Jan 17 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 20.03-5
- General spec cleanups

* Tue Jul 28 2020 Jeff Law <law@redhat.com> - 20.03-4
- Make comparison object invocable as const

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 20.03-2
- Rebuilt for Boost 1.73

* Mon Mar 30 2020 Dan Horák <dan[at]danny.cz> - 20.03-1
- Code::Blocks release 20.03

* Tue Feb 25 2020 Scott Talbert <swt@techie.net> - 17.12-16
- Rebuild against wxWidgets 3.0 (GTK 3 version)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 12 2019 Dan Horák <dan[at]danny.cz> - 17.12-13
- use upstream fix for #1650875

* Fri Jun 07 2019 Dan Horák <dan[at]danny.cz> - 17.12-12
- fix crash in Settings->Scripting (#1650875)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 17.12-10
- Rebuilt for Boost 1.69

* Fri Dec 07 2018 Scott Talbert <swt@techie.net> - 17.12-9
- Rebuild against wxWidgets 3.0 (GTK+ 2 version)

* Wed Aug 15 2018 Scott Talbert <swt@techie.net> - 17.12-8
- Rebuild against wxWidgets 3.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Jens Lody <fedora@jenslody.de> - 17.12-6
- Added BuildRequires for gcc and gcc-c++

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 17.12-4
- Rebuilt for Boost 1.66

* Mon Jan 15 2018 Jens Lody <fedora@jenslody.de> - 17.12-3
- Backported changes for astyle 3.1
- Rebuild for astyle 3.1

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 17.12-2
- Remove obsolete scriptlets

* Sun Dec 31 2017 Jens Lody <fedora@jenslody.de> - 17.12-1
- Code::Blocks release 17.12.
- Remove unneeded patches (all in upstream now).

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.01-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.01-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 16.01-10
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 16.01-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Mon Apr 24 2017 Jens Lody <fedora@jenslody.de> - 16.01-8
- Rebuild for astyle 3.0
- Backport crashfix (wxSmith-plugin)

* Tue Feb 14 2017 Jens Lody <fedora@jenslody.de> - 16.01-7
- Build fix, removed diff that slipped in

* Tue Feb 14 2017 Jens Lody <fedora@jenslody.de> - 16.01-6
- Backport of changes for astyle 2.06

* Tue Feb 14 2017 Jens Lody <fedora@jenslody.de> - 16.01-5
- rebuild for astyle 2.06

* Fri Feb 10 2017 Jens Lody <fedora@jenslody.de> - 16.01-4
- Fix gcc7 build-issue, due to malformed template code, also pushed upstream.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Caolán McNamara <caolanm@redhat.com> - 16.01-2
- rebuild for hunspell 1.5.4

* Wed Jul 27 2016 Jens Lody <fedora@jenslody.de> - 16.01-1
- Code::Blocks release 16.01.
- Updated unbundle patch.
- Fix rhbz #1295328 (license issues) with backport from upstream.
- Fix rhbz #1342076, #1349232, #1330252, #1350094 (crash on startup),
  gcc6 optimization issue with backport from upstream.
- Fix gcc6-build issues with backport from upstream.
- Spec-file clean up.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 13.12-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 13.12-22
- Rebuilt for Boost 1.60

* Thu Sep 03 2015 Dan Horák <dan[at]danny.cz> - 13.12-21
- rebuild for Boost 1.59

* Fri Aug 21 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 13.12-20
- Valgrind is not available only on s/390

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.12-19
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 13.12-18
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Jason L Tibbitts III <tibbs@math.uh.edu> - 13.12-16
- Indicate that this package bundles wxScintilla 1.7.1

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 13.12-15
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 13.12-14
- Rebuild for boost 1.57.0

* Fri Dec 12 2014 Dan Horák <dan[at]danny.cz> - 13.12-13
- fix resource archive loading for astyle plugin (#1172984, #1173243)

* Wed Dec 03 2014 Dan Horák <dan[at]danny.cz> - 13.12-12
- drop support for RHEL < 6
- include appdata only for Fedora

* Fri Nov 21 2014 Dan Horák <dan[at]danny.cz> - 13.12-11
- set Fedora specific paths for spellchecker and thesaurus in the SpellChecker plugin
- update for astyle 2.05 (#1166377)

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 13.12-10
- udate mime scriptlet

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 14 2014 Richard Hughes <richard@hughsie.com> - 13.12-8
- Make the MetaInfo file validate

* Mon Jul 07 2014 Richard Hughes <richard@hughsie.com> - 13.12-7
- Use the AppData and MetaInfo files written by Ryan

* Mon Jul 07 2014 Richard Hughes <richard@hughsie.com> - 13.12-6
- Remove the incorrect conditional (which doesn't work) to never use --vendor
  when installing desktop files. Using --vendor means the AppStream builder
  cannot match an AppData file which means Code::Blocks doesn't appear in the
  software center.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 13.12-4
- Rebuild for boost 1.55.0

* Thu Mar 20 2014 Dan Horák <dan[at]danny.cz> - 13.12-3
- unbundle astyle library (#1050825)

* Wed Feb 26 2014 Dan Horák <dan[at]danny.cz> - 13.12-2
- move the Occurrences Highlighting plugin to the main package (#1068971)

* Sun Dec 29 2013 Dan Horák <dan[at]danny.cz> - 13.12-1
- update to final 13.12 release (svn revision 9501)

* Mon Nov 04 2013 Dan Horák <dan[at]danny.cz> - 12.11-2
- fix Requires

* Sun Sep 01 2013 Dan Horák <dan[at]danny.cz> - 12.11-1
- update to final 12.11 release (svn revision 8629)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.05-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 10.05-12
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.05-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.05-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 22 2012 Dan Horák <dan@danny.cz> - 10.05-9
- build with system squirrel
- fix FTBFS with g++ 4.7 (#823697)

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.05-8
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.05-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 10.05-6
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Aug 28 2010 Dan Horák <dan@danny.cz> - 10.05-4
- xterm is the default terminal application, added as Requires (#622753)
- backport D language support from trunk (http://fedoraproject.org/wiki/Features/D_Programming)

* Mon Jul 12 2010 Dan Horák <dan@danny.cz> - 10.05-3
- rebuilt against wxGTK-2.8.11-2

* Thu Jul  8 2010 Dan Horák <dan[at]danny.cz> - 10.05-2
- moved license text into -libs subpackage

* Sun Jun 27 2010 Dan Horák <dan[at]danny.cz> - 10.05-1
- updated to 10.05 release

* Sat Feb 13 2010 Dan Horák <dan[at]danny.cz> - 8.02-10
- fixed linking with the new --no-add-needed default (#564644)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.02-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 15 2009 Dan Horák <dan[at]danny.cz> 8.02-8
- fix gsocket between glib >= 2.21 and wxGTK in rawhide

* Sat Feb 28 2009 Dan Horák <dan[at]danny.cz> 8.02-7
- update desktop file (#487796)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Dan Horak <dan[at]danny.cz> 8.02-5
- fix compile error with gcc 4.4/glibc 2.9.90

* Fri Oct 31 2008 Dan Horak <dan[at]danny.cz> 8.02-4
- fix gcc detection (#469096)

* Sat Sep 20 2008 Dan Horak <dan[at]danny.cz> 8.02-3
- update desktop file
- fix running console applications (#461120)

* Fri Aug 29 2008 Dan Horak <dan[at]danny.cz> 8.02-2
- refresh patches

* Sun Mar  2 2008 Dan Horak <dan[at]danny.cz> 8.02-1
- update to stable release 8.02
- update BR to use system libraries

* Mon Feb 18 2008 Dan Horak <dan[at]danny.cz> 1.0-0.30.20080211svn4872
- update to revision 4872
- really fix the multilib problem with the contrib subpackage (#433124)

* Sun Feb 10 2008 Dan Horak <dan[at]danny.cz> 1.0-0.29.20080209svn4868
- update to revision 4868

* Tue Dec 11 2007 Dan Horak <dan[at]danny.cz> 1.0-0.28.20071210svn4719
- update to revision 4719
- fix multiarch problem with contrib subpackage (#340911)
- set a fixed timestamp on all installed data files
- preserve timestamps on updated files

* Wed Aug 29 2007 Dan Horak <dan[at]danny.cz> 1.0-0.27.20070828svn4413
- update to revision 4413
- update the License tag

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.0-0.26.20070718svn4280
- Rebuild for selinux ppc32 issue (F8).

* Thu Jul 19 2007 Dan Horak <dan[at]danny.cz> 1.0-0.25.20070718svn4280
- update to revision 4280
- added missing ldconfig call for the contrib subpackage
- fix permissions for source files

* Sat Apr  7 2007 Dan Horak <dan[at]danny.cz> 1.0-0.24.20070406svn3816
- update to revision 3816

* Tue Feb 13 2007 Dan Horak <dan[at]danny.cz> 1.0-0.23.20070211svn3592
- update the autorev.patch

* Tue Feb 13 2007 Dan Horak <dan[at]danny.cz> 1.0-0.22.20070211svn3592
- update to revision 3592
- added patch for New Project wizard with wxGTK 2.8 (#225058)
- created -libs subpackage to make package multilib-aware (#228356)

* Fri Jan 26 2007 Dan Horak <dan[at]danny.cz> 1.0-0.21.20070125svn3540
- update the listbook.patch

* Fri Jan 26 2007 Dan Horak <dan[at]danny.cz> 1.0-0.20.20070125svn3540
- update to revision 3540

* Thu Jan 18 2007 Dan Horak <dan[at]danny.cz> 1.0-0.19.20070117svn3500
- update to revision 3500
- added patch for compiling with wxGTK 2.8

* Fri Dec  8 2006 Dan Horak <dan[at]danny.cz> 1.0-0.18.20061207svn3357
- update to revision 3357

* Thu Nov 30 2006 Dan Horak <dan[at]danny.cz> 1.0-0.17.20061130svn3315
- update to revision 3315

* Tue Nov 28 2006 Dan Horak <dan[at]danny.cz> 1.0-0.16.20061128svn3295
- update to revision 3295

* Sat Nov 25 2006 Dan Horak <dan[at]danny.cz> 1.0-0.15.20061125svn3268
- update to revision 3268
- fixes #217081

* Tue Nov 21 2006 Dan Horak <dan[at]danny.cz> 1.0-0.14.20061121svn3253
- update to revision 3253

* Fri Nov 10 2006 Dan Horak <dan[at]danny.cz> 1.0-0.13.20061110svn3202
- update to revision 3202
- fixed plugin loading on 64-bit platforms

* Fri Nov  3 2006 Dan Horak <dan[at]danny.cz> 1.0-0.12.20061102svn3170
- update to revision 3170

* Mon Oct 30 2006 Dan Horak <dan[at]danny.cz> 1.0-0.11.20061029svn3157
- update to revision 3157
- kill rpath in the spec file using sed
- fix directory ownership

* Sun Oct  8 2006 Dan Horak <dan[at]danny.cz> 1.0-0.10.20061007svn3030
- update to revision 3030
- change the install paths for plugins in the spec file

* Wed Sep 13 2006 Dan Horak <dan[at]danny.cz> 1.0-0.9.20060909svn2965
- do not require .svn directories for building

* Sun Sep 10 2006 Dan Horak <dan[at]danny.cz> 1.0-0.8.20060909svn2965
- update to revision 2965
- use %%configure macro
- properly install the desktop file
- update the mime database after install and uninstall
- do not own only %%{_libdir}/codeblock/plugins, but also %%{_libdir}/codeblock
- added a script for retrieving and packing a revision from the SVN repo

* Sun Sep  3 2006 Dan Horak <dan[at]danny.cz> 1.0-0.7.20060902svn2944
- update to revision 2944

* Sun Aug 20 2006 Dan Horak <dan[at]danny.cz> 1.0-0.6.20060820svn2882
- update to revision 2882
- added missing Requires for devel subpackage

* Wed Aug 16 2006 Dan Horak <dan[at]danny.cz> 1.0-0.5.20060815svn2854
- update to revision 2854

* Wed Aug 16 2006 Dan Horak <dan[at]danny.cz> 1.0-0.4.20060812svn2840
- make setup section quiet
- use only tabs for indentation

* Tue Aug 15 2006 Dan Horak <dan[at]danny.cz> 1.0-0.3.20060812svn2840
- define libdir in configure

* Sun Aug 13 2006 Dan Horak <dan[at]danny.cz> 1.0-0.2.20060812svn2840
- update to revision 2840
- added BR for autotools

* Tue Aug 08 2006 Dan Horak <dan[at]danny.cz> 1.0-0.1.2824svn
- initial spec file based on upstream
