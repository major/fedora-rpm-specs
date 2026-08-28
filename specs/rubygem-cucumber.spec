%global gem_name cucumber

Name: rubygem-%{gem_name}
Version: 11.1.1
Release: 1%{?dist}
Summary: Tool to execute plain-text documents as functional tests
License: MIT
URL: https://cucumber.io/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/cucumber/cucumber-ruby.git && cd cucumber-ruby
# git archive -v -o rubygem-cucumber-11.1.1-spec.tar.gz v11.1.1 spec/ compatibility/support/cucumber/compatibility_kit/helpers.rb cucumber.yml
Source1: %{name}-%{version}-spec.tar.gz
# git clone https://github.com/cucumber/cucumber-ruby.git && cd cucumber-ruby
# git archive -v -o rubygem-cucumber-11.1.1-features.tar.gz v11.1.1 features/
Source2: %{name}-%{version}-features.tar.gz
# This is just stub file, until the rubygem-cucumber-ci-environment package
# is in Fedora.
# https://raw.githubusercontent.com/cucumber/ci-environment/refs/heads/main/ruby/lib/cucumber/ci_environment.rb
Source3: ci_environment.rb
# Remove the HTML formatter bits until `html-formatter` is available in Fedora
# https://github.com/cucumber/html-formatter
Patch0: rubygem-cucumber-11.1.1-Drop-HTML-formatter.patch
# Provide compotibility with cucumber-core < 16
Patch1: rubygem-cucumber-11.1.1-Compatibility-shim-for-cucumber-core-16.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(base64)
BuildRequires: rubygem(builder)
BuildRequires: rubygem(cucumber-core)
BuildRequires: rubygem(cucumber-cucumber-expressions)
BuildRequires: rubygem(cucumber-messages)
BuildRequires: rubygem(multi_test)
BuildRequires: rubygem(mini_mime)
BuildRequires: rubygem(webrick)
BuildRequires: rubygem(nokogiri)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(rake)
BuildRequires: rubygem(sys-uname)
BuildArch: noarch

%description
Cucumber lets software development teams describe how software should behave
in plain text. The text is written in a business-readable domain-specific
language and serves as documentation, automated tests and development-aid.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1 -b 2

%patch 0 -p1
%patch 1 -p1

# This restores compatiblity with older cucumber-core, prior keyword arguments
# were introduced cucumber-core 13+:
# https://github.com/cucumber/cucumber-ruby-core/pull/261/changes/bc7174d641860267495f48d09a6e400cf2988738
# https://github.com/cucumber/cucumber-ruby/pull/1751
for i in lib/cucumber/{runtime,formatter/{console_issues,fail_fast,junit,pretty,rerun}}.rb; do
  echo $i; sed -i 's/strict: //' $i
done

# The rubygem-cucumber-html-formatter is currently not packaged in Fedora.
%gemspec_remove_dep -g cucumber-html-formatter
%gemspec_remove_file 'lib/cucumber/formatter/html.rb'

# TODO: The rubygem-cucumber-ci-environment is currently not available in
# Fedora. This is the new name for rubygem-cucumber-create-meta. Fake the
# required bits for a moment.
%gemspec_remove_dep -g cucumber-ci-environment
%gemspec_add_file 'lib/cucumber/ci_environment.rb'
install -m 0644 %{SOURCE3} lib/cucumber/ci_environment.rb

# Relax requires.
%gemspec_remove_dep -g cucumber-core ">= 16.2.0", "< 17"
%gemspec_add_dep -g cucumber-core

%gemspec_remove_dep -g multi_test "~> 1.1"
%gemspec_add_dep -g multi_test

%gemspec_remove_dep -g sys-uname "~> 1.5"
%gemspec_add_dep -g sys-uname

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


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
ln -s %{builddir}/compatibility compatibility

# Cucumber.yml is needed for both test suites.
# Used as fixture for rspec and options for cucumber.
ln -s %{builddir}/cucumber.yml cucumber.yml

ln -s %{builddir}/spec spec

rspec -Ilib -rspec_helper spec

ln -s %{builddir}/features features

# Skip the test that requires rubygem-cucumber-html-formatter,
# which is currently not packaged in Fedora.
sed -i -e '/^  Scenario: output html to stdout$/i @skip' \
    features/docs/formatters/html.feature

# With cucumber-core < 16.2, ambiguous test might cause crash. However, for
# test suites which have passed their CI, this should not cause any troubles.
# Therefore this might minor issue for development, but should not be an issue
# for Fedora packages.
# https://github.com/cucumber/cucumber-ruby-core/pull/311
mv features/docs/defining_steps/ambiguous_steps.feature{,.disable}

# Use RUBYOPT to make sure that the Cucumber from current directory has
# precedence over system Cucumber, which is pulled in as Aruba dependency.
RUBYOPT=-Ilib ./bin/cucumber --tags 'not @skip'
popd

%files
%dir %{gem_instdir}
%{_bindir}/cucumber
%license %{gem_instdir}/LICENSE
%{gem_instdir}/VERSION
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Mon Aug 17 2026 Vít Ondruch <vondruch@redhat.com> - 11.1.1-1
- Update to Cucumber 11.1.1.
  Resolves: rhbz#2088458

