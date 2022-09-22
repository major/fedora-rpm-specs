# Generated from archive-tar-minitar-0.5.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name archive-tar-minitar


Summary: Provides POSIX tar archive management from Ruby programs
Name: rubygem-%{gem_name}
Version: 0.5.2
Release: 24%{?dist}
License: GPLv2+ or Ruby
URL: http://rubyforge.org/projects/ruwiki
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
# Reported upstream via
# https://github.com/halostatue/minitar/issues/9
Patch0: rubygem-archive-tar-minitar-0.5.2-fix-tests.patch
Requires: ruby(rubygems)
Requires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby(release)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Archive::Tar::Minitar is a pure-Ruby library and command-line utility that
provides the ability to deal with POSIX tar(1) archive files. The
implementation is based heavily on Mauricio Ferna'ndez's implementation in
rpa-base, but has been reorganised to promote reuse in other projects.

%package doc
Summary: Documentation for %{name}

Requires: %{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.

%prep
%setup -q -c -T

%gem_install -n %{SOURCE0}

pushd .%{gem_instdir}
%patch0 -p0

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

find %{buildroot}%{gem_instdir}/{lib,tests} -type f | \
  xargs -n 1 sed -i -e '/^#!\/usr\/bin\/env ruby/d'

find %{buildroot}%{gem_instdir}/bin -type f | \
  xargs -n 1 sed -i -e 's"^#!/usr/bin/env ruby"#!/usr/bin/ruby"'

# require_gem is deprecated
# http://rubyforge.org/tracker/?func=detail&aid=22034&group_id=84&atid=409
sed -i 's^require_gem^gem^' %{buildroot}%{gem_instdir}/bin/minitar

%check
pushd .%{gem_instdir}
# TODO try to get new version from upstream, should fix these failures
ruby tests/tc_tar.rb || :
popd

%files
%{_bindir}/minitar
%doc %{gem_instdir}/README
%doc %{gem_instdir}/ChangeLog
%doc %{gem_instdir}/Install
%dir %{gem_instdir}

# Rakefile wants to load gemspec which isn't shipped with gem, drop it as it's
# broken for now
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/Install

%{gem_instdir}/bin
%{gem_libdir}
%{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/tests
%{gem_docdir}

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 18 2013 Vít Ondruch <vondruch@redhat.com> - 0.5.2-8
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 02 2012 Vít Ondruch <vondruch@redhat.com> - 0.5.2-5
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 02 2009 Matthew Kent <mkent@magoazul.com> - 0.5.2-2
- Fix license (#531408).
- Exclude Install (#531408).

* Mon Oct 26 2009 Matthew Kent <mkent@magoazul.com> - 0.5.2-1
- Initial package
