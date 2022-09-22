%global gem_name openscap

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.4.9
Release: 7%{?dist}
Summary: A FFI wrapper around the OpenSCAP library
License: GPLv2+
URL: https://github.com/isimluk/ruby-openscap
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(ffi) >= 1.0.9
# require libopenscap.so.8 in an arch neutral way
Requires: openscap >= 1.2.1
Requires: openscap < 1:1.4.0
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby >= 1.9.3
# For tests we need:
BuildRequires: openscap >= 1.2.1
BuildRequires: openscap < 1:1.4.0
BuildRequires: bzip2
BuildRequires: %{?scl_prefix}rubygem(rake)
BuildRequires: %{?scl_prefix}rubygem(bundler)
BuildRequires: %{?scl_prefix}rubygem(ffi) >= 1.0.9
BuildRequires: openscap-devel
# End (for the tests we needed)

%if 0%{?fedora} > 18
Requires:      %{?scl_prefix}ruby(release)
BuildRequires: %{?scl_prefix}ruby(release)
# For the tests we need
BuildRequires: %{?scl_prefix}rubygem(test-unit)
%else
Requires:      %{?scl_prefix}ruby(abi) >= %{rubyabi}
BuildRequires: %{?scl_prefix}ruby(abi) >= %{rubyabi}
# For the tests we need
BuildRequires: %{?scl_prefix}rubygem(minitest)
%endif

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
A FFI wrapper around the OpenSCAP library. The %{name}
provides only a subset of openscap functionality.

%package devel
Summary: Development for %{name}
Requires: %{name} = %{version}-%{release}
Requires: rubygems
BuildArch: noarch

%description devel
Development files for %{name}

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
mkdir -p .%{gem_dir}

gem build %{gem_name}.gemspec

%gem_install

%check
rake test

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%doc %{gem_instdir}/COPYING
%doc %{gem_instdir}/README.md
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files devel
%{gem_instdir}/test/
%{gem_instdir}/Rakefile

%files doc
%doc %{gem_docdir}

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Šimon Lukašík <slukasik@redhat.com> - 0.4.9-1
- new stuff is always going on

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 19 2019 Šimon Lukašík <slukasik@redhat.com> - 0.4.8-4
- rebuilt for openscap base package bumping epoch

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 20 2018 Šimon Lukašík <slukasik@redhat.com> - 0.4.9-1
- upgrade to the latest upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 18 2016 Šimon Lukašík <slukasik@redhat.com> - 0.4.7-1
- rubygem-openscap-0.4.7-1

* Tue Jun 07 2016 Šimon Lukašík <slukasik@redhat.com> - 0.4.6-1
- upgrade to the latest upstream release

* Mon Feb 15 2016 Šimon Lukašík <slukasik@redhat.com> - 0.4.5-1
- upgrade to the latest upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 27 2015 Šimon Lukašík <slukasik@redhat.com> - 0.4.4-1
- upgrade to the latest upstream release

* Thu Sep 10 2015 Šimon Lukašík <slukasik@redhat.com> - 0.4.3-1
- upgrade to the new upstream version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 12 2015 Šimon Lukašík <slukasik@redhat.com> - 0.4.2-1
- upgrade to the new upstream version

* Sat Jan 10 2015 Šimon Lukašík <slukasik@redhat.com> - 0.4.1-1
- upgrade to the new upstream version

* Tue Dec 02 2014 Šimon Lukašík <slukasik@redhat.com> - 0.4.0-1
- upgrade to the new upstream version

* Thu Oct 23 2014 Šimon Lukašík <slukasik@redhat.com> - 0.3.0-1
- upgrade to the new upstream version

* Sat Sep 27 2014 Šimon Lukašík <slukasik@redhat.com> - 0.2.0-2
- fix dependency issue

* Fri Jul 25 2014 Šimon Lukašík <slukasik@redhat.com> - 0.2.0-1
- upgrade to the new upstream version

* Wed Jul 16 2014 Šimon Lukašík <slukasik@redhat.com> - 0.1.1-1
- upgrade to the new upstream version

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Šimon Lukašík <slukasik@redhat.com> - 0.1.0-5
- Avoid requires on a specific soname

* Wed May 21 2014 Šimon Lukašík <slukasik@redhat.com> - 0.1.0-4
- Fallback to cp command

* Tue May 20 2014 Šimon Lukašík <slukasik@redhat.com> - 0.1.0-3
- Moved COPYING and readme to the main package
- Created -devel sub-package out of -doc sub-package
- Dropped the word 'currently' from the package description
- Make a use of install instead of cp

* Tue May 06 2014 Šimon Lukašík <slukasik@redhat.com> - 0.1.0-2
- corrected license tag
- avoided macro in comment

* Tue Apr 22 2014 Šimon Lukašík <slukasik@redhat.com> - 0.1.0-1
- Initial package
