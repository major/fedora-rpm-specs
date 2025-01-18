%global pkgver 2.2.16
#global prerel rc1
%global baserelease 3

Name:		bluefish
Version:	%{pkgver}
Release:	%{?prerel:0.}%{baserelease}%{?prerel:.%{prerel}}%{?dist}
Summary:	Web development application for experienced users
License:	GPL-3.0-or-later
URL:		http://bluefish.openoffice.nl/
Source0:	http://www.bennewitz.com/bluefish/stable/source/bluefish-%{version}%{?prerel:-%{prerel}}.tar.bz2
Patch0:		bluefish-2.2.13-strict-aliasing.patch
Patch1:		bluefish-2.2.16-shellbang.patch
Patch2:		bluefish-2.2.16-gcc14.patch
Patch3:		bluefish-2.2.16-gcc15.patch
BuildRequires:	coreutils
BuildRequires:	desktop-file-utils
BuildRequires:	enchant2-devel
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	gettext >= 0.19.7
BuildRequires:	glib2-devel >= 2.24
BuildRequires:	gtk3-devel >= 3.2
BuildRequires:	gucharmap-devel >= 2.90
BuildRequires:	hardlink
BuildRequires:	intltool
BuildRequires:	libxml2-devel
BuildRequires:	make
BuildRequires:	python3-devel >= 3.3
BuildRequires:	libappstream-glib >= 0.3.6
BuildRequires:	which
# Needed to check man pages
BuildRequires:	/usr/bin/man
# For the Advanced Open function
Requires:	findutils, grep
Requires:	%{name}-shared-data = %{version}-%{release}

# Automatically upgrade bluefish-unstable
Obsoletes:	bluefish-unstable < %{version}-%{release}
Provides:	bluefish-unstable = %{version}-%{release}

# XML Catalog registration
Requires(post): /usr/bin/xmlcatalog, xml-common
Requires(postun): /usr/bin/xmlcatalog, xml-common

# Move to unversioned documentation directories from F-20
# https://fedoraproject.org/wiki/Changes/UnversionedDocdirs
%global bluefish_docdir %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}

# Explicitly disable automatic byte-compilation of python in non-python library locations
%global _python_bytecompile_extra 0

%description
Bluefish is a powerful editor for experienced web designers and programmers.
Bluefish supports many programming and markup languages, but it focuses on
editing dynamic and interactive websites.

%package shared-data
Summary:	Architecture-independent data for %{name}
BuildArch:	noarch
# So that we pull in the binary when someone installs the data (#1091613)
Requires:	%{name} = %{version}-%{release}

# Automatically upgrade bluefish-unstable-shared-data
Obsoletes:	bluefish-unstable-shared-data < %{version}-%{release}
Provides:	bluefish-unstable-shared-data = %{version}-%{release}

%description shared-data
Files common to every architecture version of %{name}.

%prep
%setup -q -n %{name}-%{version}%{?prerel:-%{prerel}}

# Avoid potential aliasing issues in zencoding plugin
%patch -P 0

# Avoid use of /usr/bin/env in shipped scripts
# Also change /usr/bin/python → /usr/bin/python3
%patch -P 1

# Fix for type issue causing FTBFS with gcc 14
# https://sourceforge.net/p/bluefish/tickets/95/
%patch -P 2 -p2

# Fix for type issues causing FTBFS with gcc 15
# https://sourceforge.net/p/bluefish/tickets/101/
%patch -P 3

%build
%configure	--disable-dependency-tracking \
		--disable-static \
		--disable-update-databases \
		--disable-xml-catalog-update \
		--docdir=%{bluefish_docdir}
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_datadir}/applications
make install DESTDIR=%{buildroot} INSTALL="install -p"

# Make zencoding plugin scripts executable to placate rpmlint
find %{buildroot}%{_datadir}/bluefish/plugins/zencoding -name '*.py' |
	xargs awk '/^#!/ { print FILENAME }' |
	xargs chmod -c +x

%find_lang %{name}
%find_lang %{name}_plugin_about
%find_lang %{name}_plugin_charmap
%find_lang %{name}_plugin_entities
%find_lang %{name}_plugin_htmlbar
%find_lang %{name}_plugin_infbrowser
%find_lang %{name}_plugin_snippets
%find_lang %{name}_plugin_zencoding
cat %{name}_plugin_{about,charmap,entities,htmlbar,infbrowser,snippets,zencoding}.lang >> \
	%{name}.lang

appstream-util --nonet validate-relax \
	%{buildroot}%{_datadir}/metainfo/bluefish.appdata.xml

desktop-file-validate \
	%{buildroot}%{_datadir}/applications/bluefish.desktop

