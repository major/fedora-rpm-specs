# Generated from bcrypt_pbkdf-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name bcrypt_pbkdf

Name: rubygem-%{gem_name}
Version: 1.1.0
Release: 14%{?dist}
Summary: OpenBSD's bcrypt_pdkfd (a variant of PBKDF2 with bcrypt-based PRF)
# BSD license in files:
#   ext/mri/hash_sha512.c
#   ext/mri/blf.h
#   ext/mri/blowfish.c
# ISC License in file:
#   ext/mri/bcrypt_pbkdf.c
# Automatically converted from old format: MIT and BSD and ISC - review is highly recommended.
License: LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD AND ISC
URL: https://github.com/net-ssh/bcrypt_pbkdf-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/net-ssh/bcrypt_pbkdf-ruby/pull/21
Patch0:  bcrypt_pbkdf-pr21-minitest-5_19-compat.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
BuildRequires: rubygem(rake-compiler) >= 0.9.7
BuildRequires: rubygem(minitest) >= 5

%description
This gem implements bcrypt_pdkfd (a variant of PBKDF2 with bcrypt-based
PRF).


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}
%patch -P0 -p1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
pushd .%{gem_instdir}
ruby -Itest:$(dirs +1)%{gem_extdir_mri} -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/COPYING
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/bcrypt_pbkdf.gemspec
%{gem_instdir}/test

%changelog
* Wed Jan 08 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.0-14
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.0-13
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Vít Ondruch <vondruch@redhat.com> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Sun Sep 17 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.0-8
- Make testsuite compat with minitest 5.19+

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.0-5
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Vít Ondruch <vondruch@redhat.com> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 14 2020 Pavel Valena <pvalena@redhat.com> - 1.1.0-1
- Initial package
  Resolves: rhbz#1672601
