# Generated from activeresource-2.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name activeresource

Name: rubygem-%{gem_name}
Epoch: 1
Version: 6.0.0
Release: 3%{?dist}
Summary: REST modeling framework (part of Rails)
License: MIT
URL: http://www.rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rails/activeresource.git && cd rails/activeresource
# git archive -v -o activeresource-6.0.0-tests.tar.gz v6.0.0 test/
Source1: %{gem_name}-%{version}-tests.tar.gz
# Let's keep Requires and BuildRequires sorted alphabeticaly
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(activemodel) >= 5.0
BuildRequires: rubygem(activesupport) >= 5.0
BuildRequires: rubygem(activemodel-serializers-xml)
BuildRequires: rubygem(activejob)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(rexml)
BuildArch: noarch

%description
REST on Rails. Wrap your RESTful web app with Ruby classes and work with them
like Active Record models.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/



%check
pushd .%{gem_instdir}
# Move the tests into place
ln -s %{_builddir}/test test

# Bundler just complicates everything.
sed -i "/bundler/ s/^/#/" test/abstract_unit.rb

# The test suite is not stable. E.g. running test/cases/authorization_test.rb
# independently raises `NameError: uninitialized constant Base64`.
# https://github.com/rails/activeresource/issues/388
ruby -Ilib:test -rbase64 -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Wed Aug 31 2022 Vít Ondruch <vondruch@redhat.com> - 1:6.0.0-3
- Make the build more stable.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 17 2022 Vít Ondruch <vondruch@redhat.com> - 1:6.0.0-1
- Update to ActiveResource 6.0.0.
  Resolves: rhbz#2039043
  Resolves: rhbz#2055058

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Vít Ondruch <vondruch@redhat.com> - 1:5.1.1-2
- Add `BR: rubygem(rexml)` which is required for Ruby 3.0 compatibility.

* Tue Sep 01 2020 Vít Ondruch <vondruch@redhat.com> - 5.1.1-1
- Update to ActiveResource 5.1.1.
  Resolves: rhbz#1831913
  Resolves: rhbz#1871618

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 01 2017 Vít Ondruch <vondruch@redhat.com> - 1:5.0.0-1
- Update to ActiveResource 5.0.0.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.0-0.1.20160809gitf8abaf1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 11 2016 Vít Ondruch <vondruch@redhat.com> - 1:5.0.0-0.1.20160809gitf8abaf1
- Update to ActiveResource 5.0.0 snapshot.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 14 2015 Vít Ondruch <vondruch@redhat.com> - 1:4.0.0-7
- Return back the missing epoch from require.

* Wed Jul 08 2015 Vít Ondruch <vondruch@redhat.com> - 1:4.0.0-6
- Requires and Provides are autogenerated now.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 10 2014 Josef Stribny <jstribny@redhat.com> - 1:4.0.0-4
- Stabilize test suite

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Nov 21 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.0-2
- Adjust deps

* Tue Jul 30 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.0-1
- Update to ActiveResource 4.0.0.

* Tue Mar 19 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.13-1
- Update to ActiveResource 3.2.13.

* Mon Mar 04 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.12-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Tue Feb 12 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.12-1
- Update to ActiveResource 3.2.12.

* Wed Jan 09 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.11-1
- Update to ActiveResource 3.2.11.

* Thu Jan 03 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.10-1
- Update to ActiveResource 3.2.10.

* Mon Aug 13 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.2.8-1
- Update to ActiveResource 3.2.8.

* Mon Jul 30 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.2.7-1
- Update to ActiveResource 3.2.7.

* Tue Jul 24 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.2.6-2
- Fixed missing epoch in -doc subpackage.

* Thu Jul 19 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.2.6-1
- Update to ActiveResource 3.2.6.
- Removed no longer needed BuildRoot tag.
- Run tests without Rake.
- Introduce -doc subpackage.

* Fri Jun 15 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.0.15-1
- Update to ActiveResource 3.0.15.

* Fri Jun 01 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.0.13-1
- Update to ActiveResource 3.0.13.

* Wed Jan 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.0.11-1
- Rebuilt for Ruby 1.9.3.
- Update to ActiveResource 3.0.11

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 22 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.10-1
- Update to ActiveResource 3.0.10

* Thu Jul 07 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.9-1
- Update to ActiveResource 3.0.9

* Mon Mar 28 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.5-1
- Updated to ActiveResource 3.0.5

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 10 2011 Mohammed Morsi <mmorsi@redhat.com> - 1:3.0.3-1
- Update to rails 3

* Mon Aug 09 2010 Mohammed Morsi <mmorsi@redhat.com> - 1:2.3.8-1
- Update to 2.3.8

* Thu Jan 28 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1:2.3.5-1
- Update to 2.3.5

* Wed Oct  7 2009 David Lutterkort <lutter@redhat.com> - 1:2.3.4-2
- Bump Epoch to ensure upgrade path from F-11

* Fri Sep 18 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.3.4-1
- Update to 2.3.4
- Enable test

* Sun Jul 26 2009 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 2.3.3-1
- New upstream version

* Mon Mar 16 2009 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 2.3.2-1
- New upstream version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 23 2008 David Lutterkort <lutter@redhat.com> - 2.2.2-1
- New version

* Tue Sep 16 2008 David Lutterkort <dlutter@redhat.com> - 2.1.1-1
- New version (fixes CVE-2008-4094)

* Thu Jul 31 2008 Michael Stahnke <stahnma@fedoraproject.org> - 2.1.0-1
- New Upstream

* Tue Apr  8 2008 David Lutterkort <dlutter@redhat.com> - 2.0.2-2
- Fix dependency

* Mon Apr 07 2008 David Lutterkort <dlutter@redhat.com> - 2.0.2-1
- New version

* Mon Dec 10 2007 David Lutterkort <dlutter@redhat.com> - 2.0.1-1
- Initial package
