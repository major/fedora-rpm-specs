# Generated from spring-watcher-listen-2.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name spring-watcher-listen

Name: rubygem-%{gem_name}
Version: 2.0.1
Release: 17%{?dist}
Summary: Makes spring watch files using the listen gem
License: MIT
URL: https://github.com/jonleighton/spring-watcher-listen
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Spring 2.1.0+ moved the spring/test to be part of the test suite. Use the
# necessary bits as long as spring-watcher-listen is not fixed (which does not
# look very likely ATM :/)
# git clone https://github.com/rails/spring.git && cd spring
# git archive -v -o spring-2.1.1-tests.tar.gz v2.1.1 test/
Source1: spring-2.1.1-tests.tar.gz
# Fix Ruby 2.5 compatibility.
# https://github.com/jonleighton/spring-watcher-listen/pull/22
Patch0: rubygem-spring-watcher-listen-2.0.1-Really-delete-the-directories.patch
# Fir Ruby 3.0 compatibility.
# https://github.com/rails/spring/pull/632
Patch1: spring-2.1.1-Use-keyword-argument-instead-of-Has-as-optional-argument.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(spring)
BuildRequires: rubygem(listen)
BuildRequires: rubygem(activesupport)
# spring requires bundler as a runtime dependency.
BuildRequires: rubygem(bundler)

BuildArch: noarch

%description
This gem makes Spring watch the filesystem for changes using Listen rather than
by polling the filesystem. On larger projects this means spring will be more
responsive, more accurate and use less cpu on local filesystems.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1

%patch0 -p1

pushd %{_builddir}
%patch1 -p1
popd

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Run the test suite
%check
pushd .%{gem_instdir}
sed -i '/bundler\/setup/ s/^/#/' test/helper.rb

# Use the Spring test suite bits.
sed -i '/spring\/test/ s/spring/support/' test/helper.rb
sed -i '/spring\/test/ s/^/#/' test/unit_test.rb
# spring-watcher-listen does not support #check_stale call, comparing to
# Spring polling or even abstract adapter.
sed -i '/watcher.check_stale/i\        skip' %{_builddir}/test/support/watcher_test.rb

# Run only unit test now, acceptance test wants to compile gems extensions
mv test/acceptance_test.rb{,.disable}
# Asking about tests finish with a error "undefined method callback!".
# https://github.com/jonleighton/spring-watcher-listen/issues/12
ruby -Ilib:test:%{_builddir}/test/ -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spring-watcher-listen.gemspec
%{gem_instdir}/test

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Vít Ondruch <vondruch@redhat.com> - 2.0.1-12
- Fix FTBFS due to Ruby 3.0.

* Thu Oct 01 2020 Vít Ondruch <vondruch@redhat.com> - 2.0.1-2
- Fix test suite compatibility with Spring 2.1.0+.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Vít Ondruch <vondruch@redhat.com> - 2.0.1-4
- Fix Ruby 2.5 compatibility.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Jun Aruga <jaruga@redhat.com> - 2.0.1-1
- Update to 2.0.1

* Thu Jul 28 2016 Jun Aruga <jaruga@redhat.com> - 2.0.0-1
- Initial package
