# Generated from httparty-0.6.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name httparty

Name: rubygem-%{gem_name}
Version: 0.21.0
Release: 6%{?dist}
Summary: Makes http fun! Also, makes consuming restful web services dead easy
License: MIT
URL: https://github.com/jnunemaker/httparty
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/jnunemaker/httparty.git && cd httparty
# git archive -v -o httparty-0.21.0-spec.tar.gz v0.21.0 spec/
Source1: %{gem_name}-%{version}-spec.tar.gz
# https://github.com/jnunemaker/httparty/issues/807
# support ruby3.4 hash inspect format change
Patch0:  httparty-issue807-ruby34-inspect-format-change.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.3.0
BuildRequires: rubygem(csv)
BuildRequires: rubygem(mini_mime)
BuildRequires: rubygem(multi_xml)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(webmock)
BuildArch: noarch

%description
Makes http fun! Also, makes consuming restful web services dead easy.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1
(
cd %{_builddir}
%patch -P0 -p1
)

%build
# lib/httparty.rb:require 'json'
%gemspec_add_dep -g json ">= 2.6"
%gemspec_add_dep -g base64 ">= 0.2.0"
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
# Move the tests into place
ln -s %{_builddir}/spec spec

# We are not interested in code coverage.
sed -i '/[sS]imple[cC]ov/ s/^/#/' spec/spec_helper.rb

rspec spec

# This would require Mongrel we don't have and don't want.
# cucumber
popd

%files
%dir %{gem_instdir}
%{_bindir}/httparty
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/Changelog.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Guardfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/cucumber.yml
%doc %{gem_instdir}/docs
%{gem_instdir}/examples
%{gem_instdir}/httparty.gemspec
%{gem_instdir}/script
%{gem_instdir}/website

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Nov 24 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.21.0-5
- Support ruby3.4 hash inspect format change
- Explicitly add base64 dependency

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 05 2024 Vít Ondruch <vondruch@redhat.com> - 0.21.0-1
- Update to HTTParty 0.20.0.
  Resolves: rhbz#1701659
  Related: rhbz#2256881
  Resolves: rhbz#2256882

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 18 2021 Vít Ondruch <vondruch@redhat.com> - 0.18.1-3
- Fix test suite compatibility with Ruby 3.0.0.
  Resolves: rhbz#1923679

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jul 30 2020 Vít Ondruch <vondruch@redhat.com> - 0.18.1-2
- Drop `BR: %%{_bindir}/cucumber` accidental testing leftover.

* Thu Jul 30 2020 Vít Ondruch <vondruch@redhat.com> - 0.18.1-1
- Update to HTTParty 0.18.1.
  Resolves: rhbz#1701659

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 01 2019 Vít Ondruch <vondruch@redhat.com> - 0.16.4-1
- Update to HTTParty 0.16.4.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jul 31 2017 František Dvořák <valtri@civ.zcu.cz> - 0.15.6-1
- Update to 0.15.6 (#1473872)
- EPEL 7 support

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 František Dvořák <valtri@civ.zcu.cz> - 0.15.5-1
- Update to 0.15.5 (#1450238)
- Packaging updates according to gem2rpm template

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Vít Ondruch <vondruch@redhat.com> - 0.14.0-2
- Fix Ruby 2.4 compatibility.

* Tue Oct 18 2016 Vít Ondruch <vondruch@redhat.com> - 0.14.0-1
- Update to HTTParty 0.14.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jul 10 2014 Vít Ondruch <vondruch@redhat.com> - 0.13.1-1
- Update to httparty 0.13.1.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 14 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.10.2-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Updated to Httparty 0.10.2.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 07 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.8.1-1
- Rebuilt for Ruby 1.9.3
- Update to version 0.8.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Mar 01 2011 <stahnma@fedoraproject.org> - 0.7.4-1
- New version upstream

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 07 2010 Michael Stahnke <stahnma@fedorapojrect.org> - 0.6.1-2
- Review updates
- Changed to strict version of rubygem(crack) for Requires

* Sat Aug 07 2010 Michael Stahnke <stahnma@fedoraproject.org> - 0.6.1-1
- Initial package
