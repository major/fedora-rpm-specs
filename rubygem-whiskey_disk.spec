%global gem_name whiskey_disk

Summary: Ruby tool for embarrassingly fast deployments
Name: rubygem-%{gem_name}
Version: 0.6.24
Release: 23%{?dist}
License: MIT
URL: http://github.com/flogic/whiskey_disk
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:        ruby(release)
Requires: ruby(rubygems)
Requires:       rubygem(rake)
BuildRequires: rubygems-devel
BuildRequires:  rubygem(rake)
# Commenting out these BRs and %%check right now to fix FTBFS bug 716028
BuildRequires:  rubygem(bacon)
BuildRequires:  rubygem(facon)
BuildArch:      noarch
Provides:       rubygem(%{gem_name}) = %{version}

%description
Opinionated gem for doing fast git-based server deployments.

%package doc
Summary:           Documentation for %{name}
Requires:          %{name} = %{version}-%{release}

%description doc
Documentation for %{name}.

%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{gem_dir}
mv .%{_bindir}/* %{buildroot}%{_bindir}
mv .%{gem_dir}/* %{buildroot}%{gem_dir}
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

rm -f %{buildroot}%{gem_instdir}/.gitignore
rm -f %{buildroot}%{gem_instdir}/*.gemspec

%check
pushd %{buildroot}%{gem_instdir}
RUBYOPT=-I. rake
popd

%files
%{_bindir}/wd*
%dir %{gem_instdir}
%doc %{gem_instdir}/README.markdown
%doc %{gem_instdir}/MIT-LICENSE
%doc %{gem_instdir}/VERSION
%doc %{gem_instdir}/WHY.txt
%doc %{gem_instdir}/CHANGELOG
%{gem_spec}
%{gem_cache}
%{gem_instdir}/bin
%{gem_libdir}


%files doc
%{gem_docdir}
%{gem_instdir}/examples
%{gem_instdir}/Rakefile
%{gem_instdir}/README.integration_specs
%{gem_instdir}/spec
%{gem_instdir}/tasks
%{gem_instdir}/init.rb
%{gem_instdir}/install.rb
# This contains other git repos, used for testing
%{gem_instdir}/scenarios

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.24-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.24-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.24-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.24-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.24-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.24-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.24-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.24-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.24-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.24-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.24-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.24-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.24-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.24-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.24-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.24-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 18 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.6.24-6
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 07 2012 Vít Ondruch <vondruch@redhat.com> - 0.6.24-3
- Fix broken dependency.

* Fri Feb 03 2012 Vít Ondruch <vondruch@redhat.com> - 0.6.24-2
- Rebuilt for Ruby 1.9.3.

* Sun Jan 08 2012 <stahnma@fedoraproject.org> -  0.6.24-1
- Update to 0.6.24
- Fix 716028

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 24 2010 Michael Stahnke <stahnma@fedoraproject.org> - 0.6.2-1
- New version from upstream

* Fri Nov 12 2010 Michael Stahnke <stahnma@fedoraproject.org> - 0.5.4-1
- New version from upstream

* Mon Oct 25 2010 Michael Stahnke <stahnma@fedoraproject.org> - 0.5.3-1
- Initial package
