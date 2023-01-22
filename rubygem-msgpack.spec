# Generated from msgpack-0.5.9.gem by gem2rpm -*- rpm-spec -*-
%global gem_name msgpack

Name: rubygem-%{gem_name}
Version: 1.4.4
Release: 4%{?dist}
Summary: MessagePack, a binary-based efficient data interchange format
License: ASL 2.0
URL: http://msgpack.org/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: gcc
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires:  rubygem(rspec)
# BuildRequires: rubygem(rake-compiler) < 0.9
# BuildRequires: rubygem(json) < 2
# BuildRequires: rubygem(yard) < 0.9

%description
MessagePack is a binary-based efficient object serialization library. It
enables to exchange structured objects between many languages like JSON. But
unlike JSON, it is very fast and small.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -ar .%{gem_extdir_mri}/{gem.build_complete,%{gem_name}} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

# Disable the test suite for ppc64le
# https://github.com/msgpack/msgpack-ruby/issues/265
%ifnarch ppc64le
%check
pushd .%{gem_instdir}
rm -rf spec/jruby
rspec -Ilib -I%{buildroot}%{gem_extdir_mri} spec
popd
%endif

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/appveyor.yml
%{gem_instdir}/bench
%{gem_libdir}
%{gem_instdir}/msgpack.org.md
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/ChangeLog
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/doclib
%{gem_instdir}/msgpack.gemspec
%{gem_instdir}/spec

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.4-3
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 06 2022 Pavel Valena <pvalena@redhat.com> - 1.4.4-1
- Update to msgpack 1.4.4.
  Resolves: rhbz#1533462

* Wed Jan 26 2022 Vít Ondruch <vondruch@redhat.com> - 1.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan  6 2021 Vít Ondruch <vondruch@redhat.com> - 1.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.0

* Wed Aug 05 2020 Merlin Mathesius <mmathesi@redhat.com> - 1.1.0-13
- Minor conditional fixes for ELN

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.0-11
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Vít Ondruch <vondruch@redhat.com> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Mon Aug 13 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.0-7
- Add C compiler as BR

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.1.0-4
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.0-3
- F-28: rebuild for ruby25

* Fri Jul 21 2017 Sandro Bonazzola <sbonazzo@redhat.com> - 1.1.0-2
- Re-applied changes lost during rebase

* Thu Jun 29 2017 Rich Megginson <rmeggins@redhat.com> - 1.1.0-1
- version 1.1.0

* Thu Jan 19 2017 Sandro Bonazzola <sbonazzo@redhat.com> - 0.5.12-2
- Rebuilding adding ppc64le arch

* Fri Sep 16 2016 Rich Megginson <rmeggins@redhat.com> - 0.5.12-1
- update to 0.5.12

* Mon Jan 05 2015 Graeme Gillies <ggillies@redhat.com> - 0.5.11-1
- Initial package
