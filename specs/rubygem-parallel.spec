%global gem_name parallel

Name:           rubygem-%{gem_name}
Version:        1.12.1
Release:        16%{?dist}
Summary:        Run any kind of code in parallel processes
License:        MIT

URL:            https://github.com/grosser/parallel
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

# Generated tarball of spec tests (not present in the gem file)
# git clone https://github.com/grosser/parallel parallel-repo
# pushd parallel-repo
# git checkout v1.12.1
# git archive -o ../parallel-1.12.1-spec.tar.gz v1.12.1 spec
# popd
# rm -rf parallel-repo
Source1:        %{gem_name}-%{version}-spec.tar.gz

# Disable broken tests
Patch0:         00-disable-broken-tests.patch

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby >= 1.9.3

BuildRequires:  rubygem(bundler)
BuildRequires:  rubygem(rspec)

BuildRequires:  lsof
BuildRequires:  procps-ng

Requires:       lsof
Requires:       procps-ng

BuildArch:      noarch

%description
Run any kind of code in parallel processes.


%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    doc
Documentation for %{name}.


%prep
%setup -q -n %{gem_name}-%{version}
%setup -q -n %{gem_name}-%{version} -a1

%patch -P0 -p1


%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/


%check
export GEM_PATH="%{buildroot}/%{gem_dir}:%{gem_dir}"

# Ignore test results for now;
# there are load-dependent failures / timeouts happening during koji builds.
rspec -I"lib" spec || :


%files
%license %{gem_instdir}/MIT-LICENSE.txt

%dir %{gem_instdir}

%{gem_libdir}

%exclude %{gem_cache}

%{gem_spec}


%files doc
%doc %{gem_docdir}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Fabio Valentini <decathorpe@gmail.com> - 1.12.1-2
- Ignore test failures due to possible load-dependent timeouts.

* Tue Jun 12 2018 Fabio Valentini <decathorpe@gmail.com> - 1.12.1-1
- Update to version 1.12.1.
- Update patch to disable broken tests.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 27 2014 Troy Dawson <tdawson@redhat.com> - 1.3.3-1
- Updated to latest release

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 24 2014 Troy Dawson <tdawson@redhat.com> - 1.0.0-1
- Update to version 1.0.0

* Mon Feb 17 2014 Troy Dawson <tdawson@redhat.com> - 0.9.2-3
- More test fixups

* Fri Feb 14 2014 Troy Dawson <tdawson@redhat.com> - 0.9.2-2
- Fix test Buildrequires

* Wed Feb 12 2014 Troy Dawson <tdawson@redhat.com> - 0.9.2-1
- Update to 0.9.2
- Fix tests

* Mon Jan 13 2014 Troy Dawson <tdawson@redhat.com> - 0.9.1-1
- Update to 0.9.1

* Thu Oct 17 2013 Troy Dawson <tdawson@redhat.com> - 0.8.4-2
- Included spec directory for testing

* Tue Oct 08 2013 Troy Dawson <tdawson@redhat.com> - 0.8.4-1
- Initial package

