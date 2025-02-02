# Generated from shoulda-matchers-2.6.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name shoulda-matchers

Name: rubygem-%{gem_name}
Version: 5.1.0
Release: 11%{?dist}
Summary: Simple one-liner tests for common Rails functionality
License: MIT
URL: https://matchers.shoulda.io/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/thoughtbot/shoulda-matchers.git && cd shoulda-matchers
# git archive -v -o shoulda-matchers-5.1.0-specs.tar.gz v5.1.0 spec/
Source1: %{gem_name}-%{version}-specs.tar.gz
# Fix bootsnap removal which is not enclosed in quotes.
# https://github.com/thoughtbot/shoulda-matchers/pull/1478
Patch0: rubygem-shoulda-matchers-5.1.0-Skip-bootsnap-on-the-test-project-creation.patch

# Fix RoR 7+ compatibility.
# https://github.com/thoughtbot/shoulda-matchers/pull/1485
Patch1: rubygem-shoulda-matchers-5.1.0-Only-mark-classes-as-unloadable-when-Rails-supports-it.patch
Patch2: rubygem-shoulda-matchers-5.1.0-conditionally-use-unloadable-in-another-spot.patch
Patch3: rubygem-shoulda-matchers-5.1.0-Use-a-hard-coded-DateTime-instead-of-DateTime.now-1.patch
Patch4: rubygem-shoulda-matchers-5.1.0-Address-differences-in-has_secure_password-in-Rails-7.patch
Patch5: rubygem-shoulda-matchers-5.1.0-Address-differences-in-has_secure_password-in-Rails-7-test.patch

# Don't try to connect to rubygems.org.
# https://github.com/thoughtbot/shoulda-matchers/pull/1504
Patch6: rubygem-shoulda-matchers-5.1.0-Using-local-gems-should-be-enough-for-testing.patch

# Use sqlite3 1.4 unconditionally.
# https://github.com/thoughtbot/shoulda-matchers/pull/1484/commits/7656cdf9abb4a0f7c4fd4cb9c971e474bfc0f9ee
Patch7: rubygem-shoulda-matchers-5.1.0-Always-use-sqlite-1.4.patch

# catch ruby3.3 format NoMethodError message
# https://github.com/thoughtbot/shoulda-matchers/pull/1579
Patch8: rubygem-shoulda-matchers-pr1579-ruby33-NoMethodError-msg.patch

# It seems ruby3.3.0dev needs the following patch:
# https://github.com/thoughtbot/shoulda-matchers/pull/1506/commits/6a0b3128bdedc7445c444c784275572170a42a62
Patch9: rubygem-shoulda-matchers-pr1506-action_text_rich_texts.patch

# Fix for Ruby 3.1 `Psych::BadAlias: Unknown alias: default
# https://github.com/thoughtbot/shoulda-matchers/pull/1506/commits/a4b25f8702e054b160a876af3dc1cb378c5a8670
Patch10: rubygem-shoulda-matchers-pr1506-psych-load.patch

# Fix Ruby 3.4 compatibility due to backticks and Hash#inspect changes.
# https://github.com/thoughtbot/shoulda-matchers/pull/1657
Patch11: rubygem-shoulda-matchers-6.4.0-Add-Ruby-3.4-support.patch
Patch12: rubygem-shoulda-matchers-6.4.0-Add-Ruby-3.4-support-spec.patch

# Support rspec-rails 7.1
# behavior changed on:
# https://github.com/rspec/rspec-rails/commit/efca5295a196d74c187ebd0349abd10903c68928
Patch13: rubygem-shoulda-matchers-5.1.0-support-rspec-rails-7_1.patch

# Enable sqlite3 2.x+
# https://github.com/thoughtbot/shoulda-matchers/pull/1661
Patch14: rubygem-shoulda-matchers-6.4.0-Enable-sqlite3-2-x-.patch

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(bcrypt)
BuildRequires: rubygem(jbuilder)
BuildRequires: rubygem(puma)
BuildRequires: rubygem(rails)
BuildRequires: rubygem(rails-controller-testing)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(rspec-rails)
BuildRequires: rubygem(shoulda-context)
BuildRequires: rubygem(spring)
BuildRequires: rubygem(sqlite3)
BuildArch: noarch

%description
Shoulda Matchers provides RSpec- and Minitest-compatible one-liners to test
common Rails functionality that, if written by hand, would be much longer,
more complex, and error-prone.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1

%patch 4 -p1
%patch 8 -p1
%patch 11 -p1

pushd %{builddir}
%patch 0 -p1
%patch 1 -p1
%patch 2 -p1
%patch 3 -p1
%patch 5 -p1
%patch 6 -p1
%patch 7 -p1
%patch 9 -p1
%patch 10 -p1
%patch 12 -p1
%patch 13 -p1
%patch 14 -p1
popd

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
ln -s %{_builddir}/spec spec

# It is easier to recreate the Gemfile to use local versions of gems.
cat << GF > Gemfile
source 'https://rubygems.org'

gem 'actiontext'
gem 'bcrypt'
gem 'rails'
gem 'rails-controller-testing'
gem 'rspec'
gem 'rspec-rails'
gem 'sqlite3'
gem 'spring'
GF

# Pry is useless for our purposes.
sed -i "/require 'pry/ s/^/#/" spec/spec_helper.rb

