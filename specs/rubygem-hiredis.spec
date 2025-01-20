# Generated from hiredis-0.6.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name hiredis

Name: rubygem-%{gem_name}
Version: 0.6.3
Release: 24%{?dist}
Summary: Ruby wrapper for hiredis
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: http://github.com/redis/hiredis-rb
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Get the test suite:
# git clone https://github.com/redis/hiredis-rb.git && cd hiredis-rb/
# git checkout v0.6.3 && tar czvf hiredis-0.6.3-tests.tgz test/
Source1: %{gem_name}-%{version}-tests.tgz
# Build against system hiredis library
Patch0: rubygem-hiredis-0.6.1-Build-against-system-hiredis.patch
# Compatibility with hiredis 1.0.0.
# https://github.com/redis/hiredis-rb/pull/69
Patch1: hiredis-0.6.3-bump-hiredis-to-1.0.0.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: gcc
BuildRequires: hiredis-devel
BuildRequires: rubygem(minitest)

%description
Ruby wrapper for hiredis (protocol serialization/deserialization and blocking
I/O).

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b1


# Remove bundled hiredis
%gemspec_remove_file Dir.glob('vendor/**/*')
rm -rf ./vendor

# Use system hiredis
%patch -P0 -p1
%patch -P1 -p1


%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}/hiredis/ext
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/%{gem_name}/ext/*.so %{buildroot}%{gem_extdir_mri}/%{gem_name}/ext

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/


%check
pushd .%{gem_instdir}
cp -a %{_builddir}/test .

# Tests calling #flush don't work properly.
# https://github.com/redis/hiredis-rb/issues/62
sed -i '/^  def test_recover_from_partial_write/ a skip' \
  test/connection_test.rb
sed -i '/^  def test_eagain_on_write_followed_by_remote_drain/ a skip' \
  test/connection_test.rb

# Make sure the test does not fail in mock with disabled networking.
sed -i -r '/(name or service not known)/ s|(/i)|\|(temporary failure in name resolution)\1|' \
  test/connection_test.rb

ruby -Ilib:$(dirs +1)%{gem_extdir_mri} -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%license %{gem_instdir}/COPYING
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/ext
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Vít Ondruch <vondruch@redhat.com> - 0.6.3-23
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.3-22
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat May 11 2024 Kevin Fenzi <kevin@scrye.com> - 0.6.3-20
- rebuild for hiredis soname bump

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Vít Ondruch <vondruch@redhat.com> - 0.6.3-17
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.3-14
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 11 2022 Vít Ondruch <vondruch@redhat.com> - 0.6.3-12
- Change hiredis 0.13.3 for 1.0.0 compat patch.
  Resolves: rhbz#2046703
  Resolves: rhbz#2042941

* Wed Jan 26 2022 Pavel Valena <pvalena@redhat.com> - 0.6.3-11
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 Vít Ondruch <vondruch@redhat.com> - 0.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.0

* Tue Aug 11 03:22:23 GMT 2020 Pavel Valena <pvalena@redhat.com> - 0.6.3-6
- Fix FTBFS.
  Resolves: rhbz#1865413

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Pavel Valena <pvalena@redhat.com> - 0.6.3-2
- Rebuild for Ruby 2.7: https://fedoraproject.org/wiki/Changes/Ruby_2.7

* Mon Sep 30 2019 Pavel Valena <pvalena@redhat.com> - 0.6.3-1
- Update to hiredis 0.6.3.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Vít Ondruch <vondruch@redhat.com> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 01 2018 Pavel Valena <pvalena@redhat.com> - 0.6.1-1
- Initial package
