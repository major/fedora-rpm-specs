%global gem_name boxgrinder-core

Summary:     Core library for BoxGrinder
Name:        rubygem-%{gem_name}
Version:     0.3.14
Release:     6%{?dist}
License:     LGPLv3+
URL:         http://boxgrinder.org/
Source0:     http://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/boxgrinder/boxgrinder-core/pull/3
Patch0:      rubygem-boxgrinder-core-0.3.14-Fix-Psych-compatibility.patch
# https://github.com/boxgrinder/boxgrinder-core/pull/2
Patch1:      rubygem-boxgrinder-core-0.3.14-RSpec-are-now-sensitive-to-stub-order-which-is-nice-.patch

%if 0%{fedora} >= 19
Requires: ruby(release)
%else
Requires: ruby(abi) = 1.9.1
%endif

Requires: rubygem(open4)
Requires: rubygem(kwalify)
Requires: rubygem(term-ansicolor)

BuildRequires: rubygem(rake)
BuildRequires: rubygem(open4)
BuildRequires: rubygem(echoe)
BuildRequires: rubygem(kwalify)
BuildRequires: rubygems-devel
BuildRequires: rubygem(term-ansicolor)
BuildRequires: rubygem(rspec)

BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Core library containing files required by BoxGrinder family of projects

