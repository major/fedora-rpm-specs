# Generated from minitest-1.4.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name minitest

Name: rubygem-%{gem_name}5
Version: 5.8.4
Release: 5%{?dist}
Summary: minitest provides a complete suite of testing facilities
Group: Development/Languages
License: MIT
URL: https://github.com/seattlerb/minitest
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: rubygem(%{gem_name}5) = %{version}

%description
minitest provides a complete suite of testing facilities supporting
TDD, BDD, mocking, and benchmarking.

minitest/unit is a small and incredibly fast unit testing framework.
It provides a rich set of assertions to make your tests clean and
readable.

minitest/spec is a functionally complete spec engine. It hooks onto
minitest/unit and seamlessly bridges test assertions over to spec
expectations.

minitest/benchmark is an awesome way to assert the performance of your
algorithms in a repeatable manner. Now you can assert that your newb
co-worker doesn't replace your linear algorithm with an exponential
one!

minitest/mock by Steven Baker, is a beautifully tiny mock (and stub)
object framework.

minitest/pride shows pride in testing and adds coloring to your test
output. I guess it is an example of how to write IO pipes too. :P
minitest/unit is meant to have a clean implementation for language
implementors that need a minimal set of methods to bootstrap a working
test suite. For example, there is no magic involved for test-case
discovery.

minitest doesn't reinvent anything that ruby already provides, like:
classes, modules, inheritance, methods. This means you only have to
learn ruby to use minitest and all of your regular OO practices like
extract-method refactorings still apply.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -c -T

%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
rm -rf %{buildroot}%{gem_instdir}/Rakefile %{buildroot}%{gem_instdir}/test

%check
pushd .%{gem_instdir}

ruby -Ilib:test -e 'Dir.glob "./test/minitest/test_*.rb", &method(:require)'

popd

%files
%doc %{gem_instdir}/README.rdoc
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.rdoc
%doc %{gem_instdir}/Manifest.txt
%{gem_instdir}/design_rationale.rb

%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Greg Hellings <greg.hellings@gmail.com> - 5.8.4-1
- Updated to new upstream
- Removed Rakefile and installed tests

* Wed Jan 13 2016 Greg Hellings <greg.hellings@gmail.com> - 5.8.1-2
- Modifying for EPEL7
- Changing package name to rubygem-minitest5 to avoid collisions

* Wed Oct 21 2015 Vít Ondruch <vondruch@redhat.com> - 5.8.1-1
- Update to minitest 5.8.1.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 01 2014 Vít Ondruch <vondruch@redhat.com> - 5.3.1-1
- Update to minitest 5.3.1.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 27 2013 Josef Stribny <jstribny@redhat.com> - 4.7.0-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Update to minitest 4.7.0.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 22 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.10.1-1
- 2.10.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 10 2011 Vít Ondruch <vondruch@redhat.com> - 1.6.0-3
- Removed Rake circular dependency.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue May  4 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.6.0-1
- Update to 1.6.0 (#586505)
- Patch0 removed

* Sat Nov 21 2009 Matthew Kent <mkent@magoazul.com> - 1.4.2-3
- Drop Requires on hoe, only used by Rakefile (#538303).
- Move Rakefile to -doc (#538303).

* Sat Nov 21 2009 Matthew Kent <mkent@magoazul.com> - 1.4.2-2
- Better Source (#538303).
- More standard permissions on files.

* Tue Nov 17 2009 Matthew Kent <mkent@magoazul.com> - 1.4.2-1
- Initial package
