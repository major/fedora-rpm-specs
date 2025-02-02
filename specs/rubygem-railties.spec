# Generated from railties-3.0.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name railties

# Circular dependency with rubygem-{rails,jquery-rails,uglifier}.
%bcond_with bootstrap

Name: rubygem-%{gem_name}
Version: 7.0.8
Release: 8%{?dist}
Summary: Tools for creating, working with, and running Rails applications
License: MIT
URL: http://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}%{?prerelease}.gem
# Get the test suite:
# git clone http://github.com/rails/rails.git
# cd rails/railties && git archive -v -o railties-7.0.8-tests.txz v7.0.8 test/
Source1: %{gem_name}-%{version}%{?prerelease}-tests.txz
# The tools are needed for the test suite, are however unpackaged in gem file.
# You may check it out like so
# git clone http://github.com/rails/rails.git --no-checkout
# cd rails && git archive -v -o rails-7.0.8-tools.txz v7.0.8 tools/
Source2: rails-%{version}%{?prerelease}-tools.txz
# Fixes for Minitest 5.16+
# https://github.com/rails/rails/pull/45380
Patch1: rubygem-railties-7.0.2.3-Remove-the-multi-call-form-of-assert_called_with.patch
# Fix `ApplicationTests::TestRunnerTest#test_run_in_parallel_with_unmarshable_exception`
# test case compabitility with Minitest 5.16.3.
# https://github.com/rails/rails/pull/45370
Patch2: rubygem-railties-7.1.0-Fix-tests-for-minitest-5.16.patch
# https://github.com/rails/rails/pull/45848
Patch3: rubygem-railties-7.1.0-Fix-unmarshalable-test-for-minitest-5.16.3.patch
# Fix `FullStackConsoleTest` test cases for Ruby 3.3.
# https://github.com/rails/rails/pull/48369/commits/cf45394d104b00679c900e9d2dd09154cadcbe11
Patch4: rubygem-railties-7.1.0-Run-Rails-console-test-against-IRB-with-Reline-instead-of.patch
# Relax dependency on Puma.
# https://github.com/rails/rails/pull/46254
Patch5: rubygem-railties-7.1.0-Bump-Puma-to-v6-0-0.patch
Patch6: rubygem-railties-7.1.0-Bump-Puma-to-v6-0-0-test.patch
# Minitest 5.21.0 started to output relative paths.
# https://github.com/rails/rails/pull/50724
Patch7: rubygem-railties-7.1.4-Fix-failing-test-due-to-the-relative-path-output-of-minitest.patch
# Ruby 3.4 `Hash#inspect` compatibility.
# https://github.com/rails/rails/pull/53202/commits/ab97c585c4b1b53bc2391fd99b0269df217629b7
Patch8: rubygem-railties-8.0.0-Update-Railties-test-suite-for-Ruby-3-4-Hash-inspect.patch
# Ruby 3.4 backtrace compatibility.
# https://github.com/rails/rails/pull/51101
Patch9: rubygem-railties-7.2.0-Update-test-suite-for-compatibility-with-Ruby-3-4-dev.patch
# Unlock Sqlite3 2.x+
# https://github.com/rails/rails/issues/52309
# https://github.com/rails/rails/commit/3271c4f6d221a73af801d7d57905f0cece374e05
Patch10: rubygem-railties-7.1.4-Allow-sqlite3-to-float-to-version-2.patch
Patch11: rubygem-railties-7.1.4-Allow-sqlite3-to-float-to-version-2-tests.patch


