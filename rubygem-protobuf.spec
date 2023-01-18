# Generated from protobuf-3.10.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name protobuf

Name: rubygem-%{gem_name}
Version: 3.10.3
Release: 5%{?dist}
Summary: Google Protocol Buffers serialization and RPC implementation for Ruby
# MIT: main library
# BSD: proto/google/protobuf/compiler/plugin.proto
# and proto/google/protobuf/descriptor.proto
License: MIT and BSD
URL: https://github.com/localshred/protobuf
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# We need the following PRs for compatibility with rubygem-cucumber-messages.
# https://github.com/ruby-protobuf/protobuf/pull/410
# https://github.com/ruby-protobuf/protobuf/pull/411
# https://github.com/ruby-protobuf/protobuf/pull/415
Patch0: %{name}-%{version}-generate-camel-cased-keys_add-message-from-json_64bit-int-as-json.patch
# https://github.com/ruby-protobuf/protobuf/commit/4d2278e2fb5c365f2cf61ac56204f6e2fcbef09e
# Needed for rails 6.x and higher, already included in 3.10.6
Patch1: %{name}-3.10.6-Use-activesupport_all-in-tests.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(middleware)
BuildRequires: rubygem(activesupport)
BuildRequires: rubygem(timecop)
BuildRequires: rubygem(thor)
BuildRequires: rubygem(thread_safe)
# rubygem-ffi-rzmq is not a runtime dependency.
# BuildRequires: rubygem(ffi-rzmq)
BuildArch: noarch

%description
Google Protocol Buffers serialization and RPC implementation for Ruby.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%patch0 -p1
%patch1 -p1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}

# Avoid bundler dependency
sed -i -e '/require .pry./ s/^/#/g' \
       -e '/require .bundler./ s/^/#/g' \
       -e '/^Bundler\./ s/^/#/g' \
  spec/spec_helper.rb

# Bypass require, as we don't have ffi-rzmq.
# The second test fails without internet access.
sed -i -e "s/require .protobuf\/zmq./require 'protobuf\/rpc\/connectors\/ping'/g" \
       -e '/context .when a select timeout is fired./,/^    end$/ s/^/#/' \
  spec/lib/protobuf/rpc/connectors/ping_spec.rb

# There is not currently a ffi-rzmq gem in Fedora,
# let's disable test suites testing the rzmq capability.
for file in  spec/lib/protobuf/rpc/servers/zmq/server_spec.rb \
             spec/lib/protobuf/rpc/servers/zmq/util_spec.rb \
             spec/functional/zmq_server_spec.rb \
             spec/lib/protobuf/rpc/connectors/zmq_spec.rb ; do
  mv $file{,.disabled}
done
# Another ffi-zmq test that needs disabling.
sed -i -e "/context ..*zmq.*. do/,/^      end$/ s/^/#/g" \
  spec/lib/protobuf/cli_spec.rb

rspec spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/protoc-gen-ruby
%{_bindir}/rpc_server
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/bin
%{gem_libdir}
%{gem_instdir}/profile.html
%{gem_instdir}/proto
%{gem_instdir}/varint_prof.rb
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/protobuf.gemspec
%{gem_instdir}/spec
%doc %{gem_instdir}/CHANGES.md
%{gem_instdir}/install-protobuf.sh

%changelog
* Mon Jan 16 2023 Mamoru TASAKA <mtasaka@feodraproject.org> - 3.10.3-5
- Patch for upstream to support rails 6.x or higher

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Oct 30 2020 Jarek Prokop <jprokop@redhat.com> - 3.10.3-1
- Initial package
