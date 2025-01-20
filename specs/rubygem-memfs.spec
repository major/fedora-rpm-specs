%global gem_name memfs

Name: rubygem-%{gem_name}
Version: 1.0.0
Release: 24%{?dist}
Summary: Fake file system that can be used for tests
License: MIT
URL: http://github.com/simonc/memfs
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/simonc/memfs/commit/d8e61aba482fe3167e6399a888763ce2a796b30d
Patch0: 0001_file_extname_27_behavior.patch
# https://github.com/simonc/memfs/pull/40
# Fix handling of kwargs with rspec-mocks 3.12+
Patch1: 0002-kwargs-handling-fix.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec) => 3.0
BuildRequires: rubygem(rspec) < 4
BuildArch: noarch

%description
MemFs provides a fake file system that can be used for tests. Strongly
inspired by FakeFS.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




%check
pushd .%{gem_instdir}
# We don't care about coverage.
sed -i '/[Cc]overalls/ s/^/#/' spec/spec_helper.rb
# This is temporary due to https://github.com/simonc/memfs/issues/27
# Include the file if version > 1.0.0
rm spec/fileutils_spec.rb

rspec spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/memfs.png
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/memfs.png
%{gem_instdir}/Rakefile
%{gem_instdir}/memfs.gemspec
%{gem_instdir}/spec
%{gem_instdir}/Guardfile

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 25 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.0-18
- Fix handling of kwargs with rspec-mocks 3.12+

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 1.0.0-12
- Apply upstream patches to support Ruby = 2.7
- Apply latest rubygem packaging guidelines

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 1.0.0-7
- Use original 1.0.0 version

* Sun Feb 18 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 1.0.0-6.20180218git26e0cb9
- Fix directory name for %%prep

* Sun Feb 18 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 1.0.0-5.20180218git26e0cb9
- Fix downloaded tarball name

* Sun Feb 18 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 1.0.0-4.20180218git26e0cb9
- Include patch for new ruby 2.5 Fileutils behavior

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 03 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 1.0.0-1
- Initial package