# Needed by `rails console`.
Recommends: rubygem(irb)
# dbconsole requires the executable.
Suggests: %{_bindir}/sqlite3
# Required by generators, e.g.:
# https://github.com/rails/rails/blob/7-0-stable/railties/lib/rails/generators/rails/app/app_generator.rb#L75
Recommends: %{_bindir}/git
# Let's keep Requires and BuildRequires sorted alphabeticaly
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.2.2
%if %{without bootstrap}
BuildRequires: rubygem(actioncable) = %{version}
BuildRequires: rubygem(actionmailer) = %{version}
BuildRequires: rubygem(actionpack) = %{version}
BuildRequires: rubygem(activerecord) = %{version}
BuildRequires: rubygem(activestorage) = %{version}
BuildRequires: rubygem(activesupport) = %{version}
BuildRequires: rubygem(bootsnap)
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(capybara)
BuildRequires: rubygem(dalli)
BuildRequires: rubygem(importmap-rails)
BuildRequires: rubygem(irb)
BuildRequires: rubygem(listen)
BuildRequires: rubygem(method_source)
BuildRequires: rubygem(mysql2)
BuildRequires: rubygem(pg)
BuildRequires: rubygem(puma)
BuildRequires: rubygem(rack-cache)
BuildRequires: rubygem(rails)
BuildRequires: rubygem(rake) >= 0.8.7
BuildRequires: rubygem(selenium-webdriver)
BuildRequires: rubygem(sprockets-rails)
BuildRequires: rubygem(sqlite3)
BuildRequires: rubygem(thor) >= 0.18.1
BuildRequires: rubygem(zeitwerk)
BuildRequires: rubygem(webrick)
BuildRequires: %{_bindir}/git
BuildRequires: %{_bindir}/memcached
BuildRequires: %{_bindir}/postgres
BuildRequires: %{_bindir}/sqlite3
BuildRequires: tzdata
%endif
BuildArch: noarch

%description
Rails internals: application bootup, plugins, generators, and rake tasks.
Railties is responsible to glue all frameworks together. Overall, it:
* handles all the bootstrapping process for a Rails application;
* manages rails command line interface;
* provides Rails generators core;

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}%{?prerelease} -b1 -b2

%patch 5 -p2
%patch 10 -p2

pushd %{_builddir}
%patch 1 -p2
%patch 2 -p2
%patch 3 -p2
%patch 4 -p2
%patch 6 -p2
%patch 7 -p2
%patch 8 -p2
%patch 9 -p2
%patch 11 -p2
popd

%build
gem build ../%{gem_name}-%{version}%{?prerelease}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -p .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/exe -type f | xargs chmod a+x

%if %{without bootstrap}
%check
# fake RAILS_FRAMEWORK_ROOT
ln -s %{gem_dir}/specifications/rails-%{version}%{?prerelease}.gemspec .%{gem_dir}/gems/rails.gemspec
# Needed to prevent YARN dependnecy.
ln -s %{gem_dir}/gems/actionview-%{version}%{?prerelease}/ .%{gem_dir}/gems/actionview
ln -s ${PWD}%{gem_instdir} .%{gem_dir}/gems/railties

pushd .%{gem_dir}/gems/railties

ln -s %{_builddir}/tools ..
mv %{_builddir}/test .

# Expected by InfoTest#test_rails_version
echo '%{version}%{?prerelease}' > ../RAILS_VERSION

touch ../Gemfile
echo 'gem "actioncable"' >> ../Gemfile
echo 'gem "actionmailer"' >> ../Gemfile
echo 'gem "actionpack"' >> ../Gemfile
echo 'gem "activerecord"' >> ../Gemfile
echo 'gem "activestorage"' >> ../Gemfile
echo 'gem "activesupport"' >> ../Gemfile
echo 'gem "bootsnap"' >> ../Gemfile
echo 'gem "capybara"' >> ../Gemfile
echo 'gem "dalli"' >> ../Gemfile
echo 'gem "importmap-rails"' >> ../Gemfile
echo 'gem "irb"' >> ../Gemfile
echo 'gem "listen"' >> ../Gemfile
echo 'gem "method_source"' >> ../Gemfile
echo 'gem "mysql2"' >> ../Gemfile
echo 'gem "pg"' >> ../Gemfile
echo 'gem "puma"' >> ../Gemfile
echo 'gem "rack-cache"' >> ../Gemfile
echo 'gem "rails"' >> ../Gemfile
echo 'gem "rake"' >> ../Gemfile
echo 'gem "rdoc"' >> ../Gemfile
echo 'gem "selenium-webdriver"' >> ../Gemfile
echo 'gem "sprockets-rails"' >> ../Gemfile
echo 'gem "sqlite3"' >> ../Gemfile
echo 'gem "thor"' >> ../Gemfile
echo 'gem "webrick"' >> ../Gemfile

export RUBYOPT="-I${PWD}/../railties/lib"
export PATH="${PWD}/../railties/exe:$PATH"
export BUNDLE_GEMFILE=${PWD}/../Gemfile

# Start PostgreSQL server, required by e.g.
# test/application/bin_setup_test
PG_DIR=$(mktemp -d)
PG_DATA_DIR=${PG_DIR}/data
export PGHOST=localhost
initdb -E UTF8 --no-locale -D ${PG_DATA_DIR}
pg_ctl -o "-p 5432 -k ${PG_DIR}" -D ${PG_DATA_DIR} -l ${PG_DIR}/logfile start

