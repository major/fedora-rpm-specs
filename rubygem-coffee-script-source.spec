# Generated from coffee-script-source-1.2.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name coffee-script-source

%global coffee_script_version 1.10.0
%global coffee_script_require js-coffee-script = %{coffee_script_version}


Name: rubygem-%{gem_name}
Version: %{coffee_script_version}
Release: 14%{?dist}
Summary: The CoffeeScript Compiler
License: MIT
URL: http://jashkenas.github.com/coffee-script/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{coffee_script_require}
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: %{coffee_script_require}
BuildRequires: web-assets-devel
BuildArch: noarch
%if 0%{?rhel} == 7
Provides:       rubygem(%{gem_name}) = %{version}
%endif

%description
CoffeeScript is a little language that compiles into JavaScript.
Underneath all of those embarrassing braces and semicolons,
JavaScript has always had a gorgeous object model at its heart.
CoffeeScript is an attempt to expose the good parts of JavaScript
in a simple way.


%package doc
Summary: Documentation for %{name}
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

# Un-bundle coffee-script.js.
ln -sf %{_jsdir}/coffee-script/coffee-script.js \
  %{buildroot}%{gem_libdir}/coffee_script/coffee-script.js


%check
# No test suite included. Some tests are included in rubygem-coffee-script,
# which is the only consumer of this package.


%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Greg Hellings <greg.hellings@gmail.com> - 1.6.3-2
- Set explicit Provides

* Mon Nov 16 2015 Vít Ondruch <vondruch@redhat.com> - 1.10.0-1
- Update to coffee-script-source 1.10.0.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 23 2014 Vít Ondruch <vondruch@redhat.com> - 1.6.3-1
- Update to coffee-script-source 1.6.3.
- Un-bundle coffee-script.js.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 06 2013 Vít Ondruch <vondruch@redhat.com> - 1.6.1-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Update to the coffee-script-source 1.6.1.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Vít Ondruch <vondruch@redhat.com> - 1.3.3-1
- Updated to the coffee-script-source 1.3.3.

* Wed Feb 29 2012 Fotios Lindiakos <fotios@redhat.com> - 1.2.0-2
- Rebuilt with new gem_* macros

* Mon Feb 27 2012 Fotios Lindiakos <fotios@redhat.com> - 1.2.0-1
- Initial package
