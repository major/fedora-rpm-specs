%define	BothRequires() \
Requires:	%1 \
BuildRequires:	%1 \
%{nil}

%define		mainver		1.0
%define		betaver		beta7

%if 0%{fedora} < 19
%define		rubyabi		1.9.1
%endif

%define		baserelease	27


%define		fullrel		%{?betaver:0.}%{baserelease}%{?betaver:.%betaver}

Name:		fantasdic
Version:	%{mainver}
Release:	%{fullrel}%{?dist}
Summary:	Dictionary application using Ruby

# SPDX confirmed
License:	GPL-2.0-or-later
URL:		http://www.gnome.org/projects/fantasdic/
Source0:	http://www.mblondel.org/files/fantasdic/%{name}-%{mainver}%{?betaver:-%betaver}.tar.gz
# ruby-gnome2-Bugs-2865895
# Patch0:	fantasdic-1.0-beta7-workaround-rg2-bg2865895.patch
# Various ruby19 fixes
# Need utf-8 encoding direction
Patch10:	fantasdic-1.0-beta7-ruby19-utf8.patch
# Syntax error fix
Patch11:	fantasdic-1.0-beta7-ruby19-syntax.patch
# Path fix for modules in ruby 19
Patch12:	fantasdic-1.0-beta7-ruby19-pathfix.patch
# Guard sigtrap when calling Gdk::flush (bug 844754, bug 799804)
Patch13:	fantasdic-1.0-beta7-guard-sigtrap.patch
# ::Config was finally renamed to RbConfig in Ruby 2.2.
Patch14:	fantasdic-1.0-beta7-ruby22-rbconfig-fix.patch
# rbpango 3.1.6: use no-gi for now
# pango 1.44.x changed massively: use rbpango gi
Patch15:	fantasdic-1.0-beta7-use-pango-gi.patch
# ruby psych 4.0.x needs YAML.unsafe_load
Patch16:	fantasdic-1.0-beta7-yaml-unsafe-load.patch
# Remove duplicate test names
Patch17:	fantasdic-1.0-beta7-testsuite-remove-dupes.patch
# # Ruby 3.2 completely removes File.exists?
Patch18:	fantasdic-1.0-beta7-ruby32-file_exist.patch
# Misc fixes for ruby 3.2
Patch19:	fantasdic-1.0-beta7-ruby32-misc-fix.patch
# Dict server configuration update
Patch20:	fantasdic-1.0-beta7-dict-server-update.patch

BuildArch:	noarch

Requires:	ruby(release)
BuildRequires:	ruby(release)

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:  ruby-devel

%BothRequires	ruby
%BothRequires	rubygem(gettext)

%BothRequires	ruby(libglade2)
%BothRequires	ruby(gconf2)
%BothRequires	ruby(gnome2)
%BothRequires	ruby(gtk2)
# F-31+: use rbpango-gi
%BothRequires	rubygem(pango)
BuildRequires:	rubygem(test-unit)
BuildRequires:	%{_bindir}/xvfb-run

%description
Fantasdic is a dictionary application. It allows to look up words in 
various dictionary sources. It is primarily targetting the GNOME 
desktop but it should work with other platforms, including Windows. 
Fantasdic is Free Software.

%prep
%setup -q -n %{name}-%{mainver}%{?betaver:-%betaver}
#%%patch0 -p1
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1
%patch -P13 -p1
%patch -P14 -p1
ln -sf lib vendor_ruby
%patch -P15 -p4
unlink vendor_ruby
# ruby 3.1 (psych 4.x)
%patch -P16 -p1
%patch -P17 -p1
%patch -P18 -p1
%patch -P19 -p1
%patch -P20 -p1

