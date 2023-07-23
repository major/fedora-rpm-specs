# Generated from redis-client-0.12.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name redis-client

Name: rubygem-%{gem_name}
Version: 0.12.1
Release: 2%{?dist}
Summary: Simple low-level client for Redis 6+
License: MIT
URL: https://github.com/redis-rb/redis-client
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/redis-rb/redis-client.git && cd redis-client
# git archive -v -o redis-client-0.12.1-tests.txz v0.12.1 test/
Source1: %{gem_name}-%{version}-tests.txz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygem(connection_pool)
BuildRequires: rubygem(minitest)
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

# Do not download Redis, use the system one.
# https://github.com/redis-rb/redis-client/issues/88
sed -i '/build_redis/ s/^/#/' test/test_helper.rb
sed -i '/build_redis/ s/^/#/' test/sentinel/test_helper.rb
sed -i '/def redis_server_bin/,/end/ s/redis_builder.bin_path/"redis-server"/' test/support/servers.rb

# We don't have Toxiproxy in Fedora :/
# https://github.com/redis-rb/redis-client/issues/89
sed -i '/toxiproxy/ s/^/#/' test/env.rb
sed -i '/TOXIPROXY,/ s/^/#/' test/support/servers.rb
sed -i '/REDIS.*79/ s/79/80/' test/support/servers.rb
sed -i '/Toxiproxy\[/i\
      skip' test/redis_client/connection_test.rb

# Required by RedisClientTest#test_encoding.
export LC_ALL=C.UTF-8

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
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 02 2023 Vít Ondruch <vondruch@redhat.com> - 0.12.1-1
- Initial package
