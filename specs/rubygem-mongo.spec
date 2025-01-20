%global gem_name mongo
# Disable tests as MongoDB was dropped from Fedora because of a licensing issue.
# https://src.fedoraproject.org/rpms/mongodb/blob/master/f/dead.package
%bcond_with tests

Name: rubygem-%{gem_name}
Version: 2.14.0
Release: 12%{?dist}
Summary: Ruby driver for MongoDB
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: https://docs.mongodb.com/ruby-driver/current/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
%if %{with tests}
# For running the tests
BuildRequires: rubygem(bson) >= 4.8.2
# ffi is an optional runtime dependency.
# https://jira.mongodb.org/browse/RUBY-2465
BuildRequires: rubygem(ffi)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(timecop)
%endif
BuildArch: noarch

%description
A Ruby driver for MongoDB.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

# This is borken symlink, which is not created by the recent RubyGems:
# https://github.com/rubygems/rubygems/issues/5768
# https://jira.mongodb.org/browse/RUBY-2467
%gemspec_remove_file -t 'spec/support/ocsp'
%gemspec_remove_file 'spec/support/ocsp'

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Drop the shebang, file is not executable anyway.
# https://jira.mongodb.org/browse/RUBY-2469
sed -i '/#!\// d' %{buildroot}%{gem_instdir}/Rakefile

%if %{with tests}
%check
pushd .%{gem_instdir}

# Create data directory and start testing mongo instance.
mkdir data
# The enableTestCommands=1 is required.
# https://github.com/mongodb/mongo-ruby-driver/blob/master/spec/README.md#standalone
# https://github.com/mongodb/mongo-ruby-driver/blob/master/spec/README.md#fail-points
mongod \
  --dbpath data \
  --logpath data/log \
  --setParameter enableTestCommands=1 \
  --fork

# timeout-interrupt is not available in Fedora yet.
# timeout-interrupt does not work on glibc >= 2.32.
# https://jira.mongodb.org/projects/RUBY/issues/RUBY-2462
sed -i "/^if SpecConfig\.instance\.mri?$/i\\
require 'timeout'\\
TimeoutInterrupt = Timeout\\
" spec/lite_spec_helper.rb
sed -i "/^if SpecConfig\.instance\.mri?$/,/^end$/ s/^/#/" spec/lite_spec_helper.rb

# rspec-retry is not available in Fedora yet.
sed -i "/require 'rspec\/retry'/ s/^/#/" spec/spec_helper.rb

# ice_nine is not available in Fedora yet.
sed -i "/^autoload :IceNine, 'ice_nine'/ s/^/#/" spec/lite_spec_helper.rb
sed -i "/IceNine\.deep_freeze/ s/^/#/" spec/runners/transactions/test.rb
sed -i "s/IceNine\.deep_freeze(spec)/spec/" spec/runners/crud/operation.rb

# Drop byebug dependency that is not needed to build.
sed -i '/^if \%w(1 true yes)\.include\?/,/^end$/ s/^/#/' spec/lite_spec_helper.rb
sed -i "/autoload :Byebug, 'byebug'/ s/^/#/" spec/support/aws_utils.rb

# rubydns is not available in Fedora yet.
sed -i "/require 'rubydns'/ s/^/#/" spec/support/dns.rb
mv spec/integration/srv_monitoring_spec.rb{,.disabled}
mv spec/integration/srv_spec.rb{,.disabled}
sed -i "/^    context 'in unknown topology' do$/,/^    end$/ s/^/#/" \
  spec/integration/reconnect_spec.rb

# Skip tests using internet.
# https://jira.mongodb.org/browse/RUBY-2468
mv spec/mongo/uri/srv_protocol_spec.rb{,.disabled}

# Creates necessary user accounts in the cluster
# See Rakefile "spec:prepare".
# https://jira.mongodb.org/browse/RUBY-2466
ruby -I lib:spec/shared/lib:spec <<EOR
  require 'mongo'
  require 'support/utils'
  require 'support/spec_setup'
  SpecSetup.new.run
EOR
# Explicitly set rspec format option for a better maintainability,
# as without this, the format option `-f fuubar` requiring the external gem is
# executed on the interactive shell mode.
CI=1 EXTERNAL_DISABLED=1 rspec spec -f p

# Shutdown mongo and cleanup the data.
mongod --shutdown --dbpath data
rm -rf data
popd
%endif

