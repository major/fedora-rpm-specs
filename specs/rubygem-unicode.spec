%global gem_name unicode

Name:           rubygem-%{gem_name}
Version:        0.4.4.5
Release:        2%{?dist}
Summary:        Unicode normalization library for Ruby
License:        Ruby
URL:            https://github.com/blackwinter/unicode
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/blackwinter/unicode/issues/7
Source1:        https://www.ruby-lang.org/en/about/license.txt
# This is a C extension linked against MRI, it's not compatible with other 
# interpreters. So we require MRI specifically instead of ruby(release).
BuildRequires:  gcc
BuildRequires:  ruby-devel
BuildRequires:  rubygems-devel

%description
Unicode normalization library for Ruby.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

cp -p %{SOURCE1} .
%gemspec_add_file "license.txt"

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/%{gem_name} %{buildroot}%{gem_extdir_mri}/

find %{buildroot}%{gem_instdir}/tools -type f -name '*.rb' -print0 | xargs -0 chmod +x
find %{buildroot}%{gem_instdir}/tools -type f -name '*.rb' -print0 \
  | xargs -0 -n1 sed -i 's|/usr/local/bin/ruby|/usr/bin/ruby|'


# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
pushd .%{gem_instdir}
ruby -Ilib:$(dirs +1)%{gem_extdir_mri} test/test.rb
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/license.txt
%{gem_extdir_mri}
%{gem_spec}
%{gem_libdir}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README
%{gem_instdir}/Rakefile
%{gem_instdir}/test
%{gem_instdir}/tools
%{gem_instdir}/unicode.gemspec

%changelog
* Wed Jan 08 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.4.5-2
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Sun Nov 03 2024 Dan Callaghan <djc@djc.id.au> - 0.4.4.5-1
- New upstream release 0.4.4.5

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 16 2024 Dan Callaghan <djc@djc.id.au> - 0.4.4.4-11
- Fixed build failures with GCC 14

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Vít Ondruch <vondruch@redhat.com> - 0.4.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.4.4-6
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.4.4-4
- F-36: rebuild against ruby31

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 16 2021 Pavel Valena <pvalena@redhat.com> - 0.4.4.4-1
- Update to unicode 0.4.4.4.
- Update license file.
- Fix URL.
- Add doc subpackage.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 Vít Ondruch <vondruch@redhat.com> - 0.4.4.2-18
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.4.2-15
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Vít Ondruch <vondruch@redhat.com> - 0.4.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.4.4.2-9
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.4.2-8
- F-28: rebuild for ruby25

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Vít Ondruch <vondruch@redhat.com> - 0.4.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Vít Ondruch <vondruch@redhat.com> - 0.4.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Wed Nov 04 2015 Dan Callaghan <dcallagh@redhat.com> - 0.4.4.2-1
- upstream bug fix release 0.4.4.2

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Vít Ondruch <vondruch@redhat.com> - 0.4.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Fri Jan 09 2015 Dan Callaghan <dcallagh@redhat.com> - 0.4.4.1-3
- RHBZ#1179543 include gem.build_complete file so that rubygems doesn't attempt 
  to rebuild the gem

* Mon Jul 14 2014 Dan Callaghan <dcallagh@redhat.com> - 0.4.4.1-2
- run test program in %%check
- use HTTPS for Ruby license source URL

* Thu Jun 05 2014 Dan Callaghan <dcallagh@redhat.com> - 0.4.4.1-1
- updated to upstream release 0.4.4.1
- fixed spec for rubygem changes in F21+

* Tue Jan 28 2014 Dan Callaghan <dcallagh@redhat.com> - 0.4.4-1
- Initial package
