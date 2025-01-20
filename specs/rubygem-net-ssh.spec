# Generated from net-ssh-2.2.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name net-ssh

Name: rubygem-%{gem_name}
Version: 7.3.0
Release: 2%{?dist}
Summary: Net::SSH: a pure-Ruby implementation of the SSH2 client protocol
License: MIT
URL: https://github.com/net-ssh/net-ssh
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/net-ssh/net-ssh.git --no-checkout
# cd net-ssh && git archive -v --format=tar.gz -o net-ssh-7.3.0-tests.tar.gz v7.3.0 test/
Source1: %{gem_name}-%{version}-tests.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(base64)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(mocha)
# rubygem-ed25519 support
BuildRequires: rubygem(bcrypt_pbkdf)
BuildRequires: rubygem(ed25519)
Recommends: rubygem(bcrypt_pbkdf)
Recommends: rubygem(ed25519)
BuildArch: noarch

%description
Net::SSH: a pure-Ruby implementation of the SSH2 client protocol. It allows
you to write programs that invoke and interact with processes on remote
servers, via SSH2.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b1

%gemspec_add_dep -g openssl

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/test test

# This requires rubygem-x25519 which is not yet in Fedora.
mv test/transport/kex/test_curve25519_sha256.rb{,.disable}

# Fedora switched from zlib to zlib-ng -> causes tests with compression to fail
# (compressed data is not same byte-to-byte) -> disable tests with compression
# https://github.com/net-ssh/net-ssh/issues/965
sed -i 's;\[false, :standard\].each do |compress|;[false].each do |compress|;g' test/transport/test_packet_stream.rb

# Use custom upstream OpenSSL config to enable all tested ciphers. There is
# a plan to remove outdated ciphers (see "To remove") which might make this
# unnecessary.
# https://github.com/net-ssh/net-ssh/issues/705
OPENSSL_CONF="$PWD/test/openssl3.conf" ruby -Ilib:test test/test_all.rb
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/appveyor.yml
%exclude %{gem_instdir}/{D,d}ocker*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGES.txt
%{gem_instdir}/Gemfile*
%doc %{gem_instdir}/ISSUE_TEMPLATE.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Manifest
%doc %{gem_instdir}/THANKS.txt
%{gem_instdir}/Rakefile
%{gem_instdir}/support
%doc %{gem_instdir}/SECURITY.md
%doc %{gem_instdir}/DEVELOPMENT.md
# Required to run tests
%{gem_instdir}/net-ssh.gemspec
%exclude %{gem_instdir}/net-ssh-public_cert.pem

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 06 2024 Zdenek Zambersky <zzambers@redhat.com> - 7.3.0-1
- Update to net-ssh 7.3.0
  Resolves: rhbz#2227501

* Wed Nov 06 2024 Zdenek Zambersky <zzambers@redhat.com> - 7.1.0-5
- Enable whole test suite to fix FTBFS
  Resolves: rhbz#2301254
  Resolves: rhbz#2311882

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 03 2023 Zdenek Zambersky <zzambers@redhat.com> - 7.1.0-1
- Update to net-ssh 7.1.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Jarek Prokop <jprokop@redhat.com> - 6.1.0-6
- Support ed25519 cipher.
  Resolves: rhbz#2087076

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr 21 2022 Jarek Prokop <jprokop@redhat.com> - 6.1.0-4
- Fix compatibility with rubygem-openssl 3.0.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Pavel Valena <pvalena@redhat.com> - 6.1.0-1
- Update to net-ssh 6.1.0.
  Resolves: rhbz#1825780

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 07 2020 Pavel Valena <pvalena@redhat.com> - 5.2.0-1
- Update to net-ssh 5.2.0.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Pavel Valena <pvalena@redhat.com> - 5.1.0-1
- Update to net-ssh 5.1.0.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 pvalena <pvalena@redhat.com> - 5.0.2-1
- Update to net-ssh 5.0.2.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 03 2018 Vít Ondruch <vondruch@redhat.com> - 4.2.0-2
- Require Logger to fix FTBFS.

* Wed Jan 31 2018 Pavel Valena <pvalena@redhat.com> - 4.2.0-1
- Update to Net::SSH 4.2.0.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 24 2017 Vít Ondruch <vondruch@redhat.com> - 4.1.0-1
- Update to Net::SSH 4.1.0.

* Mon Feb 06 2017 Vít Ondruch <vondruch@redhat.com> - 3.2.0-3
- Add dependency on OpenSSL, which was gemified in Ruby 2.4.

* Mon Feb 06 2017 Vít Ondruch <vondruch@redhat.com> - 3.2.0-2
- Fix Ruby 2.4 compatibility.

* Fri Jul 29 2016 Vít Ondruch <vondruch@redhat.com> - 3.2.0-1
- Update to Net::SSH 3.2.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jul 03 2014 Vít Ondruch <vondruch@redhat.com> - 2.9.1-1
- Update to net-ssh 2.9.1.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 08 2013 Vít Ondruch <vondruch@redhat.com> - 2.6.6-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Update to net-ssh 2.6.6.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.2.1-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 04 2011 Shreyank Gupta <sgupta@redhat.com> - 2.2.1-1
- Updated to version 2.2.1-1

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 24 2010 Adam Tkac <atkac redhat com> - 2.0.23-5
- rebuild to ensure F14 has higher NVR than F13

* Fri Jun 11 2010 Shreyank Gupta <sgupta@redhat.com> - 2.0.23-4
- Bring back the BR: rubygem(rake) and rake test

* Thu Jun 10 2010 Shreyank Gupta <sgupta@redhat.com> - 2.0.23-3
- test command from test/README.txt
- Remove gem "test-unit" line
- Removed Requires rubygem(rake)
- BuildRequires/Requires: rubygem(mocha) for tests

* Thu Jun 10 2010 Shreyank Gupta <sgupta@redhat.com> - 2.0.23-2
- Using %%exclude for setup.rb
- Keeping net-ssh.gemspec for tests
- Moved file-not-utf8 correction to before %%check section

* Wed Jun 09 2010 Shreyank Gupta <sgupta@redhat.com> - 2.0.23-1
- Initial package
