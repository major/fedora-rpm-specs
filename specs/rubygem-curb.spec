# Generated from curb-0.7.7.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name curb

Name: rubygem-%{gem_name}
Version: 1.0.5
Release: %autorelease
Summary: Ruby libcurl bindings
License: Ruby
URL: https://github.com/taf2/curb
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Make sure no external connectivity is needed to pass the test suite.
# https://github.com/taf2/curb/pull/448
Patch0: rubygem-curb-1.0.5-Use-TestServlet-url-instead-of-external-connectivity.patch
# Fix build with curl 8.7 and above
# https://github.com/taf2/curb/issues/451
# https://github.com/taf2/curb/pull/453
Patch1: rubygem-curb-1.0.5-fix-callback-function-read_data_handler.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: rubygem(test-unit)
BuildRequires: rubygem(webrick)
BuildRequires: libcurl-devel
# https://github.com/taf2/curb/blob/13144ec5d50ffea0460298cc5de8a0b33db78d22/tests/tc_curl_multi.rb#L42
BuildRequires: %{_sbindir}/ss
BuildRequires: gcc

%description
Curb (probably CUrl-RuBy or something) provides Ruby-language bindings for the
libcurl(3), a fully-featured client-side URL transfer library. cURL and
libcurl live at http://curl.haxx.se/.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%patch 0 -p1
%patch 1 -p1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/


%check
pushd .%{gem_instdir}
# Enable mistakenly disabled test case
# https://github.com/taf2/curb/issues/447
sed -i '/omit/ s/^/#/' tests/tc_curl_multi.rb

ruby -I$(dirs +1)%{gem_extdir_mri} -e 'Dir.glob "./tests/tc_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Rakefile
%{gem_instdir}/doc.rb
%{gem_instdir}/tests

%changelog
%autochangelog
