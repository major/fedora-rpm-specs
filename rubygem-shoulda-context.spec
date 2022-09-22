%global gem_name shoulda-context

Name: rubygem-%{gem_name}
Version: 1.2.2
Release: 12%{?dist}
Summary: Context framework extracted from Shoulda
License: MIT
URL: https://github.com/thoughtbot/shoulda-context
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(jquery-rails)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(rails)
BuildRequires: rubygem(sass-rails)
BuildRequires: rubygem(sqlite3)
BuildRequires: rubygem(test-unit)
BuildArch: noarch

%description
Shoulda's contexts make it easy to write understandable and maintainable
tests for Test::Unit. It's fully compatible with your existing tests in
Test::Unit, and requires no retooling to use.

Refer to the shoulda gem if you want to know more about using shoulda
with Rails or RSpec.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

# Fix wrong-file-end-of-line-encoding for rpmlint
sed -i 's/\r$//' MIT-LICENSE

# Remove /usr/bin/env from shebang so RPM doesn't consider this a dependency
sed -i 's|#!/usr/bin/env ruby|#!/usr/bin/ruby|' bin/convert_to_should_syntax

# Remove zero-length developer-only file
rm test/fake_rails_root/vendor/plugins/.keep
sed -i -r 's|"test/fake_rails_root/vendor/plugins/\.keep"(\.freeze)?,||' %{gem_name}.gemspec


%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
# Remove locks to be able to use system dependencies.
rm gemfiles/*.lock

# Relax mocha and test-unit dependencies.
%gemspec_remove_dep -s shoulda-context.gemspec -g mocha -d '~> 0.9.10'
%gemspec_add_dep -s shoulda-context.gemspec -g mocha -d '~> 1.0'
%gemspec_remove_dep -s shoulda-context.gemspec -g test-unit -d '~> 2.1.0'
%gemspec_add_dep -s shoulda-context.gemspec -g test-unit -d '~> 3.0'

# Get rid of unnecessary dependencies.
%gemspec_remove_dep -s shoulda-context.gemspec -g appraisal -d
%gemspec_remove_dep -s shoulda-context.gemspec -g byebug -d
%gemspec_remove_dep -s shoulda-context.gemspec -g pry -d
%gemspec_remove_dep -s shoulda-context.gemspec -g pry-byebug -d

# Use RoR available in build root.
sed -i '/gem "rails"/ s/, :github=>"rails\/rails", :branch=>"4-1-stable"//' gemfiles/rails_4_1.gemfile

# Fix compatibility with Mocha 1.0+.
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=743071
sed -i "/require 'mocha'/ s/mocha/mocha\/setup/" test/test_helper.rb

BUNDLE_GEMFILE=gemfiles/test_unit.gemfile bundle exec ruby -Itest -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
BUNDLE_GEMFILE=gemfiles/minitest_5_x.gemfile bundle exec ruby -Itest -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
BUNDLE_GEMFILE=gemfiles/rails_4_1.gemfile bundle exec ruby -Itest -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{_bindir}/convert_to_should_syntax
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Appraisals
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/gemfiles
%{gem_instdir}/init.rb
%dir %{gem_instdir}/rails
%{gem_instdir}/rails/init.rb
%{gem_instdir}/Rakefile
# This is not the original file.
%exclude %{gem_instdir}/shoulda-context.gemspec
%{gem_instdir}/tasks
%{gem_instdir}/test

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 20 2017 Vít Ondruch <vondruch@redhat.com> - 1.2.2-1
- Update to shoulda-context 1.2.2.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 26 2015 Vít Ondruch <vondruch@redhat.com> - 1.2.1-2
- Fix test suite compatibility with latest Mocha and RoR.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jul 02 2014 Vít Ondruch <vondruch@redhat.com> - 1.2.1-1
- Update to shoulda-context 1.2.1.

* Tue Nov 05 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.1.6-2
- Update to shoulda-context 1.1.6
- Clean up comments
- Remove unnecessary BR: on ruby
- Exclude developer-only files from binary packages

* Tue Aug 27 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.1.5-1
- Initial package
