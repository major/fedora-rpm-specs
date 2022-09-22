# Generated from thread_safe-0.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name thread_safe

Name: rubygem-%{gem_name}
Version: 0.3.6
Release: 12%{?dist}
Summary: Thread-safe collections and utilities for Ruby
# jsr166e.LondAdder, jsr166e.Striped64, jsr166e.ConcurrentHashMapV8
# and their Ruby ports are Public Domain
License: ASL 2.0 and Public Domain
URL: https://github.com/ruby-concurrency/thread_safe
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(atomic)
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
A collection of data structures and utilities to make thread-safe
programming in Ruby easier.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Fix for rpmlint
sed -i -e 's|^#!/usr/bin/env ruby|#!/usr/bin/ruby|' \
  %{buildroot}%{gem_instdir}/examples/bench_cache.rb

%check
pushd ./%{gem_instdir}
sed -i "/^require 'simplecov'/ s/^/#/" spec/spec_helper.rb
sed -i "/^SimpleCov.formatter/,/^end$/ s/^/#/" spec/spec_helper.rb
sed -i "/^require 'coveralls'/ s/^/#/" spec/spec_helper.rb
sed -i "/logger/ s/^/#/" spec/spec_helper.rb
rspec -Ilib spec

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%exclude %{gem_instdir}/ext
%{gem_libdir}
%exclude %{gem_instdir}/thread_safe.gemspec
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/spec
# Remove .gitignore files for rpmlint
# https://github.com/ruby-concurrency/thread_safe/pull/31
%exclude %{gem_instdir}/spec/.gitignore
%exclude %{gem_instdir}/spec/support/.gitignore
%exclude %{gem_instdir}/spec/thread_safe/.gitignore
%{gem_instdir}/tasks
%{gem_instdir}/yard-template


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 rebase-helper <rebase-helper@localhost.local> - 0.3.6-1
- Update to 0.3.6

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 24 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.3.5-1
- Update to 0.3.5
- New upstream URL.
- Remove extraneous BR: ruby. This is covered by BR: ruby(release).
- Patch to make simplecov and coveralls optional dependencies.
- Remove optional minitest/reporters dependency.
- Drop Rakefile shebang removal. This is fixed upstream.
- Use %%license macro.

* Mon Aug 18 2014 Josef Stribny <jstribny@redhat.com> - 0.3.4-1
- Update to 0.3.4

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 08 2014 Josef Stribny <jstribny@redhat.com> - 0.3.3-1
- Update to 0.3.3

* Tue Feb 04 2014 Josef Stribny <jstribny@redhat.com> - 0.1.3-3
- Add Public Domain to licenses

* Mon Jan 27 2014 Josef Stribny <jstribny@redhat.com> - 0.1.3-2
- Fix license

* Wed Oct 30 2013 Josef Stribny <jstribny@redhat.com> - 0.1.3-1
- Update to thread_safe 0.1.3

* Tue Jul 30 2013 Josef Stribny <jstribny@redhat.com> - 0.1.2-3
- Remove shebang from Rakefile
- Add BR: rubygem(atomic)

* Mon Jul 29 2013 Josef Stribny <jstribny@redhat.com> - 0.1.2-2
- Remove JRuby for now

* Fri Jul 26 2013 Josef Stribny <jstribny@redhat.com> - 0.1.2-1
- Update to 0.1.2
- Add JRuby support

* Thu May 09 2013 Josef Stribny <jstribny@redhat.com> - 0.1.0-1
- Initial package
