%define BothRequires() \
Requires:       %{*} \
BuildRequires:  %{*} \
%{nil}

%define		majorver	0.7.9
%undefine		minorver	
%undefine		ifpre	

%define		baserelease	8
%define		rel		%{?ifpre:0.}%{baserelease}%{?minorver:.%minorver}



Name:		alexandria
Version:	%{majorver}
Release:	%{rel}%{?dist}
Summary:	Book collection manager

# Overall	GPL-2.0-or-later
# share/gnome/help/alexandria/C/alexandria.xml	GFDL-1.2-or-later
# SPDX confirmed
License:	GPL-2.0-or-later AND GPL-2.0-or-later
URL:		https://github.com/mvz/alexandria-book-collection-manager/
Source0:	%{url}/archive/v%{version}/%{name}-%{version}%{?minorver:-%{minorver}}.tar.gz
# Patches discussing with the upstream
# Trial fix for hang up when importing list containing invalid isdn
# ref: alexandria-Bugs-25348
# Check if this issue is fixed in rev 1154
#Patch2:		alexandria-0.6.4.1-hang-importing-invalid-isdn.patch
# Trial fix for crash when importing a book with isdn
# With alexandria-0.6.6, the fix for this issue is still incomplete
# ref: alexandria-BUgs-28263
Patch3:		alexandria-0.7.4-dont_use_thread_when_adding_file_by_isdn.patch
# Fix crash when searching book
# ref: alexandria-Bugs-29479 Patch by Tomoh K.
# Applied in 0.6.9
# Patch4:		alexandria-0.6.8-set_status_label.patch
# Upstream patches
# Patches not submitted to the upstream
# Force encoding type to make rake happy
Patch14:	alexandria-0.7.9-ascii-fix.patch
# Fix kcode issues with 1.9
# Well, with the original fix, some strange failure on startup
# happens on ja_JP.utf8...
#Patch15:	alexandria-0.6.8-kcodefix.patch
# Two fixes:
# a. loading yaml file generated by ruby 18x will show garbage characters
# b. moving book entry to another library which also contains the
#    same book will cause crash..
Patch18:	alexandria-0.7.9-utf8-convert.patch
# More UTF-8 fix on ruby 1.9, when exporting library to HTML
# (bug 819188)
Patch19:	alexandria-0.7.4-export-to-HTML-with-ruby19.patch
# More UTF-8 fix on ruby 1.9, when exporting library to csv
# or bibtex
Patch20:	alexandria-0.7.5-export-to-CSV-bintex-with-ruby19.patch
# Remove garbage character with icon view on multibyte locate
Patch21:	alexandria-0.7.4-iconview-multibyte.patch
# Split Patch18 into two patches, one for lib/alexandria/models/library.rb
# (this file) and other. Also handle broken yaml file correctly and let
# user redownload it
# (bug 861740)
Patch22:	alexandria-0.7.9-yaml-unescape.patch
# Add a feature to remove broken yaml files at startup when requested
# (bug 869556)
Patch23:	alexandria-0.7.4-delete-broken-yaml.patch
# Handle the case thread was not created with adding new book
Patch25:	alexandria-0.7.6-newbook-nothread.patch
# Make z3950 provider work
# ZOOM::Connection.count must be string
Patch26:	alexandria-0.7.9-z3950-zoom-count.patch
# Read negative value as integer in case position has such value
# (bug 1014295)
# https://github.com/mvz/alexandria-book-collection-manager/issues/135
# Applied in 0.7.9
#Patch27:	alexandria-0.7.6-negative-value.patch
# Specify goocanvas version (bug 1024931)
# This is obsolete with 0.7.4. 0.7.4 uses goocanvas2 with introspection
# Make glade2 translatable text actually translated (i10ned)
Patch29:	alexandria-0.7.4-glade-gettext.patch
# Workaround: more force_encoding for title, etc for loading old yaml
Patch30:	alexandria-0.7.4-title-force-encoding.patch
# Remove undefined / unneeded method
Patch31:	alexandria-0.7.4-remove-undefined-method.patch
# Once reset search text when adding new book (bug 1909500)
# https://github.com/mvz/alexandria-book-collection-manager/issues/106
Patch32:	alexandria-0.7.8-reset-search-when-adding-new-book.patch
# Explicitly specify image_size gem
Patch33:	alexandria-0.7.8-explicitly-specify_gem_image_size.patch

BuildArch:	noarch

Requires:	ruby(release)
BuildRequires:	ruby(release)

