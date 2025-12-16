# Generated from redis-client-0.12.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name redis-client

%bcond_without regenerate_certs

Name: rubygem-%{gem_name}
Version: 0.22.2
Release: 5%{?dist}
Summary: Simple low-level client for Redis 6+
License: MIT
URL: https://github.com/redis-rb/redis-client
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/redis-rb/redis-client.git && cd redis-client
# git archive -v -o redis-client-0.22.2-tests.txz v0.22.2 test/
Source1: %{gem_name}-%{version}-tests.txz
# https://github.com/redis-rb/redis-client/commit/95c96666868fb60286b473abbef1daa18d827b52
# ruby4_0 removes Ractor#take
Patch0:  redis-client-GH95c9666-Ractor-ruby4_0.patch
# https://github.com/redis-rb/redis-client/issues/270
# https://github.com/redis-rb/redis-client/commit/e5869bf151c2b922fbc52e87edba8f7d1efe8b93
# Adjust to Ractor warning change
Patch1:  redis-client-GHe5869bf-Ractor-warning-change.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygem(benchmark)
BuildRequires: rubygem(connection_pool)
BuildRequires: rubygem(minitest)
%{?with_regenerate_certs:BuildRequires: %{_bindir}/openssl}
BuildRequires: %{_bindir}/redis-server
BuildArch: noarch

%description
Simple low-level client for Redis 6+.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1
(
cd %{_builddir}
%patch -P0 -p1
%patch -P1 -p1
)

%build
# Create the gem as gem install only works on a gem file
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
cp -a %{_builddir}/test .

# Make sure we are using fresh certificates.
%{?with_regenerate_certs: test/fixtures/generate-certs.sh}

# Do not download Redis, use the system one.
# https://github.com/redis-rb/redis-client/issues/88
sed -i '/build_redis/ s/^/#/' test/test_helper.rb
sed -i '/build_redis/ s/^/#/' test/sentinel/test_helper.rb
sed -i '/def redis_server_bin/,/end/ s/redis_builder.bin_path/"redis-server"/' test/support/servers.rb

# Reduce the unix socket nesting, because RPM 4.20+ adds one additional layer
# of nesting and that results in test failures such as:
# `ArgumentError: too long unix socket path (130bytes given but 108bytes max)`
sed -i '/^\s*REDIS_SOCKET_FILE/ s/ServerManager::ROOT\.join("tmp\/redis\.sock")/"\/tmp\/redis\.sock"/' test/support/servers.rb

# We don't have Toxiproxy in Fedora :/
# https://github.com/redis-rb/redis-client/issues/89
sed -i '/toxiproxy/ s/^/#/' test/env.rb
sed -i '/TOXIPROXY,/ s/^/#/' test/support/servers.rb
sed -i '/REDIS.*79/ s/79/80/' test/support/servers.rb
sed -i '/Toxiproxy\[/i\
      skip' test/redis_client/connection_test.rb

ruby -Ilib:test -e '
  Dir["./test/**/*_test.rb"]
    .reject{|i| i.start_with?("./test/sentinel/")}
    .each &method(:require)
'

# TODO: Add sentinel and hiredis tests.
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile.lock
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/redis-client.gemspec

%changelog
* Sun Dec 14 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.22.2-5
- Apply upstream patch for ruby4_0 Ractor warning change

* Sun Nov 30 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.22.2-4
- Add BR: rubygem(benchmark) for testsuite for ruby4_0 explicitly
- Backport upstream patch to support ruby4_0 Ractor change

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 08 2024 Vít Ondruch <vondruch@redhat.com> - 0.22.2-1
- Update to RedisClient 0.22.2.
  Resolves: rhbz#2232505

* Thu Aug 08 2024 Vít Ondruch <vondruch@redhat.com> - 0.15.0-3
- Fix FTBFS due RPM 4.20+ additional nesting.
  Resolves: rhbz#2301257

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Aug 04 2023 Vít Ondruch <vondruch@redhat.com> - 0.15.0-1
- Update to RedisClient 0.15.0.
  Resolves: rhbz#2170659
  Resolves: rhbz#2226405

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 02 2023 Vít Ondruch <vondruch@redhat.com> - 0.12.1-1
- Initial package
