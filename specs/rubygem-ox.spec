%global gem_name ox

Name:           rubygem-%{gem_name}
Version:        2.14.17
Release:        6%{?dist}
Summary:        Fast XML parser and object serializer

License:        MIT
URL:            http://www.ohler.com/ox
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/ohler55/ox && cd ox
# git archive -v -o rubygem-ox-2.14.17-repo.tgz v2.14.17 test/ examples/
Source1:        %{name}-%{version}-repo.tgz

BuildRequires:  gcc
BuildRequires:  rubygems-devel
BuildRequires:  ruby-devel
BuildRequires:  rubygem(bigdecimal)
BuildRequires:  rubygem(test-unit)
# not automagically detected (from the compiled part)
Requires:       rubygem(bigdecimal)

%description
A fast XML parser and object serializer that uses only standard C lib.
Optimized XML (Ox), as the name implies was written to provide speed optimized
XML handling. It was designed to be an alternative to Nokogiri and other Ruby
XML parsers for generic XML parsing and as an alternative to Marshal for
Object serialization.


%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for %{name}.


%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version} -a1

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

# fix shebang in examples
sed -i -e '1 s,#!/usr/bin/env ruby,#!/usr/bin/ruby,' examples/*


%build
gem build %{gem_name}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}/ox
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/*.so %{buildroot}%{gem_extdir_mri}/ox/
rm -rf %{buildroot}%{gem_instdir}/ext/

# examples - script interpreter, not executable
cp -a examples/ %{buildroot}%{gem_instdir}
sed -i -e 's|/usr/bin/env ruby|/usr/bin/ruby|' %{buildroot}%{gem_instdir}/examples/*
chmod -x %{buildroot}%{gem_instdir}/examples/*


%check
cp -pr test/ ./%{gem_instdir}
pushd ./%{gem_instdir}
ruby -Ilib:test:%{buildroot}%{gem_extdir_mri} test/tests.rb
ruby -Ilib:test:%{buildroot}%{gem_extdir_mri} test/sax/sax_test.rb
rm -rf test/
popd


%files
%dir %{gem_instdir}/
%license %{gem_instdir}/LICENSE
%{gem_extdir_mri}/
%{gem_libdir}/
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}/
%doc %{gem_instdir}/examples/
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 08 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.17-5
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Vít Ondruch <vondruch@redhat.com> - 2.14.17-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Mon Jul 31 2023 František Dvořák <valtri@civ.zcu.cz> - 2.14.17-1
- Update to 2.14.17 (#2185668)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Apr 08 2023 František Dvořák <valtri@civ.zcu.cz> - 2.14.14-1
- Update to 2.14.14 (#2165160)

* Fri Jan 20 2023 František Dvořák <valtri@civ.zcu.cz> - 2.14.13-1
- Update to 2.14.13 (#2161449)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.12-2
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sat Dec 31 2022 František Dvořák <valtri@civ.zcu.cz> - 2.14.12-1
- Update to 2.14.12 (#2156597)

* Sun Dec 25 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.11-4
- Add %%gem_extdir_mri for RUBYLIB for %%check due to ruby3.2 change
  for ext cleanup during build

* Tue Dec 20 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.11-3
- Backport upstream patch for Ox.dump order change on ruby3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr 04 2022 František Dvořák <valtri@civ.zcu.cz> - 2.14.11-1
- Update to 2.14.11 (#2052606)

* Thu Feb 10 2022 František Dvořák <valtri@civ.zcu.cz> - 2.14.8-1
- Update to 2.14.8 (#2052606)

* Mon Feb 07 2022 František Dvořák <valtri@civ.zcu.cz> - 2.14.7-1
- Update to 2.14.7 (#2020043)

* Wed Jan 26 2022 Vít Ondruch <vondruch@redhat.com> - 2.14.4-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar 19 2021 František Dvořák <valtri@civ.zcu.cz> - 2.14.4-1
- Update to 2.14.4 (#1940978)

* Fri Mar 12 2021 František Dvořák <valtri@civ.zcu.cz> - 2.14.3-1
- Update to 2.14.3 (#1936244)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.1-1
- Update to 2.14.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.12.1-1
- Update to 2.12.1 (which supports ruby 2.7)
- F-32: rebuild against ruby 2.7

* Sun Jan 05 2020 František Dvořák <valtri@civ.zcu.cz> - 2.12.0-1
- Update to 2.12.0 (#1714386)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Vít Ondruch <vondruch@redhat.com> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Mon Dec 31 2018 František Dvořák <valtri@civ.zcu.cz> - 2.10.0-1
- Update to 2.10.0
- Added examples

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.8.2-3
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.2-2
- F-28: rebuild for ruby25

* Fri Nov 03 2017 František Dvořák <valtri@civ.zcu.cz> - 2.8.2-1
- Update to 2.8.2 (#1480036)
- Fixes CVE-2017-15928 (#1509206)
- Removed EPEL 7 support (only on epel7 branch now)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 František Dvořák <valtri@civ.zcu.cz> - 2.5.0-1
- Update to 2.5.0 (#1448435)

* Fri Apr 28 2017 František Dvořák <valtri@civ.zcu.cz> - 2.4.13-1
- Update to 2.4.13 (#1441440)

* Thu Mar 23 2017 František Dvořák <valtri@civ.zcu.cz> - 2.4.11-2
- Patch for ruby 2.4 to revert on EPEL 7 (missing RSTRUCT_GET symbol)

* Wed Mar 22 2017 František Dvořák <valtri@civ.zcu.cz> - 2.4.11-1
- Update to 2.4.11 (#1433806)

* Tue Feb 21 2017 František Dvořák <valtri@civ.zcu.cz> - 2.4.9-1
- Update to 2.4.9 (#1413428)
- Add gcc BR as required by C and C++ guidelines

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Vít Ondruch <vondruch@redhat.com> - 2.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Mon Jan 09 2017 František Dvořák <valtri@civ.zcu.cz> - 2.4.7-1
- Update to 2.4.7 (#1400215)

* Wed Nov 23 2016 Vít Ondruch <vondruch@redhat.com> - 2.4.5-2
- Bump the release to get ppc64 builds.

* Fri Oct 28 2016 František Dvořák <valtri@civ.zcu.cz> - 2.4.5-1
- Update to 2.4.5 (#1365703)
- Move README.md to doc subpackage (package review #1344101)

* Tue Jul 05 2016 František Dvořák <valtri@civ.zcu.cz> - 2.4.3-1
- Update to 2.4.3 (#1352504)
- Enable tests on EPEL 7

* Sun Jun 19 2016 František Dvořák <valtri@civ.zcu.cz> - 2.4.1-2
- Add bigdecimal runtime dependency

* Tue May 10 2016 František Dvořák <valtri@civ.zcu.cz> - 2.4.1-1
- Update to 2.4.1 (#1327571)

* Sat Mar 19 2016 František Dvořák <valtri@civ.zcu.cz> - 2.3.0-1
- Update to 2.3.0 (#1310639)

* Sun Feb 07 2016 František Dvořák <valtri@civ.zcu.cz> - 2.2.4-1
- Update to 2.2.4
- Removed F20 from macros
- Add bigdecimal BR

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 František Dvořák <valtri@civ.zcu.cz> - 2.2.3-1
- Update to 2.2.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 27 2015 František Dvořák <valtri@civ.zcu.cz> - 2.1.8-2
- Use the %%license tag
- Move README.md to the main package

* Tue Feb 17 2015 František Dvořák <valtri@civ.zcu.cz> - 2.1.8-1
- Update to 2.1.8

* Tue Feb 10 2015 František Dvořák <valtri@civ.zcu.cz> - 2.1.7-1
- Update to 2.1.7

* Wed Dec 31 2014 František Dvořák <valtri@civ.zcu.cz> - 2.1.6-1
- Update to 2.1.6
- Changed license from BSD to MIT (https://github.com/ohler55/ox/issues/104)
- Tests added

* Fri Oct 03 2014 František Dvořák <valtri@civ.zcu.cz> - 2.1.3-1
- Initial package
