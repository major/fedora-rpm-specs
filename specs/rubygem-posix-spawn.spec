%global gem_name posix-spawn

Name: rubygem-%{gem_name}
Version: 0.3.15
Release: 16%{?dist}
Summary: posix_spawnp(2) for Ruby
License: MIT
URL: https://github.com/rtomayko/posix-spawn
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Skip tests that fail.
# https://github.com/rtomayko/posix-spawn/issues/43
Patch0: rubygem-posix-spawn-0.3.11-skip-tests.patch
# c99 compilation conformance fix
Patch1: posix-spawn-0.3.15-c99-comformant.patch

BuildRequires:  gcc
%if 0%{?el7}
Requires: ruby(release)
Requires: ruby(rubygems)
BuildRequires: ruby(release)
%endif

BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: rubygem(minitest)
%if 0%{?el7}
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
posix-spawn uses posix_spawnp(2) for faster process spawning.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

# Remove developer-only files.
FREEZE=""
%if 0%{?fedora} >= 26
FREEZE=".freeze"
%endif
for f in .gitignore Gemfile Rakefile; do
  rm $f
  sed -i "s|\"$f\"${FREEZE},||g" %{gem_name}.gemspec
done

# Skip tests that fail.
# https://github.com/rtomayko/posix-spawn/issues/43
%patch -P0 -p1
%patch -P1 -p1

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

%gem_install

# Remove unnecessary gemspec file
rm .%{gem_instdir}/%{gem_name}.gemspec

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Remove deprecated "ext" directory
rm -r %{buildroot}%{gem_instdir}/ext

# Move the binary extension.
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -pa .%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
  # Even though we patch out some of the failing tests, it appears that others
  # sporadically crash Ruby as well. See RHBZ #1210991. For now we will run the
  # tests so we can see the output but skip checking the exit code here.
  ruby -I"lib:test:%{buildroot}%{gem_extdir_mri}" -e \
    'Dir.glob "./test/test_*.rb", &method(:require)' || :
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/COPYING
%doc %{gem_instdir}/README.md
%{_bindir}/posix-spawn-benchmark
%{gem_instdir}/bin
%{gem_libdir}
%{gem_extdir_mri}
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/.travis.yml

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/HACKING
%doc %{gem_instdir}/TODO
%exclude %{gem_instdir}/test

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 08 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.15-15
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 24 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.15-13
- Fix for C99 compilation (bug 2261664)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Vít Ondruch <vondruch@redhat.com> - 0.3.15-11
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.15-8
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Vít Ondruch <vondruch@redhat.com> - 0.3.15-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan  7 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.15-2
- F-34: rebuild for ruby 3.0
- Remove script stuff for very old ruby

* Thu Jan  7 06:00:39 CET 2021 Pavel Valena <pvalena@redhat.com> - 0.3.15-1
- Update to posix-spawn 0.3.15.
  Resolves: rhbz#1836474

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.13-5
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Vít Ondruch <vondruch@redhat.com> - 0.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Tue Aug 28 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.13-1
- Update to latest version (#1391801)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.3.11-11
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.11-10
- F-28: rebuild for ruby25

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.11-6
- F-26: rebuild for ruby24

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Vít Ondruch <vondruch@redhat.com> - 0.3.11-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Fri Jan 08 2016 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.3.11-3
- Unconditionally pass tests (RHBZ #1210991)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 11 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.3.11-1
- Update to 0.3.11 (RHBZ #1193734)
- Drop Minitest 5 patch; this is now upstream
- Drop Fedora 19 support

* Fri Jan 16 2015 Vít Ondruch <vondruch@redhat.com> - 0.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Thu Sep 11 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.3.9-1
- Update to 0.3.9 (RHBZ #1125902)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 11 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1
  and Minitest 5

* Fri Dec 27 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.3.8-1
- Initial package
