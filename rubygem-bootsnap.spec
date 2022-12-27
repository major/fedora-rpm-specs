# Generated from bootsnap-1.3.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name bootsnap

Name: rubygem-%{gem_name}
Version: 1.4.7
Release: 8%{?dist}
Summary: Boot large ruby/rails apps faster
License: MIT
URL: https://github.com/Shopify/bootsnap
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# The bootsnap gem doesn't ship with the test suite.
# You may check it out like so:
# git clone http://github.com/Shopify/bootsnap.git --no-checkout
# cd bootsnap && git archive -v -o bootsnap-1.4.7-tests.txz v1.4.7 test/
Source1: %{gem_name}-%{version}-tests.txz

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel >= 2.0.0
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(mocha)
# Bundler is needed just for one test, that is failing atm.
# BuildRequires: rubygem(bundler)
BuildRequires: rubygem(msgpack)
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc

%description
Bootsnap is a library that plugs into Ruby, with optional support
for ActiveSupport and YAML, to optimize and cache expensive computations.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -a 1

sed -i -e "/^\s*\$CFLAGS / s/^/#/g" \
  ext/bootsnap/extconf.rb

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}/%{gem_name}
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/%{gem_name}/*.so %{buildroot}%{gem_extdir_mri}/%{gem_name}

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
# copy the previously unpacked test files
cp -a test/ .%{gem_instdir}
pushd .%{gem_instdir}

# Remove bundler dependency, also, we have
# newer minitest than upstream is testing with.
sed -i -e "/^require('bundler/ s/^/#/" \
  test/test_helper.rb
mv test/bundler_test.rb{,.disable}

# '/usr/share/ruby/time.rb' is expected to be in stable prefix,
# but that is failing for some reason. Same issue with bundler.
# https://github.com/Shopify/bootsnap/issues/173
sed -i -e "/^\s*assert(stable.stable?,/ s/^/#/g" \
       -e "/^\s*refute(stable.volatile?,/ s/^/#/g" \
       -e "/^\s*assert(bundler.stable?,/ s/^/#/g" \
       -e "/^\s*Bundler/ s/^/#/g" \
  test/load_path_cache/path_test.rb

ruby -rpathname -rset -Ilib:test:%{buildroot}%{gem_extdir_mri} -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd


%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/bootsnap.gemspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.jp.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/dev.yml
%{gem_instdir}/shipit.rubygems.yml
%{gem_instdir}/bin
%doc %{gem_instdir}/CODE_OF_CONDUCT.md

%changelog
* Sun Dec 25 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.7-8
- Use %%gem_extdir_mri instead of ext for %%check due to ruby3.2 change
  for ext cleanup during build

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Pavel Valena <pvalena@redhat.com> - 1.4.7-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 Vít Ondruch <vondruch@redhat.com> - 1.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.0

* Fri Jul 31 09:47:28 GMT 2020 Pavel Valena <pvalena@redhat.com> - 1.4.7-1
- Update to bootsnap 1.4.7.
  Resolves: rhbz#1862090

* Fri Jul 31 09:19:53 GMT 2020 Vít Ondruch <vondruch@redhat.com> - 1.3.2-7
- Re-enable ARM support. The problem should be gone since Ruby 2.6+.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2-4
- Apply upstream patch to support ruby 2.7
- Unpack test tarball beforehand, as the above patch needs applying
- Rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 18 2019 Pavel Valena <pvalena@redhat.com> - 1.3.2-1
- Update to Bootsnap 1.3.2.
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Pavel Valena <pvalena@redhat.com> - 1.3.0-1
- Initial package
