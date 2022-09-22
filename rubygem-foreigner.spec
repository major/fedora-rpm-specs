# Generated from foreigner-0.9.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name foreigner

Summary:       Foreign Keys for Rails
Name:          rubygem-%{gem_name}
Version:       1.7.4
Release:       5%{?dist}
License:       MIT

URL:           http://github.com/matthuhiggins/foreigner
Source0:       http://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildArch:     noarch

BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.5

Requires:      rubygem(activerecord) >= 3.0.0
%if 0%{?fc20} || 0%{?el7}
Requires:      ruby(release)
Requires:      rubygems

Provides:      rubygem(%{gem_name}) = %{version}
%endif



%description
Adds helpers to migrations and correctly dumps foreign keys to schema.rb.


%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}
BuildArch: noarch


%description doc
%{summary}.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

# apply any patches here


%build
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/


%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/MIT-LICENSE


%files doc
%doc %{gem_docdir}

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Pavel Valena <pvalena@redhat.com> - 1.7.4-1
- Update to foreigner 1.7.4.
  Resolves: rhbz#1060120

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 21 2015 Darryl L. Pierce <dpierce@redhat.com> - 1.7.2-1
- Rebased on Foreigner 1.7.2.
- Fixed the conditionals for the Requires to be easier to read.

* Tue Jun 10 2014 Darryl L. Pierce <dpierce@redhat.com> - 1.6.1-1
- Rebased on Foreign 1.6.1.
- Removed elements from specfile for < F19.
- Resolves: BZ#1107122

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 23 2013 Darryl L. Pierce <dpierce@redhat.com> - 1.6.0-1
- Rebased on foreigner 1.6.0.

* Mon Sep  9 2013 Darryl L. Pierce <dpierce@redhat.com> - 1.5.0-1
- Rebased on foreigner 1.5.0.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Darryl L. Pierce <dpierce@redhat.com> - 1.4.2-1
- Rebased on foreigner 1.4.2.

* Mon Apr  8 2013 Darryl L. Pierce <dpierce@redhat.com> - 1.4.1-1
- Rebased on foreigner 1.4.1.

* Wed Mar 13 2013 Darryl L. Pierce <dpierce@redhat.com> - 1.4.0-2
- Updated the specfile to meet current Ruby packaging guidelines.

* Tue Feb 26 2013 Darryl L. Pierce <dpierce@redhat.com> - 1.4.0-1
- Rebased on Foreigner 1.4.0.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 16 2013 Darryl L. Pierce <dpierce@redhat.com> - 1.3.0-1
- Rebased on foreigner 1.3.0.

* Mon Jan  7 2013 Darryl L. Pierce <dpierce@redhat.com> - 1.2.1-1.2
- Package now installs recreated gemfile.

* Thu Dec 20 2012 Darryl L. Pierce <dpierce@redhat.com> - 1.2.1-1.1
- Updated the specfile to reflect current Ruby packaging guidelines.

* Thu Aug  9 2012 Darryl L. Pierce <dpierce@redhat.com> - 1.2.1-1
- Rebased on foreigner release 1.2.1.

* Wed Jul 18 2012 Darryl L. Pierce <dpierce@redhat.com> - 1.2.0-1
- Rebased on foreigner release 1.2.0.
- Removed the tests since they were not invoked.

* Thu Apr 05 2012 Darryl L. Pierce <dpierce@redhat.com> - 1.1.6-1
- Release 1.1.6 of Foreigner.
- Added BuildRequires: {ruby(rubygems), ruby(abi) ruby} fields to the spec.

* Thu Mar 08 2012 Darryl L. Pierce <dpierce@redhat.com> - 1.1.5-1
- Release 1.1.5 of Foreigner.

* Tue Mar 06 2012 Darryl L. Pierce <dpierce@redhat.com> - 1.1.4-1
- Release 1.1.4 of Foreigner.

* Sat Feb 18 2012 Darryl L. Pierce <dpierce@redhat.com> - 1.1.2-1
- Release 1.1.2 of Foreigner.

* Wed Feb 08 2012 Vít Ondruch <vondruch@redhat.com> - 1.1.1-4
- Fixed broken dependencies.

* Thu Feb 02 2012 Vít Ondruch <vondruch@redhat.com> - 1.1.1-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug  9 2011 Darryl L. Pierce <dpierce@redhat.com> - 1.1.1-1
- Release 1.1.1 of Foreigner gem.

* Mon Aug  1 2011 Darryl L. Pierce <dpierce@redhat.com> - 1.1.0-1
- Release 1.1.0 of Foreigner gem.
- Added the doc subpackage.
- Added requirement on rubygem-activerecord >= 3.0.0

* Wed Jul 20 2011 Darryl L. Pierce <dpierce@redhat.com> - 1.0.3-1
- New release of Foreigner gem.
- Added version requirement for rubygems.

* Tue May 10 2011 Darryl L. Pierce <dpierce@redhat.com> - 0.9.2-2
- Fixed license.
- Added dependency on Ruby 1.8.
- Fixed global macros.

* Tue Apr 19 2011 Darryl L. Pierce <dpierce@redhat.com> - 0.9.2-1
- Initial package
