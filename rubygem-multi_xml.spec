# Generated from multi_xml-0.4.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name multi_xml

Name: rubygem-%{gem_name}
Version: 0.6.0
Release: 15%{?dist}
Summary: A generic swappable back-end for XML parsing
License: MIT
URL: https://github.com/sferik/multi_xml
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/sferik/multi_xml.git && cd multi_xml/
# git checkout v0.6.0 && tar czf multi_xml-0.6.0-specs.tgz spec/
Source1: multi_xml-%{version}-specs.tgz
# https://github.com/sferik/multi_xml/pull/60
Patch0: multi_xml-ox-white-space.patch
# ruby package has just soft dependency on rubygem(bigdecimal), while
# MultiXML always requires it.
Requires: rubygem(bigdecimal)
BuildRequires: ruby
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(bigdecimal)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(nokogiri)
BuildRequires: rubygem(ox)
BuildRequires: rubygem(rexml)
BuildArch: noarch

%description
Provides swappable XML backends utilizing LibXML, Nokogiri, Ox, or REXML.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version} -a1
%patch0 -p1

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec


%build
gem build %{gem_name}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%check
pushd .%{gem_instdir}
tar xzf %{SOURCE1}

# We don't care about code coverage.
sed -i '/simplecov/,/^end$/ s/^/#/' spec/helper.rb

rspec spec
popd


%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}


%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/*.gemspec


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 13:15:51 CET 2021 Vít Ondruch <vondruch@redhat.com> - 0.6.0-11
- Add `BR: rubygem(rexml)` since it was removed from StdLib in Ruby 3.0.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 19 2017 František Dvořák <valtri@civ.zcu.cz> - 0.6.0-3
- Patch to support Ox > 2.4.11

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Vít Ondruch <vondruch@redhat.com> - 0.6.0-1
- Update to MultiXML 0.6.0.

* Mon Oct 31 2016 František Dvořák <valtri@civ.zcu.cz> - 0.5.5-5
- Enable tests with Ox parser

* Fri Apr 08 2016 Vít Ondruch <vondruch@redhat.com> - 0.5.5-4
- Explicitly set rubygem(bigdecimal) dependency.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 24 2015 Vít Ondruch <vondruch@redhat.com> - 0.5.5-1
- Update to MultiXML 0.5.5.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 04 2013 Vít Ondruch <vondruch@redhat.com> - 0.5.2-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 14 2013 Vít Ondruch <vondruch@redhat.com> - 0.5.2-1
- Update to multi_xml 0.5.2.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 02 2012 Vít Ondruch <vondruch@redhat.com> - 0.4.1-3
- Update review.

* Mon Feb 20 2012 Michael Stahnke <stahnma@fedoraproject.org> - 0.4.1-2
- Update review

* Fri Jan 20 2012 Michael Stahnke <mastahnke@gmail.com> - 0.4.1-1
- Initial package