%files
%dir %{gem_instdir}
%{_bindir}/mongo_console
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/mongo.gemspec
%{gem_instdir}/spec

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 2.14.0-11
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 09 2022 Vít Ondruch <vondruch@redhat.com> - 2.14.0-6
- Fix FTBFS caused by RubyGems 3.3.20+.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec  7 16:15:23 CET 2020 Jun Aruga <jaruga@redhat.com> - 2.14.0-1
- Update to mongo 2.14.0.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 04 2020 Jun Aruga <jaruga@redhat.com> - 2.11.3-1
- Update to mongo 2.11.3.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Jun Aruga <jaruga@redhat.com> - 2.11.2-1
- Update to mongo 2.11.2.

* Tue Nov 19 2019 Jun Aruga <jaruga@redhat.com> - 2.11.1-1
- Update to mongo 2.11.1.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 Jun Aruga <jaruga@redhat.com> - 2.8.0-1
- Update to mongo 2.8.0.

* Tue Feb 05 2019 Troy Dawson <tdawson@redhat.com> - 2.6.2-3
- Remove tests because they depended on mongodb
-- https://pagure.io/fesco/issue/2078

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 12 2018 Jun Aruga <jaruga@redhat.com> - 2.6.2-1
- Make tests conditional enableing tests as a default.

* Mon Sep 10 2018 Vít Ondruch <vondruch@redhat.com> - 2.6.2-1
- Update to mongo 2.6.2.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 23 2018 Jun Aruga <jaruga@redhat.com> - 2.5.1-1
- Update to mongo 2.5.1.

* Fri Feb 16 2018 Jun Aruga <jaruga@redhat.com> - 2.5.0-1
- Update to mongo 2.5.0.

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.4.3-2
- Escape macros in %%changelog

* Wed Aug 16 2017 Vít Ondruch <vondruch@redhat.com> - 2.4.3-1
- Update to mongo 2.4.3.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 04 2017 Vít Ondruch <vondruch@redhat.com> - 2.4.1-1
- Update to mongo 2.4.1.

* Thu Dec 15 2016 Vít Ondruch <vondruch@redhat.com> - 2.4.0-1
- Update to mongo 2.4.0.

* Wed Aug 31 2016 Vít Ondruch <vondruch@redhat.com> - 2.3.0-1
- Update to mongo 2.3.0.

* Tue Feb 16 2016 Troy Dawson <tdawson@redhat.com> - 1.10.2-5
- Disable tests until mongodb becomes stable in rawhide again.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 27 2015 Troy Dawson <tdawson@redhat.com> - 1.10.2-2
- Fix tests

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 26 2014 Vít Ondruch <vondruch@redhat.com> - 1.10.2-1
- Update to mongo 1.10.2.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 19 2013 Vít Ondruch <vondruch@redhat.com> - 1.9.2-1
- Update to mongo 1.9.2.
- Enabled test suite.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 13 2013 Troy Dawson <tdawson@redhat.com> - 1.6.4-4
- Fix to make it build/install on F19+

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 10 2012 Troy Dawson <tdawson@redhat.com> - 1.6.4-2
- Fixed doc
- removed more BuildRequires that are not required

* Thu Aug 09 2012 Troy Dawson <tdawson@redhat.com> - 1.6.4-1
- Updated to latest version
- Removed BuildRequires that are not needed

* Thu Aug 09 2012 Troy Dawson <tdawson@redhat.com> - 1.4.0-7
- Fixed checks.  
  Only run checks that do not require a running mongodb server

* Tue Aug 07 2012 Troy Dawson <tdawson@redhat.com> - 1.4.0-6
- Changed .gemspec and Rakefile to not be doc
- Added checks

* Thu Aug 02 2012 Troy Dawson <tdawson@redhat.com> - 1.4.0-5
- Fixed rubygem(bson) requires

* Mon Jul 23 2012 Troy Dawson <tdawson@redhat.com> - 1.4.0-4
- Updated to meet new fedora rubygem guidelines

* Thu Nov 17 2011 Troy Dawson <tdawson@redhat.com> - 1.4.0-3
- Changed group to Development/Languages
- Changed the global variables
- Seperated the doc and test into the doc rpm

* Thu Nov 17 2011 Troy Dawson <tdawson@redhat.com> - 1.4.0-2
- Added %%{?dist} to version

* Tue Nov 15 2011  <tdawson@redhat.com> - 1.4.0-1
- Initial package
