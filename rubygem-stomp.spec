%global gem_name stomp

Summary: Ruby client for the Stomp messaging protocol
Name: rubygem-%{gem_name}
Version: 1.4.10
Release: 10%{?dist}
License: Apache-2.0
URL: http://stomp.codehaus.org/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/stompgem/stomp/pull/175
Patch0: https://salsa.debian.org/ruby-team/ruby-stomp/-/raw/5be6383a7a34a1d1891708d6aa8688cb4a6f89a5/debian/patches/fix-FTBFS-with-ruby-rspec-3.12.patch
BuildRequires: rubygems-devel 
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
Ruby client for the Stomp messaging protocol

%package doc
Summary: Documentation for %{name}

Requires: %{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}
%patch -P 0 -p1

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
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
pushd %{buildroot}/%{gem_instdir}
rspec  -Ilib spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/catstomp
%{_bindir}/stompcat
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/stomp.gemspec
%{gem_spec}


%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/spec
%doc %{gem_instdir}/notes
%doc %{gem_instdir}/examples
%doc %{gem_instdir}/test
%doc %{gem_instdir}/adhoc


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 20 2023 Steve Traylen <steve.traylen@cern.ch> - 1.4.10-9
- Use an SPDX License field for Apache II

* Thu Mar 30 2023 Steve Traylen <steve.traylen@cern.ch> - 1.4.10-8
- Fix for rspec 3.12, https://bugs.debian.org/1027092

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 22 2021 Steve Traylen  <steve.traylen@cern.ch> - 1.4.10-4
- Test with rspec(3) now that rspec2 has gone.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 20 2020 Steve Traylen  <steve.traylen@cern.ch> - 1.4.10-1
- Upstream 1.4.10 release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 02 2017 Steve Traylen  <steve.traylen@cern.ch> - 1.4.4-1
- Upstream 1.4.4 release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 23 2017 Steve Traylen  <steve.traylen@cern.ch> - 1.4.3-1
- Upstream 1.4.3 release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 10 2016 Steve Traylen  <steve.traylen@cern.ch> - 1.3.5-1
- Upstream 1.3.5 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 11 2015 Steve Traylen  <steve.traylen@cern.ch> - 1.3.4-2
- Force rspec 2 tests.

* Wed Mar 11 2015 Steve Traylen  <steve.traylen@cern.ch> - 1.3.4-1
- Upstream 1.3.4 release

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 18 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.8-2
- BR: rubygem(rspec), not rubygem(rspec-core).

* Mon Mar 18 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.8-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Updated to version 1.2.8.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 28 2012 Michael Stahnke <stahnma@puppetlabs.com> - 1.2.2-1
- Update to 1.2.2

* Fri Feb 03 2012 Vít Ondruch <vondruch@redhat.com> - 1.1.9-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 26 2011 Michael Stahnke <stahnma@puppetlabs.com> -  1.19-1
- New version from upstream

* Fri Mar 18 2011 <stahnma@fedoraproject.org> - 1.1.8-1
- New version from upstream

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 05 2010 Michael Stahnke <stahnma@fedoraproject.org> - 1.1.6-1
- Initial Package