* Tue Aug 11 2026 Vít Ondruch <vondruch@redhat.com> - 7.1.0-19
- Relax cucumber-wire dependency.

* Fri Aug 07 2026 Vít Ondruch <vondruch@redhat.com> - 7.1.0-18
- Relax cucumber-core dependency.

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Wed Apr 22 2026 Vít Ondruch <vondruch@redhat.com> - 7.1.0-16
- Fix compatibility with Cucumber Messages 25.0.0+

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 03 2025 Vít Ondruch <vondruch@redhat.com> - 7.1.0-12
- Fix Ruby 3.4 backtrace and Hash#inspect formatting compatibility.

* Thu Nov 28 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 7.1.0-11
- Add base64 dependency explicitly for ruby34

* Fri Nov 01 2024 Vít Ondruch <vondruch@redhat.com> - 7.1.0-10
- Fix Ruby 3.4 compatibility due to `Hash.new` now accepting `:capacity`
  keyword option.

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jan 30 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 7.1.0-3
- BR: rubygem(rake) due to recent rubygem(rspec-core) dependency change

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 27 2021 Jarek Prokop <jprokop@redhat.com> - 7.1.0-1
- Update to cucumber 7.1.0.

* Mon Sep 06 2021 Pavel Valena <pvalena@redhat.com> - 7.0.0-1
- Update to cucumber 7.0.0.
  Resolves: rhbz#1842885

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Vít Ondruch <vondruch@redhat.com> - 3.1.2-5
- Properly filter Ruby StdLib locations from backtrace.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 14 2018 Vít Ondruch <vondruch@redhat.com> - 3.1.2-3
- Remove step argument test case to tix FTBFS.

* Fri Sep 07 2018 Vít Ondruch <vondruch@redhat.com> - 3.1.2-2
- Fix wire protocol.

* Thu Aug 23 2018 Jaroslav Prokop <jar.prokop@volny.cz> - 3.1.2-1
- Update to Cucumber 3.1.2.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Vít Ondruch <vondruch@redhat.com> - 2.4.0-1
- Update to Cucumber 2.4.0.

* Thu Nov 24 2016 Vít Ondruch <vondruch@redhat.com> - 2.3.3-2
- Fix FTBFS.

* Tue Apr 05 2016 Vít Ondruch <vondruch@redhat.com> - 2.3.3-1
- Update to Cucumber 2.3.3.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.18-1
- 1.3.18
  ref: https://github.com/cucumber/cucumber/issues/781

* Wed Jun 18 2014 Josef Stribny <jstribny@redhat.com> - 1.3.15-1
- Update to cucumber 1.3.15

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 23 2013 Vít Ondruch <vondruch@redhat.com> - 1.2.1-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Drop useless build requires.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Mo Morsi <mmorsi@redhat.com> - 1.2.1-1
- Update cucumber to version 1.2.1

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 27 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.1.9-1
- Update cucumber to version 1.1.9

* Wed Feb 01 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.1-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 12 2011 Mo Morsi <mmorsi@redhat.com> - 1.0.1-1
- update to latest upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Michal Fojtik <mfojtik@redhat.com> - 0.10.0-1
- Version bump

* Mon Sep 27 2010 Michal Fojtik <mfojtik@redhat.com> - 0.9.0-4
- Fixed JSON version again

* Fri Sep 24 2010 Michal Fojtik <mfojtik@redhat.com> - 0.9.0-3
- Fixed JSON version

* Fri Sep 24 2010 Michal Fojtik <mfojtik@redhat.com> - 0.9.0-2
- Fixed gherkin version in dependency list

* Fri Sep 24 2010 Michal Fojtik <mfojtik@redhat.com> - 0.9.0-1
- Version bump to match upstream
- Fixed dependency issue with new gherkin package

* Wed Aug 04 2010 Michal Fojtik <mfojtik@redhat.com> - 0.8.3-4
- Fixed JSON version

* Wed Aug 04 2010 Michal Fojtik <mfojtik@redhat.com> - 0.8.3-3
- Removed JSON patch (JSON updated in Fedora)

* Sun Aug 01 2010 Michal Fojtik <mfojtik@redhat.com> - 0.8.3-2
- Patched Rakefile and replaced rspec beta version dependency
- Patched Rakefile and downgraded JSON dependency

* Wed Jun 30 2010 Michal Fojtik <mfojtik@redhat.com> - 0.8.3-1
- Newer release

* Sun Oct 18 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.4.2-1
- Newer release

* Mon Oct 12 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.4.0-1
- Newer release

* Fri Jun 26 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.3.10-3
- Get rid of duplicate files (thanks to Mamoru Tasaka)

* Mon Jun 08 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.3.10-2
- Use geminstdir macro where appropriate
- Do not move examples around
- Depend on ruby(abi)
- Replace defines with globals

* Fri Jun 05 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.3.10-1
- Package generated by gem2rpm
- Move examples into documentation
- Remove empty files
- Fix up License