# Get temporary PID file name and start memcached daemon required by
# test/application/middleware/cache_test.rb
MC_PID=%(mktemp)
memcached -d -P "${MC_PID}"

# Remove unneded dependency minitest/retry
sed -i -e '/require..minitest.retry./ s/^/#/' \
  test/isolation/abstract_unit.rb

# Fake the directory to prevent YARN dependnecy.
mkdir test/isolation/assets/node_modules

# TODO: Mismatch in RAILS_FRAMEWORK_ROOT, not sure how to fix it.
sed -i '/test "i18n files have lower priority than application ones" do$/,/^    end$/ s/^/#/' \
  test/railties/engine_test.rb

# It seems that the test either does not run in development mode, which would
# display the exception or there is some issue.
sed -i '/test "displays statement invalid template correctly" do/a\
    skip' test/application/middleware/exceptions_test.rb

# Needs network access to reach GitHub.
sed -i '/test_template_from_url/a\
    skip' test/generators/app_generator_test.rb

# We don't have {turbo,tailwindcss,cssbundling}-rails in Fedora.
sed -r -i '/test_(hotwire|css_option_with_(asset_pipeline_tailwind|cssbundling_gem))/a\
    skip' test/generators/app_generator_test.rb

# It seems that ActionMailbox does not work properly. Is it due to missing
# `turbo-rails`?
sed -i '/^\s*def test_create_migrations/ a \  skip' \
  test/generators/action_mailbox_install_generator_test.rb
# Neither the ActiveMailbox routes are generated for some reason :/
mv test/commands/routes_test.rb{,.disable}

# Do not print the git hint message which clogs the test output
git config --global init.defaultBranch master

# Tests needs to be executed in isolation. Also, use `bundle exec`, there
# is nothing to loose here and some tests depends on the Bundler (e.g.
# test/generators/app_generator_test.rb).
# The `$NOTIFY_SOCKET` is needed due to Puma 6+ bundling sd_notify, resulting
# in `ApplicationTests::ServerTest#test_restart_rails_server_with_custom_pid_file_path`
# test failures. Other option would be to skip this test. There is also chance
# that something is off for other reasons:
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/RHCFUMSMYCQ435LRPTFYDKTECHZHD4R7/
find test -type f -name '*_test.rb' -print0 | \
  sort -z | \
  xargs -0 -n1 -i sh -c "echo '* Test file: {}'; env -u NOTIFY_SOCKET bundle exec ruby -Itest -- '{}' || exit 255"

# Kill memcached daemon.
kill -TERM $(< "${MC_PID}")

# Stop PostgreSQL server
pg_ctl -D ${PG_DATA_DIR} stop
rm -rf ${PG_DIR}
popd
%endif

%files
%dir %{gem_instdir}
%{_bindir}/rails
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/exe
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/RDOC_MAIN.rdoc
%doc %{gem_instdir}/README.rdoc

%changelog
* Thu Jan 30 2025 Vít Ondruch <vondruch@redhat.com> - 7.0.8-8
- Unlock Sqlite3 2.x+

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 26 2024 Vít Ondruch <vondruch@redhat.com> - 7.0.8-6
- Ruby 3.4 compatibility fixes.

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Feb 07 2024 Vít Ondruch <vondruch@redhat.com> - 7.0.8-4
- Fix FTBFS due to Minitest 5.21.0+ incompatibility.
  Resolves: rhbz#2261665

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Vít Ondruch <vondruch@redhat.com> - 7.0.8-3
- Fix tests for Puma 6+ compatibility.
- Relax Rails generators to support Puma 6+.

* Fri Dec 15 2023 Vít Ondruch <vondruch@redhat.com> - 7.0.8-2
- Fix test compatibility with Ruby 3.3.

* Sun Sep 10 2023 Pavel Valena <pvalena@redhat.com> - 7.0.8-1
- Update to railties 7.0.8.

* Mon Aug 28 2023 Pavel Valena <pvalena@redhat.com> - 7.0.7.2-1
- Update to railties 7.0.7.2.

* Thu Aug 10 2023 Pavel Valena <pvalena@redhat.com> - 7.0.7-1
- Update to railties 7.0.7.

* Sun Jul 23 2023 Pavel Valena <pvalena@redhat.com> - 7.0.6-1
- Update to railties 7.0.6.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 30 2023 Pavel Valena <pvalena@redhat.com> - 7.0.5-1
- Update to railties 7.0.5.

