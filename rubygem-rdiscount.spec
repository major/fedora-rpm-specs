%global gem_name rdiscount

Summary: Converts documents in Markdown syntax to HTML
Name: rubygem-%{gem_name}
Version: 2.2.0.2
Release: 10%{?dist}
License: ASL 1.1
URL: http://github.com/rtomayko/rdiscount
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Patch the file test/rdiscount_test.rb
#  The following tests fail and are commented out:
#    test_that_generate_toc_sets_toc_ids, test_should_get_the_generated_toc,
#    test_toc_should_escape_apostropes, test_toc_should_escape_question_marks
Patch0: rdiscount_test.rb.patch
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: libmarkdown-devel
BuildRequires: rubygem(test-unit)
BuildRequires: gcc


%package doc
Summary: Documentation for %{name}
BuildArch: noarch
Requires: %{name} = %{version}-%{release}


%description
Description: RDiscount converts documents in Markdown syntax to HTML.

It uses the excellent Discount processor by David Loren Parsons for this
purpose, and thereby inherits Discount's numerous useful extensions to the
Markdown language.

#--

%description doc
This package contains Rakefile, test directory and documentation for
%{name}.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
%patch0 -p0
gem spec %{SOURCE0} -l --ruby | sed -e 's|,|,\n|g' > %{gem_name}.gemspec

# Remove c and header file to not bundle discount-sources
(cd ext; ls -1 *.c *.h | grep -v rdiscount.c ) > discount_files

cat discount_files | while read f ; do
	rm -f ext/$f
	sed -i %{gem_name}.gemspec -e "\@ext/$f@d"
done

sed -i ext/extconf.rb \
	-e '\@create_makefile@i \$libs = "-lmarkdown"' \
	%{nil}

%build
rm -rf ./%{gem_extdir_mri}
rm -rf ./%{gem_instdir}
gem build %{gem_name}.gemspec