# For ruby macros
BuildRequires:	ruby-devel
BuildRequires:	rubygem(rake)
BuildRequires:	desktop-file-utils
# For gconf related macros
BuildRequires:	GConf2
BuildRequires:	gettext
BuildRequires:	intltool
# From 0.7.4
BuildRequires:	rubygem(rspec)
# Needed since Ruby 3.0.
# https://github.com/mvz/alexandria-book-collection-manager/issues/124
%BothRequires	rubygem(rexml)
# rspec test
BuildRequires:	%{_bindir}/xvfb-run
BuildRequires:	%{_bindir}/ping
BuildRequires:	rubygem(webmock)
BuildRequires:	rubygem(json)
BuildRequires:	rubygem(pry)
BuildRequires:	gstreamer1-plugins-base
# autoaudiosink
BuildRequires:	gstreamer1-plugins-good

# 0.7.9 uses nokogiri instead of hpricot
#Requires:	ruby(amazon)
%BothRequires	rubygem(gettext)
%BothRequires	rubygem(htmlentities)
%BothRequires	rubygem(image_size)
%BothRequires	rubygem(nokogiri)
# Dependency removed on 0.6.4b1
#Requires:	ruby(mechanize)
# Kill ruby(revolution) dependency
#Requires:	ruby(revolution)
%BothRequires	rubygem(psych)

# ruby(zoom) -> rubygem(zoom) switch
#Requires:	ruby(zoom)
%BothRequires	rubygem(zoom) >= 0.3.0
%BothRequires	rubygem(marc)

# Killed on 0.6.8
#Requires:	ruby(gconf2)
# Explicitly
Requires:	GConf2
%BothRequires	rubygem(gdk_pixbuf2)
%BothRequires	rubygem(glib2)
# Killed on 0.6.8
#Requires:	ruby(gnome2)
#Requires:	ruby(libglade2)
# Added from 0.6.8
# Requires:	rubygem(goocanvas)
# The above needs more explicit
# With 0.7.4 this dependency changed, goocanvas2 + introspection
%BothRequires	rubygem(goocanvas) >= 2
%BothRequires	rubygem(gstreamer)
%BothRequires	rubygem(gtk3)
# Uses syck (bug 922217)
%BothRequires	rubygem(syck)

Requires(pre):		GConf2
Requires(post):		GConf2
Requires(preun):	GConf2

%description
Alexandria is a GNOME application to help you manage your book collection.

%prep
%setup -q -n %{name}-book-collection-manager-%{majorver}%{?minorver:-%{?minorver}}

# Check if patch2 issue is fixed in rev 1154
#%%patch -P2 -p0 -b .up25348
%patch -P3 -p1 -b .up28263.isdn
#%%patch -P4 -p0 -b .up29479.search
%patch -P14 -p1 -b .ascii -Z
#%%patch -P15 -p1 -b .kcodefix 
%patch -P18 -p1 -b .ruby19_utf8 -Z
%patch -P19 -p1 -b .export_html -Z
%patch -P20 -p1 -b .export_csv -Z
%patch -P21 -p1 -b .icon_kanji -Z
%patch -P22 -p1 -b .broken_yaml -Z
%patch -P23 -p1 -b .delete_yaml -Z
%patch -P25 -p1 -b .nothread -Z
%patch -P26 -p1 -b .z3950_count -Z
#%%patch -P27 -p1 -b .negative -Z
%patch -P29 -p1 -b .gettext -Z
%patch -P30 -p1 -b .utf8_2 -Z
%patch -P31 -p1 -b .undefined_method -Z
%patch -P32 -p1 -b .reset_search -Z
%patch -P33 -p1 -b .image_size -Z

# Part of https://github.com/mvz/alexandria-book-collection-manager/commit/d9116e99242c209129bf09c3c1ad9a4ff6fdcf44
# Needed for ruby3.2 - removes File.exists?
sed -i util/rake/gettextgenerate.rb -e 's|unless FileTest.exists.*$||'

# Embed Fedora EVR
%{__sed} -i.evr \
	-e "s|\(DISPLAY_VERSION = \).*$|\1'%{version}-%{release}'|" \
	Rakefile

# Make msgfmt verbose
%{__sed} -i.msgfmt \
	 -e '/system/s|msgfmt |msgfmt --statistics |' \
	util/rake/gettextgenerate.rb

# Workaround for directory hierarchy
ln -sf share data

# Use system wide directory for datadir
sed -i lib/alexandria/config.rb \
	-e "\@^[ \t]*SHARE_DIR@s|SHARE_DIR[ \t]*=.*|SHARE_DIR = '/usr/share'|"

%build
rake build --trace