%{__chmod} 0644 tools/*.rb
%{__sed} -i.path -e 's|%{_bindir}/||' fantasdic.desktop

# Fix up documents directory
%{__sed} \
	-i.dir -e '/html/s|%{name}|%{name}-%{mainver}|' \
	lib/fantasdic/ui/browser.rb

%build
export LANG=C.UTF-8

ruby setup.rb config \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--siterubyver=%{ruby_vendorlibdir} \
	--datadir=%{_datadir} \
	--without-scrollkeeper
ruby setup.rb setup

%install
ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

desktop-file-install \
	--add-category 'GTK' \
	--add-category 'Dictionary' \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	%{name}.desktop

# hicolor png icon symlinks
target="../../../.."
for n in 16 22 24 32 48
	do
	%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${n}x${n}/apps
	%{__ln_s} -f \
		${target}/%{name}/icons/%{name}_${n}x${n}.png \
		$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${n}x${n}/apps/%{name}.png
done

# symlink check
pushd $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${n}x${n}/apps
pushd $target
if [ "x$(pwd)" != "x$RPM_BUILD_ROOT%{_datadir}" ] ; then
	echo "Possibly symlink broken"
	exit 1
fi
popd
popd

%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
%{__ln_s} -f ${target}/%{name}/icons/%{name}.svg \
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/


# Clean up documents
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/doc/

%{find_lang} %{name}


%check
STATUS=0

# Tweak configuration for local test (without fantasdic itself being installed)
sed -i.save lib/fantasdic/config.rb -e "s|'%{_prefix}|'%{buildroot}%{_prefix}|"

NET_STATUS=0
ping -w3 www.google.co.jp || NET_STATUS=1

if [ $NET_STATUS != 0 ] ; then
	# disable test requiring net connection
	mv test/test_dict_server.rb{,.save}
fi
# google test not working, skip
mv test/test_google_translate.rb{,.save}

# Test suite expects that /bin/true is found
export PATH=/bin:$PATH

export LANG=C.utf8
xvfb-run \
	ruby -Ilib:. -e "Dir.glob('test/**/test_*.rb'){|f| require f}" || \
	STATUS=1

find . -name \*.save | while read f ; do
	mv $f ${f%.save}
done

exit $STATUS

%files	-f %{name}.lang 
%defattr(-,root,root,-)
%doc	AUTHORS
%license	COPY*
%doc	ChangeLog
%doc	NEWS
%doc	README
%doc	THANKS
%doc	TODO

%doc	tools/
%doc	data/doc/fantasdic/html/

%{_bindir}/%{name}

%{_datadir}/%{name}/
%{_datadir}/gnome/help/%{name}/
%{_datadir}/omf/%{name}/

%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%{_mandir}/man1/%{name}.1*

%{ruby_vendorlibdir}/%{name}.rb
%{ruby_vendorlibdir}/%{name}/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.27.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.26.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.25.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.24.beta7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan  3 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0-0.23.beta7
- SPDX migration

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.22.beta7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.21.beta7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov  9 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0-0.21.beta7
- Use YAML.unsafe_load for psych 4.0.x
- Some misc fixes for ruby 3.1
- Server configuration update for DICT
- Enable testsuite

* Thu Oct 13 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0-0.19.beta7
- Fix for ruby3.2 wrt File.exists? removal

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.18.beta7.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.18.beta7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 13 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0-0.18.beta7
- Drop old scrollkeeper stuff
- Drop old ruby BR stuff

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.17.beta7.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.17.beta7.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.17.beta7.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.17.beta7.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct  3 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0-0.17.beta7
- F-31+: use rbpango-gi because of pango 1.44 change

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.16.beta7.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.16.beta7.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0-0.16.beta7.5
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.16.beta7.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.16.beta7.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0-0.16.beta7.2
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.16.beta7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun  6 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0-0.16.beta7
- F-26+: use no-gi for pango 3.1.6

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.15.beta7.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.15.beta7.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.15.beta7.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 19 2015 Vít Ondruch <vondruch@redhat.com> - 1.0-0.15.beta7.3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.15.beta7.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.15.beta7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 14 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0-0.15.beta7
- Fix DATADIR and installation path

* Wed Mar 20 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0-0.14.beta7
- F-19: rebuild for ruby 2.0

* Sat Feb  9 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0-0.13-beta7
- F-19: kill vendorization of desktop file (fpc#247)

* Thu Aug  2 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.0-0.12.beta7
- Guard sigtrap when calling Gdk::flush (bug 844754, bug 799804)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.11.beta7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May  3 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.0-0.11.beta7
- Patch to work with ruby 1.9 (bug 817855)

* Mon Feb 27 2012 Vít Ondruch <vondruch@redhat.com> - 1.0-0.10.beta7
- Fix Gettext dependency.

* Tue Feb 07 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0-0.9.beta7
- Rebuilt for Ruby 1.9.3.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.8.beta7.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.8.beta7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Sep 27 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0-0.8.beta7
- Revert the last change; fixed in ruby-gnome2 side

* Sun Sep 27 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0-0.7.beta7
- Add workaround for ruby-gnome2-Bugs-2865895

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0-0.6.beta7
- F-12: Mass rebuild

* Sun Mar 29 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0-0.5.beta7
- Remove previous modification for bindtextdomain()
  Fixed on rubygem-gettext side (rubygem-gettext bug 24947, GNOME bug 576826)

* Thu Mar 26 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0-0.4.beta7
- 1.0 beta 7
- Fix arguments of bindtextdomain() for ruby(gettext) 2.0.0

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0-0.3.beta6
- GTK icon cache updating script update

* Wed Sep 10 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0-0.2.beta6
- 1.0 beta6

* Sun Jan 20 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0-0.1.beta5
- Initial packaging