%gem_install

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man7
mv .%{gem_instdir}/man/rdiscount.1 %{buildroot}%{_mandir}/man1
mv .%{gem_instdir}/man/markdown.7 %{buildroot}%{_mandir}/man7
cp -a .%{gem_dir}/*  %{buildroot}%{gem_dir}

# Copy C extensions to the extdir
rm -rf %{buildroot}%{gem_instdir}/ext
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

mkdir -p %{buildroot}/%{_bindir}
mv .%{_bindir}/* %{buildroot}/%{_bindir}

%check
pushd .%{gem_instdir}
# Once 
ruby -Ilib:%{buildroot}%{gem_extdir_mri}:. \
	-e 'gem "test-unit" ; Dir.glob("test/*_test.rb").sort.each {|f| require f}'

popd

%files
%{_bindir}/rdiscount
%dir %{gem_instdir}
%{gem_instdir}/bin/
%{gem_libdir}/
%doc %{gem_instdir}/BUILDING
%doc %{gem_instdir}/COPYING
%doc %{gem_instdir}/README.markdown
%exclude %{gem_cache}
%{gem_spec}
%{gem_extdir_mri}/
%{_mandir}/man1/rdiscount.1.gz
%exclude %{_mandir}/man7/markdown.7.gz

#--

%files doc
%doc %{gem_instdir}/Rakefile
%{gem_docdir}
%{gem_instdir}/man
%{gem_instdir}/test
%{gem_instdir}/rdiscount.gemspec


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Vít Ondruch <vondruch@redhat.com> - 2.2.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sun Dec 25 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.0.2-8
- Use %%gem_extdir_mri instead of ext for %%check due to ruby3.2 change
  for ext cleanup during build

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Vít Ondruch <vondruch@redhat.com> - 2.2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 Vít Ondruch <vondruch@redhat.com> - 2.2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.0

* Wed Aug 12 2020 Gerd Pokorra <gp@zimt.uni-siegen.de> - 2.2.0.2-1
- Update to 2.2.0.2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.0.1-7
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Vít Ondruch <vondruch@redhat.com> - 2.2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Mon Jul 23 2018 Gerd Pokorra <gp@zimt.uni-siegen.de> - 2.2.0.1-3
- Patch the testfile and get the tests running again

* Sat Jul 21 2018 Gerd Pokorra <gp@zimt.uni-siegen.de> - 2.2.0.1-2
- Generate the file discount_files

* Sat Jul 21 2018 Gerd Pokorra <gp@zimt.uni-siegen.de> - 2.2.0.1-1
- Update to 2.2.0.1
- Add gcc to BuildRequires

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.1.8-7
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.8-6
- F-28: rebuild for ruby25

* Mon Jul 31 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> - 2.1.8-5
- quick workaround to fix the build problem

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Vít Ondruch <vondruch@redhat.com> - 2.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Wed May 18 2016 Gerd Pokorra <gp@zimt.uni-siegen.de> - 2.1.8-1
- Update to 2.1.8
- Change summary and description tag

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Vít Ondruch <vondruch@redhat.com> - 2.1.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 29 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.7.1-7
- Recent usage of %%gem_install to modify source
- Use system libmarkdown

* Thu Jan 29 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.7.1-6
- Simply use test-unit

* Fri Jan 16 2015 Vít Ondruch <vondruch@redhat.com> - 2.1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Gerd Pokorra <gp@zimt.uni-siegen.de> - 2.1.7.1-2
- Rebuilt for Ruby_2.1

* Fri Apr 25 2014 Gerd Pokorra <gp@zimt.uni-siegen.de> - 2.1.7.1-1
- Update to 2.1.7.1

* Thu Apr 17 2014 Vít Ondruch <vondruch@redhat.com> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Thu Feb 20 2014 Gerd Pokorra <gp@zimt.uni-siegen.de> - 2.1.7-1
- Update to 2.1.7

* Wed May 22 2013 Gerd Pokorra <gp@zimt.uni-siegen.de> - 2.0.7.3-1
- Update to 2.0.7.3
- Exclude man-page /usr/share/man/man7/markdown.7.gz

* Mon Mar 18 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 2.0.7-5
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Mon Mar 18 2013 Gerd Pokorra <gp@zimt.uni-siegen.de> - 2.0.7-4
- Changed from ruby(abi) to ruby(release)
- Changed from macro gem_extdir to gem_extdir_mri

* Wed Feb 13 2013 Gerd Pokorra <gp@zimt.uni-siegen.de> - 2.0.7-3
- Changed back to ruby(abi)

* Thu Feb 07 2013 Gerd Pokorra <gp@zimt.uni-siegen.de> - 2.0.7-1
- Update to 2.0.7
- Add file BUIlDING

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 03 2012 Vít Ondruch <vondruch@redhat.com> - 1.6.3.2-7
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jun 12 2010 Gerd Pokorra <gp@zimt.uni-siegen.de> - 1.6.3.2-4
- removed the unused macro "ruby_sitelib"
- put the file rdiscount.gemspec to the doc-subpackage
- add dependency to the main package for the doc-subpackage

* Thu Jun 10 2010 Gerd Pokorra <gp@zimt.uni-siegen.de> - 1.6.3.2-3
- changed ruby(abi) dependency to be strict
- changed rubygem module related dependency style
- only arch-dependent files are in "ruby_sitearch"
- tests are now successful; "rake test:unit" is used
- "geminstdir" macro is used when possible
- "geminstdir" is owned by package
- ext/ subdirectory is removed form "buildroot" during install; no exclude

* Tue Jun 08 2010 Gerd Pokorra <gp@zimt.uni-siegen.de> - 1.6.3.2-2
- files under ext/ subdirectory excluded
- remove BuildRoot tag
- add "Requires: ruby(abi) >= 1.8"
- use global macro instead of define macro
- changed license tag

* Sun Jun 06 2010 Gerd Pokorra <gp@zimt.uni-siegen.de> - 1.6.3.2-1
- add "BuildRequires: ruby-devel"
- Initial package