* Tue Mar 14 2023 Pavel Valena <pvalena@redhat.com> - 7.0.4.3-1
- Update to railties 7.0.4.3.

* Wed Feb 01 2023 Vít Ondruch <vondruch@redhat.com> - 7.0.4.2-2
- Test revamp + build dependencies update.

* Wed Jan 25 2023 Pavel Valena <pvalena@redhat.com> - 7.0.4.2-1
- Update to railties 7.0.4.2.

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 15 2022 Pavel Valena <pvalena@redhat.com> - 7.0.4-1
- Update to railties 7.0.4.

* Wed Aug 03 2022 Vít Ondruch <vondruch@redhat.com> - 7.0.2.3-3
- Fix Minitest 5.16+ compatibility.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 14 2022 Pavel Valena <pvalena@redhat.com> - 7.0.2.3-1
- Update to railties 7.0.2.3.

* Wed Feb 09 2022 Pavel Valena <pvalena@redhat.com> - 7.0.2-1
- Update to railties 7.0.2.

* Thu Feb 03 2022 Pavel Valena <pvalena@redhat.com> - 7.0.1-1
- Update to railties 7.0.1.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 17 2021 Pavel Valena <pvalena@redhat.com> - 6.1.4.1-1
- Update to railties 6.1.4.1.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 30 2021 Pavel Valena <pvalena@redhat.com> - 6.1.4-1
- Update to railties 6.1.4.

* Tue May 18 2021 Pavel Valena <pvalena@redhat.com> - 6.1.3.2-1
- Update to railties 6.1.3.2.

* Fri Apr 09 2021 Pavel Valena <pvalena@redhat.com> - 6.1.3.1-1
- Update to railties 6.1.3.1.

* Tue Apr 06 2021 Vít Ondruch <vondruch@redhat.com> - 6.1.3-2
- Add `rubygem(irb)` dependency, which was previosly pulled in indirectly.

* Thu Feb 18 2021 Pavel Valena <pvalena@redhat.com> - 6.1.3-1
- Update to railties 6.1.3.

* Mon Feb 15 2021 Pavel Valena <pvalena@redhat.com> - 6.1.2.1-1
- Update to railties 6.1.2.1.

* Wed Jan 27 2021 Pavel Valena <pvalena@redhat.com> - 6.1.1-1
- Update to railties 6.1.1.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct  8 11:34:50 CEST 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.4-1
- Update to railties 6.0.3.4.
  Resolves: rhbz#1877509

* Tue Sep 22 00:33:17 CEST 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.3-1
- Update to railties 6.0.3.3.
  Resolves: rhbz#1877509

* Mon Aug 17 05:27:18 GMT 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.2-1
- Update to railties 6.0.3.2.
  Resolves: rhbz#1742801

* Tue Aug 04 16:14:56 GMT 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.1-1
- Update to Railties 6.0.3.1.
  Resolves: rhbz#1742801

* Mon Aug 03 2020 Vít Ondruch <vondruch@redhat.com> - 5.2.3-6
- Fix test failure due to Ruby 2.7 and Puma 4.2.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 28 2019 Pavel Valena <pvalena@redhat.com> - 5.2.3-2
- Enable tests.

* Thu Mar 28 2019 Pavel Valena <pvalena@redhat.com> - 5.2.3-1
- Update to Railties 5.2.3.

* Mon Mar 18 2019 Pavel Valena <pvalena@redhat.com> - 5.2.2.1-2
- Enable tests.

* Thu Mar 14 2019 Pavel Valena <pvalena@redhat.com> - 5.2.2.1-1
- Update to Railties 5.2.2.1.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Pavel Valena <pvalena@redhat.com> - 5.2.2-2
- Update to Railties 5.2.2.

* Thu Aug 09 2018 Pavel Valena <pvalena@redhat.com> - 5.2.1-2
- Enable tests.

* Wed Aug 08 2018 Pavel Valena <pvalena@redhat.com> - 5.2.1-1
- Update to Railties 5.2.1.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 04 2018 Pavel Valena <pvalena@redhat.com> - 5.2.0-2
- Enable tests.

* Mon Apr 23 2018 Pavel Valena <pvalena@redhat.com> - 5.2.0-1
- Update to Railties 5.2.0.

* Mon Feb 19 2018 Pavel Valena <pvalena@redhat.com> - 5.1.5-2
- Enable tests.