%install
rake install_package_staging \
	DESTDIR=$RPM_BUILD_ROOT \
	RUBYLIBDIR=%{ruby_vendorlibdir}

desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications/ \
	--delete-original \
	$RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

# Move gconf files to where Fedora uses
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}
%{__mv} \
	$RPM_BUILD_ROOT%{_datadir}/gconf/ \
	$RPM_BUILD_ROOT%{_sysconfdir}/

# %%{_datadir}/menu seems to be used for debian
# Removing for Fedora
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/menu/

# Cleanups
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/pixmaps/
%{__rm} -f $RPM_BUILD_ROOT%{_bindir}/%{name}.*

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/metainfo
cat > $RPM_BUILD_ROOT%{_datadir}/metainfo/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!--
BugReportURL: https://github.com/mvz/alexandria-book-collection-manager/issues/2
SentUpstream: 2014-09-18
-->
<application>
  <id type="desktop">alexandria.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Manage your physical book collection</summary>
  <description>
    <p>
      Alexandria is an application that allows you to manage your book library.
      It lets you build and keep a detailed database (on your local machine) of
      information about books you own and have read.
    </p>
    <p>
      Alexandria also allows you to rate books, note when you have read them,
      and even track who you have loaned books out to.
      It also has interfaces with a online book information sources so you don’t
      have to type in all the information about a book, and also provides book
      cover art for many books.
    </p>
  </description>
  <url type="homepage">http://alexandria.rubyforge.org/</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/alexandria/a.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

%find_lang %{name}

%check
export LANG=C.utf8
# Tweak config path for %%check
sed -i.testsuite lib/alexandria/config.rb \
	-e 's|/usr/share|%{buildroot}%{_datadir}|'
# Kill tests which needs network
disable_test() {
	sed -i.testsuite $1 -e "\@$2@s|it|xit|"
}


rm -rf .config/gconf
mkdir -p .config/gconf
export XDG_CONFIG_HOME=$(pwd)/.config

# fake bundler
mkdir -p FAKE/bundler
touch FAKE/bundler/setup.rb
touch FAKE/simplecov.rb
export RUBYLIB=$(pwd)/FAKE

# Disable z3950 provider test
disable_test spec/alexandria/book_providers/bl_provider_spec.rb "works"

ping -w3 www.google.co.jp && \
	{
		# Need taking a look at this
		disable_test spec/alexandria/book_providers/loc_provider_spec.rb "works for a book";
		true;
	} \
	|| \
	{
		disable_test spec/alexandria/book_providers/thalia_provider_spec.rb "works when searching by ISBN";
		disable_test spec/alexandria/book_providers/loc_provider_spec.rb "works for a book";
		disable_test spec/alexandria/book_providers/sbn_provider_spec.rb "works";
		sed -i spec/alexandria/book_providers_spec.rb -e "\@Alexandria::BookProviders::SBNProvider@{n;s|it|xit|}";
	}

xvfb-run \
	-s "-screen 0 640x480x24" \
	rake spec:unit

find . -name \*.testsuite | while read f
do
	mv ${f} ${f%.testsuite}
done

%pre
%gconf_schema_prepare %{name}

%post
%gconf_schema_upgrade %{name}

%preun
%gconf_schema_remove %{name}

%files -f %{name}.lang
%license COPYING
%doc ChangeLog*
%doc INSTALL.md
%doc README*
%doc TODO.md
%doc doc/[A-Z]*
%doc doc/cuecat_support.rdoc

%{_mandir}/man1/%{name}.1*

%{_bindir}/%{name}
%{ruby_vendorlibdir}/%{name}.rb
%{ruby_vendorlibdir}/%{name}/

%{_sysconfdir}/gconf/schemas/%{name}.schemas

%{_datadir}/%{name}/
%{_datadir}/gnome/help/%{name}/
%{_datadir}/omf/%{name}/
%{_datadir}/sounds/%{name}/

%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan  2 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.9-5
- SPDX migration

* Fri Dec 22 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.9-4
- Disable z3950x provider test

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 17 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.9-2
- Backport some changes on upstream git for ruby3.2 File.exists? removal

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.9-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.9-1
- 0.7.9

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-6.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Kevin Fenzi <kevin@scrye.com> - 0.7.8-6.1
- Rebuild for hiredis 1.0.2

* Fri Aug 27 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.8-6
- Switch to image_size gem, specify explicitly
- Disable 1 failing test

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Mar  7 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.8-5
- set XDG_CONFIG_HOME for test suite

* Fri Mar  5 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.8-4
- Simply use rake spec, and fake bundler / simplecov

