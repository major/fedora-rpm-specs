# Generated from actionpack-1.13.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name actionpack

# Circular dependency with rubygem-railties.
%bcond_with bootstrap

Name: rubygem-%{gem_name}
Epoch: 1
Version: 7.0.8
Release: 9%{?dist}
Summary: Web-flow and rendering framework putting the VC in MVC (part of Rails)
License: MIT
URL: http://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}%{?prerelease}.gem
# ActionPack gem doesn't ship with the test suite.
# You may check it out like so
# git clone http://github.com/rails/rails.git
# cd rails/actionpack && git archive -v -o actionpack-7.0.8-tests.txz v7.0.8 test/
Source1: %{gem_name}-%{version}%{?prerelease}-tests.txz
# The tools are needed for the test suite, are however unpackaged in gem file.
# You may get them like so
# git clone http://github.com/rails/rails.git --no-checkout
# cd rails && git archive -v -o rails-7.0.8-tools.txz v7.0.8 tools/
Source2: rails-%{version}%{?prerelease}-tools.txz
# Fixes for Minitest 5.16+
# https://github.com/rails/rails/pull/45370
Patch0: rubygem-actionpack-7.0.2.3-Fix-tests-for-minitest-5.16.patch
# From https://github.com/rails/rails/pull/51510
# Remove OpenStruct usage due to json 2.7.2 change
Patch1: rubygem-actionpack-pr51510-remove-openstruct-usage.patch
# Ruby 3.4 `Hash#inspect` compatibility.
# https://github.com/rails/rails/pull/53202/commits/f5401a4175187cb52f93f9666723040ca0cc0843
Patch2: rubygem-actionpack-8.0.0-Update-Action-Pack-test-suite-for-Ruby-3-4-Hash-inspect.patch
# Ruby 3.4 Prism parser fixes.
# https://github.com/rails/rails/pull/52943
Patch3: rubygem-actionpack-8.0.0-Address-DebugExceptionsTest-failures-against-Ruby-with.patch
# Ruby 3.4 backtrace compatibility.
# https://github.com/rails/rails/pull/51101
Patch4: rubygem-actionpack-7.2.0-Update-test-suite-for-compatibility-with-Ruby-3-4-dev.patch
# Drop mutex_m dependency to ease Ruby 3.4 compatibility.
# https://github.com/rails/rails/pull/49674
Patch5: rubygem-actionpack-7.2.0-Drop-dependency-on-mutex-m.patch
# Mitigate `URI::RFC3986_PARSER.escape is obsolete. Use
# URI::RFC2396_PARSER.escape explicitly.` warnings, which might be quite
# extensive.
# https://github.com/rails/rails/pull/53164
Patch6: rubygem-actionpack-7.1.5-7-1-Fix-URI-DEFAULT-PARSER-warnings.patch
Patch7: rubygem-actionpack-7.1.5-7-1-Fix-URI-DEFAULT-PARSER-warnings-test.patch
# Add support for selenium-webdriver 4.22+
# https://github.com/rails/rails/pull/52172
Patch8: rubygem-actionpack-7.1.5.1-Support-selenium-webdriver-4-22-0-that-enables-CDP-in-Firefox.patch


# Let's keep Requires and BuildRequires sorted alphabeticaly
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.2.2
%if %{without bootstrap}
BuildRequires: rubygem(activemodel) = %{version}
BuildRequires: rubygem(activerecord) = %{version}
BuildRequires: rubygem(activesupport) = %{version}
BuildRequires: rubygem(actionview) = %{version}
BuildRequires: rubygem(railties) = %{version}
BuildRequires: rubygem(rack)
BuildRequires: rubygem(rack-cache)
BuildRequires: rubygem(rack-test)
BuildRequires: rubygem(puma)
BuildRequires: rubygem(capybara) >= 3.26
BuildRequires: rubygem(selenium-webdriver)
BuildRequires: rubygem(rexml)
%endif
BuildArch: noarch

%description
Eases web-request routing, handling, and response as a half-way front,
half-way page controller. Implemented with specific emphasis on enabling easy
unit/integration testing that doesn't require a browser.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}%{?prerelease} -b1 -b2

