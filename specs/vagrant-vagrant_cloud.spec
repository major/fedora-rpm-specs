# Generated from vagrant_cloud-2.0.1.gem by gem2rpm -*- rpm-spec -*-
%global vagrant_plugin_name vagrant_cloud

Name: vagrant-%{vagrant_plugin_name}
Version: 3.0.5
Release: 8%{?dist}
Summary: Vagrant Cloud API Library
License: MIT
URL: https://github.com/hashicorp/vagrant_cloud
Source0: %{vagrant_plugin_name}-%{version}.gem
# Upstream gem doesn't ship tests, pull it from upstream
# git clone --no-checkout https://github.com/hashicorp/vagrant_cloud.git
# git -C vagrant_cloud archive -v -o vagrant_cloud-3.0.5-spec.txz v3.0.5 spec
Source1: %{vagrant_plugin_name}-%{version}-spec.txz
Requires: vagrant
BuildRequires: vagrant
BuildRequires: rubygem(rdoc)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(webmock)
BuildRequires: rubygem(excon)
BuildArch: noarch
Provides: vagrant(%{vagrant_plugin_name}) = %{version}

%description
Ruby library for the HashiCorp Vagrant Cloud API.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{vagrant_plugin_name}-%{version} -b1

%build
gem build ../%{vagrant_plugin_name}-%{version}.gemspec
%vagrant_plugin_install

%install
mkdir -p %{buildroot}%{vagrant_plugin_dir}
cp -a .%{vagrant_plugin_dir}/* \
        %{buildroot}%{vagrant_plugin_dir}/

%check
pushd .%{vagrant_plugin_instdir}
ln -s %{_builddir}/spec .

rspec spec
popd

%files
%dir %{vagrant_plugin_instdir}
%license %{vagrant_plugin_instdir}/LICENSE
%{vagrant_plugin_libdir}
%exclude %{vagrant_plugin_cache}
%{vagrant_plugin_spec}

%files doc
%doc %{vagrant_plugin_docdir}
%doc %{vagrant_plugin_instdir}/README.md

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Mar 22 2021 Pavel Valena <pvalena@redhat.com> - 3.0.5-1
- Initial package
  Resolves: rhbz#1668515
