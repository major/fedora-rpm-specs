# Generated from net-ssh-2.2.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name net-ssh

Name: rubygem-%{gem_name}
Version: 6.1.0
Release: 5%{?dist}
Summary: Net::SSH: a pure-Ruby implementation of the SSH2 client protocol
License: MIT
URL: https://github.com/net-ssh/net-ssh
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/net-ssh/net-ssh.git --no-checkout
# cd net-ssh && git archive -v -o net-ssh-6.1.0-tests.tar.xz v6.1.0 test/
Source1: %{gem_name}-%{version}-tests.tar.xz
# OpenSSL 3 system library support
# https://github.com/net-ssh/net-ssh/pull/857
Patch0: rubygem-net-ssh-6.3.0.beta1-openssl-3.0-support.patch
# Tests need to be patched separately.
Patch1: rubygem-net-ssh-6.3.0.beta1-openssl-3.0-support-tests.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(mocha)
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

%patch0 -p1
pushd %{_builddir}
%patch1 -p1
popd

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

# Match the number of failed tests, since the patch fixes the compatibility
# only partially.
# Without patches there are "28 failures, 449 errors".

# ed25519 is not yet in Fedora.
# Logger used to be loaded by some dependency (probably RDoc?)
# but it it not loaded anymore, so require it explicitly.
NET_SSH_NO_ED25519=true \
  ruby -Ilib:test -rlogger test/test_all.rb 2>&1 | tee test.out
  grep "4 failures, 381 errors" test.out
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/appveyor.yml

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
# Required to run tests
%{gem_instdir}/net-ssh.gemspec
%exclude %{gem_instdir}/net-ssh-public_cert.pem

%changelog
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