pushd %{_builddir}
%patch 0 -p2
%patch 1 -p2
%patch 2 -p2
%patch 3 -p2
%patch 4 -p2
%patch 7 -p2
%patch 8 -p2
popd

%patch 5 -p2
%patch 6 -p2

%build
gem build ../%{gem_name}-%{version}%{?prerelease}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%if %{without bootstrap}
%check
pushd .%{gem_instdir}
ln -s %{_builddir}/tools ..
# Copy the tests into place
cp -a %{_builddir}/test .

# TODO: relative paths to fixtures are not resolved properly
for tname in 'rendering a relative path with dot' 'rendering a relative path'; do
  sed -i "/^\s* test \"$tname\" do/ a \      skip" \
    test/controller/new_base/render_file_test.rb
done

# Tests need to run in isolation
find test -type f -name '*_test.rb' -print0 | \
  sort -z | \
  xargs -0 -n1 -i sh -c "echo '* Test file: {}'; ruby -Ilib:test -- '{}' || exit 255"

popd
%endif

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.rdoc

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 23 2024 Vít Ondruch <vondruch@redhat.com> - 1:7.0.8-8
- Add support for selenium-webdriver 4.22+

* Wed Dec 04 2024 Vít Ondruch <vondruch@redhat.com> - 1:7.0.8-7
- Mitigate extensive `URI::RFC3986_PARSER.escape is obsolete.` warnings.

* Wed Nov 20 2024 Vít Ondruch <vondruch@redhat.com> - 1:7.0.8-6
- Ruby 3.4 compatibility fixes.

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat May 04 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:7.0.8-4
- Backport upstream patch for removing OpenStruct usage due to json 2.7.2 change

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Sep 10 2023 Pavel Valena <pvalena@redhat.com> - 1:7.0.8-1
- Update to actionpack 7.0.8.

* Mon Aug 28 2023 Pavel Valena <pvalena@redhat.com> - 1:7.0.7.2-1
- Update to actionpack 7.0.7.2.

* Thu Aug 10 2023 Pavel Valena <pvalena@redhat.com> - 1:7.0.7-1
- Update to actionpack 7.0.7.

* Sun Jul 23 2023 Pavel Valena <pvalena@redhat.com> - 1:7.0.6-1
- Update to actionpack 7.0.6.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 30 2023 Pavel Valena <pvalena@redhat.com> - 1:7.0.5-1
- Update to actionpack 7.0.5.

* Tue Mar 14 2023 Pavel Valena <pvalena@redhat.com> - 1:7.0.4.3-1
- Update to actionpack 7.0.4.3.

* Wed Jan 25 2023 Pavel Valena <pvalena@redhat.com> - 1:7.0.4.2-1
- Update to actionpack 7.0.4.2.

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 15 2022 Pavel Valena <pvalena@redhat.com> - 1:7.0.4-1
- Update to actionpack 7.0.4.

* Tue Aug 02 2022 Vít Ondruch <vondruch@redhat.com> - 1:7.0.2.3-3
- Fix Minitest 5.16+ compatibility.
  Resolves: rhbz#2113683

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 14 2022 Pavel Valena <pvalena@redhat.com> - 1:7.0.2.3-1
- Update to actionpack 7.0.2.3.

* Wed Feb 09 2022 Pavel Valena <pvalena@redhat.com> - 1:7.0.2-1
- Update to actionpack 7.0.2.

* Thu Feb 03 2022 Pavel Valena <pvalena@redhat.com> - 1:7.0.1-1
- Update to actionpack 7.0.1.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 17 2021 Pavel Valena <pvalena@redhat.com> - 1:6.1.4.1-1
- Update to actionpack 6.1.4.1.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 30 2021 Pavel Valena <pvalena@redhat.com> - 1:6.1.4-1
- Update to actionpack 6.1.4.

* Tue May 18 2021 Pavel Valena <pvalena@redhat.com> - 1:6.1.3.2-1
- Update to actionpack 6.1.3.2.

* Fri Apr 09 2021 Pavel Valena <pvalena@redhat.com> - 1:6.1.3.1-1
- Update to actionpack 6.1.3.1.

* Thu Feb 18 2021 Pavel Valena <pvalena@redhat.com> - 1:6.1.3-1
- Update to actionpack 6.1.3.

