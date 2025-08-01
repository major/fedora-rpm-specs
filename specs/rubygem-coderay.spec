%global gem_name coderay

%if %{undefined rhel}
%bcond_without shoulda
%endif

Name: rubygem-%{gem_name}
Version: 1.1.3
Release: 11%{?dist}
Summary: Fast syntax highlighting for selected languages
License: MIT
URL: http://coderay.rubychan.de
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rubychan/coderay --no-checkout
# cd coderay && git archive -v -o coderay-1.1.3-tests.txz v1.1.3 test spec
Source1: %{gem_name}-%{version}-tests.txz
# Fix test suite for ruby 3.0 change for methods on subclass of Array
# https://github.com/rubychan/coderay/pull/255
Patch0: rubygem-coderay-1.1.3-fix-tests-Array-on-ruby-3.0.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.8.6
BuildRequires: rubygem(test-unit)
BuildRequires: rubygem(rspec)
%if %{with shoulda}
BuildRequires: rubygem(shoulda-context)
%endif
BuildArch: noarch

%description
Fast and easy syntax highlighting for selected languages, written in Ruby.
Comes with RedCloth integration and LOC counter.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1

pushd ..
%patch -P0 -p1
popd

%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
cp -r %{_builddir}/spec .
cp -r %{_builddir}/test .

# Comment out simplecov.
for file in \
  spec/spec_helper.rb \
  test/executable/suite.rb \
  test/functional/for_redcloth.rb \
  test/functional/suite.rb \
  test/unit/suite.rb; do
  sed -i "/^require 'simplecov'/ s/^/#/" "${file}"
done

# See https://github.com/rubychan/coderay/blob/master/rake_tasks/test.rake
LANG=C.UTF-8
ruby ./test/functional/suite.rb
ruby ./test/functional/for_redcloth.rb
ruby ./test/unit/suite.rb
# This test depends on rubygem-shoulda-context.
%if %{with shoulda}
ruby ./test/executable/suite.rb
%endif
rspec spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/coderay
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README_INDEX.rdoc

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 01 2021 Jun Aruga <jaruga@redhat.com> - 1.1.3-1
- update to new version
  Resolves: rhbz#1842013
  Resolves: rhbz#1923366

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Jun Aruga <jaruga@redhat.com> - 1.1.2-5
- Remove extended Tokens#filter for Ruby 2.6 compatibility.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.2-3
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Thu Jul 26 2018 Jun Aruga <jaruga@redhat.com> - 1.1.2-2
- Change license and text, aligning with the output of gem2rpm.

* Wed Jul 25 2018 Jun Aruga <jaruga@redhat.com> - 1.1.2-1
- update to new version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 15 2014 Jan Klepek <jan.klepek at, gmail.com> -1.1.0-3
- dropped dependency on term-ansicolor completely

* Mon Mar 3 2014 Jan Klepek <jan.klepek at, gmail.com> - 1.1.0-2
- term-ansicolor no longer run-time dependency, only build dependency

* Thu Feb 27 2014 Jan Klepek <jan.klepek at, gmail.com> - 1.1.0-1
- update to new version

* Mon Aug 19 2013 Jan Klepek <jan.klepek at, gmail.com> - 1.0.7-1
- update to new version

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 05 2013 Vít Ondruch <vondruch@redhat.com> - 1.0.6-4
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 08 2012 Jan Klepek <jan.klepek at, gmail.com> - 1.0.6-1
- Update to new version

* Mon Feb 06 2012 Vít Ondruch <vondruch@redhat.com> - 1.0.4-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 17 2011 Jan Klepek <jan.klepek at, gmail.com> - 1.0.4-1
- new version

* Sat Oct 15 2011 Jan Klepek <jan.klepek at, gmail.com> - 1.0.0-1
- new version

* Sat Jul 23 2011 Jan Klepek <jan.klepek at, gmail.com> - 0.9.8-1
- new version

* Thu Mar 10 2011 Jan Klepek <jan.klepek at, gmail.com> - 0.9.7-1
- updated to 0.9.7

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.312-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.312-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 03 2009 Jan Klepek <jan.klepekat, gmail.com> - 0.8.312-3
- correct directory ownership, fixed license

* Wed Jun 24 2009 Jan Klepek <jan.klepekat, gmail.com> - 0.8.312-2
- consistent macro usage, rewritten description, removed term-ansicolor during install

* Sun Jun 14 2009 Jan Klepek <jan.klepekat, gmail.com> - 0.8.312-1
- Initial package
