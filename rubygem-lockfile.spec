# Generated from lockfile-1.4.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name lockfile

Summary: Ruby library for creating NFS safe lockfiles
Name: rubygem-%{gem_name}
Version: 1.4.3
Release: 26%{?dist}
License: GPLv2 or Ruby
URL: http://codeforpeople.com/lib/ruby/lockfile/
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Source1: http://codeforpeople.com/lib/license.txt

Requires: ruby(release)
Requires: ruby(rubygems)
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%package doc
Summary: Documentation for %{name}
Requires:%{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%description
rlock creates NFS resistant lockfiles


%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
cp -p %{SOURCE1} %{buildroot}%{gem_instdir}

mkdir -p %{buildroot}%{_bindir}
cp -a ./%{_bindir}/* %{buildroot}%{_bindir}

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
chmod 755 %{buildroot}%{gem_instdir}/samples/lock.sh
chmod 755 %{buildroot}%{gem_instdir}/samples/a.rb
chmod 755 %{buildroot}%{gem_instdir}/bin/*

# Remove unnecessary files
rm -f %{buildroot}/%{gem_instdir}/install.rb
rm -f %{buildroot}/%{gem_instdir}/gemspec.rb
rm -f %{buildroot}/%{gem_instdir}/rlock


%files
%dir %{gem_instdir}
%{_bindir}/rlock
%{_bindir}/rlock-1.4.3
%doc %{gem_instdir}/README
%doc %{gem_instdir}/license.txt
%{gem_libdir}
%{gem_instdir}/bin
%{gem_cache}
%{gem_spec}

%files doc
%{gem_docdir}
%{gem_instdir}/samples
%{gem_instdir}/doc

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-24
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Josef Stribny <jstribny@redhat.com> - 1.4.3-10
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 03 2012 Vít Ondruch <vondruch@redhat.com> - 1.4.3-7
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 08 2010 Shreyank Gupta <sgupta@redhat.com> - 1.4.3-4
- Using cp -p instead of install -p to preserve perms

* Tue Jun 08 2010 Shreyank Gupta <sgupta@redhat.com> - 1.4.3-3
- Using install -p instead of cp for installing license.txt

* Mon Jun 07 2010 Shreyank Gupta <sgupta@redhat.com> - 1.4.3-2
- Changed license to GPLv2 from GPLv2+
- Added license.txt file to main package
- Left /bin in main package, update permissions.

* Tue Jun 02 2010 Shreyank Gupta <sgupta@redhat.com> - 1.4.3-1
- Initial package
