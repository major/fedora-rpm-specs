%global gem_name hashr

Summary: Simple Hash extension to make working with nested hashes
Name: rubygem-%{gem_name}
Version: 2.0.1
Release: 10%{?dist}
License: MIT
URL: http://github.com/svenfuchs/hashr
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygems
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
Simple Hash extension to make working with nested hashes (e.g. for
configuration) easier and less error-prone.

%package doc
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%exclude %{gem_cache}
%{gem_spec}
%license %{gem_instdir}/MIT-LICENSE
%exclude %{gem_instdir}/.*

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%exclude %{gem_instdir}/spec

%check
pushd .%{gem_instdir}
rspec -rspec_helper spec
popd

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Pavel Valena <pvalena@redhat.com> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Pavel Valena <pvalena@redhat.com> - 2.0.1-1
- Update to hashr 2.0.1.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.22-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.22-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.22-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jul 07 2014 Josef Stribny <jstribny@redhat.com> - 0.0.22-6
- Fix test suite for minitest 5

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 13 2013 Miroslav Suchý <msuchy@redhat.com> - 0.0.22-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 09 2012 Miroslav Suchý <msuchy@redhat.com> 0.0.22-1
- 874857 - rebase to rubygem-hashr-0.0.22 (msuchy@redhat.com)

* Wed Aug 08 2012 Miroslav Suchý <msuchy@redhat.com> 0.0.21-3
- 845799 - -doc subpackage require the main package (msuchy@redhat.com)
- 845799 - move test/ Gemfile* and Rakefile to -doc subpackage
  (msuchy@redhat.com)
- 845799 - simplify test (msuchy@redhat.com)

* Wed Aug 08 2012 Miroslav Suchý <msuchy@redhat.com> 0.0.21-2
- run test only in F17+ (msuchy@redhat.com)
- 845799 - use test-suite (msuchy@redhat.com)
- 845799 - use rubygems macros (msuchy@redhat.com)
- create subpackage rubygem-hashr-doc (msuchy@redhat.com)
- rubygem-hashr is released under MIT license (msuchy@redhat.com)
- 845799 - use %%global instead %%define (msuchy@redhat.com)

* Sat Aug 04 2012 Miroslav Suchý <msuchy@redhat.com> 0.0.21-1
- remove generated yardoc (msuchy@redhat.com)
- remove unused macros (msuchy@redhat.com)
- make summary shorter (msuchy@redhat.com)
- rebase to 0.0.21 (msuchy@redhat.com)

* Wed Jul 04 2012 Miroslav Suchý <msuchy@redhat.com> 0.0.19-3
- edit spec for Fedora 17 (msuchy@redhat.com)

* Tue Feb 28 2012 Brad Buckingham <bbuckingham@redhat.com> 0.0.19-2
- hashr - backing down to 0.0.19-2 (bbuckingham@redhat.com)

* Tue Feb 28 2012 Brad Buckingham <bbuckingham@redhat.com> 0.0.20-1
- hashr spec - update content autogenerated by gen2rpm (bbuckingham@redhat.com)

* Tue Feb 28 2012 Brad Buckingham <bbuckingham@redhat.com> - 0.0.19-1
- Initial package