# Manually install docs so that they go into
# %%{bluefish_docdir} even though we put them in the
# shared-data subpackage
install -m 644 -p -t %{buildroot}%{bluefish_docdir}/ \
	AUTHORS ChangeLog README TODO

# Unpackaged files
rm -f %{buildroot}%{_libdir}/bluefish/*.la

# Explicitly byte-compile "extra" python code using Python 3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/bluefish

# hardlink identical images together
hardlink -cv %{buildroot}%{_datadir}/{icons,pixmaps}

# hardlink identical message files together
hardlink -cv %{buildroot}%{_datadir}/locale

%post shared-data
xmlcatalog --noout --add 'delegateURI' \
	'http://bluefish.openoffice.nl/ns/bflang/2.0/' \
	'%{_datadir}/xml/bluefish' \
	%{_sysconfdir}/xml/catalog &> /dev/null || :

%postun shared-data
if [ "$1" = 0 ]; then
	xmlcatalog --noout --del \
		'http://bluefish.openoffice.nl/ns/bflang/2.0/' \
		%{_sysconfdir}/xml/catalog &> /dev/null || :
fi

%files
%license COPYING
%{_bindir}/bluefish
%{_libdir}/bluefish/

%files shared-data -f %{name}.lang
%doc %{bluefish_docdir}/
%{_datadir}/bluefish/
%{_datadir}/metainfo/bluefish.appdata.xml
%{_datadir}/applications/bluefish.desktop
%{_datadir}/mime/packages/bluefish.xml
%{_datadir}/icons/hicolor/*/mimetypes/application-x-bluefish-project.png
%{_datadir}/icons/hicolor/*/apps/bluefish.png
%{_datadir}/icons/hicolor/scalable/mimetypes/bluefish-project.svg
%{_datadir}/icons/hicolor/scalable/apps/bluefish-icon.svg
%{_datadir}/pixmaps/application-x-bluefish-project.png
%{_datadir}/pixmaps/bluefish.png
%{_datadir}/xml/bluefish/
%{_mandir}/man1/bluefish.1*

%changelog
* Thu Jan 16 2025 Paul Howarth <paul@city-fan.org> - 2.2.16-3
- Fix for gcc 15

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep 22 2024 Paul Howarth <paul@city-fan.org> - 2.2.16-1
- Update to 2.2.16 (rhbz#2314037)
  - Bluefish 2.2.16 is mostly a maintenance release
  - New feature: Bookmarks can now be generated from external commands such as
    ctags
  - The 2.2.16 code has a lot of small fixes and improvements for Mac OSX
  - The old built-in javascript beautifier has been removed; Bluefish now uses
    the jsbeautify from your system (if available)
  - The word-wrap function has been fixed
- Add fix for type issue causing FTBFS with gcc 14
  (https://sourceforge.net/p/bluefish/tickets/95/)
- Drop support for EL-7 and Fedora releases of a similar vintage

* Fri Sep 20 2024 Paul Howarth <paul@city-fan.org> - 2.2.15-4
- Switch from enchant to enchant2 for spell checking

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.2.15-2
- Rebuilt for Python 3.13

* Mon Mar 18 2024 Paul Howarth <paul@city-fan.org> - 2.2.15-1
- Update to 2.2.15 (rhbz#2269978)
  - Bluefish 2.2.15 is a minor maintenance release
  - New feature: it can highlight the indenting level with a vertical line,
    which is very useful during python programming and helps with a lot more
    programming languages
  - Fix zencoding for python releases newer than 3.12
  - Add a retry button when opening files from a remote location
  - Tiny performance improvement when scrolling
  - Fix a bug in the bookmarks function and the visible indenting function
    that potentially could lead to a crash
  - The perl syntax detection has been greatly improved
  - YAML syntax detection has been added
  - The code has several fixes to make it compile on modern Mac OSX releases
    and to make it compile with the clang compiler
- Hardlink identical packaged files together to save space

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 13 2023 Paul Howarth <paul@city-fan.org> - 2.2.14-5
- Fix use of incompatible pointer types (upstream rev 8991)
- Fix improper use of pointer: https://sourceforge.net/p/bluefish/tickets/80/

* Fri Sep  1 2023 Florian Weimer <fweimer@redhat.com> - 2.2.14-4
- Improve C99 compatibility

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.2.14-2
- Rebuilt for Python 3.12

* Sun Jun  4 2023 Paul Howarth <paul@city-fan.org> - 2.2.14-1
- Update to 2.2.14 (rhbz#2212156)
  - Fix three bugs that in certain situations could lead to a segfault
    - When deleting backup files on close
    - When closing some of the dialogs in a flatpak distributed version of
      bluefish
    - When the CSS language file was loaded on a 32bit system.
  - Fix zencoding functionality with python3
  - Add an option to store the scope of the search dialog to the session or
    project (this was removed in 2.2.12 because of a bug report)
  - Improve the speed of the bookmarks code
  - The build infrastructure was also slightly modernized; intltool is no
    longer used
- Avoid use of deprecated patch syntax

* Fri Feb 24 2023 Paul Howarth <paul@city-fan.org> - 2.2.13-1
- Update to 2.2.13 (rhbz#2173097)
  - Bluefish 2.2.13 is a very minor maintenance release
  - The biggest update is in the CSS syntax support
  - Next to that it improves a few user interface parts, and fixes some very
    minor bugs
  - It also has some minor improvements for the syntax highlighting in a few
    other languages, most notably python

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.2.12-7
- Rebuilt for Python 3.11

* Wed Feb  2 2022 Paul Howarth <paul@city-fan.org> - 2.2.12-6
- Drop support for EL-6 and ancient Fedora releases of similar vintage
  - Always use gtk3, never gtk2
  - Always able to use Python 3
  - No longer need to filter rpm provides for private shared objects
  - %%license macro always available

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.2.12-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov  6 2020 Paul Howarth <paul@city-fan.org> - 2.2.12-1
- Update to 2.2.12
  - This is a minor maintenance release with some minor new features
  - Most important is a fix for a crash in simple search
  - Python 3 compatibility has been further improved
  - Encoding detection in python files has been improved
  - Triple click now selects the line
  - On Mac OSX, Bluefish deals better with the new permission features
  - Using the correct language in the Bluefish user interface is fixed for
    certain languages on OSX
  - Several programming languages have improved syntax highlighting
  - Bluefish now works fine with Enchant2 for spell checking
- Python support now requires Python ≥ 3.3, available from Fedora 18 onwards
- Add patch to clean up appdata file so it passes validation

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Paul Howarth <paul@city-fan.org> - 2.2.11-1
- Update to 2.2.11
  - This is a minor maintenance release and minor feature release; the only
    exception to that is the Python 3 compatibility, which is a major change
    and may introduce new bugs
  - Double click selection has been improved (for example selecting a function
    name that has underscores), and is now configurable per language
  - Bluefish now has a feature to fill a line with spaces up to a mouse click,
    so you can start typing in any position on the screen (with a fixed width
    font)
  - A crash when running very large replace actions on disk on many files has
    been fixed
  - Search and replace now ignores backup files by default
  - Cursor highlighting and line highlighting have been fixed for a rare bug
  - A small new feature has been added, to insert output from an external
    command in the current cursor position
  - Many language files have seen updates, most notably CSS, Python and HTML
  - A data loss bug - when an unknown encoding was selected - was fixed; the
    fallback is now to save as UTF-8
  - A bug when saving with unknown characters in the filename has also been
    fixed
  - Printing has been improved, such as printing in landscape
  - Some small tweaks to the UI have been implemented, e.g. can now search in
    files in the filebrowser (right click a directory)
  - Search results can now be shown in the output pane
  - The current identifier can be selected using <shift><control><i>
  - Various fixes when Bluefish is run on top of Wayland

* Mon Nov  4 2019 Paul Howarth <paul@city-fan.org> - 2.2.10-13
- Disable Python functionality on F-32, EL-8 onwards as it requires Python 2
  https://bugzilla.redhat.com/show_bug.cgi?id=1737907
  Will re-enable when Python 3 is supported
  https://sourceforge.net/p/bluefish/tickets/10/

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Paul Howarth <paul@city-fan.org> - 2.2.10-9
- Explicitly byte-compile "extra" python code using Python 2
- Avoid use of /usr/bin/env in shipped scripts
- Provides filter not needed from F-20, EL-7 onwards

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Paul Howarth <paul@city-fan.org> - 2.2.10-7
- Revert redundant changes from previous commit

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.10-6.1
- Remove obsolete scriptlets

* Mon Jan  8 2018 Paul Howarth <paul@city-fan.org> - 2.2.10-6
- Retain legacy scriptlets for builds on legacy Fedoras
- Remove a Group: tag that was missed earlier

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.10-5.1
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.2.10-3
- Rebuild due to bug in RPM (RHBZ #1468476)

* Tue Feb  7 2017 Paul Howarth <paul@city-fan.org> - 2.2.10-2
- Avoid potential aliasing issues in zencoding plugin

* Mon Jan 30 2017 Paul Howarth <paul@city-fan.org> - 2.2.10-1
- Update to 2.2.10
  - This is a maintenance release
  - Various fixes for newer gtk versions and for gtk on wayland (which is now
    the default on Fedora)
  - Fixes for a few rare crashes
  - Various language files have been improved, most notably languages that
    include CSS
  - New feature: ability to import/export syntax color styles; included are
    styles for a light and a dark theme

* Fri Jun 17 2016 Paul Howarth <paul@city-fan.org> - 2.2.9-1
- Update to 2.2.9
  - GTK 3.20 compatibility
  - A few other minor bug fixes

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 23 2016 Paul Howarth <paul@city-fan.org> - 2.2.8-1
- Update to 2.2.8
  - A bugfix release with some small improvements and more polished existing
    features
  - Fixes a few serious but rarely occuring bugs
  - Options defined in the language definition files are now translated
  - Various default settings have been improved, most notably the command to
    launch Firefox for preview
  - The looks on newer GTK versions have been restored
  - CSS can now be compressed and decompressed
  - The installers for Windows and OSX have improvements, and there have been
    some OSX and Windows specific fixes
  - Character encoding detection has been improved.
  - Auto-completion for HTML attributes has been improved
- Don't replace new upstream AppData screenshot
- Bump python requirement to 2.7, needed for CSS decompressor

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 31 2015 Paul Howarth <paul@city-fan.org> - 2.2.7-2
- Fix back-compatibility with old Fedoras and EPEL

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 2.2.7-1.1
- Use better AppData screenshots (http://bugzilla.gnome.org/747101)

* Mon Feb  2 2015 Paul Howarth <paul@city-fan.org> - 2.2.7-1
- Update to 2.2.7 (mostly a bug fix release)
  - Fixes rare crashes in the autocompletion, the filebrowser, the htmlbar
    plugin preferences, and in file-load-cancel
  - Fixes a rare case of broken syntax highlighting after multiple
    search/replace actions
  - Displays better error/warning output when parsing language files
  - Finally fixes javascript regex syntax highlighting
  - Loading of files with corrupt encoding has been improved
  - Project loading over sftp has been improved
  - Various HTML5 tags have been added, and HTML5 is the default now for php,
    cfml and other languages that can include html syntax
  - Saving and loading of UTF-16 encoded files was broken and has been fixed
  - Various languages have better support, such as javascript, css, html,
    pascal/deplhi, and html has improved autocompletion
  - On OSX the keys for tab switching no longer confict with some keyboard
    layouts, and behavior at shutdown was improved
  - The upload/download feature has a new option to ignore backup files
  - The home/end keys now work better on wrapped text
  - The search and replace dialog correctly shows the number of results when
    searching in files on disk

* Thu Sep 18 2014 Paul Howarth <paul@city-fan.org> - 2.2.6-5
- All scriptlets should be associated with the -shared-data package
- Don't own appdata directory on distributions where the filesystem package
  owns it
- Make %%summary toolkit-agnostic
- Use %%license where possible

* Sat Aug 16 2014 Rex Dieter <rdieter@fedoraproject.org> - 2.2.6-4
- -shared-data: add icon/mime scriptlets, drop extra Requires (core glib/gtk already pull those in)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.6-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Paul Howarth <paul@city-fan.org> - 2.2.6-3
- Make the shared-data sub-package depend on the main package so that we pull
  in the binary when someone tries to install just the data, which is what
  gnome-software does (#1091613)

* Sat Jun  7 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 22 2014 Paul Howarth <paul@city-fan.org> - 2.2.6-1
- Update to 2.2.6 (mostly a bug fix release)
  - Fixes a critical bug (segfault) in filebrowser that could be triggered if
    the root directory was set as basedir
  - Fixes a specific CSS-in-HTML-tag highlighting issue
  - The filter code caused a segfault if the command did not exist
  - Development checks disabled for release builds
  - Improvements to C, Javascript and CSS language files
  - Updated translations
  - Fixed a corner case for a new document from a template that does not exist
  - The "open" submenu now opens SVG files from the filebrowser instead of
    inserting an image tag
  - The included cssmin and jsbeatify have been updated
  - Fixed a syntax scanning issue when replacing large chunks of text
  - The "Report bug" link was broken
  - A new "conditional" option to the language file that makes re-using certain
    blocks of language files easier was added
  - Error reporting in outputbox was improved
- Use Gtk3 for EL-7 build
- Drop %%defattr, redundant since rpm 4.4
- Drop Group and BuildRoot tags, %%clean section, also now redundant

* Tue Mar  4 2014 Paul Howarth <paul@city-fan.org> - 2.2.5-2
- Misc fixes backported from upstream svn:
  - Fixes Upstream Bug #723568
  - Fixes Bug #1071689
  - Fixes a bug that left development enabled (#1066710, #1068719)
  - Fix an issue in get_toplevel_name_for_uri()
  - Make sure filetreemodel_build_dir() can handle a NULL (invalid) toplevel
  - Fix a couple of miscellaneous bugs

* Sat Feb  1 2014 Paul Howarth <paul@city-fan.org> - 2.2.5-1
- Update to 2.2.5 (mostly a minor bugfix release)
  - Includes various fixes for:
    - Wrap text on right margin
    - The replace engine
    - Free jsmin implementation
    - The split lines feature
    - Auto-recovery
    - Many obscure bugs
  - Other improvements:
    - The syntax scanning engine is faster after small changes to the text
    - The file browser is also much faster with less memory usage, with various
      fixes and new features
    - Projects now store the active document and active line numbers
    - Indenting is improved in auto-completion and the smart indenting
    - Bookmarks and paste special also have been improved
    - Almost all syntax highlighting has been improved, most notably jquery in
      javascript, HTML5, and HTML5 in PHP files
    - Bluefish now has an appdata file
- Drop upstreamed fixes for syntax highlighting and jsmin.py

* Mon Dec  2 2013 Paul Howarth <paul@city-fan.org> - 2.2.4-4
- Replace v8 jsmin implementation (which doesn't work with bluefish) with an
  MIT-licensed version that will be in bluefish 2.2.5
- Add upstream fix for syntax highlighting problem (#983902, Gnome Bug #704108)

* Tue Sep  3 2013 Tom Callaway <spot@fedoraproject.org> - 2.2.4-3
- Remove non-free jsmin.py code, replace with free jsmin.py

* Sun Jul 28 2013 Paul Howarth <paul@city-fan.org> - 2.2.4-2
- Install docs to %%{_pkgdocdir} where available

* Wed Feb  6 2013 Paul Howarth <paul@city-fan.org> - 2.2.4-1
- Update to 2.2.4 (mostly a minor bugfix release)
  - Includes various fixes for:
    - Tab-width on gtk 3.6
    - Blocksync feature
    - Scrollwheel-zoom
    - Language syntax detection
    - Character encoding detection
    - Toggle comment
    - Split view
  - Performance improved, particularly for auto-completion popup speed
  - New features include:
    - More simple search options
    - Paste special (to paste for example images from Libreoffice)
    - Control-tab to switch to the most recent document
    - Save as copy
    - pylint, cssmin, jsmin, csstidy and php_beautifier integration
  - Various language syntax definition files have also been improved
- Drop upstreamed patch for Gnome Bug #678951
- Bump glib2/gtk version requirements as needed
- Revert F-15 build to gtk2 as gtk3 version there is too old
  (Gnome Bug #693255)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 Paul Howarth <paul@city-fan.org> - 2.2.3-1
- Update to 2.2.3 (many minor bugfixes and many minor enhancements)
  - Fix segfault in syntax scanner
  - Code folding has major fixes and improvements
  - Search has major fixes
  - Lorem ipsum generator added
  - GUI restructured in some areas
  - Some shortcut key combinations added
  - Visibility features such as bigger cursor and cursor highlighting added,
    and some options were improved such as zoom and custom colors
  - Changes to external commands include better cursor positioning after a
    filter has been used, user-supplied arguments, and an option to restore
    the default settings
  - Some dialogs added for HTML5
  - Thumbnail generator fixed
  - Insert color, path and relative path have been added
  - Many language files improved, and more user configurable options added to
    most language files
  - You can now select a block of text by dragging the mouse in the margin, and
    move the selected block with <ctrl><up> and <ctrl><down>
- Drop workaround for broken gucharmap pkgconfig file (#795537)
- Fix missing trailing semicolon in Spanish translation of desktop file
  (Gnome Bug #678951)
- Bump gtk2 requirement to 2.18 (F-12 and above) (Gnome Bug #678953)

* Wed Feb 29 2012 Paul Howarth <paul@city-fan.org> - 2.2.2-1
- Update to 2.2.2 (bug fix release with some very minor new features)
  - Fix segfault when closing document with active search results
  - Fix multiple replace with search results directly adjacent corrupting text
  - Fix broken cursor positioning that ruined the Zencoding plugin
  - Fix CSS dialog that was unusable on GTK-3
  - Fix position of right margin indicator on GTK-3
  - Fix several small memory leaks
  - Fix annoying scrolling of the side bar filebrowser in 'treeview' mode
  - Use multiple threads to improve start-up performance
  - Fix descriptions of language options
  - Improve HTML5 option text and menu strings
  - Improve accelerators, shortcut keys and translations
  - New features: duplicate line and delete line
  - Add Catalan translation
- Fix permissions of zencoding plugin scripts to placate rpmlint

* Mon Feb 27 2012 Paul Howarth <paul@city-fan.org> - 2.2.2-0.1.rc1
- Update to 2.2.2-rc1
- Drop upstream patch for #771227
- BR: glib2 ≥ 2.18 (Gnome Bug #670883)

* Mon Feb 20 2012 Paul Howarth <paul@city-fan.org> - 2.2.1-3
- Fix abort due to free() of invalid pointer (#771227)
- Work around broken gucharmap pkgconfig file (#795537)

* Thu Jan  5 2012 Paul Howarth <paul@city-fan.org> - 2.2.1-2
- Rebuild for gcc 4.7

* Fri Dec 23 2011 Paul Howarth <paul@city-fan.org> - 2.2.1-1
- Update to 2.2.1
  - New feature: Zencoding support
  - Fix to build on Gtk+-2.22
  - Fix for PCRE regular expression searching
  - Layout fixes for Gtk+-3.2
  - Several obscure segfault fixes
  - Fix for autocompletion of variables in PHP
  - <img> dialog fixes
  - Memory-leak fixes
- Drop patch, now included upstream
- BR: python2-devel

* Tue Nov 22 2011 Paul Howarth <paul@city-fan.org> - 2.2.0-1
- Update to 2.2.0
  - New "select block" feature
  - Block stack is displayed on the statusbar
  - Completely rewritten search and replace engine
  - Quickbar feature has been removed
  - Large changes internally for GTK3 compatibility
- Drop patches, now included upstream
- Add patch to fix build with gtk 2.22 (Gnome bug 664556)

* Fri Jul 22 2011 Paul Howarth <paul@city-fan.org> - 2.0.3-4
- Fix crash in _gtk_text_btree_get_chars_changed_stamp
  (Gnome bug 654838, #720990)
- Nobody else likes macros for commands

* Thu Mar 10 2011 Paul Howarth <paul@city-fan.org> - 2.0.3-3
- Add workaround for crash on close (Gnome bug 637990, #683497)

* Sun Feb 27 2011 Paul Howarth <paul@city-fan.org> - 2.0.3-2
- Fix highlighting of block delimiters (Gnome bugs 643150 and 643153, #680626)

* Wed Feb 23 2011 Paul Howarth <paul@city-fan.org> - 2.0.3-1
- Update to 2.0.3
- Drop gtk2 version requirement back down to 2.12

* Mon Feb  7 2011 Paul Howarth <paul@city-fan.org> - 2.0.3-0.2.rc2
- Update to 2.0.3-rc2

* Tue Jan  4 2011 Paul Howarth <paul@city-fan.org> - 2.0.3-0.1.rc1
- Update to 2.0.3-rc1
- Drop patches now integrated into upstream release
- Bump gtk2 version requirement to 2.14

* Sun Dec 19 2010 Paul Howarth <paul@city-fan.org> - 2.0.2-6
- Update patch for #663014 to fix another potential issue that was discovered

* Wed Dec 15 2010 Paul Howarth <paul@city-fan.org> - 2.0.2-5
- Fix crash in autosave (#663014)

* Thu Nov 18 2010 Paul Howarth <paul@city-fan.org> - 2.0.2-4
- Fix crash when removing files/projects from recently-used lists (#653299)

* Thu Oct  7 2010 Paul Howarth <paul@city-fan.org> - 2.0.2-3
- Drop charmap plugin from Rawhide for now

* Wed Sep 29 2010 jkeating - 2.0.2-1.1
- Rebuilt for gcc bug 634757

* Fri Sep 17 2010 Paul Howarth <paul@city-fan.org> - 2.0.2-1
- Update to 2.0.2 (minor bugfix and minor feature enhancement release)
  - Two crashes have been resolved
  - A "jump to reference" feature has been added
  - Translations improved

* Tue Sep  7 2010 Paul Howarth <paul@city-fan.org> - 2.0.2-0.1.rc1
- Update to 2.0.2-rc1
- Drop patch for #626246, no longer needed
- License changed from GPLv2+ to GPLv3+

* Thu Aug 26 2010 Paul Howarth <paul@city-fan.org> - 2.0.1-2
- Fix crash in File Open dialog with filter applied (#626246)
- Change buildreq "man" to "/usr/bin/man" since the "man" package has been
  obsoleted by "man-db" from Fedora 14

* Fri Jun 18 2010 Paul Howarth <paul@city-fan.org> - 2.0.1-1
- Update to 2.0.1
- Drop upstreamed log10 linking patch
- Drop redundant buildreqs pcre-devel and python-devel

* Wed Feb 17 2010 Paul Howarth <paul@city-fan.org> - 2.0.0-2
- Bluefish uses GIO rather than GnomeVFS so buildreq libgnomeui-devel is
  no longer needed
- Explicitly buildreq libxml2-devel

* Tue Feb 16 2010 Paul Howarth <paul@city-fan.org> - 2.0.0-1
- 2.0.0 release
- Remove upstreamed projects patch
- Update log10 linking patch

* Mon Feb 15 2010 Paul Howarth <paul@city-fan.org> - 2.0.0-0.4.rc3
- Fix FTBFS due to missing -lm linking for log10 function (#565197)

* Sun Jan 31 2010 Paul Howarth <paul@city-fan.org> - 2.0.0-0.3.rc3
- Update to 2.0.0-rc3
- Drop snippets patch
- Add upstream patch resolving some project-related issues (#549552)

* Wed Jan 27 2010 Paul Howarth <paul@city-fan.org> - 2.0.0-0.2.rc2
- Update to 2.0.0-rc2
- Apply upstream patch to re-enable snippets menu
- Disable python plugin on upstream advice (#549552 comment 6)
- Disable dependency tracking to speed up build
- Register XML catalog in %%post and %%postun

* Wed Dec 30 2009 Paul Howarth <paul@city-fan.org> - 2.0.0-0.1.rc1
- Update to major new version - 2.0.0-rc1 (#549552)
- Drop all patches
- No longer need buildreqs gail-devel, gnome-mime-data, gnome-vfs2-devel
- Buildreq gucharmap-devel >= 2.20 for charmap plugin
- Buildreq intltool for translations
- Buildreq man to check man pages
- Buildreq python-devel for python plugin
- Req findutils and grep for the Advanced Open function
- Use %%{name} macro for spec file compatibility with bluefish-unstable
- Call %%find_lang multiple times for plugin translations
- Filter provides for plugin shared objects
- Desktop file now installed as part of upstream install process, so use
  desktop-file-validate instead of desktop-file-install
- Explicitly enable python plugin (disabled by default despite docs to contrary)
- All supported releases now have noarch subpackages, so drop conditionals

* Thu Nov 19 2009 Paul Howarth <paul@city-fan.org> - 1.0.7-9
- Buildreq gnome-mime-data, not pulled in by gnome-vfs2 since 2.24.1-8 (#539223)
- Buildreq enchant-devel >= 1.4.2, needed for enchant_dict_add
- Make %%files list more explicit

* Thu Jul 30 2009 Paul Howarth <paul@city-fan.org> - 1.0.7-8
- Include patch from Caolan McNamara for using enchant rather than aspell for
  spell-checking (#509514)
  http://fedoraproject.org/wiki/Releases/FeatureDictionary
- Try to maintain timestamps on unmodified files from upstream

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Paul Howarth <paul@city-fan.org> - 1.0.7-6
- Split off shared-data noarch subpackage for Fedora 10 onwards
- Add buildreq gail-devel to fix broken detection of libgnomeui on F-9

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 14 2008 Paul Howarth <paul@city-fan.org> - 1.0.7-4
- rebuild with gcc 4.3.0 for Fedora 9

* Mon Jan 21 2008 Paul Howarth <paul@city-fan.org> - 1.0.7-3
- include patch from upstream VCS to work around problem editing syntax
  highlighting patterns (#390871)

* Sun Aug 26 2007 Paul Howarth <paul@city-fan.org> - 1.0.7-2
- clarify license as GPL version 2 or later
- unexpand tabs in spec
- update scriptlets and drop scriptlet dependencies

* Mon Nov  6 2006 Paul Howarth <paul@city-fan.org> - 1.0.7-1
- update to 1.0.7
- update download URL
- don't add category X-Fedora in desktop files

* Tue Aug 29 2006 Paul Howarth <paul@city-fan.org> - 1.0.5-4
- rebuild for dynamic linking speedups (FE6)

* Mon May 22 2006 Paul Howarth <paul@city-fan.org> - 1.0.5-3
- fix broken debuginfo packages by not stripping binaries (#192617)
- cosmetic changes to spec file
- add extra doc files AUTHORS ChangeLog NEWS README TODO
- use full command paths for reproducible builds

* Thu Feb 16 2006 Paul Howarth <paul@city-fan.org> - 1.0.5-2
- rebuild

* Mon Feb  6 2006 Paul Howarth <paul@city-fan.org> - 1.0.5-1
- update to 1.0.5
- include manpage

* Mon Sep  5 2005 Paul Howarth <paul@city-fan.org> - 1.0.4-1
- update to 1.0.4

* Sun Aug 21 2005 Paul Howarth <paul@city-fan.org> - 1.0.3-1
- update to 1.0.3

* Sat Aug 20 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.0.2-3
- rebuilt

* Fri Jul 29 2005 Paul Howarth <paul@city-fan.org> - 1.0.2-2
- buildrequire libgnomeui-devel, not libgnomeui

* Fri Jul 29 2005 Paul Howarth <paul@city-fan.org> - 1.0.2-1
- update to 1.0.2
- add dist tag
- add libgnomeui support as per upstream package (#161234, #163804)
- add project desktop entry
- desktop entry munging not needed

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.0-4
- rebuild on all arches

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sun Feb 20 2005 Phillip Compton <pcompton[AT]proteinmedia.com> 1.0-2
- Fix for absolute path to icon in desktop entry.

* Tue Jan 11 2005 Phillip Compton <pcompton[AT]proteinmedia.com> 1.0-1
- 1.0.

* Sat Jan 01 2005 Phillip Compton <pcompton[AT]proteinmedia.com> 1.0-0.1.cvs20041231
- cvs20041231

* Fri Nov 12 2004 Phillip Compton <pcompton[AT]proteinmedia.com> 0.13-0.fdr.4
- Redirect output for post/postun.
- More mime-types in desktop entry.
- Fix changelog.

* Thu Nov 11 2004 Phillip Compton <pcompton[AT]proteinmedia.com> 0.13-0.fdr.3
- Updated .desktop entry for new mime-type system.
- Added post/postun update-desktop-database.
- Removed files from old mime-type system.

* Mon Apr 12 2004 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.13-0.fdr.2
- Now including .applications file and mime info.

* Sat Apr 10 2004 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.13-0.fdr.1
- Updated to 0.13.

* Mon Nov 24 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.12-0.fdr.1
- Updated to 0.12.
- BuildReq gnome-vfs2-devel.

* Sun Oct 19 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0.11-0.fdr.5
- Release detection dropped..1

* Mon Oct 06 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.11-0.fdr.4
- Improved release detection.

* Sun Sep 28 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.11-0.fdr.3
- Modified for Fedora Core release detection.
- Updated description.

* Mon Sep 15 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.11-0.fdr.2
- Now auto-detecting RH release.

* Sun Jul 27 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.11-0.fdr.1
- Updated to 0.11.

* Fri Jul 25 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.10-0.fdr.2
- Enable feature diferention for shrike vs severn.
- BuildReq aspell-devel for severn.
- in bluefish.desktop: Terminal=0 => Terminal=false.
- Source0 path updated.

* Thu Jul 17 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.10-0.fdr.1
- Updated to 0.10.

* Thu Jul 17 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.10-0.fdr.0.1.20030716
- 2003-07-16 snapshot.

* Thu Apr 10 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.9-0.fdr.5
- Added gettext to BuildRequires.

* Tue Apr 01 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:0.9-0.fdr.4
- Changed category to X-Fedora-Extra.
- Added Epoch:0.
- Removed redundant Requires entries.

* Sun Mar 23 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0.9-0.fdr.3
- Updated for inclusion in fedora

* Wed Mar 05 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0.9-0.fdr.2
- Cleaned up spec file

* Wed Feb 19 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0.9-1.fedora.1
- Updated to 0.9

* Sat Feb 8 2003 Phillip Compton
- Update to snapshot: 20030207

* Wed Feb 5 2003 Phillip Compton
- Update to snapshot: 20030205

* Wed Jan 15 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to the latest snapshot which should be more stable.

* Sat Jan 11 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.8.
- Major spec file updates based on the one from Matthias Haase.

* Thu May  2 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt against Red Hat Linux 7.3.
- Added the %%{?_smp_mflags} expansion.

* Mon Nov 19 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.7.
- Spec file simplifications since the build is now cleaner :-)

* Wed May  2 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Spec file cleanup for Red Hat 7.1.
- Added a GNOME desktop entry.
- Compiled with kgcc and reported the problems encountered with gcc 2.96.

* Fri May 5 2000 Bo Forslund <bo.forslund@abc.se>
- fine tuning of the spec file
- possible to build with all processors on smp machines
- an entry for RedHats wmconfig

* Tue Mar 21 2000 CW Zuckschwerdt <zany@triq.net>
- complete rewrite of spec file
- relocateable on build-time
- no privileges required while building
- fix for install_location (should really be $(LIBDIR)/bluefish!)
- included man, locale and lib into RPM (was seriously broken)

* Thu Jan 13 2000 Chris Lea <chrislea@luciddesigns.com>
- Fixed up spec file some. bluefish-0.3.5

* Wed Nov 17 1999 Chris Lea <chrislea@luciddesigns.com>
- added spec file. this is my third RPM that I've made a spec
  file for, so please be merciful if I've screwed something up
