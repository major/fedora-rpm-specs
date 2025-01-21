%global vagrant_plugin_name vagrant-libvirt

%global vagrant_spec_commit 259c55e204674f2b006700c6d351d04250d13b04

Name: %{vagrant_plugin_name}
Version: 0.11.2
Release: 6%{?dist}
Summary: libvirt provider for Vagrant
License: MIT
URL: https://github.com/vagrant-libvirt/vagrant-libvirt
Source0: https://rubygems.org/gems/%{vagrant_plugin_name}-%{version}.gem
# The library has no official release yet. But since it is just test
# dependency, it should be fine to include the source right here.
# wget https://github.com/mitchellh/vagrant-spec/archive/03d88fe2467716b072951c2b55d78223130851a6/vagrant-spec-03d88fe2467716b072951c2b55d78223130851a6.tar.gz
Source1: https://github.com/mitchellh/vagrant-spec/archive/%{vagrant_spec_commit}/vagrant-spec-%{vagrant_spec_commit}.tar.gz

# https://github.com/vagrant-libvirt/vagrant-libvirt/pull/1709
# ruby3.2 fix wrt File.exits? removal and URI.split host result change
# A bit modified: spec/support/libvirt_acceptance_context.rb does not exist
# with 0.7.0 yet
Patch0: vagrant-libvirt-pr1709-ruby32-File_exists-URL-parse.patch
# Allow a mock object to receive synced_folders in config validation spec.
# We do not care about synced folder check when testing MAC configuration.
# https://github.com/vagrant-libvirt/vagrant-libvirt/pull/1721
Patch1: vagrant-libvirt-0.11.2-Allow-a-mock-object-to-receive-synced_folders.patch
# https://github.com/vagrant-libvirt/vagrant-libvirt/pull/1837
# related to https://github.com/ruby/rexml/pull/167
Patch2: vagrant-libvirt-pr1837-testsuite-support-rexml-332.patch
# Get rid of a warning generated due to usage of option
# no longer supported by fog-libvirt
# https://github.com/vagrant-libvirt/vagrant-libvirt/pull/1835
Patch3: vagrant-libvirt-0.12.2-Remove-config-unsupported-by-fog-libvirt.patch

# Enable QEMU Session by default
# https://github.com/vagrant-libvirt/vagrant-libvirt/pull/969
Patch100: vagrant-libvirt-0.11.2-enable-qemu-session-by-default.patch

Requires: ruby(release)
Requires: ruby(rubygems)
Requires: rubygem(diffy)
Requires: rubygem(fog-libvirt) >= 0.6.0
Requires: rubygem(nokogiri) >= 1.6
Requires: rubygem(rexml)
Requires: rubygem(xml-simple)
# Vagrant changed packaging scriptlets in version 1.9.1.
Requires: vagrant >= 1.9.1
# Required by "vagrant package" command (rhbz#1292217).
Recommends: %{_bindir}/virt-sysprep
BuildRequires: vagrant >= 1.9.1
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(diffy)
BuildRequires: rubygem(fog-libvirt)
BuildRequires: rubygem(rake)
BuildRequires: rubygem(rdoc)
BuildRequires: rubygem(rexml)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(thor)
BuildRequires: rubygem(xml-simple)
BuildRequires: rubygems-devel
BuildRequires: %{_bindir}/ps
BuildArch: noarch
Provides: vagrant(%{vagrant_plugin_name}) = %{version}

%description
libvirt provider for Vagrant.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{vagrant_plugin_name}-%{version} -b 1

%patch 0 -p1
%patch 1 -p1
%patch 2 -p1
%patch 3 -p1
%patch 100 -p1

%build
gem build ../%{vagrant_plugin_name}-%{version}.gemspec
%vagrant_plugin_install

