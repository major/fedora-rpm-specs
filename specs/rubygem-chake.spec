%global gem_name chake

Name: rubygem-%{gem_name}
Version: 0.21.2
Release: 12%{?dist}
Summary: Serverless configuration management tool for chef
License: MIT
URL: https://gitlab.com/terceiro/chake
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(asciidoctor)
BuildArch: noarch

%description
chake allows one to manage a number of hosts via SSH by combining chef (solo)
and rake. It doesn't require a chef server; all you need is a workstation from
where you can SSH into all your hosts. chake automates copying the
configuration management repository to the target host (including managing
encrypted files), running chef on them, and running arbitrary commands on the
hosts.


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
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

sed -f .%{gem_instdir}/man/readme2man.sed README.md > \
  .%{gem_instdir}/man/chake.adoc || \
  (rm -f .%{gem_instdir}/man/chake.adoc; false)
asciidoctor --backend manpage --out-file .%{gem_instdir}/man/chake.1 \
  .%{gem_instdir}/man/chake.adoc

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{gem_instdir}/man/chake.1 %{buildroot}%{_mandir}/man1

# Run the test suite
%check
pushd .%{gem_instdir}
rspec -Ilib spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/chake
%exclude %{gem_instdir}/coverage
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/bin
%exclude %{gem_instdir}/chake.spec.erb
%{gem_libdir}
%exclude %{gem_instdir}/man
%exclude %{gem_cache}
%exclude %{gem_instdir}/tags
%{gem_spec}
%doc %{_mandir}/man1/*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/ChangeLog.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/chake.gemspec
%{gem_instdir}/examples
%{gem_instdir}/spec

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 16 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 0.21.2-1
- Update version

* Sat Feb 29 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 0.20-1
- Update version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 30 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 0.17.1-1
- Update version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 20 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.17-3
- Revert some changes since the gemspec uses the git repo to query packge files

* Wed Sep 20 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.17-2
- Update spec to comply with new rubygems guidelines

* Wed Sep 20 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.17-1
- Version update

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.16-1
- Version update

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 12 2016 Athos Ribeiro <athoscr@fedoraproject.org> - 0.15-1
- Version update
- Add contact information to changelogs

* Thu Oct 20 2016 Athos Ribeiro <athoscr@fedoraproject.org> - 0.14-1
- Version update

* Fri Jul 1 2016 Athos Ribeiro <athoscr@fedoraproject.org> - 0.13-7
- Remove links for fonts since we want a solution for all rubygem packages

* Tue May 31 2016 Athos Ribeiro <athoscr@fedoraproject.org> - 0.13-6
- Link fonts from proper packages to avoid replication

* Tue May 31 2016 Athos Ribeiro <athoscr@fedoraproject.org> - 0.13-5
- Bump release for rebuild in order to fix checksum problems

* Fri May 20 2016 Athos Ribeiro <athoscr@fedoraproject.org> - 0.13-4
- Install manpages

* Fri May 20 2016 Athos Ribeiro <athoscr@fedoraproject.org> - 0.13-3
- Remove spec file template

* Fri May 20 2016 Athos Ribeiro <athoscr@fedoraproject.org> - 0.13-2
- Remove gitlab-ci

* Fri May 20 2016 Athos Ribeiro <athoscr@fedoraproject.org> - 0.13-1
- Version update

* Wed Jul 15 2015 Athos Ribeiro <athoscr@fedoraproject.org> - 0.7-2
- Fix install by removing unnecessary commands

* Fri Jul 10 2015 Athos Ribeiro <athoscr@fedoraproject.org> - 0.7-1
- Initial package