* Mon Feb 15 2021 Pavel Valena <pvalena@redhat.com> - 1:6.1.2.1-1
- Update to actionpack 6.1.2.1.

* Wed Jan 27 2021 Pavel Valena <pvalena@redhat.com> - 1:6.1.1-1
- Update to actionpack 6.1.1.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct  8 11:41:59 CEST 2020 Pavel Valena <pvalena@redhat.com> - 1:6.0.3.4-1
- Update to actionpack 6.0.3.4.
  Resolves: rhbz#1877506

* Wed Sep 23 2020 Vít Ondruch <vondruch@redhat.com> - 1:6.0.3.3-2
- Run the test suite above the currently built ActionPack.

* Tue Sep 22 00:41:31 CEST 2020 Pavel Valena <pvalena@redhat.com> - 1:6.0.3.3-1
- Update to actionpack 6.0.3.3.
  Resolves: rhbz#1877506

* Mon Aug 17 04:59:56 GMT 2020 Pavel Valena <pvalena@redhat.com> - 1:6.0.3.2-1
- Update to actionpack 6.0.3.2.
  Resolves: rhbz#1742790

* Mon Aug 03 08:06:29 GMT 2020 Pavel Valena <pvalena@redhat.com> - 1:6.0.3.1-2
- Update to ActionPack 6.0.3.1.
  Resolves: rhbz#1742790

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 17 2020 Vít Ondruch <vondruch@redhat.com> - 1:5.2.3-5
- Fix text failures for Rack 2.2+.
  Resolves: rhbz#1799984

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 28 2019 Pavel Valena <pvalena@redhat.com> - 1:5.2.3-2
- Enable tests.

* Thu Mar 28 2019 Pavel Valena <pvalena@redhat.com> - 1:5.2.3-1
- Update to Action Pack 5.2.3.

* Mon Mar 18 2019 Pavel Valena <pvalena@redhat.com> - 1:5.2.2.1-2
- Enable tests.

* Thu Mar 14 2019 Pavel Valena <pvalena@redhat.com> - 1:5.2.2.1-1
- Update to Action Pack 5.2.2.1.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Pavel Valena <pvalena@redhat.com> - 1:5.2.2-2
- Update to Action Pack 5.2.2.

* Thu Aug 09 2018 Pavel Valena <pvalena@redhat.com> - 1:5.2.1-2
- Enable tests.

* Wed Aug 08 2018 Pavel Valena <pvalena@redhat.com> - 1:5.2.1-1
- Update to Action Pack 5.2.1.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 04 2018 Pavel Valena <pvalena@redhat.com> - 1:5.2.0-2
- Enable tests.

* Mon Apr 23 2018 Pavel Valena <pvalena@redhat.com> - 1:5.2.0-1
- Update to Action Pack 5.2.0.

* Mon Feb 19 2018 Pavel Valena <pvalena@redhat.com> - 1:5.1.5-2
- Enable tests.

* Fri Feb 16 2018 Pavel Valena <pvalena@redhat.com> - 1:5.1.5-1
- Update to Action Pack 5.1.5.
  Remove patch{0,1}; subsumed

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 12 2018 Vít Ondruch <vondruch@redhat.com> - 1:5.1.4-3
- Fix Ruby 2.5 compatibility.

* Mon Sep 11 2017 Pavel Valena <pvalena@redhat.com> - 1:5.1.4-2
- Enable tests.

* Mon Sep 11 2017 Pavel Valena <pvalena@redhat.com> - 1:5.1.4-1
- Update to Action Pack 5.1.4.

* Sat Aug 12 2017 Pavel Valena <pvalena@redhat.com> - 1:5.1.3-2
- Enable tests.

* Tue Aug 08 2017 Pavel Valena <pvalena@redhat.com> - 1:5.1.3-1
- Update to Action Pack 5.1.3.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Pavel Valena <pvalena@redhat.com> - 1:5.1.2-2
- Enable tests.

* Tue Jun 27 2017 Pavel Valena <pvalena@redhat.com> - 1:5.1.2-1
- Update to Action Pack 5.1.2.

* Thu Jun 01 2017 Pavel Valena <pvalena@redhat.com> - 1:5.1.1-2
- Enable tests.

* Mon May 22 2017 Pavel Valena <pvalena@redhat.com> - 1:5.1.1-1
- Update to Action Pack 5.1.1.

