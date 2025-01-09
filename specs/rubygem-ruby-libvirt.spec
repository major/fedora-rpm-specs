# Generated from ruby-libvirt-0.4.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ruby-libvirt

Summary: Ruby bindings for LIBVIRT
Name: rubygem-%{gem_name}
Version: 0.8.4
Release: 2%{?dist}
License: LGPL-2.1-or-later
URL: http://libvirt.org/ruby/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: libvirt-daemon-kvm
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: ruby-devel
BuildRequires: libvirt-devel
BuildRequires: gcc

%description
Ruby bindings for libvirt.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -n %{gem_name}-%{version}

%build
export CONFIGURE_ARGS="--with-cflags='%{build_cflags} -fPIC'"
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# remove shebangs from test files
pushd %{buildroot}%{gem_instdir}/tests
find -type f -name '*.rb' -print | xargs sed -i '/#!\/usr\/bin\/ruby/d'
popd

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}%{gem_instdir}/ext

%check
pushd .%{gem_instdir}

ruby -Ilib:%{buildroot}%{gem_extdir_mri}:test  -e "Dir.glob('./tests/**/test_*.rb').sort.each {|t| require t}"

popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/COPYING
%{gem_libdir}
%{gem_extdir_mri}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/NEWS.rst
%doc %{gem_instdir}/README.rst
%doc %{gem_instdir}/doc/main.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/tests

%changelog
* Tue Jan 07 2025 Vít Ondruch <vondruch@redhat.com> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Thu Jan 02 2025 Jarek Prokop <jprokop@redhat.com> - 0.8.4-1
- Upgrade rubygem-ruby-libvirt to 0.8.4.
  Resolves: rhbz#2023528
  Resolves: rhbz#2292229

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.1-23
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Vít Ondruch <vondruch@redhat.com> - 0.7.1-20
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Vít Ondruch <vondruch@redhat.com> - 0.7.1-17
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.1-15
- F-36: rebuild against ruby31
- Build with -fPIC

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 Vít Ondruch <vondruch@redhat.com> - 0.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.0

* Fri Nov 27 05:45:02 CET 2020 Pavel Valena <pvalena@redhat.com> - 0.7.1-10
- Fix include for Ruby 3.0.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Vít Ondruch <vondruch@redhat.com> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Vít Ondruch <vondruch@redhat.com> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Fri Jul 27 2018 Vít Ondruch <vondruch@redhat.com> - 0.7.1-3
- Add "BR: gcc" to fix FTBFS (rhbz#1606259).

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 Vít Ondruch <vondruch@redhat.com> - 0.7.1-2
- Remove obsoletes, since ruby-libvirt was retired long time ago.

* Sun Feb 18 2018 Chris Lalancette <clalancette@gmail.com> - 0.7.1-1
- Update to upstream 0.7.1 release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.7.0-8
- Rebuilt for switch to libxcrypt

* Tue Jan 09 2018 Chris Lalancette <clalancette@gmail.com> - 0.7.0-7
- Remove inproper Obsoletes

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.0-6
- F-28: rebuild for ruby25

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Vít Ondruch <vondruch@redhat.com> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Thu Sep 22 2016 Chris Lalancette <clalancette@gmail.com> - 0.7.0-1
- Update to upstream 0.7.0 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Vít Ondruch <vondruch@redhat.com> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Fri Nov 20 2015 Chris Lalancette <clalancette@gmail.com> - 0.6.0-1
- Update to upstream 0.6.0 release

* Mon Sep 14 2015 Josef Stribny <jstribny@redhat.com> - 0.5.2-4
- Add requirement on libvirt-daemon-kvm

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Josef Stribny <jstribny@redhat.com> - 0.5.2-2
- Fix obsoletes for ruby-libvirt

* Tue Jun 09 2015 Josef Stribny <jstribny@redhat.com> - 0.5.2-1
- Update to 0.5.2

* Fri Jan 16 2015 Vít Ondruch <vondruch@redhat.com> - 0.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 17 2014 Vít Ondruch <vondruch@redhat.com> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.4.0-4
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.4.0-1
- Initial package
