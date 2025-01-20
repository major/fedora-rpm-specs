%global gem_name xmlparser

Summary: Ruby bindings to the Expat XML parsing library
Name: rubygem-%{gem_name}
Version: 0.7.2.1
Release: 46%{?dist}
Group: Development/Languages
# src/lib/xml/xpath.rb is GPLv2+
# src/ext/encoding.h and the functions of encoding map are GPLv2+ or Artistic
# All other files are Ruby or GPLv2+ or MIT
# For a breakdown of the licensing, see also README
License: GPL-2.0-or-later and (  Ruby or GPL-2.0-or-later or MIT ) and (  GPL-1.0-or-later OR Artistic-1.0-Perl )
URL: http://rubygems.org/gems/xmlparser
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
# Handle 'format not a string literal and no format arguments' error.
# https://bugzilla.redhat.com/show_bug.cgi?id=1037312
# Thanks to Gregor Herrmann for the patch.
# https://www.mail-archive.com/debian-bugs-rc@lists.debian.org/msg297233.html
Patch0: rubygem-xmlparser-ftbfs-fix.patch
Patch1: rubygem-xmlparser-enc_to_encindex-fix.patch
Patch2: rubygem-xmlparser-c99.patch
BuildRequires: perl
BuildRequires: ruby
BuildRequires: ruby(rubygems)
BuildRequires: ruby(release)
BuildRequires: ruby-devel
BuildRequires: rubygems-devel
BuildRequires: rubygem(rake)
BuildRequires: rubygem(mkrf)
BuildRequires: expat-devel

%description
Ruby bindings to the Expat XML parsing library. 

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
gem build %{gem_name}.gemspec
%gem_install

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -rp .%{gem_dir}/* %{buildroot}%{gem_dir}/

# remove development stuff
rm -rf %{buildroot}%{gem_instdir}/ext

# install externals
mkdir -p %{buildroot}%{gem_extdir_mri}/
cp -a ./%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/


%files
%{gem_extdir_mri}
%dir %{gem_instdir}/
%doc %{gem_instdir}/[A-Z]*
%doc %{gem_docdir}
%{gem_instdir}/[a-z]*
%exclude %{gem_cache}
%{gem_spec}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.1-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 08 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.2.1-45
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.1-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.1-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Florian Weimer <fweimer@redhat.com> - 0.7.2.1-42
- Fix C compatibility issues (#2256626)

* Wed Jan 03 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.2.1-41
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Wed Aug 30 2023 Ulrich Schwickerath - 0.7.2.1-40
- Add patch for undefined symbol as proposed by Antonio Terceiro for Debian

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.7.2.1-20
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.2.1-19
- F-28: rebuild for ruby25

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Vít Ondruch <vondruch@redhat.com> - 0.7.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Vít Ondruch <vondruch@redhat.com> - 0.7.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Vít Ondruch <vondruch@redhat.com> - 0.7.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 10 2014 Josef Stribny <jstribny@redhat.com> - 0.7.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1
- Fix FTBFS if "-Werror=format-security" flag is used (rhbz#1037312).

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 18 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.7.2.1-6
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 26 2012 Ulrich Schwickerath <ulrich.schwickerath@web.de> - 0.7.2.1-3
- sync with updated gem version from rubyforge instead of private copy
- use macros for files section
- cleanup macros in changelog section to make rpmlint happy

* Wed Apr 25 2012 Ulrich Schwickerath <ulrich.schwickerath@web.de> - 0.7.2-2
- use macros following the new gem packaging guidelines for fed17+

* Tue Mar 20 2012 Ulrich Schwickerath <ulrich.schwickerath@web.de> - 0.7.2-1
- spec file patch to support fedora 17+
- update to 0.7.2 from Yoshidam

* Tue Mar 06 2012 Ulrich Schwickerath <ulrich.schwickerath@web.de> - 0.6.81-9
- replace build requirement for ruby-libs by ruby 

* Wed Dec 07 2011 Ulrich Schwickerath <ulrich.schwickerath@web.de> - 0.6.81-8
- remove the link to xmlparser.so and move it to ruby_sitearch

* Wed Dec 07 2011 Ulrich Schwickerath <ulrich.schwickerath@web.de> - 0.6.81-7
- fix for /usr/lib/ruby/gems/1.8/gems/xmlparser-0.6.81 should be owned by the package
- fix installation path for .so files
- add dependency on ruby-libs which owns the ruby_sitearch directory

* Wed Jul 12 2011 Ulrich Schwickerath <ulrich.schwickerath@web.de> - 0.6.81-6
- add more details about licensing

* Wed Jul 12 2011 Ulrich Schwickerath <ulrich.schwickerath@web.de> - 0.6.81-5
- specify
- fix format of changelog
- remove ruby-sitelib

* Tue Jul 11 2011 Ulrich Schwickerath <ulrich.schwickerath@web.de> - 0.6.81-4
- cleaner way to treat SOURCE
- remove explicit dependency on expat
- make globals conditional

* Mon Jul 10 2011 Ulrich Schwickerath <ulrich.schwickerath@web.de> - 0.6.81-3
- fix build problems 

* Sat Jul 08 2011 Ulrich Schwickerath <ulrich.schwickerath@web.de> - 0.6.81-2
- add dependencies

* Wed Jul 06 2011 Ulrich Schwickerath <ulrich.schwickerath@web.de> - 0.6.81-1
- Initial package from gem2rpm