%install
mkdir -p %{buildroot}%{vagrant_plugin_dir}
cp -a .%{vagrant_plugin_dir}/* \
        %{buildroot}%{vagrant_plugin_dir}/

%check
# Edit gemspec of vagrant-spec
pushd ../vagrant-spec-%{vagrant_spec_commit}
# Remove the git reference, which is useless in our case.
sed -i '/git / s/^/#/' vagrant-spec.gemspec

# Relax the dependencies, since Fedora ships with newer versions.
sed -i '/thor/ s/~>/>=/' vagrant-spec.gemspec
sed -i '/rspec/ s/~>/>=/' vagrant-spec.gemspec
popd

# Use actual gemspec for tests
cp ../%{vagrant_plugin_name}-%{version}.gemspec .%{vagrant_plugin_instdir}/%{vagrant_plugin_name}.gemspec

pushd .%{vagrant_plugin_instdir}
# Create dummy Gemfile and load dependencies via gemspec file
cat > Gemfile <<EOG
gem 'vagrant'
gem 'base64'
gem 'logger'
gem 'ostruct'
gem 'rdoc'
gem 'rexml'
gem 'vagrant-spec', :path => '%{_builddir}/vagrant-spec-%{vagrant_spec_commit}'
gemspec
EOG

# Unless rsync binary is present, vagrant-libvirt
# decides to use other methods of folder sync in tests,
# breaking set expectations for the test environment.
# https://github.com/vagrant-libvirt/vagrant-libvirt/issues/1415#issuecomment-985272836
# Luckily, it just needs `rsync` in $PATH for tests to pass.
tmpdir=$(mktemp -d)
touch "${tmpdir}/rsync"
chmod +x "${tmpdir}/rsync"

# Suppress deprecation warnings
GEM_PATH=%{vagrant_plugin_dir}:`ruby -e "print Gem.path.join(':')"` \
PATH="$PATH:${tmpdir}" \
bundle exec rspec spec

popd

%files
%dir %{vagrant_plugin_instdir}
%exclude %{vagrant_plugin_instdir}/.*
%license %{vagrant_plugin_instdir}/LICENSE
%{vagrant_plugin_libdir}
%{vagrant_plugin_instdir}/locales
%exclude %{vagrant_plugin_cache}
%{vagrant_plugin_spec}

%files doc
%doc %{vagrant_plugin_docdir}
%doc %{vagrant_plugin_instdir}/README.md
%{vagrant_plugin_instdir}/spec

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Jarek Prokop <jprokop@redhat.com> - 0.11.2-5
- Stop warning being emitted due to setting unsupported option in fog-libvirt.

* Sun Dec 29 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.11.2-5
- Add some gem dependency on testsuite for ruby3.4
- Support REXML 3.3.2 output behavior change

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jan 29 2023 Bart Kus <me@bartk.us> - 0.11.2-1
- Update to vagrant-libvirt 0.11.2.

* Fri Jan 20 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.0-5
- Backport upstream fix for ruby3.2 compatibility
  (File.exists? removal, URI#parse host name result change)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr 11 2022 Vít Ondruch <vondruch@redhat.com> - 0.7.0-3
- Add `BR: rubygem(rake)` to fix FTBFS.

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Pavel Valena <pvalena@redhat.com> - 0.7.0-1
- Update to vagrant-libvirt 0.7.0.
  Resolves: rhbz#1963360

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Pavel Valena <pvalena@redhat.com> - 0.4.1-2
- Fix forward_ports with ruby 3.0.
  Resolves: rhbz#1947885

* Fri Apr 16 2021 Pavel Valena <pvalena@redhat.com> - 0.4.1-1
- Update to vagrant-libvirt 0.4.1.
  Resolves: rhbz#1884945

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 Vít Ondruch <vondruch@redhat.com> - 0.1.2-2
- Drop dependency on Erubis.

* Thu Aug 06 2020 Pavel Valena <pvalena@redhat.com> - 0.1.2-1
- Update to vagrant-libvirt 0.1.2.
  Resolves: rhbz#1833807

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.45-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.45-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 08 2019 Tadej Janež <tadej.j@nez.si> - 0.0.45-3
- Backport/Add useful features and fixes from upstream:
  - Allow customizing of virt-sysprep behaviour on package.
  - Use fetch to obtain environment variable value in package_domain.
  - Halt a domain before packaging it as a box to avoid hard to debug issues.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Pavel Valena <pvalena@redhat.com> - 0.0.45-1
- Update to vagrant-libvirt 0.0.45.
- Enable QEMU Session by default

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.43-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 02 2018 Pavel Valena <pvalena@redhat.com> - 0.0.43-2
- Relax fog-core dependency to work with recently rebased one.

* Mon Oct 01 2018 pvalena <pvalena@redhat.com> - 0.0.43-1
- Update to vagrant-libvirt 0.0.43.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.40-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 08 2017 Pavel Valena <pvalena@redhat.com> - 0.0.40-3
- Fix invalid XML creation on custom domain name (rhbz#1518899).

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Vít Ondruch <vondruch@redhat.com> - 0.0.40-1
- Update to vagrant-libvirt 0.0.40.

* Fri Feb 24 2017 Vít Ondruch <vondruch@redhat.com> - 0.0.37-4
- Fix Vagrant error when network is specified (rhbz#1426565).

* Mon Feb 13 2017 Vít Ondruch <vondruch@redhat.com> - 0.0.37-3
- Fix compatiblity with Vagrant 1.9.1.

* Mon Feb 06 2017 Vít Ondruch <vondruch@redhat.com> - 0.0.37-2
- Use file dependency rather then package dependency.

* Wed Feb 01 2017 Vít Ondruch <vondruch@redhat.com> - 0.0.37-1
- Update to vagrant-libvirt 0.0.37.
- Recommends libguestfs required by "vagrant package" (rhbz#1292217).

* Thu Jan 05 2017 Vít Ondruch <vondruch@redhat.com> - 0.0.36-2
- Fix compatibility with latest Bundler (rhbz#1409381).

* Sun Jan  1 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.36-2
- Relax nokogiri dependency

* Mon Oct 10 2016 Vít Ondruch <vondruch@redhat.com> - 0.0.36-1
- Update to vagrant-libvirt 0.0.36.

* Tue Oct 04 2016 Vít Ondruch <vondruch@redhat.com> - 0.0.35-1
- Update to vagrant-libvirt 0.0.35.

* Wed Aug 03 2016 Vít Ondruch <vondruch@redhat.com> - 0.0.33-1
- Update to vagrant-libvirt 0.0.33.
- Drop the polkit rules. Use libvirt group instead.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Josef Stribny <jstribny@redhat.com> - 0.0.32-1
- Update to 0.0.32

* Mon Oct 05 2015 Josef Stribny <jstribny@redhat.com> - 0.0.31-1
- Update to 0.0.31

* Mon Sep 14 2015 Josef Stribny <jstribny@redhat.com> - 0.0.30-5
- Drop the rest of libvirt deps, they should be pulled via ruby-libvirt

* Mon Sep 14 2015 Josef Stribny <jstribny@redhat.com> - 0.0.30-4
- Drop unnecessary explicit libvirt require

* Fri Jul 10 2015 Dan Williams <dcbw@redhat.com> - 0.0.30-3
- Fix: pass MAC addresses to vagrant to configure interfaces correctly

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Michael Adam <madam@redhat.com> - 0.0.30-1
- Update to 0.0.30 (#1220194)

* Tue Apr 21 2015 Josef Stribny <jstribny@redhat.com> - 0.0.26-2
- Fix: Wait for libvirt to shutdown the domain

* Mon Apr 20 2015 Josef Stribny <jstribny@redhat.com> - 0.0.26-1
- Update to 0.0.26

* Tue Mar 10 2015 Josef Stribny <jstribny@redhat.com> - 0.0.25-1
- Update to 0.0.25

* Wed Jan 28 2015 Michael Adam <madam@redhat.com> - 0.0.24-3
- Ship the polkit rules file as example in the docs package.

* Wed Jan 28 2015 Vít Ondruch <vondruch@redhat.com> - 0.0.24-2
- Do not ship polkit rules for now, since this might have security implications.

* Fri Jan 23 2015 Michael Adam <madam@redhat.com> - 0.0.24-2
- Move README.md to main package as doc.
- Rename 10-vagrant.rules to 10-vagrant-libvirt.rules.
- Move LICENSE to main package as license file.
- Remove shebang from non-executable Rakefile.

* Thu Jan 22 2015 Michael Adam <madam@redhat.com> - 0.0.24-1
- Update to version 0.0.24.

* Thu Jan 22 2015 Michael Adam <madam@redhat.com> - 0.0.23-4
- Fix rake dependency.
- Rename patch file.
- Improve description.

* Thu Nov 27 2014 Vít Ondruch <vondruch@redhat.com> - 0.0.23-4
- Add vagrant(vagrant-libvirt) virtual provide.

* Wed Nov 26 2014 Vít Ondruch <vondruch@redhat.com> - 0.0.23-3
- Enable test suite.
- Update polkit rules.

* Mon Nov 24 2014 Josef Stribny <jstribny@redhat.com> - 0.0.23-2
- Register and unregister the plugin using macros

* Tue Oct 14 2014 Josef Stribny <jstribny@redhat.com> - 0.0.23-1
- Update to 0.0.23
- Use ruby-libvirt 0.5.x
- Move the rest of the doc files to -doc

* Tue Sep 16 2014 Josef Stribny <jstribny@redhat.com> - 0.0.20-2
- Register and unregister automatically

* Wed Sep 10 2014 Josef Stribny <jstribny@redhat.com> - 0.0.20-1
- Update to 0.0.20

* Fri Jun 27 2014 Adam Miller <maxamillion@fedoraproject.org> - 0.0.16-1
- Initial package for Fedora
