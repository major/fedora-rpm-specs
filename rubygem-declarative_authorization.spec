# Generated from declarative_authorization-0.5.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name declarative_authorization
%global rubyabi 1.9.1

Summary:       Provides readable authorization rules for Rails
Name:          rubygem-%{gem_name}
Version:       0.5.7
Release:       18%{?dist}
License:       MIT

URL:           http://github.com/stffn/declarative_authorization
Source0:       http://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildArch:     noarch

BuildRequires: ruby(release)
BuildRequires: rubygems-devel

%if 0%{?fc20} || 0%{?el7}
Requires:      ruby(release)
Requires:      rubygems
%endif

Requires:      rubygem(rails) >= 2.1.0

%if 0%{?fc20} || 0%{?el7}
Provides:      rubygem(%{gem_name}) = %{version}
%endif

%description
Provides readable authorization rules for Rails.


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
%{gem_instdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/MIT-LICENSE


%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/CHANGELOG

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 21 2015 Darryl L. Pierce <dpierce@redhat.com> - 0.5.7-4
- Fixed the conditionals for the Requires to be easier to read.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 20 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.5.7-1
- Rebased on declarative_authorization 0.5.7.

* Wed Mar 13 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.5.6-3
- Updated the specfile for the current Ruby packaging guidelines.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan  7 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.5.6-1.2
- Fixed the gem installed to be the rebuilt one.

* Thu Dec 20 2012 Darryl L. Pierce <dpierce@redhat.com> - 0.5.6-1.1
- Cleaned up the specfile to match current Ruby packaging guidelines.

* Sun Sep 23 2012 Darryl L. Pierce <dpierce@redhat.com> - 0.5.6-1
- Rebased on declarative_authorization 0.5.6.
- Moved the license file into the main package.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul  8 2012 Darryl L. Pierce <dpierce@redhat.com> - 0.5.5-3
- Removed Group as unused field.
- Removed BuildRequires on ruby(abi).
- Created separate doc subpackage.

* Mon Feb 06 2012 Vít Ondruch <vondruch@redhat.com> - 0.5.5-2
- Rebuilt for Ruby 1.9.3.

* Tue Jan 10 2012 Darryl L. Pierce <dpierce@redhat.com> - 0.5.5-1
- Release 0.5.5 of declarative_authorization.
- Adjusted the description and summary to remove warnings.

* Thu Dec  1 2011 Darryl L. Pierce <dpierce@redhat.com> - 0.5.4-1
- Release 0.5.4 of declarative_authorization.
- Added new files included with this release.

* Thu Jul 21 2011 Darryl L. Pierce <dpierce@redhat.com> - 0.5.3-2
- Added dependency on Rails >= 2.1.0.
- Dropped the Ruby ABI dependency to >= 1.8.

* Wed Jul 20 2011 Darryl L. Pierce <dpierce@redhat.com> - 0.5.3-1
- Release 0.5.3 of declarative_authorization.
- Updated Ruby ABI dependency to >= 1.8.6.

* Sun Apr 17 2011 Darryl L. Pierce <dpierce@redhat.com> - 0.5.2-1
- Initial package