* Fri Mar  5 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.8-3
- Once reset search text when adding new book (bug 1909500)
- Enable test, fix Fedora specific patch (errors detected with the test)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan  7 2021 Vít Ondruch <vondruch@redhat.com> - 0.7.8-2
- Add ReXML dependency needed for Ruby 3.0.

* Thu Dec  3 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.8-1
- 0.7.8

* Mon Nov  2 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.6-1
- 0.7.6

* Fri Oct 30 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.5-1
- 0.7.5
- Once revert upstream change about setting initial visibility to false
  (upstream bug 86)

* Sun Aug  9 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.4-3
- syck is needed, adding to Requires again

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 11 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.4-2
- Fix Requires, expecially, add R: rubygem(gtk3) (bug 1833761)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.4-1
- 0.7.4, move to github mvz fork

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-11.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-11.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-11.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-11.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.9-11.3
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-11.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-11.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 15 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.9-11
- Make this compatible with gdk_pixbuf2 3.0.9

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-10.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.9-10.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.6.9-10.1
- Add an AppData file for the software center

* Mon Jan 19 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.9-10
- Remove deprecated Config:: usage yet more

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.9-9.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 12 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.9-9
- Make glade2 translatable text actually translated (i10ned)

* Fri Nov  1 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.9-8
- Change dependency on goocanvas on F-20+ (bug 1025095)
- Specify goocanvas version (bug 1024931)

* Mon Oct  7 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.9-7
- Read negative value as integer in case position has such value
  (bug 1014295)

* Wed Aug 21 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.9-6
- Change ZOOM::Connection.count to string to make z3950 provider
  work again

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.9-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 17 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.9-5
- F-19: rebuild for ruby 2.0.0
- F-19: require rubygem(syck) (bug 922217)

* Sat Feb 16 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.9-4
- Kill iconv and use encode instead
- Handle the case thread was not created with adding new book