# Avoid Appraisal and Bundler.
sed -i "/current_bundle/ s/^/#/" \
  spec/acceptance_spec_helper.rb \
  spec/support/unit/load_environment.rb
sed -i "/CurrentBundle/ s/^/#/" \
  spec/acceptance_spec_helper.rb \
  spec/support/unit/load_environment.rb

# Avoid git and sprockets dependencies.
sed -i '/def rails_new_command/,/^    end$/ {
  /rails new/ s/"$/ --skip-git --skip-asset-pipeline&/
}' \
  spec/support/unit/rails_application.rb

sed -i '/def rails_new_command/,/^    end$/ {
  /rails new/ s/"$/ --skip-git --skip-asset-pipeline&/
}' \
  spec/support/acceptance/helpers/step_helpers.rb

bundle exec rspec spec/unit

# spring-commands-rspec is not in Fedora yet, but the test suite looks to pass
# without it just fine. However, spring dependency has to be added into Gemfile.
sed -i "/add_gem 'spring-commands-rspec'/ s/^/#/" spec/support/acceptance/helpers/step_helpers.rb
sed -i "/updating_bundle do |bundle|/a \\
        bundle.add_gem 'spring'" spec/support/acceptance/helpers/step_helpers.rb

# Remove excesive test dependencies.
sed -i "/updating_bundle do |bundle|/a \\
        bundle.remove_gem 'capybara'" spec/support/acceptance/helpers/step_helpers.rb
sed -i "/updating_bundle do |bundle|/a \\
        bundle.remove_gem 'selenium-webdriver'" spec/support/acceptance/helpers/step_helpers.rb
# `debug` gem is part of bundled gems, but we are missing IRB dependency ATM:
# https://bugzilla.redhat.com/show_bug.cgi?id=2120562
sed -i "/updating_bundle do |bundle|/a \\
        bundle.remove_gem 'debug'" spec/support/acceptance/helpers/step_helpers.rb

# Drop version such as `ruby "3.4.0"` from Gemfile. This might be problematic
# with Ruby prerelease versions, failing tests with messages such as:
# `Your Ruby version is 3.4.0.dev, but your Gemfile specified 3.4.0 (Bundler::RubyVersionMismatch)`
# BTW the Ruby version was (temporarily 🤷) dropped from Rails template:
# https://github.com/rails/rails/pull/50914
sed -i "/updating_bundle do |bundle|/a \\
        bundle.updating { fs.comment_lines_matching('Gemfile', /^ *ruby (\"|')#{RUBY_VERSION}\\\1/) }" \
  spec/support/acceptance/helpers/step_helpers.rb

bundle exec rspec spec/acceptance

popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/docs
%{gem_instdir}/shoulda-matchers.gemspec

%changelog
* Thu Jan 30 2025 Vít Ondruch <vondruch@redhat.com> - 5.1.0-11
- Enable sqlite3 2.x+

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 01 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.1.0-9
- Support rspec-rails 7.1 on testsuite

* Thu Dec 05 2024 Vít Ondruch <vondruch@redhat.com> - 5.1.0-8
- Fix Ruby 3.4 compatibility due to backticks and Hash#inspect changes.

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 19 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.1.0-5
- Use upstream patch for ruby3.1+ Psych::BadAlias: Unknown alias: default issue
- Backport upstream patch for RoR 7.0 support which seems to be needed
  for ruby3.3.0dev

* Sun Nov  5 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.1.0-4
- Apply upstream PR for ruby3.3 NoMethodError message change

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 11 2022 Vít Ondruch <vondruch@redhat.com> - 5.1.0-1
- Update to should-matchers 5.1.0.
  Resolves: rhbz#1980995
  Resolves: rhbz#2113709

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 09 2021 Vít Ondruch <vondruch@redhat.com> - 4.5.1-1
- Update to should-matchers 4.5.1.
  Resolves: rhbz#1789238
  Resolves: rhbz#1923698

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Vít Ondruch <vondruch@redhat.com> - 4.1.2-5
- Fix RSpec 3.9+ compatibility.
  Resolves: rhbz#1800038
  Resolves: rhbz#1863734
- Fix Rails 6.0+ compatibility.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Vít Ondruch <vondruch@redhat.com> - 4.1.2-2
- Remove unnecessary BR: rubygem(minitest-reporters).

* Thu Nov 07 2019 Vít Ondruch <vondruch@redhat.com> - 4.1.2-1
- Update to should-matchers 4.1.2.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 11 2018 Vít Ondruch <vondruch@redhat.com> - 3.1.2-1
- Update to should-matchers 3.1.2.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 26 2015 Vít Ondruch <vondruch@redhat.com> - 2.8.0-1
- Update to should-matchers 2.8.0.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jul 07 2014 Vít Ondruch <vondruch@redhat.com> - 2.6.1-3
- Workaround RoR 4.1.2+ compatibility issue.
- Relax Rake dependency.

* Thu Jul 03 2014 Vít Ondruch <vondruch@redhat.com> - 2.6.1-2
- Add missing BR: rubygem(shoulda-context).
- Updated upstream URL.
- Relaxed BR: ruby dependency.

* Mon Jun 30 2014 Vít Ondruch <vondruch@redhat.com> - 2.6.1-1
- Initial package
