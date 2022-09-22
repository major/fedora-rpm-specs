%global gem_name semantic_puppet

%global with_test 1

Name:          rubygem-%{gem_name}
Version:       1.0.4
Release:       5%{?dist}
Summary:       Useful tools for working with Semantic Versions
License:       ASL 2.0
URL:           https://github.com/puppetlabs/semantic_puppet
Source0:       https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires: rubygems-devel
%if 0%{?with_test}
BuildRequires: rubygem(rspec)
%endif
Requires:      ruby(rubygems)

BuildArch:     noarch

%description
Tools used by Puppet to parse, validate, and compare Semantic Versions and
Version Ranges and to query and resolve module dependencies.

%package doc
Summary:       Documentation for %{name}
Requires:      %{name} = %{version}-%{release}
BuildArch:     noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
rm -rf %{buildroot}%{gem_instdir}/{appveyor.yml,.gitignore,.rubocop.yml,.travis.yml,.yardopts}

%check
%if 0%{?with_test}
pushd .%{gem_instdir}
rspec spec
popd
%endif

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/CODEOWNERS
%{gem_instdir}/Rakefile
%{gem_instdir}/semantic_puppet.gemspec
%{gem_instdir}/spec

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.0.4-2
- Include the gemspec in the main package

* Tue Jun 08 2021 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.0.4-1
- Update to 1.0.4

* Tue Jun 01 2021 Joel Capitao <jcapitao@redhat.com> - 1.0.3-1
- First build for rawhide