* Sat Feb  9 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.9-3
- F-19: kill vendorization of desktop file (fpc#247)

* Sat Oct 27 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.6.9-2
- Add a feature to remove broken yaml files at startup when requested
  (bug 869556)

* Sun Oct 14 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.6.9-1
- 0.6.9

* Sat Oct 13 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.6.8-9
- Rescue the case where parsing yaml file failed and let user
  re-download book information (bug 861740)
 
* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8-8.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 30 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.8.6-8
- More UTF-8 fix on ruby 1.9, when exporting library to CSV and bibtex
- Remove garbage character with icon view on multibyte locate

* Sun May  6 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.8.6-7
- More UTF-8 fix on ruby 1.9, when exporting library to HTML
 (bug 819188)

* Fri Apr 13 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.6.8-6
- Convert escaped characters in yaml file generated by ruby 18x to
  aviod garbage characters
- Fix crash when moving book entry to another library when the same
  entry is found

* Wed Apr 11 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.6.8-5
- Fix crash on z3950 provider with working zoom

* Sun Apr  8 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.6.8-4
- Fix crash on ja_JP.utf8 (and perhaps on other multibyte locales) 

* Fri Mar 23 2012 Tom Callaway <spot@fedoraproject.org> - 0.6.8-3
- get working again

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jan  8 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.6.8-2
- Require rubygem(gstreamer) & remove no longer needed patch

* Sun Dec 25 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.6.8-1
- Update to 0.6.8
- Dependency for old ruby-gnome2 stuff is removed
- Make always require rubygems
- Patch to support usage without rubygem(gst)

* Sun Nov 27 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.6.7-1
- Update to 0.6.7

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-2.svn1154_trunk.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 16 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.6-2.svn1154
- Update from trunk to try the following fixes
  - Hang with importing bad ISDN number (alexandria-Bugs-25348)
  - UTF-8 issue on WorldCat provider (alexandria-Bugs-28437)
  - Other fixes on providers

* Tue Jun 22 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.6-1
- Update to 0.6.6
- Still apply Patch3 (it seems isdn segv fix isn't complete)

* Fri Jun 18 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.6-0.7.beta2
- Execute add_single_book_by_isbn in non-thread, which will fix the crash
  when imporing books with ISDN (upstream bug 28263)

* Sat Jun  5 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.6-0.6.beta2
- Apply patch for upstream bug 28250, icon view rearrangement issue

* Sat May  8 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.6-0.5.beta2
- Try 0.6.6 beta2

* Sat May  8 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.6-0.4.svn1138_trunk
- Try rev 1138, supporting Duban provider
- Scriptlets update

* Wed Dec 23 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.6-0.3.beta1
- Try 0.6.6 beta1

* Fri Dec 18 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.6-0.2.alpha
- Use "rake install_package_staging" as explained by the upstream
  (in alexandria-Bugs-27578)
- Kill the creation of 64/128 icons as scalable svg is already installed

* Thu Dec 17 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.6-0.1.alpha
- Try 0.6.6 alpha

* Tue Sep  8 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Wrong patch of sanity check patch applied on F-10/11, fixing...

* Wed Sep  2 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.5-7
- Fix for parsing WorldCat provider search result (alexandria-Bugs-27028)

* Sat Aug 28 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.5-6
- Fix crash on startup in tr_TR.UTF-8 (bug 520170, alexandria-Bugs-27015)

* Thu Aug 27 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.5-5
- Add sanity check for invalid search result, now using upstream patch
- Fix DeaStore provider where search result contains no Author
  (alexandria-Bugs-27000)

* Fri Aug 21 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.5-3
- Clarify GLib.convert usage in utils.rb (does not change the 
  functionality of alexandria, alexandria-Bugs-26968)

* Thu Aug 20 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.5-2
- Kill the previous 2 patches (for now)

* Thu Aug 20 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.5-1
- Update to 0.6.5
- Remove 2 upstreamed patches (1 patch still unremoved)
- Add 2 patches, will report upstream

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- F-12: Mass rebuild

* Mon Apr 13 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.4.1-6
- Trial fix to fix hang when importing list containing invalid
  isdn (alexandria-Bugs-25348)

* Wed Apr  8 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.4.1-5
- Embed Fedora EVR

* Tue Apr  7 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.4.1-4
- Fix for strange behavior with right click on left pane
  (alexandria-Bugs-25021)

* Thu Mar 26 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.4.1-2
- Fix arguments of bindtextdomain() for ruby(gettext) 2.0.0
  (alexandria-Bugs-24882)

* Mon Mar 16 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.4.1-1
- 0.6.4.1 (fixing alexandria-Bugs-24568)

* Sun Mar 15 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.4-1
- 0.6.4
- Patch from upstream to fix issue when book entry is once sorted
  (alexandria-Bugs-24568)

* Fri Mar  6 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.4-0.2.b1
- Add ruby(htmlentities) dependency

* Tue Mar  3 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.4-0.1.b1
- Update to 0.6.4 beta 1
- Drop all patches, merged into upstream

* Fri Feb 27 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.3-11
- library UTF-8 patch update

* Thu Feb 26 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.3-10
- Use upstreamed patch for UTF-8 strings issue

* Thu Feb 26 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.3-9
- Attempt to handle UTF-8 strings in library names correctly
  (alexandria-Bugs-20168)

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- F-11: Mass rebuild

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.3-8
- Global-ize "nested" macro
- GTK icon cache update scripts update

* Wed Feb  4 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.3-7
- Add hpricot dependency again (for Amazon provider)

* Sun Jan 11 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.3-6
- Rebuild to restore ARCHIVESIZE

* Wed Jul 16 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.3-5
- Remove workaround for bug 436697 (tooltips crash).
  This was a bug on ruby-gnome2 which is fixed in 0.17.0 rc1
  (ref: alexandria-Bugs-19042)

* Thu Apr  3 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.3-4
- Drop ruby(amazon) dependency (Amazon no longer provides AWSv3,
  AWSv4 is supported by alexandria itself)

* Sun Mar 23 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.3-2
- Disable tooltips on_motion func for now to workaround for
  bug 436697

* Sat Feb 23 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.3-1
- 0.6.3
- One patch removed (applied by upstream)

* Mon Dec 31 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.2-2
- Trial workaround patch for bug 427070

* Thu Dec 20 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.2-1
- 0.6.2
- Two patches for 0.6.2b2 are removed.

* Sun Dec 16 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.2-0.6.b2
- Pass exception when user don't use evolution for mailer.
- Fix crash when yelp is not installed.
- Add INSTALL to %%doc as this file contains some useful information.

* Wed Dec 12 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.2-0.3.b2
- Also require ruby(revolution)

* Tue Nov 13 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.2-0.2.b2
- Add more requires of ruby modules to support more function

* Sun Nov  4 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.2-0.1.b2
- And try 0.6.2 beta 2

* Fri Nov  2 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.2-0.1.b1
- Try 0.6.2 beta 1

* Fri May 11 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.1-3
- This time completely disable scrollkeeper-update
- Create 128x128 icon also

* Tue May  1 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.1-2
- Fix scriptlets typo

* Sun Apr 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.1-1
- Initial packaging
