# Generated from em-websocket-0.5.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name em-websocket

Name: rubygem-%{gem_name}
Version: 0.5.3
Release: 6%{?dist}
Epoch: 1
Summary: EventMachine based WebSocket server
License: MIT
URL: http://github.com/igrigorik/em-websocket
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Test suite depends on specific version of em-websocket-client
# that isn't pushed into master branch:
# https://github.com/igrigorik/em-websocket/blob/master/Gemfile#L5
# Luckily, the package is actually just one small file:
# https://github.com/movitto/em-websocket-client/blob/expose-websocket-api/lib/em-websocket-client.rb
Source1: https://raw.githubusercontent.com/movitto/em-websocket-client/expose-websocket-api/lib/em-websocket-client.rb
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(em-http-request)
BuildRequires: rubygem(em-websocket-client)
BuildRequires: rubygem(em-spec)
BuildRequires: rubygem(http_parser.rb)
BuildArch: noarch

%description
EventMachine based WebSocket server.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
%gemspec_add_dep -g base64 ">= 0.2.0"
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
rspec -I %{dirname:%{SOURCE1}} spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%license %{gem_instdir}/LICENCE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.rdoc
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/em-websocket.gemspec
%{gem_instdir}/examples
%{gem_instdir}/spec

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 18 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:0.5.3-5
- Add runtime dependency for base64 explicitly for ruby34

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jul 31 2023 Jarek Prokop <jprokop@redhat.com> - 1:0.5.3-1
- Upgrade to em-websocket 0.5.3.
  Resolves: rhbz#2227733

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 13 11:47:40 CEST 2020 Pavel Valena <pvalena@redhat.com> - 1:0.5.2-1
- Update to em-websocket 0.5.2.
  Resolves: rhbz#1882156

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 11 2018 Jaroslav Prokop <jar.prokop@volny.cz> - 1:0.5.1-2
- Fix version number to 2 instead of 22, bump epoch as I did earlier in f28 branch.

* Thu Apr 5 2018 Jaroslav Prokop <jar.prokop@volny.cz> - 0.5.1-22
- Enable test suites after needed packages were imported to Fedora.

* Wed Jan 24 2018 Jaroslav Prokop <jar.prokop@volny.cz> - 0.5.1-1
- Initial package