%package doc
Summary: Documentation for %{name}
Requires:%{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

pushd ./%{gem_instdir}
%patch0 -p1
%patch1 -p1
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
rspec spec/**/*-spec.rb
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README
%doc %{gem_instdir}/Manifest
%exclude %{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/spec
%{gem_instdir}/Rakefile
%{gem_instdir}/rubygem-%{gem_name}.spec
%{gem_instdir}/%{gem_name}.gemspec
%doc %{gem_docdir}

%changelog
* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.14-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 08 2013 Vít Ondruch <vondruch@redhat.com> - 0.3.14-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 4 2012 Marc Savy <msavy@redhat.com> - 0.3.14-1
- Upstream release: 0.3.14
- [BGBUILD-373] Remove hashery dependency

* Wed Aug 22 2012 Marek Goldmann <mgoldman@redhat.com> - 0.3.13-1
- Upstream release: 0.3.13
- [BGBUILD-364] Validate length of appliance name

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Marek Goldmann <mgoldman@redhat.com> - 0.3.12-1
- Upstream release: 0.3.12
- Support for printing coloured terminal output

* Mon Mar 19 2012 Marek Goldmann <mgoldman@redhat.com> - 0.3.11-1
- Upstream release 0.3.11
- Make sure the spec can be used also for Fedora < 17

* Thu Feb 02 2012 Vít Ondruch <vondruch@redhat.com> - 0.3.10-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Marek Goldmann <mgoldman@redhat.com> - 0.3.10-1
- Upstream release: 0.3.10
- [BGBUILD-324] Add wildcard to packages schema
- [BGBUILD-320] Support variable substitution in any string value field of appliance definition
- [BGBUILD-327] Resolve appliance definition variables in ENV if they are not defined

* Tue Nov 15 2011 Marek Goldmann <mgoldman@redhat.com> - 0.3.9-1
- Upstream release: 0.3.9
- [BGBUILD-312] Discover which user to switch to after root dependent sections have been executed

* Sat Sep 10 2011 Marek Goldmann <mgoldman@redhat.com> - 0.3.8-1
- Upstream release: 0.3.8
- [BGBUILD-305] Incorrect version information in 0.9.6 schema causing validation errors

* Mon Sep 05 2011 Marek Goldmann <mgoldman@redhat.com> - 0.3.7-1
- Upstream release: 0.3.7
- [BGBUILD-276] Import files into appliance via appliance definition file (Files section)

* Fri Aug 26 2011 Marek Goldmann <mgoldman@redhat.com> - 0.3.6-1
- Upstream release: 0.3.6
- [BGBUILD-295] Remove arbitrary 4 CPU limit
- [BGBUILD-296] BG should refer to version and release when building new appliances

* Wed Aug 17 2011 Marek Goldmann <mgoldman@redhat.com> - 0.3.5-1
- Upstream release: 0.3.5
- [BGBUILD-273] Move to RSpec2
- [BGBUILD-275] default_repos setting is not included in schema and is not documented

* Tue Jun 28 2011 Marc Savy <msavy@redhat.com> - 0.3.4-1
- Upstream release: 0.3.4

* Tue Jun 28 2011 Marc Savy <msavy@redhat.com> - 0.3.3-1
- Upstream release: 0.3.3
- [BGBUILD-233] BoxGrinder Build fails to report a missing config file

* Tue May 10 2011 Marek Goldmann <mgoldman@redhat.com> - 0.3.2-1
- Upstream release: 0.3.2
- [BGBUILD-210] In Fedora 14 parameters are not being expanded, and cause early string truncation.
- [BGBUILD-208] Kickstart files not working with 0.9.1
- [BGBUILD-218] Incorrect error messages since revision of parser/validator

* Wed Apr 27 2011 Marek Goldmann <mgoldman@redhat.com> - 0.3.1-1
- Upstream release: 0.3.1
- [BGBUILD-164] Guestfs writes to /tmp/ by default, potentially filling the root filesystem
- [BGBUILD-97] some filesystems dont get unmounted on BG interruption
- [BGBUILD-155] Images built on Centos5.x (el5) for VirtualBox kernel panic (/dev/root missing)
- [BGBUILD-190] Allow to specify kernel variant (PAE or not) for Fedora OS
- [BGBUILD-192] Use IO.popen4 instead open4 gem on JRuby
- [BGBUILD-198] root password is not inherited
- [BGBUILD-156] Validate appliance definition files early and return meaningful error messages
- Removed Rake patch

* Wed Mar 09 2011 Marek Goldmann <mgoldman@redhat.com> - 0.3.0-2
- Added Rake 0.9.0 require patch

* Sat Mar 05 2011 Marek Goldmann <mgoldman@redhat.com> - 0.3.0-1
- Upstream release: 0.3.0
- [BGBUILD-178] Remove sensitive data from logs
- [BGBUILD-168] Support deprecated package inclusion format in appliance definitions
- [BGBUILD-142] Backtraces make output unreadable - add option to enable them, and disable by default
- [BGBUILD-150] Cyclical inclusion dependencies in appliance definition files are not detected/handled
- [BGBUILD-79] Allow to use BoxGrinder Build as a library
- [BGBUILD-127] Use appliance definition object instead of a file when using BG as a library
- [BGBUILD-68] Global .boxgrinder/config or rc style file for config
- [BGBUILD-93] Add Red Hat Enterprise Linux 6 support
- [BGBUILD-133] Support a consolidated configuration file
- [BGBUILD-101] Don't use 'includes' subsection when specifying packages
- [BGBUILD-60] Post section merging pattern for appliances depending on the same appliance
- [BGBUILD-151] Overriding hardware partitions via inclusion in Appliance Definition File causes build failure
- [BGBUILD-100] Enable boxgrinder_build to create a Fedora image with encrypted partition(s)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 12 2010 Marek Goldmann <mgoldman@redhat.com> - 0.1.5-1
- Updated to upstream version: 0.1.5
- [BGBUILD-73] Add support for kickstart files

* Thu Dec 02 2010 Marek Goldmann <mgoldman@redhat.com> - 0.1.4-1
- Updated to new upstream release: 0.1.4

* Wed Nov 17 2010 Marek Goldmann <mgoldman@redhat.com> - 0.1.3-3
- Added: BuildRequires: rubygem(echoe)
- Changed the way Gem is installed and tests are exeuted

* Mon Nov 15 2010 Marek Goldmann <mgoldman@redhat.com> - 0.1.3-2
- Removing unecessary Requires: rubygems

* Mon Nov 15 2010 Marek Goldmann <mgoldman@redhat.com> - 0.1.3-1
- Removed BuildRoot tag
- Adjusted Requires and BuildRequires
- Different approach for testing
- [BGBUILD-98] Use hashery gem

* Tue Nov 09 2010 Marek Goldmann <mgoldman@redhat.com> - 0.1.2-1
- [BGBUILD-87] Set default filesystem to ext4 for Fedora 13+
- [BGBUILD-65] Allow to specify own repos overriding default repos provided for selected OS

* Tue Nov 09 2010 Marek Goldmann <mgoldman@redhat.com> - 0.1.1-2
- [BGBUILD-85] Adjust BoxGrinder spec files for review
- Added 'check' section that executes tests

* Mon Oct 18 2010 Marek Goldmann <mgoldman@redhat.com> - 0.1.1-1
- Initial package