* Tue Mar 07 2017 Pavel Valena <pvalena@redhat.com> - 1:5.0.2-2
- Enable tests.

* Thu Mar 02 2017 Pavel Valena <pvalena@redhat.com> - 1:5.0.2-1
- Update to Action Pack 5.0.2.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 03 2017 Pavel Valena <pvalena@redhat.com> - 1:5.0.1-2
- Enable tests.

* Mon Jan 02 2017 Pavel Valena <pvalena@redhat.com> - 1:5.0.1-1
- Update to Action Pack 5.0.1.

* Tue Aug 16 2016 Pavel Valena <pvalena@redhat.com> - 1:5.0.0.1-2
- Enable tests

* Tue Aug 16 2016 Pavel Valena <pvalena@redhat.com> - 1:5.0.0.1-2
- Enable tests

* Mon Aug 15 2016 Pavel Valena <pvalena@redhat.com> - 1:5.0.0.1-1
- Update to Actionpack 5.0.0.1

* Tue Jul 12 2016 Vít Ondruch <vondruch@redhat.com> - 1:5.0.0-1
- Update to ActionPack 5.0.0.

* Tue Mar 08 2016 Pavel Valena <pvalena@redhat.com> - 1:4.2.6-2
- Enable tests

* Tue Mar 08 2016 Pavel Valena <pvalena@redhat.com> - 1:4.2.6-1
- Update to actionpack 4.2.6

* Thu Mar 03 2016 Pavel Valena <pvalena@redhat.com> - 1:4.2.5.2-2
- Enable tests

* Wed Mar 02 2016 Pavel Valena <pvalena@redhat.com> - 1:4.2.5.2-1
- Update to actionpack 4.2.5.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Pavel Valena <pvalena@redhat.com> - 1:4.2.5.1-3
- Fix macros in comment

* Tue Jan 26 2016 Pavel Valena <pvalena@redhat.com> - 1:4.2.5.1-2
- Enable tests

* Tue Jan 26 2016 Pavel Valena <pvalena@redhat.com> - 1:4.2.5.1-1
- Update to actionpack 4.2.5.1

* Wed Nov 18 2015 Pavel Valena <pvalena@redhat.com> - 1:4.2.5-2
- Enable tests

* Wed Nov 18 2015 Pavel Valena <pvalena@redhat.com> - 1:4.2.5-1
- Update to actionpack 4.2.5

* Wed Aug 26 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.4-2
- Enable tests

* Wed Aug 26 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.4-1
- Update to actionpack 4.2.4

* Wed Jul 01 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.3-2
- Enable tests

* Tue Jun 30 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.3-1
- Update to actionpack 4.2.3

* Tue Jun 23 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.2-2
- Run tests

* Mon Jun 22 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.2-1
- Update to actionpack 4.2.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 20 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.1-2
- Run tests

* Fri Mar 20 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.1-1
- Update to actionpack 4.2.1

* Fri Feb 13 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.0-2
- Run all tests

* Mon Feb 09 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.0-1
- Update to actionpack 4.2.0

* Mon Aug 25 2014 Josef Stribny <jstribny@redhat.com> - 4.1.5-1
- Update to actionpack 4.1.5

* Fri Jul 04 2014 Josef Stribny <jstribny@redhat.com> - 4.1.4-1
- Update to actionpack 4.1.4

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Josef Stribny <jstribny@redhat.com> - 1:4.1.1-1
- Update to ActionPack 4.1.1

* Fri Apr 18 2014 Josef Stribny <jstribny@redhat.com> - 1:4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Mon Apr 14 2014 Josef Stribny <jstribny@redhat.com> - 1:4.1.0-1
- Update to ActionPack 4.1.0

* Wed Feb 26 2014 Josef Stribny <jstribny@redhat.com> - 1:4.0.3-1
- Update to ActionPack 4.0.3

* Thu Dec 05 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.2-1
- Update to ActionPack 4.0.2
  - Fixes CVE-2013-6417, CVE-2013-6414, CVE-2013-6415, CVE-2013-6416 and CVE-2013-4491

* Thu Nov 14 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.1-1
- Update to ActionPack 4.0.1