* Fri Feb 16 2018 Pavel Valena <pvalena@redhat.com> - 5.1.5-1
- Update to Railties 5.1.5.
  Removed patch{6,7,8}; subsumed

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Vít Ondruch <vondruch@redhat.com> - 5.1.4-3
- Fix Minitest 5.11 compatibility.

* Mon Sep 11 2017 Pavel Valena <pvalena@redhat.com> - 5.1.4-2
- Enable tests.

* Mon Sep 11 2017 Pavel Valena <pvalena@redhat.com> - 5.1.4-1
- Update to Railties 5.1.4.

* Sat Aug 12 2017 Pavel Valena <pvalena@redhat.com> - 5.1.3-2
- Enable tests.

* Tue Aug 08 2017 Pavel Valena <pvalena@redhat.com> - 5.1.3-1
- Update to Railties 5.1.3.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Pavel Valena <pvalena@redhat.com> - 5.1.2-2
- Enable tests.

* Tue Jun 27 2017 Pavel Valena <pvalena@redhat.com> - 5.1.2-1
- Update to Railties 5.1.2.

* Mon Jun 26 2017 Pavel Valena <pvalena@redhat.com> - 5.1.1-2
- Enable tests.

* Mon May 22 2017 Pavel Valena <pvalena@redhat.com> - 5.1.1-1
- Update to Railties 5.1.1.
  - git support with tests
  - puma dependent tests

* Sat May 13 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.0.2-3
- Patch for minitest 5.10.2 compatibility (rhbz 1449430)

* Tue Mar 07 2017 Pavel Valena <pvalena@redhat.com> - 5.0.2-2
- Enable tests.

* Thu Mar 02 2017 Pavel Valena <pvalena@redhat.com> - 5.0.2-1
- Update to Railties 5.0.2.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Vít Ondruch <vondruch@redhat.com> - 5.0.1-2
- Fix Listen 3.1.x compatibility.

* Mon Jan 02 2017 Pavel Valena <pvalena@redhat.com> - 5.0.1-1
- Update to Railties 5.0.1.
- Remove Patch0 and Patch1: rubygem-railties-5.0.0-Do-not-run-bundle-install-when-generating-a-new-plugin{,-test}.patch; subsumed

* Wed Aug 17 2016 Vít Ondruch <vondruch@redhat.com> - 5.0.0.1-2
- Enable whole test suite.

* Mon Aug 15 2016 Pavel Valena <pvalena@redhat.com> - 5.0.0.1-1
- Update to Railties 5.0.0.1

* Tue Jul 12 2016 Vít Ondruch <vondruch@redhat.com> - 5.0.0-1
- Update to Railties 5.0.0.

* Tue Mar 08 2016 Pavel Valena <pvalena@redhat.com> - 4.2.6-1
- Update to railties 4.2.6

* Wed Mar 02 2016 Pavel Valena <pvalena@redhat.com> - 4.2.5.2-1
- Update to railties 4.2.5.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Pavel Valena <pvalena@redhat.com> - 4.2.5.1-1
- Update to railties 4.2.5.1

* Wed Nov 18 2015 Pavel Valena <pvalena@redhat.com> - 4.2.5-1
- Update to railties 4.2.5

* Wed Aug 26 2015 Josef Stribny <jstribny@redhat.com> - 4.2.4-1
- Update to railties 4.2.4

* Tue Jun 30 2015 Josef Stribny <jstribny@redhat.com> - 4.2.3-1
- Update to railties 4.2.3

* Mon Jun 22 2015 Josef Stribny <jstribny@redhat.com> - 4.2.2-1
- Update to railties 4.2.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 20 2015 Josef Stribny <jstribny@redhat.com> - 4.2.1-1
- Update to railties 4.2.1

* Mon Feb 09 2015 Josef Stribny <jstribny@redhat.com> - 4.2.0-1
- Update to railties 4.2.0
- Disable tests for now, they are too unstable

* Mon Aug 25 2014 Josef Stribny <jstribny@redhat.com> - 4.1.5-1
- Update to railties 4.1.5

* Fri Jul 04 2014 Josef Stribny <jstribny@redhat.com> - 4.1.4-1
- Update to railties 4.1.4

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Josef Stribny <jstribny@redhat.com> - 4.1.1-1
- Update to Railties 4.1.1

