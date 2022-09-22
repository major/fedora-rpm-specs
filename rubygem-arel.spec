%global gem_name arel

Name: rubygem-%{gem_name}
Version: 9.0.0
Release: 11%{?dist}
Summary: Arel is a SQL AST manager for Ruby
License: MIT
URL: https://github.com/rails/arel
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rails/arel.git && cd arel
# git checkout v9.0.0 && tar czvf arel-9.0.0-tests.tgz ./test/
Source1: arel-%{version}-tests.tgz
# BigDecimal.new is deprecated in Ruby 2.5.
# https://github.com/rails/arel/commit/cbbe9ed392bfe146fc0871653aad9b619cef8509
Patch0: rubygem-arel-9.0.0-BigDecimal.new-is-deprecated-in-Ruby-2.5.patch
# ruby package has just soft dependency on rubygem(bigdecimal), while
# Arel always requires it.
Requires: rubygem(bigdecimal)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(bigdecimal)
BuildRequires: rubygem(concurrent-ruby)
BuildArch: noarch

%description
Arel is a Relational Algebra for Ruby. It 1) simplifies the generation complex
of SQL queries and it 2) adapts to various RDBMS systems. It is intended to be
a framework framework; that is, you can build your own ORM with it, focusing
on innovative object and collection modeling as opposed to database
compatibility and query generation.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1

pushd %{_builddir}
%patch0 -p1
popd

%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/test test

ruby -Ilib:test -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/README.md

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 17 2020 Vít Ondruch <vondruch@redhat.com> - 9.0.0-6
- Fix Ruby 2.7 compatibility.
  Resolves: rhbz#1799989

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 24 2018 Pavel Valena <pvalena@redhat.com> - 9.0.0-1
- Update to Arel 9.0.0.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 22 2017 Pavel Valena <pvalena@redhat.com> - 8.0.0-1
- Update to Arel 8.0.0.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 11 2016 Vít Ondruch <vondruch@redhat.com> - 7.1.4-1
- Update to Arel 7.1.4.

* Thu Jul 07 2016 Vít Ondruch <vondruch@redhat.com> - 7.0.0-1
- Update to Arel 7.0.0.

* Fri Apr 08 2016 Vít Ondruch <vondruch@redhat.com> - 6.0.3-3
- Explicitly set rubygem(bigdecimal) dependency.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 24 2015 Josef Stribny <jstribny@redhat.com> - 6.0.3-1
- Update to 6.0.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 09 2015 Josef Stribny <jstribny@redhat.com> - 6.0.0-1
- Update to 6.0.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 11 2014 Josef Stribny <jstribny@redhat.com> - 5.0.0-1
- Update to arel 5.0.0
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Josef Stribny <jstribny@redhat.com> - 4.0.0-1
- Update to arel 4.0.0.

* Wed Feb 27 2013 Vít Ondruch <vondruch@redhat.com> - 3.0.2-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Vít Ondruch <vondruch@redhat.com> - 3.0.2-1
- Update to Arel 3.0.2.

* Fri Mar 09 2012 Vít Ondruch <vondruch@redhat.com> - 2.0.9-4
- Fix dependency on BigDecimal.

* Thu Jan 19 2012 Vít Ondruch <vondruch@redhat.com> - 2.0.9-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 24 2011 Vít Ondruch <vondruch@redhat.com> - 2.0.9-1
- Update to Arel 2.0.9
- Removed unnecessary cleanup

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 28 2011 Vít Ondruch <vondruch@redhat.com> - 2.0.7-1
- Updated to Arel 2.0.7 
- Removed some build dependencies

* Fri Jan 07 2011 Vít Ondruch <vondruch@redhat.com> - 2.0.6-3
- Move all documentation into subpackage

* Fri Jan 07 2011 Vít Ondruch <vondruch@redhat.com> - 2.0.6-2
- Clean buildroot

* Fri Jan 7 2011 Vít Ondruch <vondruch@redhat.com> - 2.0.6-1
- Initial package
