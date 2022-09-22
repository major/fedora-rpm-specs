%global gem_name hiera-eyaml

Name:           rubygem-%{gem_name}
Version:        3.2.0
Release:        6%{?dist}
Summary:        Hiera backend for decrypting encrypted yaml properties

License:        MIT
URL:            https://rubygems.org/gems/optimist
Source:         https://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildRequires:  rubygems-devel

BuildArch:      noarch

%description
%{summary}.

%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
%{summary}.

%prep
%autosetup -n %{gem_name}-%{version}
%gemspec_remove_dep -g highline "~> 1.6.19"
%gemspec_add_dep -g highline

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a ./%{_bindir}/* %{buildroot}%{_bindir}

rm -vr %{buildroot}%{gem_instdir}/{.gitignore,.travis.yml,sublime_text,tools}
rm -v %{buildroot}%{gem_cache}

%files
%license %{gem_instdir}/LICENSE.txt
%{_bindir}/eyaml
%dir %{gem_instdir}
%{gem_instdir}/bin

%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/{README,CHANGELOG,HISTORY,PLUGINS}.md
%{gem_instdir}/{Gemfile,Rakefile,%{gem_name}.gemspec}

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 16 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 3.2.0-1
- Initial package
