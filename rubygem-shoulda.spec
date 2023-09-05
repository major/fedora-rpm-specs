# Generated from shoulda-3.5.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name shoulda

Name: rubygem-%{gem_name}
Version: 4.0.0
Release: 1%{?dist}
Summary: Making tests easy on the fingers and eyes
License: MIT
URL: https://github.com/thoughtbot/shoulda
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch

%description
Making tests easy on the fingers and eyes.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%gemspec_remove_dep -g shoulda-matchers '~> 4.0'
%gemspec_add_dep -g shoulda-matchers ['>= 4.0', '< 6']

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
# We don't have available snow globe gem, which is required for Rails related
# test cases. Unfortunately, that leaves nothing to test :'(
mv test/acceptance/integrates_with_rails_test.rb{,.disable}

ruby -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Appraisals
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/gemfiles
%{gem_instdir}/script
%{gem_instdir}/shoulda.gemspec
%{gem_instdir}/test

%changelog
* Mon Sep 04 2023 Vít Ondruch <vondruch@redhat.com> - 4.0.0-1
- Update to Shoulda 4.0.0.
  Resolves: rhbz#1846902

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 24 2022 Vít Ondruch <vondruch@redhat.com> - 3.6.0-12
- Fix RoR 7+ compatibility.
  Resolves: rhbz#2113708
- Relax shoulda-matchers dependency.
  Related: rhbz#1980995

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 17 2021 Vít Ondruch <vondruch@redhat.com> - 3.6.0-8
- Adjust test for Rails 6+ compatibility.
  Resolves: rhbz#1923648

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Vít Ondruch <vondruch@redhat.com> - 3.6.0-5
- Remove minitest-reporters dependency.

* Fri Nov 08 2019 Vít Ondruch <vondruch@redhat.com> - 3.6.0-4
- Relax shoulda-matchers dependency.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 19 2018 Vít Ondruch <vondruch@redhat.com> - 3.6.0-1
- Update to Shoulda 3.6.0.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 26 2014 Vít Ondruch <vondruch@redhat.com> - 3.5.0-1
- Update to Shoulda 3.5.0.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 08 2013 Vít Ondruch <vondruch@redhat.com> - 2.11.3-7
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 02 2012 Vít Ondruch <vondruch@redhat.com> - 2.11.3-4
- Rebuilt for Ruby 1.9.3.

* Sun Jan 08 2012 <stahnma@fedoraproject.org> - 2.11.3-2
- Jumped in to help with FTBFS bz#715949

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 01 2010 Michael Stahnke <stahnma@fedoraproject.org> - 2.11.3-1
- New version
- Fix many broken tests 
- Split into -doc package

* Sat Jan  9 2010 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 2.10.2-2
- Fix BuildRequires
- First package
