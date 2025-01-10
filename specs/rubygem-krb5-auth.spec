%global githash a86ddf2c102a388863f7db99c5597f40ea2ad971
%global shorthash a86ddf2

%define gem_name krb5-auth

Summary: Kerberos binding for Ruby
Name: rubygem-%{gem_name}
Version: 0.8.3
Release: 27.git%{shorthash}%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL: https://github.com/timfel/krb5-auth
# Use tar.gz, convert to gem during build
Source0: https://github.com/timfel/krb5-auth/archive/%{githash}/timfel-%{gem_name}-%{shorthash}.tar.gz
Patch0: rubygem-krb5-auth-fix-metadata.patch
Patch1: rubygem-krb5-auth-fix-warning.patch
Patch2: rubygem-krb5-auth-fix-fsf-address.patch
BuildRequires: gcc
BuildRequires: ruby-devel
BuildRequires: rubygems-devel
BuildRequires: rubygem(rake)
BuildRequires: krb5-devel

%description
Kerberos binding for Ruby

%prep
%setup -q -c -T -a 0
cd %{gem_name}-%{githash}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
cd %{gem_name}-%{githash}
rake gem
cd pkg
%gem_install

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{gem_extdir_mri}
cd %{gem_name}-%{githash}/pkg
cp -pa .%{gem_dir}/* %{buildroot}%{gem_dir}/
rm -f .%{gem_extdir_mri}/gem.build_complete
rm -f .%{gem_extdir_mri}/gem_make.out
rm -f .%{gem_extdir_mri}/mkmf.log
cp -pa .%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

rm -rf %{buildroot}%{gem_instdir}/ext

%files
%dir %{gem_instdir}
%doc %{gem_docdir}
%doc %{gem_instdir}/COPYING
%doc %{gem_instdir}/README
%{gem_instdir}/examples
%{gem_instdir}/Rakefile
%{gem_extdir_mri}/
%exclude %{gem_cache}
%{gem_spec}


%changelog
* Wed Jan 08 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.3-27.gita86ddf2
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.8.3-26.gita86ddf2
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-25.gita86ddf2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-24.gita86ddf2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-23.gita86ddf2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Vít Ondruch <vondruch@redhat.com> - 0.8.3-22.gita86ddf2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-21.gita86ddf2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-20.gita86ddf2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.3-19.gita86ddf2
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-18.gita86ddf2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Vít Ondruch <vondruch@redhat.com> - 0.8.3-17.gita86ddf2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-16.gita86ddf2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-15.gita86ddf2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-14.gita86ddf2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 Vít Ondruch <vondruch@redhat.com> - 0.8.3-13.gita86ddf2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-12.gita86ddf2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-11.gita86ddf2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.3-10.gita86ddf2
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-9.gita86ddf2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-8.gita86ddf2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Vít Ondruch <vondruch@redhat.com> - 0.8.3-7.gita86ddf2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Fri Jan 04 2019 Björn Esser <besser82@fedoraproject.org> - 0.8.3-6.gita86ddf2
- Add BuildRequires: gcc, fixes FTBFS (#1606212)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-5.gita86ddf2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-4.gita86ddf2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.8.3-3.gita86ddf2
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.3-2.gita86ddf2
- F-28: rebuild for ruby25

* Wed Nov 22 2017 Chris Lalancette <clalancette@gmail.com> - 0.8.3-1.gita86ddf2
- Change upstream to https://github.com/timfel/krb5-auth
- Update to upstream 0.8.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Vít Ondruch <vondruch@redhat.com> - 0.7-18
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Vít Ondruch <vondruch@redhat.com> - 0.7-16
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Vít Ondruch <vondruch@redhat.com> - 0.7-14
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 15 2014 Vít Ondruch <vondruch@redhat.com> - 0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Vít Ondruch <vondruch@redhat.com> - 0.7-9
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 03 2012 Vít Ondruch <vondruch@redhat.com> - 0.7-6
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jun 20 2008 Chris Lalancette <clalance@redhat.com> 0.7-1
- Convert from hand-coded makes to a proper Rakefile
- Update to 0.7

* Wed May 21 2008 Alan Pevec <apevec@redhat.com> 0.6-1
- add debuginfo support, taken from rubygem-zoom.spec
- include COPYING file in the gem (for licensing)
- bump the version number to 0.6

* Fri May 16 2008 Alan Pevec <apevec@redhat.com> 0.5-2
- package shared library per Packaging/Ruby guidelines

* Tue Apr 22 2008 Chris Lalancette <clalance@redhat.com> - 0.5-1
- Move project to krb5-auth on RubyForge

* Fri Jan 11 2008 Chris Lalancette <clalance@redhat.com> - 0.4-3
- Update the destroy method to use alternate caches

* Fri Jan 11 2008 Chris Lalancette <clalance@redhat.com> - 0.4-2
- Update the cache method to use alternate caches

* Wed Jan 02 2008 Chris Lalancette <clalance@redhat.com> - 0.4-1
- Initial package