* Wed Apr 23 2014 Josef Stribny <jstribny@redhat.com> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Tue Apr 15 2014 Josef Stribny <jstribny@redhat.com> - 4.1.0-1
- Update to Railties 4.1.0

* Wed Feb 26 2014 Josef Stribny <jstribny@redhat.com> - 4.0.3-1
- Update to Railties 4.0.3

* Wed Feb 05 2014 Josef Stribny <jstribny@redhat.com> - 4.0.2-2
- Fix license (SyntaxHighlighter is removed in 4.x.x)

* Thu Dec 05 2013 Josef Stribny <jstribny@redhat.com> - 4.0.2-1
- Update to Railties 4.0.2

* Thu Nov 14 2013 Josef Stribny <jstribny@redhat.com> - 4.0.1-1
- Update to Railties 4.0.1.

* Thu Aug 08 2013 Josef Stribny <jstribny@redhat.com> - 4.0.0-1
- Update to Railties 4.0.0.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Josef Stribny <jstribny@redhat.com> - 3.2.13-1
- Fix license.

* Sat Mar 09 2013 Vít Ondruch <vondruch@redhat.com> - 3.2.12-3
- Relax RDoc dependency.

* Fri Mar 08 2013 Vít Ondruch <vondruch@redhat.com> - 3.2.12-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Tue Feb 12 2013 Vít Ondruch <vondruch@redhat.com> - 3.2.12-1
- Update to Railties 3.2.12.

* Wed Jan 09 2013 Vít Ondruch <vondruch@redhat.com> - 3.2.11-1
- Update to Railties 3.2.11.

* Fri Jan 04 2013 Vít Ondruch <vondruch@redhat.com> - 3.2.10-1
- Update to Railties 3.2.10.

* Mon Aug 13 2012 Vít Ondruch <vondruch@redhat.com> - 3.2.8-1
- Update to Railties 3.2.8.

* Mon Jul 30 2012 Vít Ondruch <vondruch@redhat.com> - 3.2.7-1
- Update to Railties 3.2.7.

* Mon Jul 23 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.2.6-1
- Update to Railties 3.2.6.
- Move some files into -doc subpackage.
- Remove the unneeded %%defattr.
- Introduce %%check section (not running tests yet, as they are part of dependency loop).

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Vít Ondruch <vondruch@redhat.com> - 3.0.15-1
- Update to Railties 3.0.15.

* Fri Jun 01 2012 Vít Ondruch <vondruch@redhat.com> - 3.0.13-1
- Update to Railties 3.0.13.

* Wed Feb 01 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.0.11-1
- Rebuilt for Ruby 1.9.3.
- Update to Railties 3.0.11.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 22 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.10-1
- Update to Railties 3.0.10

* Thu Jul 21 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.9-2
- Added missing RDoc dependency.

* Thu Jul 07 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.9-1
- Update to Railties 3.0.9

* Mon Jun 27 2011  <mmorsi@redhat.com> - 3.0.5-2
- include fix for BZ #715385

* Tue Mar 29 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.5-1
- Updated to Railties 3.0.5

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 02 2011  <Minnikhanov@gmail.com> - 3.0.3-7
- Fix Comment 11 #665560. https://bugzilla.redhat.com/show_bug.cgi?id=668090#c11
- Take LICENSE file from upstream.

* Mon Jan 31 2011  <Minnikhanov@gmail.com> - 3.0.3-6
- Fix Comment 9 #665560. https://bugzilla.redhat.com/show_bug.cgi?id=668090#c9
- Temporarily test suite is blocked.

* Thu Jan 27 2011  <Minnikhanov@gmail.com> - 3.0.3-5
- Fix Comment 7 #665560. https://bugzilla.redhat.com/show_bug.cgi?id=668090#c7 

* Tue Jan 25 2011  <Minnikhanov@gmail.com> - 3.0.3-4
- Fix Comment 5 #665560. https://bugzilla.redhat.com/show_bug.cgi?id=668090#c5 

* Mon Jan 24 2011  <Minnikhanov@gmail.com> - 3.0.3-3
- Fix Comment 3 #665560. https://bugzilla.redhat.com/show_bug.cgi?id=668090#c3 

* Sun Jan 23 2011  <Minnikhanov@gmail.com> - 3.0.3-2
- Fix Comment 1 #665560. https://bugzilla.redhat.com/show_bug.cgi?id=668090#c1 

* Fri Jan 07 2011  <Minnikhanov@gmail.com> - 3.0.3-1
- Initial package

