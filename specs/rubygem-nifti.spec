%global gem_name nifti

Name:          rubygem-%{gem_name}
Version:       0.0.2
Release:       27%{?dist}
Summary:       A pure Ruby API to the NIfTI Neuroimaging Format
License:       LGPL-3.0-or-later
URL:           https://github.com/brainmap/%{gem_name}
Source0:       https://rubygems.org/downloads/%{gem_name}-%{version}.gem
Patch0:        nifti-0.0.2-deprecation.patch
Patch1:	       nifti-0.0.2-spec_config.patch
Patch2:        nifti-0.0.2-feature.patch
Patch3:        nifti-0.0.2-fix_endianness.patch
BuildRequires: ruby
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(cucumber)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(narray)
BuildRequires: rubygem(simplecov)
BuildArch: noarch


%description
Ruby NIfTI is a pure-ruby library for handling NIfTI data in Ruby.
NIfTI (Neuroimaging Informatics Technology Initiative) is an image format 
designed primarily for the storage and analysis of MRI & PET imaging data.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%patch 0 -p0
%patch 1 -p0
%patch 2 -p0
%patch 3 -p0

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%check
pushd .%{gem_instdir}
  # rspec 2 -> 3
  grep -rl be_true spec | xargs sed -i -e 's|be_true|be_truthy|'
  grep -rl be_false spec | xargs sed -i -e 's|be_false|be_falsey|'
  rspec -Ilib --tag ~skip_in_ci spec
  ruby -Ilib -S cucumber --tags 'not @skip_in_ci'
popd

%files
%dir  %{gem_instdir}
%doc %{gem_instdir}/README.markdown
%doc %{gem_instdir}/CHANGELOG
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_spec}
%exclude  %{gem_instdir}/.*
%{gem_instdir}/features
%exclude  %{gem_cache}


%files doc
%doc %{gem_docdir}
%exclude  %{gem_instdir}/Gemfile
%exclude  %{gem_instdir}/Rakefile
%exclude  %{gem_instdir}/nifti.gemspec
%exclude  %{gem_instdir}/spec
%exclude  %{gem_docdir}/rdoc



%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul  17 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0.2-25
- convert license to SPDX

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 18 2023 Ilia Gradina <ilgrad@fedoraproject.org> - 0.0.2-23
- byte order fixed for building on s390x

* Mon Jul 31 2023 Ilia Gradina <ilgrad@fedoraproject.org> - 0.0.2-22
- fix tests

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.2-17
- Actually execute cucumber test

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Apr  7 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.2-15
- Use rspec 3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Mar 13 2016 Ilya Gradina <ilya.gradina@gmail.com> - 0.0.2-5
- change in files

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Ilya Gradina <ilya.gradina@gmai.com> - 0.0.2-3
- change check and description section

* Fri Dec 11 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.0.2-2
- change license, delete group

* Wed Dec 09 2015 Ilya Gradina <ilya.gradina@gmail.com> - 0.0.2-1
- Initial package
