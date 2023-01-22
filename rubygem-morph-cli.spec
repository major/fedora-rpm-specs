%global gem_name morph-cli

Name:           rubygem-%{gem_name}
Version:        0.2.3
Release:        14%{?dist}
Summary:        Runs Morph scrapers from the command line

License:        MIT
URL:            https://github.com/openaustralia/morph-cli
Source0:        https://github.com/openaustralia/morph-cli/archive/v%{version}.tar.gz
Patch0:         0001-Disallow-gzip.patch
BuildArch:      noarch

BuildRequires:  rubygems-devel
BuildRequires:  git
Requires:       ruby(release) >= 1.9
Requires:       rubygem(thor) >= 0.17
Requires:       rubygem(rest-client)
Requires:       rubygem(archive-tar-minitar)
Requires:       rubygems

%description
Actually it will run them on the Morph server identically to the real thing.
That means not installing a bucket load of libraries and bits and bobs that are
already installed with the Morph scraper environments.


%prep
%setup -qn %{gem_name}-%{version}
%patch0 -p1

# Someone had a clever idea to use "git ls-files" to obtain the list of
# sources. Oh well, let's just pretend we're an actual Git checkout.
git init
git config user.name 'Fedora package maintainers'
git config user.email '%{name}-owner@fedoraproject.org'
git add lib
git commit -m 'Import'


%build
gem build %{gem_name}.gemspec
%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{_bindir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
cp -a ./%{_bindir}/* %{buildroot}%{_bindir}


%files
%{_bindir}/*
%dir %{gem_instdir}
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_docdir}
%{gem_spec}
%doc LICENSE.txt README.md scraper.rb


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-11
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov  6 10:34:43 CET 2020 Vít Ondruch <vondruch@redhat.com> - 0.2.3-9
- Drop 'BR: rubygem(json_pure)' which is not really needed.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 29 2017 Lubomir Rintel <lkundrak@v3.sk> - 0.2.3-1
- New upstream release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 15 2015 Lubomir Rintel <lkundrak@v3.sk> - 0.2.2-1
- New upstream release

* Sat Jul 12 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.2.1-2
- Disallow gzip TE

* Sun Jun  8 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.2.1-1
- New upstream release

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.2-1
- Initial packaging