* Thu Aug 08 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.0-1
- Update to ActionPack 4.0.0.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 20 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.13-2
- Test suite passes once again.

* Tue Mar 19 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.13-1
- Update to the ActionPack 3.2.13.

* Fri Mar 08 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.12-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Tue Feb 12 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.12-1
- Update to the ActionPack 3.2.12.

* Wed Jan 09 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.11-1
- Update to the ActionPack 3.2.11.

* Thu Jan 03 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.10-1
- Update to the ActionPack 3.2.10.

* Sat Oct 13 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.2.8-2
- Relaxed Builder dependency.

* Mon Aug 13 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.2.8-1
- Update to the ActionPack 3.2.8.

* Wed Aug 01 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.2.7-2
- Remove the unneded symlink used for tests in previous versions (RHBZ #840119).

* Mon Jul 30 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.2.7-1
- Update to the ActionPack 3.2.7.

* Tue Jul 24 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.2.6-2
- Fixed missing epoch in -doc subpackage.

* Mon Jul 23 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.2.6-1
- Updated to the ActionPack 3.2.6.
- Remove Rake dependency.
- Introduce -doc subpackage.
- Relax sprockets dependency.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.0.15-1
- Updated to the ActionPack 3.0.15.

* Fri Jun 01 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.0.13-1
- Updated to the ActionPack 3.0.13.

* Fri Mar 16 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.0.11-3
- The CVE patches names now contain the CVE id.

* Tue Mar 06 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.0.11-2
- Fix for CVE-2012-1098.
- Fix for CVE-2012-1099.

* Tue Jan 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.0.11-1
- Rebuilt for Ruby 1.9.3.
- Updated to ActionPack 3.0.11.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 22 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.10-1
- Update to ActionPack 3.0.10

* Mon Jul 04 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.9-1
- Update to ActionPack 3.0.9

* Thu Jun 16 2011 Mo Morsi <mmorsi@redhat.com> - 1:3.0.5-3
- Include fix for CVE-2011-2197

* Fri Jun 03 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.5-2
- Removed regin and multimap dependencies. They were added into rack-mount
  where they actually belongs.

* Fri Mar 25 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.5-1
- Updated to ActionPack 3.0.5

* Wed Feb 16 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.3-4
- Relaxed erubis dependency
- Fixed build compatibility with RubyGems 1.5

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 07 2011 Mohammed Morsi <mmorsi@redhat.com> - 1:3.0.3-2
- changelog fixes

* Mon Jan 10 2011 Mohammed Morsi <mmorsi@redhat.com> - 1:3.0.3-1
- Update to rails 3

* Thu Aug 12 2010 Mohammed Morsi <mmorsi@redhat.com> - 1:2.3.8-2
- Bumped actionpack rack dependency to version 1.1.0

* Mon Aug 09 2010 Mohammed Morsi <mmorsi@redhat.com> - 1:2.3.8-1
- Update to 2.3.8

* Mon May 17 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1:2.3.5-2
- Set TMPDIR environment at %%check to make it sure all files created
  during rpmbuild are cleaned up

* Thu Jan 28 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1:2.3.5-1
- Update to 2.3.5

* Fri Jan  8 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1:2.3.4-4
- Workaround patch to fix for rack 1.1.0 dependency (bug 552972)

* Thu Dec 10 2009 David Lutterkort <lutter@redhat.com> - 1:2.3.4-3
- Patch for CVE-2009-4214 (bz 542786)

* Wed Oct  7 2009 David Lutterkort <lutter@redhat.com> - 1:2.3.4-2
- Bump Epoch to ensure upgrade path from F-11

* Sun Sep 20 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.3.4-1
- Update to 2.3.4 (bug 520843, CVE-2009-3009)
- Fix tests

* Sun Aug  2 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.3.3-1
- 2.3.3
- Enable test (some tests fail, please someone investigate!!)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 16 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 2.3.2-1
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
- New version

* Thu Nov 29 2007 David Lutterkort <dlutter@redhat.com> - 1.13.6-1
- New version

* Tue Nov 13 2007 David Lutterkort <dlutter@redhat.com> - 1.13.5-2
- Fix buildroot; mark docs in geminstdir cleanly

* Tue Oct 30 2007 David Lutterkort <dlutter@redhat.com> - 1.13.5-1
- Initial package
